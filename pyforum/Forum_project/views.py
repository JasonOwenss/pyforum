from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Forum
from .models import Comment
from .forms import ForumForm,CommentForm

def home(request):
    forums = Forum.objects.all()
    return render(request,'home.html',{'forums':forums})

def create_forum(request):
    form = ForumForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('Forum-Home')
    
    return render(request,'forum_form.html', {'form':form})

def open_forum(request,id):
    forum = Forum.objects.get(id=id)
    comments = Comment.objects.filter(forum=id)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = CommentForm()
            #return render(request,'forum_temp.html',{'forum':forum, 'comments':comments, 'form':form})
            return HttpResponseRedirect('/open/'+str(id)+'/')
    else:
        form = CommentForm()
    form = CommentForm()
    return render(request,'forum_temp.html',{'forum':forum, 'comments':comments, 'form':form})




