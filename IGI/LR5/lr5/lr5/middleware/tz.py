import zoneinfo
from django.utils import timezone
import requests
from django.http import HttpRequest
import logging


class TzMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        ip = request.META["REMOTE_ADDR"]
        try:
            location_data = requests.get(
                f'http://ip-api.com/json/{ip}', timeout=1).json()
        except:
            logging.warning("Timeout for determining timezone")
        try:
            tzname = location_data['timezone']
            request.session['django_timezone'] = tzname
            timezone.activate(zoneinfo.ZoneInfo(tzname))
        except:
            logging.warning(
                "Unable to determine user timezone, reverting to default (Europe/Minsk)")
            tzname = 'Europe/Minsk'
            request.session['django_timezone'] = tzname
        return self.get_response(request)
