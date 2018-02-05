Sequel.migration do
  change do
     create_table(:insphead) do
      column :ih_id, :varchar, :size => 10
      column :ih_type, :varchar, :size => 1
      column :ih_al_id, :varchar, :size => 10
      column :ih_invent_, :varchar, :size => 30
      column :ih_date, :date
      column :ih_part_nu, :varchar, :size => 30
      column :ih_rev_num, :varchar, :size => 3
      column :ih_part_de, :varchar, :size => 50
      column :ih_lot_qty, :integer
      column :ih_lot_num, :varchar, :size => 20
      column :ih_cust_co, :varchar, :size => 6
      column :ih_cust_na, :varchar, :size => 33
      column :ih_po_num, :varchar, :size => 15
      column :ih_order_n, :varchar, :size => 12
      column :ih_inspect, :varchar, :size => 15
      column :ih_inspec2, :varchar, :size => 35
      column :ih_inv_rev, :varchar, :size => 3
      column :ih_rev_lev, :varchar, :size => 3
      column :ih_heat_nu, :varchar, :size => 20
    end
  end
end
