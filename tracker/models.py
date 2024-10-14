from django.db import models

# Create your models here.

class JobApplication(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    application_date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted')
    ])

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
