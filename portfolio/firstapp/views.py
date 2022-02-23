from django.shortcuts import render
from .forms import FeedbackForm, FeedbackModel
import os
from .scrape import REPOS
from . import details

print (details.message)
# Create your views here.
def index(request):
    return render(request,"firstapp/index.html",context = {"message":details.message,
                                        "short_bio1": details.short_bio1,
                                        "short_bio2": details.short_bio2,
                                        "short_bio3": details.short_bio3,
                                        "status": details.status
                                        })

def bio(request):
    
    return render(request,"firstapp/bio.html",context = {"message":details.message_bio, "skills":details.skills,"repos":REPOS})

def get_data():
    return FeedbackModel.objects.order_by('-post_time')

def feedback(request):

    feedback_data = get_data()

    form = FeedbackForm()
    message = ""
    if request.method == "POST":

        submitted =  request.POST.copy()
        submitted["name"] = request.user.first_name+" "+request.user.last_name
        print (submitted)
        # submitted.name = request.user.first_name+" "+request.user.last_name
        form =  FeedbackForm(submitted)
        if form.is_valid():
            # print (form.name)
            form.save(commit=True)
            form = FeedbackForm()
            message="You have submitted your feedback"
            return render(request,"firstapp/feedback.html",context = {"message":message,"form":form,"feedbacks":feedback_data.iterator()})
    return render(request,"firstapp/feedback.html",context = {"message":message,"form":form,
                                                         "feedbacks":feedback_data.iterator()})