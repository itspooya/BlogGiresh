from django.views import generic
from .models import Post
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from . import forms



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'


def Representation(request):
    return render(request, "Representation.html")
def Acrelycen(request):
    return render(request, "aclerycen.html")
def Govashen(request):
    return render(request, "govashen.html")

def standard(request):
    return render(request,"standard.html")

def standarden(request):
    return render(request, "standarden.html")

def About(request):
    return render(request, "about.html")

def Archive(request):
    return render(request,"archive.html")

def govash(request):
    return render(request, "govash.html")

# def send_email(request):
#     if request.method == "POST":
#         sub = forms.Subscribe(request.POST)
#         name = sub["name"].value()
#         email = sub["email"].value()
#         subject = sub["subject"].value()
#         message = sub["message"].value()
#         send_mail(subject,message,"support@giresh.com",[email],fail_silently=False)
#     return redirect("/")





def acleryc(request):
    return render(request, "acleryc.html")


def catalog(request):
    return render(request, "catalog.html")

def abouten(request):
    return render(request,"about_en.html")

def indexen(request):
    return render(request,"index_en.html")

def catalogen(request):
    return render(request,"catalogen.html")
