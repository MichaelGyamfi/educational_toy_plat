from django.shortcuts import render
from .models import Child
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    children = Child.objects.filter(user=request.user)
    return render(request, 'parent_dashboard/dashboard.html', {'children': children})

