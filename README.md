# django-gis-tutorial
This code is recreation of the official django gis tutorial.

### Setup:
Install PostgreSQL and PostGIS for data base. If you want to analyze the metadata of the shapefiles, you would also need to install the GDAL package. Consult your distro's documentation for doing this.

This app assumes an "admin" user for any PostGIS operations. If you are using any other username, do not forget to replace "admin" everywhere in the following steps, and also in settings.py for the app. 
```bash
su - postgres
createuser admin
```

Now create a new database and load it with postgis default template data:
```bash
createdb -U admin -O admin template_postgis -E UTF-8
createlang -U admin plpgsql template_postgis
psql -U admin -d template_postgis -f /usr/share/postgresql/contrib/postgis-2.1/postgis.sql
psql -U admin -d template_postgis -f /usr/share/postgresql/contrib/postgis-2.1/spatial_ref_sys.sql
```

Open up the PostgreSQL shell and mark this database as a template:
```bash
psql -U admin
>>> UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template_postgis';
```

Finally, create a new database using the template we just created, run the migrations and load the shape data into the database:
```bash
createdb -U admin -T template_postgis geodb
python manage.py migrage
python load.py
```
