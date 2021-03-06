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
        if request.user.is_authenticated():
            print(request.user.username)
            report_list = Report.objects.filter(user = request.user).order_by('-created_date')
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
            user = request.user,
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
    # 삭제하고 다시 저장
    time.activity.clear()
    time.feeling.clear()

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

    feeling_list = request.POST.getlist('feeling')
    for f in feeling_list:
        print('-------------------'+f+'-------------------')
        feeling = Feeling.objects.get(feeling = f )
        time.feeling.add(feeling)
    return redirect('/')

    return render(request, 'tif/index.html')

# def time_data(request):
#     time_id = request.GET.get('timeId')
#     time = get_object_or_404(Time, pk=time_id)
#     if request.method == "GET":
#         # Partnerform 객체 생성
#         print('----------'+time.id+'-------------')
#         result = {
#             'title': memo.title,
#             'content':memo.content
#         }
#         result = json.dumps(result)
#
#     return HttpResponse(result)

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

def time_data(request):
    time_id = request.GET.get('timeId')
    time = get_object_or_404(Time, pk=time_id)
    result = []
    if request.method == "GET":
        for activity in time.activity.all():
            print('----------'+activity.content+'-------------')
            result.append({
                'activity' : activity.content
            })
        for feeling in time.feeling.all():
            result.append({
                'feeling' : feeling.feeling
            })

    result = json.dumps(result)

    return HttpResponse(result)
