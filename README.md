# django-gis-tutorial
This code is recreation of the official django gis tutorial.

### Setup:
This app uses PostgreSQL and PostGIS for data base operations. If you want to analyze the metadata of the shapefiles, you would also need to install the GDAL package. Consult your distro's docs and/or package manager for more info.

This app uses a Postgres user "admin". If you are using any other username, please replace "admin" in the following steps, and also in settings.py for the app. 
```bash
su - postgres
createuser admin
```

Now create a new database and load the default PostGIS template data in it:
```bash
createdb -U admin -O admin template_postgis -E UTF-8
createlang -U admin plpgsql template_postgis
psql -U admin -d template_postgis -f /usr/share/postgresql/contrib/postgis-2.1/postgis.sql
psql -U admin -d template_postgis -f /usr/share/postgresql/contrib/postgis-2.1/spatial_ref_sys.sql
```

Open up a PostgreSQL shell and mark this database as a template:
```bash
psql -U admin
>>> UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template_postgis';
```

Finally, create a new database using the template we just created, run the migrations on it and load the shape data into it:
```bash
createdb -U admin -T template_postgis geodb
python manage.py migrage
python load.py
```

### Running the app
This app features a cool django-admin page from the GeoDjango project for editing the country polygons. To see it in action, create a superuser account and login to django-admin using this account:
```python
python manage.py createsuperuser
python manage.py runserver
```
Now open up a web browser and browse to http://localhost:8000/admin/, and browse any of the WorldBorder objects. The map is editable, so be careful while saving!

This app also features a GET endpoint that accepts lat and lon as arguments and returns the country that contains the GEOS Geometry Object corresponding to the input lat/lon.

An error message is returned if either of lat or lon are not provided, or if they are not float convertible, or if no country is found that contains this point.

```bash
curl -X GET 'localhost:8000/gis/country?lat=12.936647&lon=77.613350'
{"status": "ok", "response": {"name": "India", "area": 297319, "lon": 78.5, "iso3": "IND", "iso2": "IN", "lat": 21.0, "id": 83}}
```
