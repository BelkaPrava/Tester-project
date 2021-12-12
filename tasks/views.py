from django.shortcuts import redirect, render, get_object_or_404
from .models import Collection, Task
from django.views.generic import DetailView
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User
from .forms import TaskForm, CollectionForm
from django.contrib.auth.decorators import login_required
import json


@login_required(login_url='login')
def profile(request):
    obj = Collection.objects.filter(author=request.user)
    context = {
        "object": obj
    }
    return render(request, 'tasks/profile.html', context)


def collection_list_view(request):
    obj = Collection.objects.filter(is_public=True)
    context = {
        "object": obj
    }
    return render(request, 'tasks/tasks_home.html', context)


def collection_detail_view(request, id=None):
    obj = get_object_or_404(Collection, id=id)
    array = [i.answer for i in obj.task_set.all()]
    context = {
        "object": obj,
        'is_author': 1 if obj.author == request.user else 0,
        'array': json.dumps(array, ensure_ascii=False)
    }
    return render(request, 'tasks/details_view.html', context)

@login_required(login_url='login')
def collection_create_view(request):
    form = CollectionForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'tasks/create_tasks.html', context)

@login_required(login_url='login')
def collection_update_view(request, id=None):
    obj = get_object_or_404(Collection, id=id, author=request.user)
    form = CollectionForm(request.POST or None, instance=obj)
    TaskFormset = modelformset_factory(Task, form=TaskForm, extra=0)
    qs = obj.task_set.all()
    formset = TaskFormset(request.POST or None, queryset=qs)
    context = {
        'form': form,
        'formset': formset,
        "object": obj
    }
    if all([formset.is_valid(), form.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            child.module = parent
            child.save()
        context['message'] = 'Data saved'
    return render(request, 'tasks/update_tasks.html', context)

# def tasks_home(request):
#     model = Collection.objects.all()
#     return render(request, 'tasks/tasks_home.html', {'collection': model[::-1]})
#
#
# def TasksDetail(request, pk):
#     tasks = get_object_or_404(Collection, pk=pk)
#     return render(request, 'tasks/details_view.html', {'tasks': tasks})
#
#
# def create_task(request):
#     formset = TaskFormSet(request.POST or None)
#     author = request.user
#
#     if request.method == "POST":
#         if formset.is_valid():
#             formset.save()
#             return redirect("create_task")
#
#     context = {
#         "formset": formset,
#         "author": author,
#     }
#
#     return render(request, "tasks/update_tasks.html", context)


# model = Collection.objects.get(pk=pk)
# class NewsDetail(request):
#    model = Collection.objects.all()
#    return render(request, 'tasks/details_view.html', {'collection': model[::-1]})

# def NewsDetail(request, pk):
#   book = get_object_or_404(Collection, id=pk)
#  context = {
#     "tasks": book
# }
# return render(request, "partials/book_detail.html", context)
