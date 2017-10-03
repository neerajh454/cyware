from usersearch.models import *
from datetime import datetime
from django.db.models import Count, Min, Sum, Avg

def run_cron_every_day():
    today_date = datetime.now().date()
    key = "added_per_day_users"
    value = UserDetails.objects.filter(created_at=today_date).count()
    all_hits = Hits.objects.get_or_create(key=key, created_at=today_date, value=value)


def run_cron_every_sunday():
    today_date = datetime.now().date()
    seven_days = datetime.now().date() - timedelta(days=6)
    key = "added_per_week_users"
    value = UserDetails.objects.filter(created_at__gte=seven_days).count()
    all_hits = Hits.objects.get_or_create(key=key, created_at=today_date, value=value)
    key = "hits_per_week_on_url"
    value = Hits.objects.filter(key="hit_url_per_day", created_at__gte=seven_days).aggregate(Sum('value'))['value__sum']
    all_hits = Hits.objects.get_or_create(key=key, created_at=today_date, value=value)


