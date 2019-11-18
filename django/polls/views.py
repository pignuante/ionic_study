from django.http import HttpResponse


# Create your views here.
def index(requests):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse(
        "You're looking at question {question_id}".format(question_id=question_id)
    )


def results(request, question_id):
    response = "You're looking at the result of question {question_id}".format(
        question_id=question_id
    )
    return HttpResponse(
        response
    )


def vote(request, question_id):
    response = "You're voting on question {question_id}".format(question_id=question_id)
    return HttpResponse(
        response
    )
