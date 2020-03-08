from django.urls import path
from .views import them_vi, yc_them_vi, show_qlct_ca_nhan_page, yc_them_linhvuc, them_linhvuc, yc_them_chi_tieu, them_chitieu, lay_ls_chi_tieu, lay_bieu_do


urlpatterns = [
    path('', show_qlct_ca_nhan_page, name='qlct_canhan_page'),
    path('themvi', yc_them_vi, name='themvi'),
    path('themvi/thuc_hien', them_vi, name='thuc_hien_them_vi'),
    path('themlinhvuc', yc_them_linhvuc, name='themlinhvuc'),
    path('themlinhvuc/thuc_hien', them_linhvuc, name='thuc_hien_them_linh_vuc'),
    path('lsct/<int:id_vi>', lay_ls_chi_tieu, name = 'lay_ls_chi_tieu' ),
    path('bieudo/<int:id_vi>', lay_bieu_do, name = 'lay_bieu_do'),
    path('themchitieu/', yc_them_chi_tieu, name='themchitieu'),
    path('themchitieu/thuc_hien', them_chitieu, name='thuc_hien_them_chi_tieu'),
]