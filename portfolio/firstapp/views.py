from email import message
from django.shortcuts import render
from .forms import FeedbackForm, FeedbackModel
# from .models import ShortSummary

# Create your views here.
def index(request):
   
    # print (request.user)
    
    message = "Welcome to my portfolio"
    short_bio = "Hello, my name is Shyam Ramakrishnan and I am a fresh IT graduate."
    status = "I am currently looking for a job."
    return render(request,"firstapp/index.html",context = {"message":message,
                                        "short_bio": short_bio,
                                        "status": status
                                        })

def bio(request):
    message = "This is my bio"
    return render(request,"firstapp/bio.html",context = {"message":message})

def get_data():
    return FeedbackModel.objects.all()

def feedback(request):

    feedback_data = get_data()
    print(feedback_data)
    for star in feedback_data.iterator():
        print(star.name)
        print(star.comment)

    form = FeedbackForm()
    message = "This is feedback page"
    if request.method == "POST":

        submitted =  request.POST.copy()
        submitted["name"] = request.user.first_name+" "+request.user.last_name
        print (submitted)
        # submitted.name = request.user.first_name+" "+request.user.last_name
        form =  FeedbackForm(submitted)
        if form.is_valid():
            # print (form.name)
            form.save(commit=True)
            message+=" you have submitted your feedback"
            return render(request,"firstapp/feedback.html",context = {"message":message,"form":form})
    return render(request,"firstapp/feedback.html",context = {"message":message,"form":form,
                                                         "feedbacks":feedback_data.iterator()})