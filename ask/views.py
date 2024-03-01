from django.shortcuts import render
from .models import Questions
# Create your views here.

def Question(request):
    data=Questions.objects.all()
    return render(request,'question_list.html',{'questions':data})

def Question_detail(request,question_id):
    data=Questions.objects.get(id=question_id)
    return render(request,'question_detail.html',{'question':data})

