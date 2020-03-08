from django.http import HttpResponse
from django.shortcuts import redirect, render
from hoadon.views import lay_ds_hoa_don, them_hoa_don
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Nhom, NhomUser, ViNhom



def show_qlct_nhom_page(request):
    current_user = request.user
    ds_nhom = current_user.nhom_set.filter(is_deleted=0)
    ds_vi = current_user.vicanhan_set.filter(is_deleted=0)
    ds_hoa_don = lay_ds_hoa_don(id_vi_ca_nhan = 1)
    x = len (ds_hoa_don)
    
    context = {
        'ds_nhom': ds_nhom,
        'ds_vi': ds_vi,
        'email': current_user.email,
        'chitieu': ds_hoa_don[x-1],
    }
    return render(request, 'qlct_nhom/qlct_nhompage.html', context=context)


def yc_them_nhom(request):
    context = {
        'email': request.user.email,
    }
    return render(request, 'qlct_nhom/themnhom.html', context=context)


def them_nhom(request):
    current_user = request.user
    ten = request.POST['ten']
    dinh_muc = request.POST['dinh_muc']
    
    nhom = Nhom(ten=ten, dinh_muc=dinh_muc)
    nhom.save()
    nhom_user = NhomUser(auth_user=current_user, nhom=nhom, is_leader=1)
    nhom_user.save()
    context = {
        'email': request.user.email,
    }

    return render(request, 'qlct_nhom/themnhom_thuchien.html', context=context)

def xoa_nhom(request, id_nhom):
    nhom = Nhom.objects.get(pk=id_nhom)
    nhom.delete()

def yc_them_nhom_user(request):
    context = {
        'email': request.user.email,
    }
    return render(request, 'qlct_nhom/them_nhomuser.html', context=context)

def them_nhom_user(request, id_nhom, id_user, dinh_muc):

    nhom = Nhom.objects.get(pk=id_nhom)
    user = User.objects.get(pk=id_user)
    nhom_user = NhomUser(auth_user=user, nhom=nhom, dinh_muc=dinh_muc)
    nhom_user.save()
    context = {
        'email': request.user.email,
    }
    return render('qlct_nhom/them_nhomuser_thuchien.html', context=context)


def xoa_nhom_user(request, id_nhom, id_user):
    nhom = Nhom.objects.get(pk=id_nhom)
    user = User.objects.get(pk=id_user)
    nhom_user = NhomUser.objects.filter(auth_user=user, nhom=nhom)
    nhom_user.delete()
    context = {
        'email': request.user.email,
    }
    return render('qlct_nhom/xoa_nhomuser_thuchien.html', context=context)


def lay_ds_user(request, id_nhom):
    id_user = NhomUser.objects.filter(nhom_id = id_nhom).values('auth_user_id')
    ds_user = User.objects.filter(id__in = id_user)
    idnhom = "global"
    idnhom = id_nhom
    context = {
        'email': request.user.email,
        'ds_user': ds_user,
    }   
    return render(request, "qlct_nhom/ds_nhomuser.html", context=context)

def info_nhom_user(request, id_user):
    user = User.objects.get(pk = id_user)
    user_dm = NhomUser.objects.filter(auth_user_id = id_user).values('dinh_muc')
    context = {
        'username': user.username,
        'email': user.email,
        'dinh_muc': user_dm,
    }
    return render(request, 'qlct_nhom/info_nhomuser.html', context=context)

def dat_dinh_muc_user(request, id_nhom, id_user, dinh_muc):
    nhom = Nhom.objects.get(pk=id_nhom)
    if request.user.is_authenticated():
        current_user = request.user
        thanh_vien = NhomUser.objects.filter(auth_user=current_user, nhom=nhom)
        if thanh_vien.is_leader == 1:
            user = User.objects.get(pk=id_user)
            nhom_user = NhomUser.objects.filter(auth_user=user, nhom=nhom)
            nhom_user.dinh_muc = dinh_muc
            nhom_user.save()
            return HttpResponse("thành công")
        else:
            return HttpResponse("Hãy liên lạc chủ nhóm")
    else:
        return HttpResponse("Hãy tạo tài khoản")

def them_vi(request, id_nhom, ten, dinh_muc, so_du):
    nhom = Nhom.objects.get(pk=id_nhom)
    nhom.vinhom_set.create(ten=ten, dinh_muc=dinh_muc, so_du=so_du)


def chinh_sua_vi(request, id_vi, ten, dinh_muc, so_du):
    vi = ViNhom.objects.get(pk=id_vi)
    vi.ten = ten
    vi.dinh_muc = dinh_muc
    vi.so_du = so_du
    vi.save()

def lay_ds_vi(request, id_nhom):
    nhom = Nhom.objects.get(pk=id_nhom)
    ds_vi = nhom.vinhom_set.filter(is_deleted=0)
    return HttpResponse("chức năng lấy ds ví")

def yc_them_vi_nhom(request):
    current_user = request.user
    ds_nhom = current_user.nhom_set.filter(is_deleted=0)
    context = {
        'ds_nhom': ds_nhom,
    }
    return render(request, 'qlct_nhom/themvinhom.html', context=context)


def them_vi_nhom(request):   
    ten = request.POST['ten']
    dinh_muc = request.POST['dinh_muc']
    so_du = request.POST['so_du']
    id_nhom = request.POST["auth_group"]

    nhom = Nhom.objects.get(pk=id_nhom)
    nhom.vinhom_set.create(ten=ten, dinh_muc=dinh_muc, so_du=so_du)

    return render(request, 'qlct_nhom/themvinhom_thuchien.html')


def yc_them_chi_tieu(request):
    current_user = request.user
    ds_linhvuc = current_user.linhvuc_set.all()
    ds_vi = []
    ds_nhom = current_user.nhom_set.filter(is_deleted=0)
    for nhom in ds_nhom:
        ds_vi_nhom = nhom.vinhom_set.all()
        ds_vi.extend(ds_vi_nhom)
    context = {
        'ds_vi': ds_vi,
        'email': current_user.email,
        'ds_linhvuc': ds_linhvuc,
    }
    return render(request, 'qlct_nhom/themchitieu.html', context)


def them_chi_tieu(request):
    current_user = request.user
    ten_hoa_don = request.POST["ten_hoa_don"]
    so_tien = request.POST["so_tien"]
    ghi_chu = request.POST["ghi_chu"]
    date = request.POST["thoi_gian_giao_dich_0"]
    time = request.POST["thoi_gian_giao_dich_1"]
    id_linhvuc = request.POST["linh_vuc"]
    id_vi = request.POST["vi_nhom"]

    print(ghi_chu)

    if not current_user.is_authenticated:
        print('permission deni')
        return redirect('login')

    date_time = date + ' ' + time
    result = them_hoa_don(
        current_user=current_user,
        ten_hoa_don=ten_hoa_don,
        so_tien=so_tien,
        thoi_gian_giao_dich=date_time,
        id_linh_vuc=id_linhvuc,
        ghichu=ghi_chu,
        id_vi_nhom=id_vi,
    )

    return render(request, 'qlct_nhom/themchitieu_thuchien.html')




