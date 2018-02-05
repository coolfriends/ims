Sequel.migration do
  change do
     create_table(:state) do
      column :st_id, :varchar, :size => 10
      column :st_co_id, :varchar, :size => 10
      column :st_name, :varchar, :size => 25
      column :st_code, :varchar, :size => 3
    end
  end
end
