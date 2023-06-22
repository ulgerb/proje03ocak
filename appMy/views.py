from django.shortcuts import render

# Create your views here.

def indexPage(request):
   context = {}
   return render(request, 'index.html', context)


def detailPage(request):
   context = {}
   return render(request, 'detail.html', context)


def categoryPage(request):
   context = {}
   return render(request, 'category.html', context)
