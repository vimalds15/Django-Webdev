from django.shortcuts import render,redirect
from demo.models import Comment 
import datetime
from demo.forms import CommentForm
from django.utils import timezone
from django.views.generic import ListView

def index(request):
    return render (request,'demo/index.html')

class IndexListView(ListView):
    comment = Comment

    def get_context_data(self, **kwargs):
        context = super(IndexListView).get_context_data(**kwargs)
        return context
     
def javascript(request):
    return render(request,'demo/javascript.html')

def python(request):
    return render(request,'demo/python.html')

def java(request):
    return render(request,'demo/java.html')

def kotlin(request):
    return render(request,'demo/kotlin.html')

def cpp(request):
    return render(request,'demo/cpp.html')

def suggestions(request):
    form = CommentForm(request.POST or None)

    if request.method=='POST':
        if form.is_valid():
            comment=form.save(commit=False)
            comment.log_date=timezone.now()
            comment.save()
            return redirect ("indexpage")

    else:
        return render(request, "demo/comment.html"),{"form":form}