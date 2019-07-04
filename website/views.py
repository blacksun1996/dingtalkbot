from django.shortcuts import render,HttpResponse
from website.tasks import start_running
# Create your views here.

#celery 测试
def get(request):
    print('>=====开始发送请求=====<')
    start_running.delay('发送短信')
    # start_running.apply_async(('发送短信',), countdown=10)  # 10秒后再执行异步任务
    return HttpResponse('<h2> 请求已发送 </h2>')