from django.urls import path

from .api.viewsets import UserSignupViewSet


user_signup = UserSignupViewSet.as_view({'post': 'create'})
user_logout = UserSignupViewSet.as_view({'post': 'logout'})
user_login = UserSignupViewSet.as_view({'post': 'login'})

urlpatterns = [
    path('login', user_login, name='user-login'),
    path('signup', user_signup, name='user-signup'),
    path('logout', user_logout, name='user-logout'),
    # path('me', name='user-me'),
    # path('<username>/details', name='user-details'),
    # path('<username>/short', name='user-short'),
    # path('<username>/edit', name='user-edit')
]
