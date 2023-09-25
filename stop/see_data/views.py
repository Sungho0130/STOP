from django.shortcuts import render
from .models import Post
# Create your views here.

def main_page(request):
    return render(request, "page/main_page.html")

def detail_page(request):
    return render(request, "page/tableau_detail.html")

def analysis_page(request):
    return render(request, "page/analysis.html")

def cause_of_page(request):
    return render(request, "page/cause_of.html")

def preventive_page(request):
    return render(request, "page/preventive.html")