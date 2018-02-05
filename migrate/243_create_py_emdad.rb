Sequel.migration do
  change do
     create_table(:py_emdad) do
      column :dd_id, :varchar, :size => 10
      column :dd_da_id, :varchar, :size => 10
      column :dd_occurs, :integer
      column :dd_desc, :varchar, :size => 30
      column :dd_inactiv, :boolean
    end
  end
end
