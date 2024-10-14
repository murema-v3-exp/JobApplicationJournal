from django.shortcuts import render, redirect
from .models import JobApplication
from .forms import JobApplicationForm


# Create your views here.
    
def job_list(request):
    # List all job applications
    jobs = JobApplication.objects.all()
    return render(request, 'tracker/job_list.html', {'jobs':jobs})


def add_job(request):
    # Handle job form submission
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'tracker/add_job.html', {'form': form})
