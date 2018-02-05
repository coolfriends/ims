Sequel.migration do
  change do
     create_table(:partmat) do
      column :pm_id, :varchar, :size => 10
      column :pm_code, :varchar, :size => 2
      column :pm_desc, :varchar, :size => 30
    end
  end
end
