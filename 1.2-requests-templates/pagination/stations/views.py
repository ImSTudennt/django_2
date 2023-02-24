from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

lis = []

with open(r'C:\Users\vladi\Desktop\dj-homeworks\1.2-requests-templates\pagination\data-398-2018-08-30.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for el in reader:
        lis.append(el)


def index(request):
    return redirect(reverse('bus_stations'))






def bus_stations(request):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(lis, 10)
    pag = paginator.get_page(page_num)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': pag,
        'page': pag,
    }
    return render(request, 'stations/index.html', context)
