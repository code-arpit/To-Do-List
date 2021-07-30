from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.views.generic.edit import DeleteView


from .models import TodoItem
from .forms import TodoForm
# Create your views here.
def home(request):
    return render(request, 'todoapp/home.html', {})

class ItemView(ListView):
    template_name = 'todoapp/view.html'
    queryset = TodoItem.objects.all()

class ItemDetail(DetailView):
    template_name = 'todoapp/detail.html'
    queryset = TodoItem.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("my_item")
        return get_object_or_404(TodoItem, id=id_)

class ItemCreate(CreateView):
    template_name = 'todoapp/create.html'
    form_class = TodoForm
    query_set = TodoItem.objects.all()
    success_url = '../'+'viewitem/'
    # print(success_url)

    def form_valid(self, form):
        print (form.cleaned_data)
        return super().form_valid(form)

class ItemUpdate(UpdateView):
    template_name = 'todoapp/create.html'
    form_class = TodoForm
    query_set = TodoItem.objects.all()
    success_url = '../'
    # print(success_url)

    def get_object(self):
        id_ = self.kwargs.get('my_item')
        return get_object_or_404(TodoItem, id=id_)

    def form_valid(self, form):
        print (form.cleaned_data)
        return super().form_valid(form)


class ItemDelete(DeleteView):
    template_name ='todoapp/delete.html'
    # success_url = '../../'

    def get_object(self):
        id_ = self.kwargs.get('my_item')
        return get_object_or_404(TodoItem, id=id_)
    
    def get_success_url(self):
        return reverse('view')

