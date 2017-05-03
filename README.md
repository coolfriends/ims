
### Create the db user
```
sudo su - postgres
createuser -P ims
```

### Create the db
```
sudo su - postgres
createdb -O ims ims
```
### Create the db schema migrations (table data must exist in data/\*.dbf)
```
ruby bin/migrations.rb
```

### Fix the created migrations
```
sed -i -e 's/:datetime$/DateTime/' migrate/*.rb
sed -i -e 's/:binary$/:bytea/' migrate/*.rb
```

### Migrate the schema
```
sequel -m ./migrate postgres://ims:<password>@localhost/ims
```

### Import the data (TODO)
```
ruby bin/import_data.rb
```

### Generate new models.py
```
python manage.py inspectdb > reports/models.py
```




