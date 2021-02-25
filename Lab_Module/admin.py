from django.contrib import admin
from .models import LabExam

# Register your models here.
class LabExamAdmin(admin.ModelAdmin):
    list_display = ["exam_date", "exam_name", "exam_description", "total_marks","pass_marks","exam_status"]

class Meta:
    model = LabExam
    admin.site.register(LabExam, LabExamAdmin)

