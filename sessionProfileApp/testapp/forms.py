from django import forms

# Name Form
class NameForm(forms.Form):
    name = forms.CharField()

# Age Form
class AgeForm(forms.Form):
    age = forms.IntegerField()

# Course Form
class CourseForm(forms.Form):
    # (Actual Value, Human-readable Name)
    COURSE_CHOICES = [
        ('See Courses', 'See Courses 👇'),
        ('python', 'Python Programming'),
        ('web_dev', 'Web Development'),
        ('data_science', 'Data Science'),
        ('ui_ux', 'UI/UX Design'),
        ('ai', 'Artificial Intelligence'),
        ('machine_learning', 'Machine Learning'),
        ('blockchain', 'Blockchain'),
        ('cyber_security', 'Cyber Security'),
        ('game_dev', 'Game Development'),
    ]
    
    course = forms.ChoiceField(
        choices=COURSE_CHOICES, 
        label="Select a Course",
        widget=forms.Select(attrs={'class': 'form-control'}) # Optional: CSS class ke liye
    )

# City Form
class CityForm(forms.Form):
    city = forms.CharField()

