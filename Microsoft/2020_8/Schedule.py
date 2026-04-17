"""
Cron parser: return the next runtime nearest to the current time based on the schedule
min hour dayofweek
0   6   6
30  17   1

"""
from datetime import datetime, timedelta


def get_next_run_time(schedules):
    if schedules == []: return ""
    candidates = []
    now = datetime.now()
    for m,h,d in schedules:
        days = (d-now.isoweekday()) % 7
        t = now.replace(hour=h,minute=m,second=0,microsecond=0) + timedelta(days=days)
        if t<=now:
            t+=timedelta(days=7)
        print(t)
        candidates.append(t)
    return min(candidates)

def get_next_run_time2(schedules):
    if schedules == []: return ""
    now = datetime.now()
    def next_time(min,hour,weekday):
        candidate = now.replace(hour=hour,minute=min,second=0,microsecond=0)
        delta_days = (weekday-now.isoweekday()) % 7
        candidate += timedelta(delta_days)
        if candidate < now:
            candidate += timedelta(7)
        return candidate
    return (min(next_time(*s) for s in schedules))


if __name__=="__main__":
    schedules=[(0,6,6),(30,17,1)]
    next_run_time = get_next_run_time(schedules)
    print(next_run_time)
    next_run_time2 = get_next_run_time2(schedules)
    print(next_run_time2)