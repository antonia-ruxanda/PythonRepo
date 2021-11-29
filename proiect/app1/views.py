from django.shortcuts import render

# Create your views here.
# CreateView -> adaugare date in DB
# UpdateView -> modificare date in formular
# DeleteView -> stergere date din DB
# IndexView -> informare cu privire la formular
# ListView -> informatii de tip lista din DB
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView

from app1.models import Location


class CreateLocationView(CreateView):
    model = Location
    # fields = 'all'
    fields = ['city', 'country']
    template_name = 'app1/location_form.html'

    def get_success_url(self):
        return reverse('app1:listare')


class UpdateLocationView(UpdateView):
    model = Location
    # fields = 'all'
    fields = ['city', 'country']
    template_name = 'app1/location_form.html'

    def get_success_url(self):
        return reverse('app1:listare')


class ListLocationView(ListView):
    model = Location
    template_name = 'app1/location_index.html'