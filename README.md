Note: All steps performed from root project directory unless otherwise specified

### Create the db user and the db
```
sudo su - postgres
createuser -P ims
createdb -O ims ims
```
You can exit the postgres user shell after this step.

### Obtain IMS data
Talk to Jordan or Kyri for data, it will be in a .tar.gz

### Extract IMS data
```
cd /path/to/data
tar -xzf im_data.tar.gz
```

### Possible necessary dependencies
A few dependencies you might need to complete further steps (required on Ubuntu 16.04):
```
sudo apt-get install libsqlite3-dev libpq-dev postgresql-server-dev-9.5
```

### Install dependencies from Gemfile
```
bundle install
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
This step will take a while.
```
ruby bin/import_data.rb
```

### Install python dependencies (if using virtual environment, make sure it is activated prior to this step)
```
pip install requirements.txt
```

### Generate new models.py (not necessary unless DB has been changed/updated)
* run from ims/ims
```
python manage.py inspectdb > reports/models.py
```

### Open python shell to interact with DB
* run from ims/ims
```
python ./manage.py shell
```
Check that Sord object contains records
```
from reports.models import Sord
Sord.objects.all()
```

### Run Django server and access report
* run from ims/ims
```
python manage.py runserver
```
* In a web-browser, navigate to http://127.0.0.1:8000/reports/sales_invoice_order_report/ and enter a sales order number

