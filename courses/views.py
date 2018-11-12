from django.shortcuts import render, get_object_or_404
from simplemooc.models import Course
from .forms import ContactCourse


def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context_name = {'courses': courses}
    return render(request,template_name, context_name)


# def details(request, pk):
#    course = get_object_or_404(Course, pk=pk)
#    template_name = 'courses/details.html'
#    context_name = {'course': course}
#    return render(request, template_name, context_name)


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    template_name = 'courses/details.html'
    context_name = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context_name['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()

    context_name['course'] = course
    context_name['form'] = form
    return render(request, template_name, context_name)
