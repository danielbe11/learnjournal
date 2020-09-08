from django.shortcuts import render, get_object_or_404, redirect
from django.core.checks import messages
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from .forms import ResourceForm
from django.http import HttpResponse, HttpResponseRedirect
from journal.models import Resource


def view_resources(request):
    query = request.GET.get("q")
    if query:
        list_resources = Resource.objects.filter(
            Q(name_text__icontains=query) |
            Q(language__icontains=query) |
            Q(framework__icontains=query) |
            Q(notes__icontains=query) |
            Q(link__icontains=query)
                ).distinct()

    else:
        list_resources = Resource.objects.all().order_by('post_date')

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
        messages.info(request, 'Resource was saved')

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
                # return HttpResponseRedirect(reverse('journal:view_resources'))
                messages.info(request, 'Updated')

        except Exception as e:
            messages.info(request, 'Your post was not saved due to an error:'.format(e))

    else:
        form = ResourceForm(instance=resource)

    context = {
        'form': form,
        'resource': resource,
    }

    return render(request, template, context)


def delete_resource(request, resource_id):
    template = 'journal/delete_resource.html'
    resource = get_object_or_404(Resource, pk=resource_id)

    if request.method == "POST":
        resource.delete()
        messages.success(request, 'You have successfully deleted Resource {resource_name}'.format(resource_name=
                                                                                                  resource.name_text))
        return redirect('../../')
    context = {
        'resource': resource
    }

    return render(request, template, context)


# def get_resource_queryset(query=None): # search function
#     template = 'journal/view_resources.html'
#     queryset = []
#     queries = query.split[" "]
#     for q in queries:
#         resources = Resource.objects.filter(
#             Q(name_text__icontains=q) |
#             Q(language__icontains=q) |
#             Q(framework__icontains=q) |
#             Q(notes__icontains=q)
#         ).distinct()
#
#         for resource in resources:
#             queryset.append(resource)
#
#     return list(set(queryset))
#

