from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "cabinet/home.html"

index_template_view = IndexTemplateView.as_view()