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
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.objects(description__icontains=keyword)

    data = {
        'tubers':tubers
    }
    return render(request,'youtubers/search.html',data)

def youtubers_detail(request,id):
    youtuber = get_object_or_404(Youtuber,pk=id)
    data = {
        'youtuber':youtuber
    }
    return render(request,'youtubers/youtuber_detail.html',data)
    
