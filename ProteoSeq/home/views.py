from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/index.html')
def contact_us(request):
    return render(request,'home/contactus.html')
def documentation(request):
    return render(request,'home/doc.html')
