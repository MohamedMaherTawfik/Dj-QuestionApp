from django import forms
from .models import Questions,Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Questions
        #fields='__all__'
        exclude=('author',)
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        #fields="__all__"
        exclude=('question','author',)