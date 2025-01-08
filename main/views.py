from django.shortcuts import render

from .models import *


def home_view(request):
    soz = request.GET.get("soz", "")
    correct = None
    incorrects = None
    if soz is not "":
        if Correct.objects.filter(word=soz):
            correct = Correct.objects.get(word=soz)
            incorrects = Incorrect.objects.filter(correct=correct)
        elif Incorrect.objects.filter(word=soz):
            incorrect = Incorrect.objects.get(word=soz)
            correct = incorrect.correct
            incorrects = Incorrect.objects.filter(correct=correct)
        elif 'h' not in soz and 'x' not in soz:
            correct = "so'z tarkibida 'x' yoki 'h' mavjud emas!"
        else:
            correct = "Omborda mavjud emas!"
    context = {
        "correct": correct,
        "incorrects": incorrects,

    }
    return render(request, "index.html", context)
