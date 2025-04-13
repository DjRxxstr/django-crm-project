from django.urls import path
from .views import (
    home_page_view,
    # login_user,
    logout_user
    );

urlpatterns = [
    path('', home_page_view, name = 'home-page-view'),
    # path('login/', login_user, name = 'login-user'),
    path('logout/', logout_user, name = 'logout-user'),
]