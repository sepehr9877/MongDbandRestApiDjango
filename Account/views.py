from django.shortcuts import render


def LogingPage(request):
    return render(request=request,template_name='Account/loginpage.html')
def Register(request):
    return render(request=request,template_name='Account/register.html')
def Updating(request):
    return render(request=request,template_name='Account/Updating.html')