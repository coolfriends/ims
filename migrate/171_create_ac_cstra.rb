Sequel.migration do
  change do
     create_table(:ac_cstra) do
      column :cr_id, :varchar, :size => 10
      column :cr_calc, :varchar, :size => 70
      column :cr_name, :varchar, :size => 35
      column :cr_protect, :boolean
    end
  end
end
