from apscheduler.schedulers.blocking import BlockingScheduler
from automation import send_msg

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_msg, 'interval', seconds=5)

sched.start()