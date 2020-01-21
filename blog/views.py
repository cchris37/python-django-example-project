from django.shortcuts import render
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

def about (request):
	return render (request, 'blog/about.html', {'title': 'About'})

# Create your views here.