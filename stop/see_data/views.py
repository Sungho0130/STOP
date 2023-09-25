from django.shortcuts import render, redirect
from .models import Post
from .forms import Askform
from django.core.mail import EmailMessage
import json
from .validators import email_validate

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

def ask_page(request):
    if request.method == "POST":
        form = Askform(request.POST)
        email = EmailMessage(
            f"{request.POST.get('writer', '고객님')}의 예약 요청",  # 이메일 제목
            f"""{request.POST.get("writer", "익명의 고객님")}님의 문의 요청 건
내용 : {request.POST.get("content", "문의 내용")} 
이메일 : {request.POST.get("tel", "연락처 미공개")}""", #이메일 내용
            to=['starhochoitest@gmail.com'],  # 받는 이메일
        )
        email.send()
        return redirect("main_page")
    else:
        form = Askform()
        return render(request, "page/ask_page.html", {"form": form})