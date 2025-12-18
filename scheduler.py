# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler

def remove_expired_users():
    pass  # DB check + kick user

scheduler = BackgroundScheduler()
scheduler.add_job(remove_expired_users, 'interval', hours=1)
scheduler.start()
