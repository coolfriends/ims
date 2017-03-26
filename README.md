
After running bin/migrations.rb

```
sed -i -e 's/:datetime/DateTime' migrate/*.rb
sed -i -e 's/:binary/:bytea/' migrate/360_create_vshop.rb
```

Then fix migrate/075\*.rb, it has a column named datetime.

