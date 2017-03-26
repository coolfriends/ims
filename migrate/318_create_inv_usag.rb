Sequel.migration do
  change do
     create_table(:inv_usag) do
      column :iu_jc_id, :varchar, :size => 10
      column :iu_item, :integer
      column :iu_invent_, :varchar, :size => 30
      column :iu_invent2, :varchar, :size => 30
      column :iu_qty, :float
      column :iu_calc, :varchar, :size => 2
      column :iu_heat_nu, :varchar, :size => 30
      column :iu_stock_u, :float
      column :iu_ppbar, :float
      column :iu_ij_id, :varchar, :size => 10
      column :iu_mat_cos, :float
      column :iu_ad_ij_i, :varchar, :size => 10
      column :iu_adjust_, :float
      column :iu_wip_val, :float
      column :iu_overrid, :boolean
      column :iu_length, :float
      column :iu_width, :float
      column :iu_il_id, :varchar, :size => 10
      column :iu_ib_id, :varchar, :size => 10
      column :iu_lot_num, :varchar, :size => 20
      column :iu_al_id, :varchar, :size => 10
      column :iu_return, :boolean
      column :iu_order_n, :varchar, :size => 12
      column :iu_rel_num, :integer
      column :iu_operati, :integer
      column :iu_emp_id, :varchar, :size => 5
      column :iu_run_dat, :date
      column :iu_ext_mat, :float
      column :iu_ext_lab, :float
      column :iu_ext_bur, :float
      column :iu_ext_oth, :float
      column :iu_rev_num, :varchar, :size => 3
      column :iu_rev_lev, :varchar, :size => 3
      column :iu_rework, :boolean
      column :iu_comment, :varchar, :size => 10
      column :iu_offset, :boolean
      column :iu_wp_id, :varchar, :size => 10
      column :iu_tag_num, :integer
      column :iu_user_id, :varchar, :size => 5
      column :iu_transti, :datetime
      column :iu_remwidt, :float
      column :iu_remleng, :float
      column :iu_remquan, :integer
      column :iu_unit_co, :float
    end
  end
end
