from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def portfolio_index(request):
    portfolio = Portfolio.objects
    context = {'portfolio': portfolio}
    return render(request,'portfolio_index.html',context)
