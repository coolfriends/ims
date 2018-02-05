Sequel.migration do
  change do
     create_table(:inv_cost) do
      column :ic_id, :varchar, :size => 10
      column :ic_ij_id, :varchar, :size => 10
      column :ic_il_id, :varchar, :size => 10
      column :ic_ib_id, :varchar, :size => 10
      column :ic_invent_, :varchar, :size => 30
      column :ic_supp_co, :varchar, :size => 6
      column :ic_heat_nu, :varchar, :size => 30
      column :ic_order_n, :varchar, :size => 12
      column :ic_date, :date
      column :ic_notes, :text
      column :ic_quantit, :float
      column :ic_unit_co, :float
      column :ic_ext_cos, :float
      column :ic_order_2, :varchar, :size => 12
      column :ic_tr_date, :date
      column :ic_tr_il_i, :varchar, :size => 10
      column :ic_tr_ib_i, :varchar, :size => 10
      column :ic_tr_orde, :varchar, :size => 12
      column :ic_tr_user, :varchar, :size => 5
      column :ic_tr_use2, :date
      column :ic_tr_quan, :float
      column :ic_tr_ship, :varchar, :size => 8
      column :ic_tr_sd_i, :integer
      column :ic_lot_num, :varchar, :size => 20
      column :ic_unit_ma, :float
      column :ic_unit_la, :float
      column :ic_unit_bu, :float
      column :ic_unit_ot, :float
      column :ic_image_p, :varchar, :size => 60
      column :ic_tr_lot_, :varchar, :size => 20
      column :ic_op_num, :integer
      column :ic_tr_op_n, :integer
      column :ic_width1, :float
      column :ic_width2, :float
      column :ic_length1, :float
      column :ic_length2, :float
      column :ic_rev_num, :varchar, :size => 6
      column :ic_rev_lev, :varchar, :size => 3
      column :ic_tr_rev_, :varchar, :size => 3
      column :ic_tr_rev2, :varchar, :size => 3
      column :ic_tr_heat, :varchar, :size => 30
      column :ic_std_mat, :float
      column :ic_std_lab, :float
      column :ic_std_bur, :float
      column :ic_std_oth, :float
      column :ic_std_uni, :float
      column :ic_cust_co, :varchar, :size => 6
      column :ic_cust_c2, :varchar, :size => 6
      column :ic_melt_co, :text
      column :ic_color_c, :varchar, :size => 10
      column :ic_po_num, :varchar, :size => 7
      column :ic_tag_num, :integer
      column :ic_conditi, :varchar, :size => 20
      column :ic_expire_, :date
      column :ic_id_pare, :varchar, :size => 10
      column :ic_roll, :varchar, :size => 20
      column :ic_tr_tag_, :integer
      column :ic_rem_qty, :integer
    end
  end
end
