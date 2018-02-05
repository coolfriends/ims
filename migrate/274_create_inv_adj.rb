Sequel.migration do
  change do
     create_table(:inv_adj) do
      column :ia_id, :varchar, :size => 10
      column :ia_invent_, :varchar, :size => 30
      column :ia_il_id, :varchar, :size => 10
      column :ia_ib_id, :varchar, :size => 10
      column :ia_quantit, :float
      column :ia_count, :float
      column :ia_adjust, :float
      column :ia_type, :varchar, :size => 1
      column :ia_date, :date
      column :ia_user_id, :varchar, :size => 5
      column :ia_ij_id, :varchar, :size => 10
      column :ia_batch_n, :integer
      column :ia_uom, :varchar, :size => 10
      column :ia_order_n, :varchar, :size => 12
      column :ia_lot_num, :varchar, :size => 20
      column :ia_heat_nu, :varchar, :size => 30
      column :ia_supp_co, :varchar, :size => 6
      column :ia_op_num, :integer
      column :ia_rev_num, :varchar, :size => 6
      column :ia_rev_lev, :varchar, :size => 3
      column :ia_adj_dat, :date
      column :ia_order_2, :varchar, :size => 12
      column :ia_unit_co, :float
      column :ia_ext_cos, :float
      column :ia_unit_ma, :float
      column :ia_unit_la, :float
      column :ia_unit_bu, :float
      column :ia_unit_ot, :float
      column :ia_po_num, :varchar, :size => 7
      column :ia_notes, :text
      column :ia_cust_co, :varchar, :size => 6
      column :ia_cust_c2, :varchar, :size => 6
      column :ia_melt_co, :text
      column :ia_color_c, :varchar, :size => 10
      column :ia_width1, :float
      column :ia_length1, :float
      column :ia_tag_num, :integer
      column :ia_unit_ty, :integer
      column :ia_expire_, :date
      column :ia_conditi, :varchar, :size => 20
    end
  end
end
