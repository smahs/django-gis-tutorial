import os, sys, django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'djgis.settings'
django.setup()

from django.conf import settings
from django.contrib.gis.utils import LayerMapping
from world.models import WorldBorder

world_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'world/data/TM_WORLD_BORDERS-0.3.shp'))


def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping,
                      transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)


if __name__ == "__main__":
    run()
