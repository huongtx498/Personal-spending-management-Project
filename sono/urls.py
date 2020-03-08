from django.urls import path
from .views import show_sono_page, yc_them_so_no, them_sono, chi_tiet_so_no


urlpatterns = [
    path('', show_sono_page, name='sono_page'),
    path('themsono/', yc_them_so_no, name='them_sono'),
    path('themsono/thuc_hien', them_sono, name='thuc_hien_them_sono'),
    path('chitiet-sono/<int:id_sono>', chi_tiet_so_no, name='chi_tiet_sono'),
]
