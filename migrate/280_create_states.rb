Sequel.migration do
  change do
     create_table(:states) do
      column :st_id, :varchar, :size => 2
      column :st_name, :varchar, :size => 25
      column :st_country, :varchar, :size => 15
    end
  end
end
