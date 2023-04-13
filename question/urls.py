from django.urls import path, include

from . import views
from .views import upload_question_paper, upload_solution, download_question_paper, download_solution

urlpatterns = [
    path('upload_question_paper/', views.upload_question_paper, name="upload_question_paper"),
    path('download_question_paper/<int:document_id>/', views.download_question_paper, name='download_question_paper'),
    path('upload_solution/<int:question_paper_id>', views.upload_solution, name="upload_solution"),
    path('download_solution/<int:pk>/', views.download_solution, name='download_solution'),

]
