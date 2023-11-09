from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'first.html')
def three(request):
    return render(request,'three.html')
def two(request):
    return render(request,'two.html')
def four(request):
    return render(request,'four.html')