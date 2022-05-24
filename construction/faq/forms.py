from django import forms
from .models import Question,Answer,Reply,QuestionUser,AnswerUser

class QuestionForm(forms.ModelForm):
    class Meta:
        model   = Question
        fields  = ["title","content","accept_dt","user"]


class QuestionUserForm(forms.ModelForm):
    class Meta:
        model   = QuestionUser
        fields  = ["user","seriousness"]



class AnswerUserForm(forms.ModelForm):
    class Meta:
        model   = AnswerUser
        fields  = ["user","company"]


