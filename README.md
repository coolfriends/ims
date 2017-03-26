
After running bin/migrations.rb

```
sed -i -e 's/:datetime/DateTime' migrate/*.rb
```

Then fix migrate/075\*.rb, it has a column named datetime.
