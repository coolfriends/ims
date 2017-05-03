Sequel.migration do
  change do
     create_table(:et_sys) do
      column :es_group, :varchar, :size => 10
      column :es_counter, :integer
    end
  end
end
