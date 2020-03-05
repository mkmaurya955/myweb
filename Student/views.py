from django.shortcuts import render,redirect, get_object_or_404

from . models import Student
from django.utils import timezone
from . forms import RegisterForm
from django.contrib import messages
from django.db.models import Q

def home(request):
	students=Student.objects
	return render(request, 'Student/students/home.html', {'students':students})


def create(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            messages.success(request, "Successfully saved and Your student id is: " +str(student.id))
            return  redirect('/Student/create')
        else:
            return render(request, 'Student/students/create.html', {'error':'Please enter all required fields'})
    else:
        form = RegisterForm()

    return render(request, 'Student/students/create.html', {'form': form})



def detail(request):
	student=Student.objects.all()
	return render(request, 'Student/students/detail.html', {'student':student})

def search(request):
    if request.method== 'POST':
        srch=request.POST['search']
        if srch:
            match=Student.objects.filter(Q(id__icontains=srch) | Q(stu_name__icontains=srch) | Q(email__icontains=srch))
            if match:
                return render(request, 'Student/students/search.html' , {'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return redirect('/Student/search')
    return render(request, 'Student/students/search.html')


