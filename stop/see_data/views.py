from django.shortcuts import render
from .models import Post
# Create your views here.

def main_page(request):
    return render(request, "page/main_page.html")

def detail_page(request):
    return render(request, "page/tableau_detail.html")