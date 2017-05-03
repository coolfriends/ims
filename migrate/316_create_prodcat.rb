Sequel.migration do
  change do
     create_table(:prodcat) do
      column :pc_prod_co, :varchar, :size => 5
      column :pc_prod_de, :varchar, :size => 30
      column :pc_dv_code, :varchar, :size => 2
      column :pc_dp_code, :varchar, :size => 2
    end
  end
end
