from django import forms
from resumes.models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user','created_at']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'desired_salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1',
                'placeholder': '1'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (999) 999-99-99'
            }),
            'profession': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'})}
