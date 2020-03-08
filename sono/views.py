from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import SoNo


# Create your views here.
def show_sono_page(request):
    current_user = request.user
    id_chusono = current_user.id
    ds_sono = SoNo.objects.filter(auth_user_id=id_chusono)
    x = len (ds_sono)
    context = {
        'ds_sono': ds_sono,
        'email': current_user.email,
        'sono': ds_sono[x-1],
    }
    return render(request, 'sono/sonopage.html', context=context)


def yc_them_so_no(request):
    return render(request, 'sono/themsono.html')


def them_sono(request):
    current_user = request.user
    ten = request.POST['ten_so_no']
    so_tien = request.POST['so_tien']
    doi_tac = request.POST['doi_tac']
    loai = request.POST['loai']
    ngay_vay = request.POST['ngay_vay_0'] + " " + request.POST['ngay_vay_1']
    ngay_tra = request.POST['ngay_tra_0'] + " " + request.POST['ngay_tra_1']
    if current_user.is_authenticated:
        current_user.sono.create(ten_so_no=ten, so_tien=so_tien, doi_tac=doi_tac,
                             loai=loai, ngay_vay=ngay_vay, ngay_tra=ngay_tra, is_deleted=0)
        return render(request, 'sono/themsono_thuchien.html')
    else:
        print('user invalid')
        return redirect('login')

def chi_tiet_so_no(request, id_sono):
    sono_info = SoNo.objects.get(pk=id_sono)
    context = {
        'sono': sono_info,
    }
    return render(request, 'sono/chitiet_sono.html', context=context)