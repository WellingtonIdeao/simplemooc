from django.shortcuts import render
from simplemooc.models import Course


def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context_name = {'courses': courses}
    return render(request,template_name, context_name)
