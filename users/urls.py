from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from users.views import (UserCreateView, UserDestroyView, UserListView,
                         UserRetrieveView, UserUpdateView)

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserRetrieveView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDestroyView.as_view()),
    path('token/', token_obtain_pair),
    path('token/refresh/', token_refresh),
]
