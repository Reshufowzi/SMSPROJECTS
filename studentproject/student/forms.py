from django import forms
from .models import Search
class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = '__all__'

        labels = {
            'student_name': 'Student Full Name :',
            'student_phonenumber': 'Student Contact Details :',
            'student_email': 'Student Email Address :',
            'student_image': 'Upload Student Image :',
        }
