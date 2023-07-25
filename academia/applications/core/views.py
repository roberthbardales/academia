from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


#pagina de inicio
class HomeView(TemplateView):
    template_name = "home.html"

#pagina de precios

class PricingView(TemplateView):
    template_name = "pricing.html"


