from django.shortcuts import render,redirect
from .models import Questions
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .forms import QuestionForm
# Create your views here.

def Question_list(request):
    data=Questions.objects.all()
    return render(request,'question_list.html',{'questions':data})

def Question_detail(request,question_id):
    data=Questions.objects.get(id=question_id)
    return render(request,'question_detail.html',{'question':data})

def Question_create(request):
    if request.method=='POST':
        form=QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform=request.user
            myform.save()
            return redirect('/questions')
    else:
        form=QuestionForm()
    return render(request,'create_question.html',{'form':form})

class AddQuestion(CreateView):
    model=Questions
    fields=['title','author','question','draft']
    success_url='/questions'
    template_name='ask/create_question.html'
    
def question_edit(request,question_id):
    data=Questions.objects.get(id=question_id)
    if request.method=='POST':
        form=QuestionForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            myform=form.save(commit=False)
            myform=request.user
            myform.save()
            return redirect('/questions')
    else:
        form=QuestionForm(instance=data)
    return render(request,'ask/question_update.html',{'form':form})

class edit_questions(UpdateView):
    model=Questions
    fields=['title','author','draft','question']
    success_url='/questions'
    template_name='ask/question_update.html'
    
class delete_question(DeleteView):
    model=Questions
    success_url='/questions'
    template_name='ask/delete_question.html'
    
