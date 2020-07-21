from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.views.generic import ListView, DetailView
# Create your views here.

def post(request, pk):
   post = get_object_or_404(Post, pk=pk)
   form = CommentForm()
   if request.method == "POST":
      form = CommentForm(request.POST, author=request.user, post=post)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect(request.path)
   return render(request, "blog/post.html", {"post": post, "form": form})


class PostListView(ListView):
   queryset = Post.objects.all().order_by('-date')
   template_name = 'blog/blog.html'
   context_object_name = 'Posts'
   paginate_by = 5

class PostDetailView(DetailView):
   model = Post
   template_name = 'blog/post.html'
   queryset = Post.objects.all()