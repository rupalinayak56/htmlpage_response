from django.shortcuts import render

# Create your views here.
def cutest(request):
    return render(request,'cutest.html')
def expression(request):
    return render(request,'expression.html')