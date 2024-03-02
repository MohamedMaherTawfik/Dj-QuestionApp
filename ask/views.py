from django.shortcuts import render,redirect
from .models import Questions,Answer
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .forms import QuestionForm,AnswerForm
# Create your views here.

def Question_list(request):
    data=Questions.objects.all()
    return render(request,'question_list.html',{'questions':data})

def Question_detail(request,pk):
    data=Questions.objects.get(id=pk)
    answer_question=Answer.objects.filter(question=data)
    if request.method=='POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.question= data
            myform.save()
    else:
        form=AnswerForm()
    return render(request,'question_detail.html',{'question':data,'form':form,'answer_question':answer_question})

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


