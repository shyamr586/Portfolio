from email import message
from django.shortcuts import render
from .models import ShortSummary

# Create your views here.
def index(request):
    message = "Welcome to my profile!"
    summary = ShortSummary.objects.get()
    status = ShortSummary.objects.order_by("employment_status")[0]
    return render(request,"firstapp/index.html",context = {"message":message,
                                        "short_bio": summary.description,
                                        "status": summary.employment_status
                                        })

def bio(request):
    message = "This is my bio"
    return render(request,"firstapp/bio.html",context = {"message":message})

def feedback(request):
    message = "This is feedback page"
    return render(request,"firstapp/feedback.html",context = {"message":message})