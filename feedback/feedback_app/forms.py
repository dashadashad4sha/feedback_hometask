from django import forms

from .models import FeedbackModel, Countries


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = '__all__'

        widgets = {
            'fio': forms.TextInput(attrs={'class': 'fio-input'}),
            'feedback': forms.Textarea(attrs={'class': 'feedback-input'}),
        }
