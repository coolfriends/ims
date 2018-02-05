Sequel.migration do
  change do
     create_table(:py_emdas) do
      column :da_id, :varchar, :size => 10
      column :da_desc, :varchar, :size => 30
      column :da_freq, :varchar, :size => 1
      column :da_inactiv, :boolean
    end
  end
end
