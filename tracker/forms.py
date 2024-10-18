from django import forms
from .models import JobApplication

class JobApplicationForm (forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["company_name", "job_title", "application_date", "status"]
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date'}) 
        }


class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['status']