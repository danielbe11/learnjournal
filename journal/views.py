from django.shortcuts import render

from .forms import ResourceForm
from django.http import HttpResponse
from journal.models import Resource

# def view_resources(request):
#     return HttpResponse("Hello, world. You're at the view resources webpage.")

def view_resources(request):
    list_resources = Resource.objects.all()
    context = {'list_resources': list_resources}
    return render(request, 'journal/view_resources.html', context)


def create_new_resource(request):
    form = ResourceForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'journal/create_new_resource.html', context)
