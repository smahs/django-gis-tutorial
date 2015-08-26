from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.gis.geos import Point
from json import dumps
from models import WorldBorder


class JSONBaseView(View):

    def send_error(self, e):
        return HttpResponse(dumps({
            'error': e,
            'status': 'error'
        }), content_type="application/json")

    def send_json(self, context):
        return HttpResponse(dumps({
            "status": "ok",
            "response": context
        }), content_type="application/json")


class GetCountryByLL(JSONBaseView):
    keys = ["area", "lat", "lon", "iso2", "iso3", "name", "id"]

    def get(self, request):
        if 'lat' not in request.GET or 'lon' not in request.GET:
            msg = "This endpoint requires lat and lon as input"
            return self.send_error(msg)
        lat = request.GET['lat']
        lon = request.GET['lon']
        try:
            pnt = Point(float(lon), float(lat))
            sm = WorldBorder.objects.get(mpoly__intersects=pnt)
            return self.send_json({i: sm.__dict__[i] for i in self.keys})
        except (WorldBorder.DoesNotExist, ValueError):
            msg = "No country found for given lat and lng."
            return self.send_error(msg)
