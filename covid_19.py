import requests
from win10toast import ToastNotifier    #show notification in the notification area in window 10
import json  #fatch data from web site
import time


def update(url='www.google.com'):
    r = requests.get(url)
    data = r.json()
    text = f'conformed cases: {data["cases"]} \n Deaths{data["deaths"]} \n recoverd{'recoverd'}'
    while True:
        toast = ToastNotifier()
        toast.show_toast('covid-19 Update',text,duration=20)
        time.sleep(60)

update()