from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_p = request.GET.get('sort')
    phone = Phone.objects.all() 

    if sort_p == 'name':
        phone = phone.order_by('name')
        context = {'phones': phone}
        return render(request, template, context)
    elif sort_p == 'min_price':
        phone = phone.order_by('price')
        context = {'phones': phone}
        return render(request, template, context)
    elif sort_p == 'max_price':
        phone = phone.order_by('-price')
        context = {'phones': phone}
        return render(request, template, context)


    
    phone = Phone.objects.all()
    context = {'phones': phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
