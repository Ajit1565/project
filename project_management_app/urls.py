from django.urls import path,include
from . import views
from . import PmViews

urlpatterns=[
    path('',views.loginPage,name='login'),
    path('doLogin/',views.doLogin,name='doLogin'),
    path('get_user_details/',views.get_user_details,name='get_user_details'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('admin_home/',PmViews.admin_home,name='admin_home'),
    path('admin_profile/',PmViews.admin_profile,name='admin_profile'),
    path('manage_staff/',PmViews.manage_staff,name='manage_staff'),
    path('delete_staff/<staff_id>/', PmViews.delete_staff, name="delete_staff"),
    path('edit_staff/',PmViews.edit_staff,name='edit_staff'),
    path('add_staff/', PmViews.add_staff, name="add_staff"),
    path('add_staff_save/',PmViews.add_staff_save,name='add_staff_save'),
    path('check_email_exist/', PmViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', PmViews.check_username_exist, name="check_username_exist"),
]