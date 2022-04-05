from dataclasses import field
from django import forms 
from lms.models import lms_admin, books, student 

class AdminForm(forms.ModelForm):
    class Meta:
        model = lms_admin
        fields = "__all__"

class AdminSigninForm(forms.ModelForm):

    class Meta:
        model = lms_admin
        fields = "email","password"
        
class AdminSignupForm(forms.ModelForm):
    class Meta:
        model = lms_admin
        fields = "__all__"

class BookRecordForm(forms.ModelForm):
    class Meta:
        model = books
        fields = "__all__"

class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"

class StudentSigninForm(forms.ModelForm):
    class Meta:
        model = student
        fields = "stud_email","stud_password"