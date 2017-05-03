Sequel.migration do
  change do
     create_table(:ac_terms) do
      column :te_desc, :varchar, :size => 20
      column :te_type, :integer
      column :te_netdays, :integer
      column :te_disdays, :integer
      column :te_disper, :float
      column :te_day, :integer
      column :te_export_, :varchar, :size => 31
    end
  end
end
