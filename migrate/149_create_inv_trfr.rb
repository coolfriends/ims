Sequel.migration do
  change do
     create_table(:inv_trfr) do
      column :tf_id, :varchar, :size => 10
      column :tf_invent_, :varchar, :size => 30
      column :tf_date, :date
      column :tf_quantit, :float
      column :tf_il_id, :varchar, :size => 10
      column :tf_il_id_2, :varchar, :size => 10
      column :tf_ib_id, :varchar, :size => 10
      column :tf_ib_id_2, :varchar, :size => 10
      column :tf_order_n, :varchar, :size => 12
      column :tf_order_2, :varchar, :size => 12
      column :tf_lot_num, :varchar, :size => 20
      column :tf_lot_nu2, :varchar, :size => 20
      column :tf_heat_nu, :varchar, :size => 30
      column :tf_heat_n2, :varchar, :size => 30
      column :tf_user_id, :varchar, :size => 5
      column :tf_user_da, :date
      column :tf_type, :varchar, :size => 1
      column :tf_op_num, :integer
      column :tf_op_num_, :integer
      column :tf_jc_id, :varchar, :size => 10
      column :tf_lot_dat, :date
      column :tf_lot_da2, :date
      column :tf_unit_co, :float
      column :tf_unit_ma, :float
      column :tf_unit_la, :float
      column :tf_unit_bu, :float
      column :tf_unit_ot, :float
      column :tf_rev_num, :varchar, :size => 3
      column :tf_rev_nu2, :varchar, :size => 3
      column :tf_rev_lev, :varchar, :size => 3
      column :tf_rev_le2, :varchar, :size => 3
      column :tf_tag_num, :integer
      column :tf_tag_nu2, :integer
    end
  end
end
