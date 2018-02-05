Sequel.migration do
  change do
     create_table(:inv_jrnl) do
      column :ij_id, :varchar, :size => 10
      column :ij_invent_, :varchar, :size => 30
      column :ij_order_n, :varchar, :size => 12
      column :ij_date, :date
      column :ij_type, :varchar, :size => 1
      column :ij_desc, :varchar, :size => 30
      column :ij_notes, :text
      column :ij_quantit, :float
      column :ij_unit_co, :float
      column :ij_ext_cos, :float
      column :ij_protect, :boolean
      column :ij_lo_code, :varchar, :size => 10
      column :ij_user_id, :varchar, :size => 5
      column :ij_last_mo, DateTime
      column :ij_prod_co, :varchar, :size => 2
      column :ij_dist_co, :varchar, :size => 2
      column :ij_order_2, :varchar, :size => 12
    end
  end
end
