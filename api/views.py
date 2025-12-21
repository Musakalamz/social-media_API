from rest_framework import viewsets, permissions, status, generics, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Follow, Comment, Like, Profile
from .serializers import PostSerializer, UserSerializer, FollowSerializer, UserRegistrationSerializer, CommentSerializer

def root_redirect(request):
    return redirect('/api/')

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user__username']
    search_fields = ['content', 'user__username']
    ordering_fields = ['created_at', 'likes_count']
    
    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        post = Post.objects.get(id=post_id)
        serializer.save(user=self.request.user, post=post)

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"message": "You already liked this post"}, status=status.HTTP_200_OK)
        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def feed(self, request):
        """
        Return posts from users the current user follows.
        """
        following_users = request.user.following.values_list('following', flat=True)
        posts = Post.objects.filter(user__in=following_users).order_by('-created_at')
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        # Ensure user can only update their own profile
        if instance != request.user:
             return Response({"error": "You cannot edit another user's profile"}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        # Handle profile update manually if needed, or rely on nested serializer update logic
        # For simplicity, if we want to update profile fields, we might need a custom update method
        # or use a library like drf-writable-nested. 
        # Here is a manual implementation for profile:
        profile_data = request.data.get('profile')
        if profile_data:
            profile = instance.profile
            if 'bio' in profile_data:
                profile.bio = profile_data['bio']
            if 'avatar' in profile_data:
                profile.avatar = profile_data['avatar']
            profile.save()

        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def follow(self, request, pk=None):
        target_user = self.get_object()
        if request.user == target_user:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        
        follow, created = Follow.objects.get_or_create(follower=request.user, following=target_user)
        if not created:
            return Response({"message": "You are already following this user"}, status=status.HTTP_200_OK)
        
        return Response({"message": f"You are now following {target_user.username}"}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unfollow(self, request, pk=None):
        target_user = self.get_object()
        Follow.objects.filter(follower=request.user, following=target_user).delete()
        return Response({"message": f"You have unfollowed {target_user.username}"}, status=status.HTTP_200_OK)