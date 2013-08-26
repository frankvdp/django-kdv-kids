# from django.shortcuts import get_object_or_404
# from django.shortcuts import render_to_response
# from django.template import RequestContext
from kids.models import *
from django.views.generic import ListView, DetailView


class GroupListView(ListView):
    model = Group
    context_object_name = "groups"

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        context['title'] = "Groepen"
        context['section'] = "Groepen"
        context['request'] = self.request
        return context


class GroupDetailView(DetailView):
    model = Group


class KidDetailView(DetailView):
    model = Kid
    context_object_name = "kid"


class CaretakerDetailView(DetailView):
    model = Caretaker
    context_object_name = "caretaker"
