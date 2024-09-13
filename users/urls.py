from django.urls import path
from .views import RegisterView, CustomLoginView, UserProfileView, DeleteUserView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/update/', UserProfileView.as_view(), name='update-profile'),
    path('profile/delete/', DeleteUserView.as_view(), name='delete-profile'),


]