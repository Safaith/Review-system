from django import forms
from .models import Review


# class reviewForm(forms.Form):
#     user_name = forms.CharField(label="User Name", max_length=100, error_messages={
#         "required": "your username must not be empty",
#         "max_length": "please enter short name"
#     })
#     review_text = forms.CharField(
#         label="your review", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="your rating", min_value=1, max_value=5)


class reviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "your Name",
            "review_text": "Your Text",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name": {
                "max-length": "Please,Enter short text",
                "required": "you should write your name",
            }
        }
