from django.urls import path

from .api.viewsets import UserProfileViewSet


user_signup = UserProfileViewSet.as_view({'post': 'create'})
user_logout = UserProfileViewSet.as_view({'post': 'logout'})
user_login = UserProfileViewSet.as_view({'post': 'login'})
user_me = UserProfileViewSet.as_view({
    'get': 'retrieve_me',
    'post': 'update',
})
user_retrieve = UserProfileViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('login', user_login, name='user-login'),
    path('signup', user_signup, name='user-signup'),
    path('logout', user_logout, name='user-logout'),
    path('me', user_me, name='user-me'),
    path('<username>', user_retrieve, name='user-retrieve'),
    path('<username>/<details>', user_retrieve, name='user-retrieve'),
]
