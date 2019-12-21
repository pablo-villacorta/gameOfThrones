from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
import requests
import json
from django import forms
from django.utils import timezone

from django.views import generic

from . import util

from app.forms import RegisterForm, LoginForm, PostForm, ThreadForm
from app.models import House, Allegiance, Character, Sibling, Relationship, User, Thread, Post, Episode, Appearance

from django.contrib.auth.hashers import make_password, check_password

def index(request):
    houses = House.objects.all()
    return render(request, 'lore/cover.html', {
        "houses": houses
    })

def house(request, id):
    try:
        house = House.objects.get(pk=id)
    except House.DoesNotExist:
        return handler404(request, None)
    characters = house.characters_in_house.all()
    return render(request, 'lore/house.html', {
        "house": house,
        "characters": characters,
        "allegiance": house.allegiance.all()
    })

def character(request, id):
    try:
        character = Character.objects.get(pk=id)
        appearances = [dict(),dict(),dict(),dict(),dict(),dict(),dict()]
        for i in range(len(appearances)):
            appearances[i]["numero"] = i+1
            appearances[i]["episodios"] = []
        
        for ap in character.appearances.all():
            s = ap.episode.season
            appearances[(s-1)]["episodios"].append(ap.episode)
    except Character.DoesNotExist:
        return handler404(request, None)
    print(appearances)
    return render(request, 'lore/character.html', {
        "character": character,
        "siblings": character._siblings.all(),
        "related": character.related_to.all(),
        "appearances": appearances
    })

def loginPOST(request):
    langCode = request.POST["langCode"]
    filledForm = LoginForm(request.POST)
    if filledForm.is_valid():
        username = filledForm.cleaned_data["username"]
        password = filledForm.cleaned_data["password"]
        
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # good
                request.session["username"] = username
                return redirect('/'+langCode+'/lore')
            else:
                #bad
                return redirect('/'+langCode+'/login/')
        except User.DoesNotExist:
            return redirect('/'+langCode+'/login')

def login(request):
    langCode = request.build_absolute_uri().split("/")[-3]
    if request.session.has_key('username'):
        return redirect('/'+langCode+'/')
    
    # GET o cualquier otro
    form = LoginForm()
    return render(request, 'login.html', {
        "form": form
    })

def registerPOST(request):
    filledForm = RegisterForm(request.POST)
    langCode = request.POST["langCode"]
    if filledForm.is_valid():
        username = filledForm.cleaned_data['username']
        password = filledForm.cleaned_data['password']
        repassword = filledForm.cleaned_data['repassword']
        if not password == repassword:
            return redirect('/'+langCode+'/register')
        
        try:
            User.objects.get(username=username)
            # username ya cogido -> debe cambiar
            return redirect('/'+langCode+'/register')
        except User.DoesNotExist:
            user = User()
            user.username = username
            hashed_pwd = make_password(password)
            user.password = hashed_pwd
            user.save()
            # iniciar sesión
            request.session['username'] = username

            return redirect('/'+langCode+'/')

def register(request):
    langCode = request.build_absolute_uri().split("/")[-3]
    if request.session.has_key('username'):
        return redirect('/'+langCode+'/')  

    # GET o cualquier otro metodo
    form = RegisterForm()
    return render(request, 'register.html', {
        'form': form
    })

def logout(request):
    langCode = request.build_absolute_uri().split("/")[-3]
    try:
        del request.session["username"]
    except KeyError:
        pass
    return redirect('/'+langCode+'/lore')

def handler404(request, exception):
    return render(request, 'lore/404.html', status=404)

def newPost(request, id):
    langCode = request.build_absolute_uri().split("/")[-5]
    if not request.session.has_key('username'):
        return redirect('/'+langCode+'/login')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            post = Post()
            post.content = content
            post.user = User.objects.get(username=request.session["username"])
            post.thread = Thread.objects.get(pk=id)
            post.date = timezone.now()
            post.positionInThread = len(post.thread.thread_posts.all())
            post.save()
            print('/'+langCode+'/forum/thread/'+str(id))
            return redirect('/'+langCode+'/forum/thread/'+str(id))
    else:
        # GET
        form = PostForm()
        thread = Thread.objects.get(pk=id)
        return render(request, "forum/newpost.html", {
            "form": form,
            "thread": thread,
            "numberOfPosts": thread.thread_posts.count()
        })

def newThread(request):
    langCode = request.build_absolute_uri().split("/")[-4]
    if not request.session.has_key('username'):
        return redirect('/'+langCode+'/login')
    if request.method == 'POST':
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        if thread_form.is_valid() and post_form.is_valid():
            thread = Thread()
            thread.title = thread_form.cleaned_data["title"]
            thread.description = thread_form.cleaned_data["description"]
            thread.save()
            post = Post()
            post.content = post_form.cleaned_data["content"]
            post.date = timezone.now()
            post.user = User.objects.get(username=request.session["username"])
            post.positionInThread = 0
            post.thread = thread
            post.save()
            thread.originalPost = post
            thread.save()
            return redirect("/"+langCode+"/forum/thread/"+str(thread.pk))
    else:
        # GET
        return render(request, 'forum/newthread.html', {
            "thread_form": ThreadForm(),
            "post_form": PostForm()
        })

def quiz(request):
    return render(request, "quiz.html")
        
def episode(request, id):
    try:
        ep = Episode.objects.get(pk=id)
    except Episode.DoesNotExist:
        return handler404(request, None)
    rand = ep.episode_appearance.all().order_by('?').first().character.image
    return render(request, 'lore/episode.html', {
        "episode": ep,
        "image": rand
    })

def season(request, id):
    if id > 7:
        return handler404(request, None)
    eps = Episode.objects.filter(season=id)
    return render(request, 'lore/season.html', {
        "episodes": eps,
        "seasonNumber": id
    })

def home(request):
    return render(request, 'home.html', {})

class ThreadListView(generic.ListView):
    model = Thread
    context_object_name = 'threads'
    queryset = Thread.objects.all().order_by('-originalPost__date')
    template_name = 'forum/list.html'

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'forum/thread.html'

    def get_queryset(self):
        thread = Thread.objects.get(pk=self.kwargs["id"])
        posts = thread.thread_posts.all().order_by('-date')
        for post in posts:
            post.content = util.createLinks(post.content, post.positionInThread)
            print(post.content)
            # don't save
        return posts
        #return thread.thread_posts.all().order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["thread"] = Thread.objects.get(pk=self.kwargs["id"])
        return context
