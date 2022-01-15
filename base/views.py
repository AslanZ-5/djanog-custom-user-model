from django.shortcuts import render

from django import forms
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from base.models import Post
from .forms import  PostInterestForm





class PostList(ListView):
    model = Post


class PostDetail(FormMixin, DetailView):
    model = Post
    form_class = PostInterestForm

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        form.instance.post = self.get_object()
        form.instance.author = self.request.user
        form.save()
        return super(PostDetail, self).form_valid(form)
