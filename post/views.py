from datetime import date
from .models import Yangiliklar,Videolar,OAV,Tabrik,Elon
from django.shortcuts import render,get_object_or_404

def news_list(request):
    news = Yangiliklar.objects.all()
    return render(request, 'news/list.html', {'news': news})

def news_detail(request, pk):
    new = get_object_or_404(Yangiliklar, pk=pk)
    return render(request, 'news/detail.html', {'new': new})

from django.shortcuts import render
import re
from .models import Videolar

def extract_youtube_id(url):
    """Extracts the YouTube video ID from a given URL."""
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
    return match.group(1) if match else None

def video_list(request):
    videos = Videolar.objects.all()

    # Add a `youtube_id` property for each video
    for video in videos:
        video.youtube_id = extract_youtube_id(video.video)

    return render(request, 'news/video.html', {'videos': videos})

def oav(request):
    list = OAV.objects.all()
    return render(request, 'news/oav.html', {'list': list})

def tabrik(request):
    list = Tabrik.objects.all()
    return render(request, 'news/tabrik.html', {'list': list})

def elon(request):
    list = Elon.objects.all()
    return render(request, 'news/elon.html', {'list': list})

def email(request):
    return render(request, 'aloqa/email.html')

def tel(request):
    return render(request, 'aloqa/tel.html')

def tel2(request):
    return render(request, 'aloqa/tel2.html')

def harid(request):
    return render(request, 'aloqa/harid.html')

def tender(request):
    return render(request, 'aloqa/tender.html')

def aksiya(request):
    return render(request, 'aloqa/aksiya.html')

def arxiv(request):
    return render(request, 'aloqa/arxiv.html')