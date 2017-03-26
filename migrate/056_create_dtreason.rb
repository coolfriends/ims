Sequel.migration do
  change do
     create_table(:dtreason) do
      column :dr_code, :varchar, :size => 5
      column :dr_desc, :varchar, :size => 30
    end
  end
end
