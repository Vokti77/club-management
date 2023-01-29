from django.shortcuts import render

def event(request):
    return render(request, 'pages/event.html')

