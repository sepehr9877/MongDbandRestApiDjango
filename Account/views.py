from django.shortcuts import render


def LogingPage(request):
    return render(request=request,template_name='Account/loginpage.html')
def Register(request):
    return render(request=request,template_name='Account/register.html')
