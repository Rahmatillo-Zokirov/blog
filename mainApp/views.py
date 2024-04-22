from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'home.html')


def blog(request):
    blogs = Blog.objects.order_by('-date')
    all_dates = Blog.objects.all().values('date').distinct().order_by('-date')
    yillar = [{'year': date['date'].year, 'month': date['date'].month} for date in all_dates]
    yil = list({item['year']: item for item in yillar}.values())
    context = {
        'blogs': blogs,
        'yillar': yil
    }
    return render(request, 'blog.html', context)



def maqola(request, maqola_id):
    maqola = Blog.objects.get(id=maqola_id)
    context = {'maqola': maqola}
    return render(request, 'maqola.html', context)


def about(request):
    return render(request, 'about.html')