from django.shortcuts import render
from .models import Article
# Create your views here.


def index(request):
    article=Article.objects.all()
    return render(request,'home/index.html',{'article':article})
    
    
