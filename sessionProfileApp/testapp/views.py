from django.shortcuts import render
from testapp.forms import NameForm, AgeForm, CourseForm, CityForm

# Create your business logic / views here👇.

# Name View
def name_view(request):
    form = NameForm()
    return render(request, 'testapp/name.html', {'form':form})

# Age View
def age_view(request):
    name = request.GET['name']  # To add data to the session
    request.session['name'] = name  # Store Data into session API
    form = AgeForm()  # age in store in form var

    return render(request, 'testapp/age.html', {'form':form, 'name':name})

# Course View
def course_view(request):
    age = request.GET['age']  # Fetch age
    request.session['age'] = age # store in session
    name = request.session['name']  # fetch the name
    form = CourseForm()

    return render(request, 'testapp/course.html', {'form':form, 'name':name})


# City View
def city_view(request):
    course = request.GET['course']  # Fetch Course
    request.session['course'] = course  # store in session
    name = request.session['name']
    form = CityForm()
    return render(request, 'testapp/city.html', {'form':form, 'name':name})


# Result View
def result_view(request):
    city = request.GET['city']  # Fetch city
    request.session['city'] = city  # Store in Session
    name = request.session['name']  # Fetch the name
    age = request.session['age']  # Fetch the age
    course = request.session['course']  # Fetch the course
    
    return render(request, 'testapp/result.html', {'name':name})

# def result_view(request):
    # course = request.GET['course']  # course store in course var

    # request.session['course'] = course  # store data into session var

    # name = request.session['name']  # Fetch the name

    # age = request.session['age']  # Fetch the age
    # return render(request, 'testapp/result.html')
