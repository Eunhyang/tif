from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import json
from .models import Report, Time
# Create your views here.

def IndexView(request):
    ctx = {}
    if request.method == "GET" :
        report_list = Report.objects.all()
        ctx.update({
            "report_list":report_list,
        })
    return render(request, 'tif/index.html', ctx)

    # return HttpResponse('투표할 질문들을 보여주는 Index Page')
def record(request, time_id):
    # ctx = {}
    # time = get_object_or_404(Time, pk=time_id)
    #
    # activity_set = ([])
    # activity = request.POST.get('activity')
    # activity_set = activity.split()
    # for activity in activity_set:
    #     if activity not in [activity.content for activity in Activity.objects.all()]:
    #         HashTag.objects.create(
    #             content = activity
    #         )
    # time.activity.add(activity)
    #
    # feeling_set = request.POST.get('feeling')
    # for feeling in feeling_set:
    #     Feeling.objects.create(
    #         feeling = feeling
    #     )
    # time.feeling.add(feeling)
    pass


# def DetailView(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#     # return HttpResponse('{} 질문의 제목, 그리고 선택지들을 보여주는 Detail Page'.format(question_id))
#
# def ResultView(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/result.html', {'question': question})
#
#     # return HttpResponse('{} 해당 질문을 투표한 후, 결과를 보여주는 Result Page'.format(question_id))
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     selected_choice.votes += 1
#     selected_choice.save()
#     return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))
#
#     # return HttpResponse('{} 지금 투표하기 기능을 실행중입니다'.format(question_id))
#
# def vote_data(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     result = []
#
#     for choice in question.choice_set.all():
#         result.append({
#             'choice_text': choice.choice_text,
#             'votes': choice.votes,
#         })
#     result = json.dumps(result)
#
#     return HttpResponse(result)
