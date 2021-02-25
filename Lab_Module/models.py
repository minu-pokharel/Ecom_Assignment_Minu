from django.db import models

# Create your models here.
class LabExam(models.Model):
    exam_date= models.DateTimeField()
    exam_name = models.CharField(max_length=200)
    exam_description= models.TextField()
    total_marks = models.FloatField()
    pass_marks= models.FloatField()
    exam_status = models.BooleanField()