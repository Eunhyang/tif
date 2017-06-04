from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages

from django.utils import timezone
import json
from .models import Report, Time, Activity, Feeling, Memo
from .forms import MemoForm
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
        report_list = Report.objects.all().order_by('-created_date')
        activity_list = Activity.objects.all()
        feeling_list = Feeling.objects.all()

        memo_form = MemoForm()

        ctx.update({
            "report_list":report_list,
            "activity_list":activity_list,
            "feeling_list":feeling_list,
            "memo_form":memo_form,
        })
    return render(request, 'tif/index.html', ctx)

def report_add(request):
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

def report_delete(request, report_id):
    report = Report.objects.get(id = report_id)
    report.delete()
    return redirect("/")

def record(request):
    ctx = {}
    time_id = request.POST.get('timeId')
    print('----------'+time_id+'-------------')
    time = get_object_or_404(Time, pk=time_id)

    activity_set = ([])
    activity_set = request.POST.get('activity').split()
    for activity_cont in activity_set:
        print('-------------------'+activity_cont+'-------------------')
        if activity_cont not in [activity.content for activity in Activity.objects.all()]:
            activity = Activity.objects.create(content = activity_cont)
            time.activity.add(activity.id)
        else :
            activity = Activity.objects.get(content = activity_cont)
            time.activity.add(activity.id)

    feeling_set = request.POST.getlist('feeling')
    for f in feeling_set:
        print('-------------------'+f+'-------------------')
        feeling = Feeling.objects.get(feeling = f )
        time.feeling.add(feeling)

    return render(request, 'tif/index.html')

def memo_add(request):
    ctx = {}
    time_id = request.POST.get('timeId')
    print('----------'+time_id+'-------------')
    time = get_object_or_404(Time, pk=time_id)

    memo_form = MemoForm(request.POST)

    if memo_form.is_valid():
        memo = memo_form.save(commit = False)
        memo.time = time
        memo.save()
        return redirect('/')

    return render(request, 'tif/index.html')

def memo_data(request):
    memo_id = request.GET.get('memoId')
    memo = get_object_or_404(Memo, pk=memo_id)
    if request.method == "GET":
        # Partnerform 객체 생성
        print('----------'+memo.title+'-------------')
        memo_form = MemoForm(instance = memo)
        result = {
            'title': memo.title,
            'content':memo.content
        }
        result = json.dumps(result)

    return HttpResponse(result)

def memo_edit(request):
    memo_id = request.POST.get('memoId')
    memo = get_object_or_404(Memo, pk=memo_id)
    # print('----------'+memo.id+'-------------')
    title = request.POST.get('title')
    content = request.POST.get('content')
    memo.title = title
    memo.content = content
    memo.save()
    return redirect('/')

    # elif request.method == "POST":
    #     memo_form = MemoForm(request.POST,instance=memo)
    #     if menu_form.is_valid():
    #         menu = menu_form.save(commit = False)
    #         menu.partner = request.user.partner
    #         menu.save()
    #         return redirect("/partner/menu/" + menu_id)
    #     else:
    #         ctx.update({"menu_form":menu_form})

    # return render(request, "menu_add.html", ctx)

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
