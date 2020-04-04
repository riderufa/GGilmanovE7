from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView
from django.views.generic.edit import BaseUpdateView
from django.urls import reverse_lazy
import redis
import pickle

from board.models import *
from board.forms import *

cache = redis.Redis(host='127.0.0.1', port=6379)

class AdvertList(ListView):
    model = Advert
    template_name = 'advert_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        adverts = cache.get('adverts')
        if adverts:
            adverts = pickle.loads(adverts)
        else:
            adverts = Advert.objects.all()
            cache.set('adverts', pickle.dumps(adverts))
        context['advert_list'] = adverts
        return context

class AdvertDetail(DetailView):
    model = Advert
    template_name = 'advert_detail.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        adverts = cache.get('adverts')
        if adverts:
            adverts = pickle.loads(adverts)
        else:
            adverts = Advert.objects.all()
            cache.set('adverts', pickle.dumps(adverts))
        context['advert'] = adverts.get(pk=self.kwargs['pk'])
        return context
        
class AdvertStat(DetailView):
    model = Advert
    template_name = 'advert_stat.html'
    context_object_name = 'advert'

class CreateTag(CreateView):
    template_name = 'tag_create.html'
    form_class = TagForm
    success_url = reverse_lazy('board:adverts-list')
    
class CreateComment(CreateView):
    template_name = 'comment_create.html'
    form_class = CommentForm
    success_url = reverse_lazy('board:adverts-list')

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.save()
            adverts = Advert.objects.all()
            cache.set('adverts', pickle.dumps(adverts))
            return HttpResponseRedirect(reverse_lazy('board:adverts-list'))
        return HttpResponseRedirect(reverse_lazy('board:adverts-list'))


class CreateAdvert(CreateView):
    template_name = 'advert_create.html'
    form_class = AdvertForm
    success_url = reverse_lazy('board:adverts-list')

    def post(self, request, *args, **kwargs):
        form = AdvertForm(request.POST)
        if form.is_valid():
            advert = form.save()
            advert.save()
            adverts = Advert.objects.all()
            cache.set('adverts', pickle.dumps(adverts))
            return HttpResponseRedirect(reverse_lazy('board:adverts-list'))
        return HttpResponseRedirect(reverse_lazy('board:adverts-list'))


class EditAdvert(UpdateView):
    template_name = 'edit_advert.html'
    model = Advert
    form_class = AdvertForm
    success_url = reverse_lazy('board:adverts-list')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        adverts = Advert.objects.all()
        cache.set('adverts', pickle.dumps(adverts))
        return super(BaseUpdateView, self).post(request, *args, **kwargs)