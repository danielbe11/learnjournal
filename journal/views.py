from django.shortcuts import render, get_object_or_404, redirect
from django.core.checks import messages
from django.contrib import messages
from .forms import ResourceForm
from django.http import HttpResponse
from journal.models import Resource


def view_resources(request):
    list_resources = Resource.objects.all()
    template = 'journal/view_resources.html'
    context = {'list_resources': list_resources}
    return render(request, template, context)


def detail_resources(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    template = 'journal/detail_resources.html'
    context = {'resource': resource}
    return render(request, template, context)


def create_new_resource(request):
    template = 'journal/create_new_resource.html'
    form = ResourceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Resource was saved')
    context = {'form': form}
    return render(request, template, context)


def edit_resource(request, resource_id):
    template = 'journal/create_new_resource.html'
    resource = get_object_or_404(Resource, pk=resource_id)

    if request.method == "POST":
        form = ResourceForm(request.POST, instance=resource)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Updated')

        except Exception as e:
            messages.warning(request, 'Your post was not saved due to an error:'.format(e))

    else:
        form = ResourceForm(instance=resource)

    context = {
        'form': form,
        'resource': resource,
    }

    return render(request, template, context)
