from dingtalkbot.celery import app

@app.task
def start_running(info):
    print(info)
    print('--->>开始执行任务<<---')
    print('比如发送短信或邮件')
    print('>---任务结束---<')
