Sequel.migration do
  change do
     create_table(:nmfc) do
      column :nm_code, :varchar, :size => 10
      column :nm_desc, :varchar, :size => 40
      column :nm_class, :varchar, :size => 10
    end
  end
end
