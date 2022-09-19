from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hr hr mahadev")


def sarthak(request):
    questions = ["one", "two", "three", "four"]
    qno = 0
    if request.GET:
        qno = int(request.GET["qno"])


        qno += 1
    print(qno)
    if qno>=len(questions):
        question="Over"
    else:
        question = questions[qno]
    return render(request, "q.html",{"qno":qno,"qshow":qno+1,"question":question})
