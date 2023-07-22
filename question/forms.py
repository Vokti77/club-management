from django import forms
from .models import QuestionPaper, Solution

class QuestionPaperForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['title','pdf_file']

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['pdf_file']