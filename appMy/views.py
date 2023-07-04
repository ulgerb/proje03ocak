from django.shortcuts import render
from .models import *

# Create your views here.

def indexPage(request):
   content2 = Card.objects.get(id=2)
   
   news = Card.objects.filter(new=True)
   cards = Card.objects.all()
   news2 = news.order_by("?")[:2] # order_by: sıralama;

   category = Category.objects.all()
   
   context = {
       "content2": content2,
       "category": category,
       "news4": news[:4],
       "news2": news2,
       "cards": cards,
   }
   return render(request, 'index.html', context)


def detailPage(request, idcard):
   print(idcard)
   card = Card.objects.get(id=idcard)
   context = {
      "card":card,
   }
   return render(request, 'detail.html', context)



def categoryPage(request, ctitle=None):
   # if Card.objects.filter(category__title=ctitle).exists():

   if ctitle is not None:
      cards = Card.objects.filter(category__title = ctitle)
   else:
      cards = Card.objects.all()
      
   category = Category.objects.all()
   
   context = {
       "cards": cards,
       "category": category,
   }
   return render(request, 'category.html', context)


def denemePage(request):
   
   if request.method == "POST":
      fname = request.POST.get("fname")
      lname = request.POST.get("lname")
      city = request.POST.get("from")
      
      print(fname,lname,city)
   
   return render(request, 'deneme.html')