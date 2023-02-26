from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api


"""Функция, добавляющая новые посты в БД в интервале 3 часов """
def start():
    sche = BackgroundScheduler()
    sche.add_job(schedule_api, 'interval', hours=8)
    sche.start()