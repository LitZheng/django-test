from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from .models import Choice, Question
from django.views import generic
from django.utils import timezone


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request,"app1/index.html", context )


def user_list(request):
    #print(request.POST["QueryDict"])
    #print(type(request.POST["QueryDict"]))
    print(request.POST.dict())
    data_dict = request.POST.dict()
    return render(request, "user.html", {"data_dict": data_dict})

def pic(request):
    return render(request, "shiguang.html")

def detail(request, question_id):
    '''
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExit:
            raise Http404("Question does not exist")
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "app1/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "app1/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("app1:results", args=(question.id,)))


class IndexView(generic.ListView):
    template_name = "app1/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "app1/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "app1/results.html"

