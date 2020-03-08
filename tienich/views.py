from django.shortcuts import render


# Create your views here.
def tienich(request):
    current_user = request.user
    email = current_user.email
    print(email)
    context = {'email': email}
    return render(request, 'tienich/tienich.html', context=context)
