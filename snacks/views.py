

from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from  django.urls import reverse_lazy



class SnacksListViews(ListView):
    template_name='snack_list.html'
    model=Snack
    def get_context_data(self, kwargs):
        context = super().get_context_data(kwargs)
        context['snack'] = Snack.objects.first()  # Replace with your desired logic to retrieve the snack object
        return context
    

class SnacksDetailsViews(DetailView):
    template_name="snack_detail.html"
    model=Snack


class SnacksCreateViews(CreateView):
    template_name="snack_create.html"
    model=Snack
    fields= 'all'


class SnacksUpdateViews(UpdateView):
    template_name="snack_update.html"
    model=Snack
    fields= 'all'
    success_url=reverse_lazy('snacklist')

class SnacksDeleteViews(DeleteView):
    template_name="snack_delete.html"
    model=Snack
    success_url = reverse_lazy('snacklist')