# django-gis-tutorial
This code is recreation of the official django gis tutorial.

Setup PostGIS:
I am using "admin" user for any PostGIS operations in this app. So create a user.
```bash
su - postgres
createuser admin
```

Now create a database template:
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
