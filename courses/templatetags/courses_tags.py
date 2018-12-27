from django.template import Library
from simplemooc.models import EnrollmentModel
register = Library()


@register.inclusion_tag('my_courses.html')
def my_courses(user):
    enrollments = EnrollmentModel.objects.filter(user=user)
    context = {'enrollments': enrollments}
    return context


@register.simple_tag
def load_my_courses(user):
    return EnrollmentModel.objects.filter(user=user)
