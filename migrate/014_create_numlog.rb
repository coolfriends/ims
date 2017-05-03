Sequel.migration do
  change do
     create_table(:numlog) do
      column :nl_datetim, DateTime
      column :nl_source, :varchar, :size => 10
      column :nl_key, :varchar, :size => 30
      column :nl_user, :varchar, :size => 5
      column :nl_note, :varchar, :size => 80
    end
  end
end
