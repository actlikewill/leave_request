from datetime import date
from django import forms
from leave_request.models import LeaveRequest

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = (
                'type', 
                'start_date', 
                'end_date', 
                )
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data['start_date']
        end_date = cleaned_data['end_date']

        if start_date > end_date:
            self.add_error('start_date', 'Start Date must be before End Date.')
            self.add_error('end_date', 'End Date must be after Start Date.')
        
        if start_date < date.today():

            self.add_error('start_date', 'You cannot set a past date.')