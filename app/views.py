from django.shortcuts import render,get_object_or_404
from post.models import Yangiliklar,Videolar
from django.utils.translation import get_language
from datetime import date
from .models import Tashriflar
from django.shortcuts import render, redirect
from .forms import MurojatlarForm
from post.models import Turi,Korporativ,Intraktiv


def get_daily_visitors_count():
    today = date.today()
    return Tashriflar.objects.filter(visit_date=today).count()

def home(request):
    if request.method == 'POST':
        form = MurojatlarForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect to a success page or a new view
    else:
        form = MurojatlarForm()

    latest_post = Yangiliklar.objects.all().order_by('-date')[:1]
    other_posts = Yangiliklar.objects.all().order_by('-date')[1:5]
    tur = Turi.objects.all()
    return render(request, 'index.html', {'latest_post': latest_post, 'other_posts': other_posts, 'form': form, 'tur':tur})

def korporative_detail(request, pk):
    tur = get_object_or_404(Turi, pk=pk)
    korporative = Korporativ.objects.filter(turi=tur)
    return render(request, 'jamiyat/detail.html', {'korporative': korporative})

def intrak(request):
    intrak = Intraktiv.objects.all()
    return render(request, 'jamiyat/int_detail.html', {'intrak': intrak})

def jamiyat_tarixi(request):
    current_language = get_language()
    videolar = Videolar.objects.all()
    articles = Yangiliklar.objects.language(current_language) 
    return render(request, 'jamiyat/jamiyat_tarixi.html', {'news': articles, 'videolar': videolar})

def jamiyat_bugun(request):
    return render(request, 'jamiyat/jamiyat_bugun.html')

def raxbar(request):
    return render(request, 'jamiyat/raxbar.html')

def ish(request):
    return render(request, 'jamiyat/ish.html')

def tuzulma(request):
    return render(request, 'jamiyat/tuzulma.html')

def strategiya(request):
    return render(request, 'jamiyat/strategiya.html')

def horij(request):
    return render(request, 'horij/horij.html')

def maxsulot(request):
    return render(request, 'jamiyat/xizmat.html')

def reja(request):
    return render(request, 'jamiyat/reja.html')

def strategy(request):
    return render(request, 'jamiyat/strategy.html')

def nizom(request):
    return render(request, 'jamiyat/nizom.html')