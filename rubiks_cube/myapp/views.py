from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ModelPost, ModelAlgorithm, ModelPattern
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here.

# Posts
class ViewModelPost(ListView):
    queryset = ModelPost.objects.all()

class CreateModelPost(CreateView):
    model = ModelPost
    fields = '__all__'
    template_name = 'models/post/create.html'

    def form_valid(self, form):
        model = form.save(commit=False)
        model.save()
        return HttpResponseRedirect(reverse('home'))

class UpdateModelPost(UpdateView):
    model = ModelPost
    fields = ['title', 'level', 'content']
    template_name = 'models/post/update.html'

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.model.objects.get(id=id)

    def form_valid(self, form):
        model = form.save(commit=False)
        model.save()
        return HttpResponseRedirect(reverse('post_manage'))

class DeleteModelPost(DeleteView):
    model = ModelPost
    template_name = 'models/post/delete.html'

    def get_success_url(self):
        return reverse('post_manage')

# 3x3 Algorithm
class ViewModelAlgorithm(ListView):
    queryset = ModelAlgorithm.objects.all()

class CreateModelAlgorithm(CreateView):
    model = ModelAlgorithm
    fields = '__all__'
    template_name = 'models/3x3alg/create.html'

    def form_valid(self, form):
        model = form.save(commit=False)
        model.youtube = convert_to_embed_link(model.youtube)
        model.save()
        return HttpResponseRedirect(reverse('alg_list'))

class UpdateModelAlgorithm(UpdateView):
    model = ModelAlgorithm
    fields = ['title', 'method', 'content', 'youtube']
    template_name = 'models/3x3alg/update.html'

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.model.objects.get(id=id)

    def form_valid(self, form):
        model = form.save(commit=False)
        model.youtube = convert_to_embed_link(model.youtube)
        model.save()
        return HttpResponseRedirect(reverse('alg_manage'))

class DeleteModelAlgorithm(DeleteView):
    model = ModelAlgorithm
    template_name = 'models/3x3alg/delete.html'

    def get_success_url(self):
        return reverse('alg_manage')

def convert_to_embed_link(link):
     # Change youtube urls to embed one
    if '://youtu.be/' in link:
        link = link.replace('youtu.be/', 'www.youtube.com/embed/').split('&')[0].split('?')[0]
    elif '://youtube.com/watch?v=' in link:
        link = link.replace('youtube.com/watch?v=', 'www.youtube.com/embed/').split('&')[0].split('?')[0]
    elif '://www.youtube.com/watch?v=' in link:
        link = link.replace('watch?v=', 'embed/').split('&')[0].split('?')[0]

    return link.replace('http://', 'https://')

# 3x3 Pattern
class ViewModelPattern(ListView):
    queryset = ModelPattern.objects.all()

class CreateModelPattern(CreateView):
    model = ModelPattern
    fields = '__all__'
    template_name = 'models/3x3pattern/create.html'

    def form_valid(self, form):
        model = form.save(commit=False)
        model.save()
        return HttpResponseRedirect(reverse('pattern_list'))

class UpdateModelPattern(UpdateView):
    model = ModelPattern
    fields = ['title', 'difficulty', 'content', 'image_url']
    template_name = 'models/3x3pattern/update.html'

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.model.objects.get(id=id)

    def form_valid(self, form):
        model = form.save(commit=False)
        model.save()
        return HttpResponseRedirect(reverse('pattern_manage'))

class DeleteModelPattern(DeleteView):
    model = ModelPattern
    template_name = 'models/3x3pattern/delete.html'

    def get_success_url(self):
        return reverse('pattern_manage')