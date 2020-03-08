from django.shortcuts import render
from qlct_nhom.models import ViNhom
from qlct_ca_nhan.models import LinhVuc, ViCaNhan


# Create your views here.
def lay_ds_hoa_don(id_vi_ca_nhan=-1, id_vi_nhom=-1):
    vi = "global"
    if id_vi_ca_nhan != -1:
        vi = ViCaNhan.objects.get(pk=id_vi_ca_nhan)
    elif id_vi_nhom != 1:
        vi = ViNhom.objects.get(pk=id_vi_nhom)
    else:
        return False

    list_hoa_don = vi.hoadon_set.all()
    return list_hoa_don


def them_hoa_don(current_user, ten_hoa_don, so_tien, thoi_gian_giao_dich, id_linh_vuc, ghichu, id_vi_ca_nhan=-1, id_vi_nhom=-1):

    vi = None
    linh_vuc = LinhVuc.objects.get(pk=id_linh_vuc)
    loai = linh_vuc.loai
    if id_vi_ca_nhan != -1:
        vi = ViCaNhan.objects.get(pk=id_vi_ca_nhan)
        so_du = vi.so_du
        hoadon = current_user.hoadon_set.create(ten_hoa_don=ten_hoa_don, so_tien=so_tien,
                                                thoi_gian_giao_dich=thoi_gian_giao_dich,
                                                linh_vuc=linh_vuc, vi_ca_nhan=vi,ghi_chu=ghichu)

        if loai == 0:
            vi.so_du = int(so_du) + int(hoadon.so_tien)
        else:
            vi.so_du = int(so_du) -int(hoadon.so_tien)

        vi.save()
    elif id_vi_nhom != -1:
        vi = ViNhom.objects.get(pk=id_vi_nhom)
        so_du = vi.so_du
        hoadon = current_user.hoadon_set.create(ten_hoa_don=ten_hoa_don, so_tien=so_tien,
                                                thoi_gian_giao_dich=thoi_gian_giao_dich,
                                                vi_nhom=vi, linh_vuc=linh_vuc,ghi_chu=ghichu)

        if loai == 0:
            vi.so_du = int(so_du) + int(hoadon.so_tien)
        else:
            vi.so_du = int(so_du) - int(hoadon.so_tien)

        vi.save()
    else:
        return 1
    
    return 0
