from django.urls import path
from .views import show_qlct_nhom_page, yc_them_nhom, them_nhom, yc_them_vi_nhom, them_vi_nhom, yc_them_chi_tieu, them_chi_tieu,  them_nhom_user, yc_them_nhom_user, xoa_nhom_user, lay_ds_hoa_don, lay_ds_user, info_nhom_user


urlpatterns = [
    path('', show_qlct_nhom_page, name='qlct_nhom_page'),
    path('themnhom/', yc_them_nhom, name='themnhom'),
    path('themnhom/thuc_hien', them_nhom, name='thuc_hien_them_nhom'),
    path('them-nhomuser/', yc_them_nhom_user, name='them_nhom_user'),
    path('them-nhomuser/thuc-hien', them_nhom_user, name='thuc_hien_them_nhom_user'),
    path('xoa-nhomuser/thuc-hien', xoa_nhom_user, name='thuc_hien_xoa_nhom_user'),
    path('themvinhom/', yc_them_vi_nhom, name='them_vinhom'),
    path('themvinhom/thuc-hien', them_vi_nhom, name='thuc_hien_them_vinhom'),
    path('ds-user/<int:id_nhom>', lay_ds_user, name='ds_user'),
    path('ds-user/user-info/<int:id_user>', info_nhom_user, name='nhom_user_info'),
    path('themchitieu', yc_them_chi_tieu, name='them_chitieu'),
    path('themchitieu/thuc-hien', them_chi_tieu, name='thuc_hien_them_chi_tieu_nhom'),
]