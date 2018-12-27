from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib.auth.decorators import login_required
from simplemooc.models import Course, EnrollmentModel
from django.contrib import messages
from .forms import ContactCourse


def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context_name = {'courses': courses}
    return render(request, template_name, context_name)


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


@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enroll, created = EnrollmentModel.objects.get_or_create(
        user=request.user, course=course,
    )
    if created:
        messages.success(request, 'Você foi inscrito no curso com sucesso!')
    else:
        messages.success(request, 'Você já está inscrito no curso!')
    return redirect('accounts:dashboard')


@login_required
def undo_enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enroll = get_object_or_404(
        EnrollmentModel, user=request.user, course=course,
    )
    if request.method == 'POST':
        enroll.delete()
        messages.success(request, 'Sua inscrição foi cancelada com sucesso')
        return redirect('accounts:dashboard')

    template = 'courses/undo_enrollment.html'
    context = {
        'enrollment': enroll,
        'course': course
    }
    return render(request, template, context)


@login_required
def announcements(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if not request.user.is_staff:
        enroll = get_object_or_404(
            EnrollmentModel, user=request.user, course=course,
        )
        if not enroll.is_approved():
            messages.error(request, 'A sua inscrição está pendente')
            redirect('accounts:dashboard')

    template = 'courses/announcements.html'
    context = {
        'course': course
    }
    return render(request, template, context)