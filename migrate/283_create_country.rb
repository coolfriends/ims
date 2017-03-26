Sequel.migration do
  change do
     create_table(:country) do
      column :co_id, :varchar, :size => 10
      column :co_name, :varchar, :size => 25
      column :co_exclude, :boolean
    end
  end
end
