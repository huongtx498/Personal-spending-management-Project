from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import LinhVuc
from hoadon.views import lay_ds_hoa_don, them_hoa_don


def show_qlct_ca_nhan_page(request, id_vi=1):
    current_user = request.user
    ds_vi = current_user.vicanhan_set.filter(is_deleted=0)
    ds_hoa_don = lay_ds_hoa_don(id_vi_ca_nhan = id_vi)
    x = len (ds_hoa_don)
    context = {
        'ds_vi': ds_vi,
        'email': current_user.email,
        'chitieu': ds_hoa_don[x-1],
    }
    return render(request, 'qlct_ca_nhan/qlct_canhanpage.html', context=context)


def yc_them_vi(request):
    context = {
        'email': request.user.email,
    }
    return render(request, 'qlct_ca_nhan/themvi.html', context=context)


def them_vi(request):
    current_user = request.user
    ten = request.POST['ten']
    dinh_muc = request.POST['dinh_muc']
    sodu = request.POST['so_du']
    if current_user.is_authenticated:
        current_user.vicanhan_set.create(
            ten=ten, dinh_muc=dinh_muc, so_du=sodu, is_deleted=0)
        context = {
        'email': request.user.email,
    }
        return render(request, 'qlct_ca_nhan/themvi_thuchien.html', context=context)
    else:
        print('user invalid')
        return redirect('login')

def lay_ds_vi(request):
    # current_user = authenticate(username='manhieu', password='1234')
    if request.user.is_authenticated():
        current_user = request.user
        ds_vi = current_user.vicanhan_set.filter(is_deleted=0)
        return HttpResponse("chức năng lấy ds ví")
    else:
        return HttpResponse('Bạn cần đăng nhập!')

def chinh_sua_vi(request, ten, dinhmuc, sodu, id):
    vi_ca_nhan = ViCaNhan.objects.get(pk=id)
    vi_ca_nhan.ten = ten
    vi_ca_nhan.dinh_muc = dinhmuc
    vi_ca_nhan.so_du = sodu
    vi_ca_nhan.save()
    return HttpResponse("chỉnh sửa thông tin ví")

def xoa_vi(request, id):
    vi_ca_nhan = ViCaNhan.objects.get(pk=id)
    vi_ca_nhan.is_deleted = 1
    vi_ca_nhan.save()
    return HttpResponse("xóa ví")

def yc_them_linhvuc(request):
    current_user = request.user
    ds_linhvuc = current_user.linhvuc_set.all()
    context = {
        'email': current_user.email,
        'ds_linhvuc': ds_linhvuc
    }
    return render(request, 'qlct_ca_nhan/themlinhvuc.html', context=context)

def them_linhvuc(request):
    current_user = request.user
    ten = request.POST['ten']
    loai = request.POST['loai']
    id_linhvuc_cha = request.POST['linh_vuc']
    # print(id_linhvuc_cha)

    linh_vuc_cha = None

    if current_user.is_authenticated:
        linhvuc = current_user.linhvuc_set.create(ten=ten, loai=loai)
        if int(id_linhvuc_cha) != -1:
            linh_vuc_cha = LinhVuc.objects.get(pk=id_linhvuc_cha)
            linhvuc.linh_vuc = linh_vuc_cha
            linhvuc.save()
        context = {
        'email': request.user.email,
    }
        return render(request, 'qlct_ca_nhan/themlinhvuc.html', context=context)
    else:
        print('user invalid')
        return redirect('login')

def lay_ds_linh_vuc(request):
    # current_user = authenticate(username='manhieu', password='1234')
    if request.user.is_authenticated():
        current_user = request.user
        ds_linh_vuc = current_user.linhvuc_set.all()
        return HttpResponse("lấy ds lĩnh vực của user")
    else:
        return HttpResponse('Bạn cần đăng nhập!')
        
def lay_ls_chi_tieu(request, id_vi):
    ds_hoa_don = lay_ds_hoa_don(id_vi_ca_nhan = id_vi)
    context = {
        'ds_chitieu': ds_hoa_don,
    } 
    return render(request, 'qlct_ca_nhan/lsct.html', context)

def yc_them_chi_tieu(request):
    current_user = request.user
    ds_linhvuc = current_user.linhvuc_set.all()
    ds_vi = current_user.vicanhan_set.filter(is_deleted=0)
    context = {
        'ds_vi': ds_vi,
        'email': current_user.email,
        'ds_linhvuc': ds_linhvuc,
    }
    return render(request, 'qlct_ca_nhan/themchitieu.html', context)


def them_chitieu(request):
    current_user = request.user
    ten_hoa_don = request.POST["ten_hoa_don"]
    so_tien = request.POST["so_tien"]
    ghi_chu = request.POST["ghi_chu"]
    date = request.POST["thoi_gian_giao_dich_0"]
    time = request.POST["thoi_gian_giao_dich_1"]
    id_linhvuc = request.POST["linh_vuc"]
    id_vi = request.POST["vi_ca_nhan"]

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
        id_vi_ca_nhan=id_vi,
    )
    context = {
        'email': request.user.email,
    }
    return render(request, 'qlct_ca_nhan/themchitieu_thuchien.html', context=context)

from django.db.models import Sum
from hoadon.models import HoaDon
def lay_bieu_do(request, id_vi):
    ds_hoa_don = lay_ds_hoa_don(id_vi_ca_nhan = id_vi)
    ds_linh_vuc = HoaDon.objects.values('linh_vuc__ten').annotate(Sum('so_tien'))

    lv1 = ds_linh_vuc[0]['linh_vuc__ten']
    so1= ds_linh_vuc[0]['so_tien__sum']

    lv2 = ds_linh_vuc[1]['linh_vuc__ten']
    so2= ds_linh_vuc[1]['so_tien__sum']

    lv3 = ds_linh_vuc[2]['linh_vuc__ten']
    so3= ds_linh_vuc[2]['so_tien__sum']

    lv4 = ds_linh_vuc[3]['linh_vuc__ten']
    so4= ds_linh_vuc[3]['so_tien__sum']

    lv5 = ds_linh_vuc[4]['linh_vuc__ten']
    so5= ds_linh_vuc[4]['so_tien__sum']

    lv6 = ds_linh_vuc[5]['linh_vuc__ten']
    so6= ds_linh_vuc[5]['so_tien__sum']

    lv7 = ds_linh_vuc[6]['linh_vuc__ten']
    so7= ds_linh_vuc[6]['so_tien__sum']

    lv8 = ds_linh_vuc[7]['linh_vuc__ten']
    so8= ds_linh_vuc[7]['so_tien__sum']

    lv9 = ds_linh_vuc[8]['linh_vuc__ten']
    so9= ds_linh_vuc[8]['so_tien__sum']

    lv10 = ds_linh_vuc[9]['linh_vuc__ten']
    so10= ds_linh_vuc[9]['so_tien__sum']


    context = {
        'lv1': lv1,
        'lv2': lv2,
        'lv3': lv3,
        'lv4': lv4,
        'lv5': lv5,
        'lv6': lv6,
        'lv7': lv7,
        'lv8': lv9,
        'lv9': lv9,
        'lv10': lv10,

        'so1': so1,
        'so2': so2,
        'so3': so3,
        'so4': so4,
        'so5': so5,
        'so6': so6,
        'so7': so7,
        'so8': so8,
        'so9': so9,
        'so10': so10,
        
    }

    print(ds_linh_vuc)
    return render(request, 'qlct_ca_nhan/bieudotron.html', context)