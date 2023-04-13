from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import QuestionPaper, Solution
from .forms import QuestionPaperForm, SolutionForm

def upload_question_paper(request):
    if request.method == 'POST':
        form = QuestionPaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_question_paper')
    else:
        form = QuestionPaperForm()
    return render(request, 'question/upload_question_paper.html', {'form': form})

def download_question_paper(request, document_id):
    question_paper = QuestionPaper.objects.get(pk=document_id)
    file_path = question_paper.pdf_file.path
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(question_paper.pdf_file.name)
    return response

def upload_solution(request, question_paper_id):
    if request.method == 'POST':
        form = SolutionForm(request.POST, request.FILES)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.question_paper_id = question_paper_id
            solution.user = request.user
            solution.save()
            return redirect('questions', pk=question_paper_id)
    else:
        form = SolutionForm()
    return render(request, 'question/upload_solution.html', {'form': form})

def download_solution(request, pk):
    solution = Solution.objects.get(pk=pk)
    file_path = solution.pdf_file.path
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(solution.pdf_file.name)
    return response