from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm
from .forms import UpdateStatusForm


# Create your views here.

def landing_page(request):
    return render(request, 'tracker/landing_page.html')
    
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
            print(form.errors)
    else:
        form = JobApplicationForm()
    return render(request, 'tracker/add_job.html', {'form': form})

def update_status(request, pk):
    application = get_object_or_404(JobApplication, id=pk)
    if request.method == 'POST':
        form = UpdateStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_detail', pk=application.pk)  # Redirect after saving
    else:
        form = UpdateStatusForm(instance=application)
    return render(request, 'tracker/update_status.html', {'form': form, 'application':application})

def application_detail(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    return render(request, 'tracker/application_detail.html', {'application': application})