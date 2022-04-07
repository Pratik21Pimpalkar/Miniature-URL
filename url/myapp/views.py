

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import LongToShort, ChartData


def hello_world(request):
    return HttpResponse("Hello world!")


def home_page(request):
    context = {
        "submitted": False,
        "error": False
    }

    if request.method == 'POST':
        data = request.POST 				# dict
        long_url = data['longurl']
        custom_name = data['custom_name']

        try:
            # CREATE
            obj = LongToShort(long_url=long_url, short_url=custom_name)
            obj.save()

            # READ
            date = obj.date
            clicks = obj.clicks

            context["long_url"] = long_url
            context["short_url"] = request.build_absolute_uri() + custom_name
            context["date"] = date
            context["clicks"] = clicks
            context["submitted"] = True

        except:

            context["error"] = True

    return render(request, "index.html", context)


def redirect_url(request, short_url):
    row = LongToShort.objects.filter(short_url=short_url)

    if len(row) == 0:
        return HttpResponse("No such short url exist")

    obj = row[0]
    long_url = obj.long_url

    obj.clicks = obj.clicks + 1
    obj.save()

    return redirect(long_url)


def task(request):

    context = {
        "my_name": "John",
        "x": 15
    }

    return render(request, "test.html", context)


def all_analytics(request):

    rows = LongToShort.objects.all()

    context = {
        "rows": rows
    }

    return render(request, "all-analytics.html", context)


def analytics(request, short_url):

    row = LongToShort.objects.filter(short_url=short_url).values(
        'date', 'long_url', 'short_url', 'clicks')
    obj = row[0]

    os = request.META['OS']
    processor = request.META['NUMBER_OF_PROCESSORS']

    
    chart = ChartData.objects.all()
    context = {
        "obj": obj,
        "chart": chart,
        'os': os,
        'processor':processor,
       
    }
    
    

    return render(request, "analytics.html", context)
