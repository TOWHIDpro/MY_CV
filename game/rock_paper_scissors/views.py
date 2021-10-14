from django.shortcuts import render

# Create your views here.

def rock_paper_scissors(request):
    return render(request, 'rock_paper_scissors/rock_paper_scissors.html')