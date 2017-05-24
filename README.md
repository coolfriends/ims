
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

### Import the data
```
ruby bin/import_data.rb
```

### Generate new models.py (if needed)
* run from ims/ims
```
python manage.py inspectdb > reports/models.py
```

### Run Django server and access report
* run from ims/ims
```
python manage.py runserver
```
* In a web-browser, navigate to http://127.0.0.1:8000/reports/sales_invoice_order_report/2722 by default to access the report (where 2722 is the sales order number)



