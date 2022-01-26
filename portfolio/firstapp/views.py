from email import message
from django.shortcuts import render
from .forms import FeedbackForm, FeedbackModel

# Create your views here.
def index(request):
    
    message = "Welcome to my Portfolio"
    short_bio1 = "Hi there! You are currently going through my portfolio."
    short_bio2 = "Glad you dropped by!"
    short_bio3 = "I'm a passionate and hard working (trust me, I am!) IT grad interested in developing \
        IT solutions."
    status = "I am currently looking for a full-time or intenship opportunity."
    return render(request,"firstapp/index.html",context = {"message":message,
                                        "short_bio1": short_bio1,
                                        "short_bio2": short_bio2,
                                        "short_bio3": short_bio3,
                                        "status": status
                                        })

def bio(request):
    message = "My name is Shyam Ramakrishnan, and I graduated from Middlesex University in April of 2021.\
        I have an honorary bachelor's degree in Information Technology.\n\nWith the increase in the\
         development of the IT sector and the many sub-sectors that are branching ever so frequently,\
        my interest in the field also advanced. After writing my very first script using Python 2.7, I\
         realized that I had an interest in the field and was very eager to learn more about the attainable\
         progress. I constantly observe the requirements put forward by the industry to see what skills\
         are desired and give my best effort to keep up with the standards. \n\nI come across my colleagues as an\
         honest and hard-working individual who would always be punctual and trustworthy."
    return render(request,"firstapp/bio.html",context = {"message":message})

def get_data():
    return FeedbackModel.objects.all()

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