from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("detail/", views.detail_page, name="detail_page"),
    path("analysis/", views.detail_page, name="analysis_page"),
    path("cause_of/", views.detail_page, name="cause_of_page"),
    path("preventive/", views.detail_page, name="preventive_page"),
    path("ask/", views.ask_page, name="ask_page"),
]