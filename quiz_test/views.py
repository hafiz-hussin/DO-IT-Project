from django.shortcuts import render
from quiz_test.models import Quiz
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def quiz_home(request):
    return render(request, "quiz_home.html", {})