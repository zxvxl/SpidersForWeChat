import os
import Queue
import time
import threading
import schedule
from scrapy import cmdline
cmdline.execute("scrapy crawl test".split())

def spider():
    os.system("scrapy crawl wx")


def worker_main():
    while 1:
        job_func = jobqueue.get()
        job_func()

jobqueue = Queue.Queue()

schedule.every(10).seconds.do(jobqueue.put, spider)
#schedule.every(10).seconds.do(jobqueue.put, spider)

worker_thread = threading.Thread(target=worker_main)
worker_thread.start()

while 1:
    schedule.run_pending()
    time.sleep(1)
