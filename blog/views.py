from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView, 
	DeleteView

)
from .models import Post

#def name():
#	return "Christian's"

#def putin_h1(string):
#	return "<h1>{}</h1>".format(string)

#def home (request):
#	return HttpResponse (putin_h1("{} Blog Home".format(name())))

#def about (recuest):
#	return HttpResponse (putin_h1("{} Blog About".format(name())))


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render (request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name ='blog/home.html' # <app>/model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']


class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		print("self.request.user: ", self.request.user)
		print("post.author: ", post.author)

		return self.request.user == post.author


class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		print("self.request.user: ", self.request.user)
		print("post.author: ", post.author)

		return self.request.user == post.author

def about (request):
	return render (request, 'blog/about.html', {'title': 'About'})


