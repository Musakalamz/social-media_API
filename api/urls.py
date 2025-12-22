from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet, CommentViewSet, UserRegistrationView, TokenLoginView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenLoginView.as_view(), name='login'),
    path('', include(router.urls)),
]