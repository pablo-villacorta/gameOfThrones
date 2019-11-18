from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
import requests
import json
from django import forms
from django.utils import timezone

from django.views import generic

from app.forms import RegisterForm, LoginForm, PostForm, ThreadForm
from app.models import House, Allegiance, Character, Sibling, Relationship, User, Thread, Post, Episode, Appearance

def index(request):
    houses = House.objects.all()
    return render(request, 'lore/cover.html', {
        "houses": houses
    })

def house(request, name):
    try:
        house = House.objects.get(name=name)
    except House.DoesNotExist:
        return handler404(request, None)
    characters = house.characters_in_house.all()
    return render(request, 'lore/house.html', {
        "house": house,
        "characters": characters,
        "allegiance": house.allegiance.all()
    })

def character(request, name):
    try:
        character = Character.objects.get(name=name)
    except Character.DoesNotExist:
        return handler404(request, None)
    return render(request, 'lore/character.html', {
        "character": character,
        "siblings": character._siblings.all(),
        "related": character.related_to.all()
    })

def login(request):
    if request.session.has_key('username'):
        return redirect('/lore')
    if request.method == 'POST':
        filledForm = LoginForm(request.POST)
        if filledForm.is_valid():
            username = filledForm.cleaned_data["username"]
            password = filledForm.cleaned_data["password"]
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    # good
                    request.session["username"] = username
                    return redirect('/lore')
                else:
                    #bad
                    form = LoginForm()
                    return render(request, 'login.html', {
                        "form": form
                    })
            except User.DoesNotExist:
                return redirect('/login')
    else:
        # GET o cualquier otro
        form = LoginForm()
        return render(request, 'login.html', {
            "form": form
        })

def register(request):
    if request.session.has_key('username'):
        return redirect('/lore')
    if request.method == 'POST':
        filledForm = RegisterForm(request.POST)

        if filledForm.is_valid():
            username = filledForm.cleaned_data['username']
            password = filledForm.cleaned_data['password']
            repassword = filledForm.cleaned_data['repassword']
            if not password == repassword:
                return redirect('/register')
            # chequear bd
            try:
                User.objects.get(username=username)
                # username ya cogido -> debe cambiar
                return redirect('/register')
            except User.DoesNotExist:
                user = User()
                user.username = username
                user.password = password
                user.save()
                # iniciar sesión
                request.session['username'] = username

                return redirect('/lore')

    # GET o cualquier otro metodo
    form = RegisterForm()
    return render(request, 'register.html', {
        'form': form
    })

def logout(request):
    try:
        del request.session["username"]
    except KeyError:
        pass
    return redirect('/lore')

def handler404(request, exception):
    return render(request, 'lore/404.html', status=404)

def newPost(request, id):
    if not request.session.has_key('username'):
        return redirect('/login')
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
            return redirect('/forum/thread/'+str(id))
    else:
        # GET
        form = PostForm()
        thread = Thread.objects.get(pk=id)
        return render(request, "forum/newpost.html", {
            "form": form,
            "thread": thread
        })

def newThread(request):
    if not request.session.has_key('username'):
        return redirect('/login')
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
            return redirect("/forum/thread/"+str(thread.pk))
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
        return thread.thread_posts.all().order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["thread"] = Thread.objects.get(pk=self.kwargs["id"])
        return context
