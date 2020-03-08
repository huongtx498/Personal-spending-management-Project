from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, home, about, profile, capnhap_taikhoan, yc_capnhap_taikhoan, thongtin_taikhoan


urlpatterns = [
    path('', home, name='blog-home'),
    path('about/', about, name='blog-about'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', register, name='register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/thongtin-taikhoan', thongtin_taikhoan, name='thongtin_taikhoan'),
    path('accounts/profile/yc-capnhap-taikhoan', yc_capnhap_taikhoan, name='yc_capnhap_taikhoan'),
    path('accounts/profile/capnhap-taikhoan-thuchien', capnhap_taikhoan, name='thuchien_capnhap_taikhoan'),
]