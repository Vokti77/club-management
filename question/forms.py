from django import forms
from .models import QuestionPaper, Solution

class QuestionPaperForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['title', 'description', 'image', 'pdf_file']

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['description', 'pdf_file']