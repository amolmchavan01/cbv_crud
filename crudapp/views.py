from django.shortcuts import render
from django.http import HttpResponse
from .models import customer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Register(CreateView):
    model = customer
    fields = "__all__"
    #form_class = CustomerFrom #(Optional)
    template_name = 'crudapp/register.html'
    success_url = reverse_lazy("Register")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = customer.objects.all()
        return context
    
class Update(UpdateView):
    model = customer
    fields = '__all__'
    template_name = 'crudapp/update.html'
    success_url = reverse_lazy("Register")

class Delete(DeleteView):
    model = customer
    template_name = 'crudapp/delete.html'
    success_url = reverse_lazy("Register")





