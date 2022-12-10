from django.shortcuts import render


def Productspage(request):
    return render(request=request,template_name='Account/Products.html')