Sequel.migration do
  change do
     create_table(:py_ethnc) do
      column :pe_code, :varchar, :size => 6
      column :pe_desc, :varchar, :size => 30
    end
  end
end
