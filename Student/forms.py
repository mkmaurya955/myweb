from .models import Student
from django import forms


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['stu_name','email','stu_father_name', 'stu_mother_name', 'stu_father_occupation', 'stu_mother_occupation','stu_father_mobilenumber','stu_mother_mobilenumber','stu_class','stu_batch','stu_gender']
       
    def clean_email(self):
        email = self.cleaned_data.get('email')
        stu_qs = Student.objects.filter(email=email)
        if stu_qs.exists():
            raise forms.ValidationError('This Email has already been exist')
        return email