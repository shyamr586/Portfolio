import re
from django import forms
from .models import FeedbackModel
from better_profanity import profanity

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = '__all__'
        widgets = {
            'name': forms.HiddenInput(),
            'post_time': forms.HiddenInput(),
            'comment': forms.Textarea(attrs={'rows':3,'placeholder': 'Type your comment'}),
        }

    def clean_comment(self):
        data = self.cleaned_data['comment']
        no_profanity = profanity.censor(data)
        return no_profanity

        
