Sequel.migration do
  change do
     create_table(:ivetissu) do
      column :is_guid, :varchar, :size => 36
      column :is_date, DateTime
      column :is_order_n, :varchar, :size => 12
      column :is_rel_num, :integer
      column :is_op_num, :integer
      column :is_invent_, :varchar, :size => 30
      column :is_uom, :varchar, :size => 10
      column :is_quantit, :float
      column :is_emp_id, :varchar, :size => 5
      column :is_il_id, :varchar, :size => 10
      column :is_ib_id, :varchar, :size => 10
      column :is_lot_num, :varchar, :size => 20
      column :is_heat_nu, :varchar, :size => 30
      column :is_rev, :varchar, :size => 6
      column :is_rev_lev, :varchar, :size => 3
      column :is_tag_num, :integer
    end
  end
end
