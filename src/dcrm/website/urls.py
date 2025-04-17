from django.urls import path
from .views import (
    home_page_view,
    # login_user,
    logout_user,
    register_user,
    customer_record,
    delete_record,
    add_record,
    update_record,
    export_csv
    );

urlpatterns = [
    path('', home_page_view, name = 'home-page-view'),
    # path('login/', login_user, name = 'login-user'),
    path('logout/', logout_user, name = 'logout-user'),
    path('register/', register_user, name = 'register-user'),
    path('record/<int:id>', customer_record, name = 'customer_record'),
    path('record/<int:id>/delete', delete_record, name = 'delete_record'),
    path('add/', add_record, name = 'add_record'),
    path('record/<int:id>/update', update_record, name = 'update_record'),
    path('export-csv/', export_csv, name = 'export_csv')
]