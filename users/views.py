from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def home(request):
    return render(request, 'users/home.html')


def about(request):
    return render(request, 'users/about.html', {'title': 'About'})


@login_required
def profile(request):
    current_user = request.user
    context = {
        'email': current_user.email,
        'username': current_user.username,
        'firstname': current_user.first_name,
        'lastname': current_user.last_name,
    }
    return render(request, 'users/profile.html', context=context)

def yc_capnhap_taikhoan(request):
    current_user = request.user
    context = {
        'username': current_user.username,
        'email': current_user.email,
    }    
    return render(request, 'users/capnhap_taikhoan.html', context=context)

def capnhap_taikhoan (request):
    current_user = request.user
    first_name = request.POST['first_name']
    last_name = request.POST['lasr_name']
    date_of_birth = request.POST['date_of_birth']
    image = request.POST['fileupload']
    email = request.POST['email']
    context = {
        'username': current_user.username,
        'firstname': current_user.first_name,
        'lastname': current_user.last_name,
        'email': current_user.email,
    }
    return render(request, 'users/capnhap_taikhoan_thuchien.html', context=context)

def thongtin_taikhoan(request):
    current_user = request.user
    context = {
        'username': current_user.username,
        'firstname': current_user.first_name,
        'lastname': current_user.last_name,
        'email': current_user.email,
    }
    return render(request, 'users/thongtin_taikhoan.html', context=context)

def qlctcanhan(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/qlct_canhan.html', contex)

def qlctnhom(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/qlct_nhom.html', contex)

def themchitieu(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/themchitieu.html', contex)

def themlinhvuc(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/themlinhvuc.html', contex)

def themvi(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/themvi.html', contex)
    
def sono(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/sono.html', contex)

def themsono(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/themsono.html', contex)

def quanlitaikhoan(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/quanlitaikhoan.html', contex)

def tienich(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/tienich.html', contex)

def bieudotron(request):
    current_user = request.user
    email = current_user.email
    an = 5
    print(email)
    contex = {'an': an,
    'email': email
    }
    return render(request, 'users/bieudotron.html', contex)

def bieudocot(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/bieudocot.html', contex)

def themnhom(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/themnhom.html', contex)

def themvinhom(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/themvinhom.html', contex)

def themchitieunhom(request):
    current_user = request.user
    email = current_user.email
    print(email)
    contex = {'email': email}
    return render(request, 'users/themchitieunhom.html', contex)