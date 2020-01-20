from django.shortcuts import render
from django.http import HttpResponse

#def name():
#	return "Christian's"

#def putin_h1(string):
#	return "<h1>{}</h1>".format(string)

#def home (request):
#	return HttpResponse (putin_h1("{} Blog Home".format(name())))

#def about (recuest):
#	return HttpResponse (putin_h1("{} Blog About".format(name())))

posts =[

{
'author': 'Christian',
'title':  "Christian's Blog Post 1",
'content': 'First post content',
'date_posted': 'Dezember 2019'
},
{
'author': 'Christian 2',
'title':  "Christian's Blog Post 2",
'content': 'Second post content',
'date_posted': 'Januar 2020',
}
]


def home(request):
	context = {
		'posts': posts
	}
	return render (request, 'blog/home.html', context)

def about (request):
	return render (request, 'blog/about.html', {'title': 'About'})

# Create your views here.
