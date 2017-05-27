from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages

from django.utils import timezone
import json
from .models import Report, Time
# Create your views here.

def create_time(report):
    Time.objects.create(
        name = '05-06',
        report = report
    )
    Time.objects.create(
        name = '06-07',
        report = report
    )
    Time.objects.create(
        name = '07-08',
        report = report
    )
    Time.objects.create(
        name = '08-09',
        report = report
    )
    Time.objects.create(
        name = '09-10',
        report = report
    )
    Time.objects.create(
        name = '10-11',
        report = report
    )
    Time.objects.create(
        name = '11-12',
        report = report
    )
    Time.objects.create(
        name = '12-13',
        report = report
    )
    Time.objects.create(
        name = '13-14',
        report = report
    )
    Time.objects.create(
        name = '14-15',
        report = report
    )
    Time.objects.create(
        name = '15-16',
        report = report
    )
    Time.objects.create(
        name = '16-17',
        report = report
    )
    Time.objects.create(
        name = '17-18',
        report = report
    )
    Time.objects.create(
        name = '18-19',
        report = report
    )
    Time.objects.create(
        name = '19-20',
        report = report
    )
    Time.objects.create(
        name = '20-21',
        report = report
    )
    Time.objects.create(
        name = '21-22',
        report = report
    )
    Time.objects.create(
        name = '22-23',
        report = report
    )
    Time.objects.create(
        name = '23-24',
        report = report
    )


def IndexView(request):
    ctx = {}
    if request.method == "GET" :
        report_list = Report.objects.all()
        ctx.update({
            "report_list":report_list,
        })
    return render(request, 'tif/index.html', ctx)

def record(request):
    ctx = {}
    now = str(timezone.now())
    now = now[:11]
    #오늘 날찌 report 등록
    if now not in [report.name for report in Report.objects.all()]:
        report = Report.objects.create(
            name = now,
            created_date = timezone.now()
        )
        create_time(report)
    else:
        messages.warning(request, '해당 날짜의 report가 존재합니다!')
        # ctx.update({"message":"이미 오늘 날짜의 report가 존재합니다!"})
    return HttpResponseRedirect('/')


    # return HttpResponse('투표할 질문들을 보여주는 Index Page')
# def record(request, time_id):
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
