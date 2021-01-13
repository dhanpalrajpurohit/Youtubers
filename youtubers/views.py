from django.shortcuts import render
from .models import Youtuber
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.

def youtubers(request):
    youtubers = Youtuber.objects.order_by('-created_date')
    data = {
        'youtubers':youtubers
    }
    return render(request,'youtubers/youtubers.html',data)

def search(request):
    youtubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_type_search = Youtuber.objects.values_list('category',flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            # tubers_name_search = Youtuber.objects.filter(name__icontains=keyword)
            # print(tubers_name_search)
            # #tubers = tubers.objects(description__icontains=keyword)
            youtubers = Youtuber.objects.filter(description__icontains=keyword)
            # youtubers = youtubers.union(tubers_name_search,tubers_description)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            youtubers = Youtuber.objects.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            youtubers = Youtuber.objects.filter(camera_type__iexact=camera_type)

    if 'category_type' in request.GET:
        category_type = request.GET['category_type']
        if category_type:
            youtubers = Youtuber.objects.filter(category_type__iexact=category_type)


    data = {
        'youtubers':youtubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_type_search':category_type_search
    }
    return render(request,'youtubers/search.html',data)

def youtubers_detail(request,id):
    youtuber = get_object_or_404(Youtuber,pk=id)
    data = {
        'youtuber':youtuber
    }
    return render(request,'youtubers/youtuber_detail.html',data)
    
