from django.contrib import admin
from simplemooc.models import Course, EnrollmentModel, Announcement, Comment


class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)
admin.site.register([EnrollmentModel, Announcement, Comment])
