Sequel.migration do
  change do
     create_table(:ship_det) do
      column :sd_id, :integer
      column :sd_ship_co, :varchar, :size => 8
      column :sd_ship_da, :date
      column :sd_order_n, :varchar, :size => 12
      column :sd_rel_num, :integer
      column :sd_rel_dat, :date
      column :sd_rel_qty, :float
      column :sd_order_s, :varchar, :size => 1
      column :sd_unit_ty, :integer
      column :sd_invent_, :varchar, :size => 30
      column :sd_part_nu, :varchar, :size => 30
      column :sd_rev_num, :varchar, :size => 6
      column :sd_desc, :varchar, :size => 50
      column :sd_pmemo, :text
      column :sd_ship_no, :text
      column :sd_po_num, :varchar, :size => 25
      column :sd_ship_c2, :boolean
      column :sd_sb1, :integer
      column :sd_sb2, :integer
      column :sd_sb3, :integer
      column :sd_sb4, :integer
      column :sd_sb5, :integer
      column :sd_eb1, :integer
      column :sd_eb2, :integer
      column :sd_eb3, :integer
      column :sd_eb4, :integer
      column :sd_eb5, :integer
      column :sd_bq1, :float
      column :sd_bq2, :float
      column :sd_bq3, :float
      column :sd_bq4, :float
      column :sd_bq5, :float
      column :sd_tb1, :integer
      column :sd_tb2, :integer
      column :sd_tb3, :integer
      column :sd_tb4, :integer
      column :sd_tb5, :integer
      column :sd_weight1, :float
      column :sd_weight2, :float
      column :sd_weight3, :float
      column :sd_weight4, :float
      column :sd_weight5, :float
      column :sd_totw1, :float
      column :sd_totw2, :float
      column :sd_totw3, :float
      column :sd_totw4, :float
      column :sd_totw5, :float
      column :sd_totp1, :float
      column :sd_totp2, :float
      column :sd_totp3, :float
      column :sd_totp4, :float
      column :sd_totp5, :float
      column :sd_tot_qty, :float
      column :sd_bo_qty, :float
      column :sd_tot_wei, :float
      column :sd_tot_box, :integer
      column :sd_tare, :float
      column :sd_tare_ty, :varchar, :size => 1
      column :sd_gt_tare, :float
      column :sd_tot_car, :integer
      column :sd_weight, :float
      column :sd_gt_weig, :float
      column :sd_num_car, :integer
      column :sd_num_ski, :integer
      column :sd_derive_, :boolean
      column :sd_sord_nu, :varchar, :size => 7
      column :sd_sord_re, :integer
      column :sd_ij_id, :varchar, :size => 10
      column :sd_sord_r2, :integer
      column :sd_sord_r3, :date
      column :sd_sord_co, :boolean
      column :sd_sord_st, :varchar, :size => 1
      column :sd_return, :boolean
      column :sd_il_id, :varchar, :size => 10
      column :sd_ib_id, :varchar, :size => 10
      column :sd_contact, :varchar, :size => 25
      column :sd_il_id_f, :varchar, :size => 10
      column :sd_ib_id_f, :varchar, :size => 10
      column :sd_lot_shi, :varchar, :size => 20
      column :sd_so_unit, :varchar, :size => 4
      column :sd_heat_nu, :varchar, :size => 30
      column :sd_lot_num, :varchar, :size => 20
      column :sd_user_id, :varchar, :size => 5
      column :sd_last_mo, DateTime
      column :sd_dont_po, :boolean
      column :sd_cm_flag, :varchar, :size => 1
      column :sd_cm_num, :varchar, :size => 7
      column :sd_select_, :boolean
      column :sd_exp_pro, :varchar, :size => 40
      column :sd_exp_tar, :varchar, :size => 20
      column :sd_exp_cnt, :varchar, :size => 20
      column :sd_exp_par, :boolean
      column :sd_exp_con, :boolean
      column :sd_exp_dut, :integer
      column :sd_exp_exp, :varchar, :size => 80
      column :sd_exp_pri, :boolean
      column :sd_exp_pr2, :boolean
      column :sd_exp_pr3, :boolean
      column :sd_complet, :boolean
      column :sd_length, :float
      column :sd_width, :float
      column :sd_quantit, :float
      column :sd_wght, :float
      column :sd_rev_nu2, :varchar, :size => 3
      column :sd_rev_lev, :varchar, :size => 3
      column :sd_who_res, :varchar, :size => 10
      column :sd_how_res, :integer
      column :sd_ls_code, :varchar, :size => 10
      column :sd_lo_code, :varchar, :size => 10
      column :sd_cert_no, :text
      column :sd_sord_r4, :integer
      column :sd_bt_code, :varchar, :size => 3
      column :sd_noresup, :boolean
      column :sd_receive, :varchar, :size => 12
      column :sd_transfe, :boolean
      column :sd_bl1, :float
      column :sd_bl2, :float
      column :sd_bl3, :float
      column :sd_bl4, :float
      column :sd_bl5, :float
      column :sd_bw1, :float
      column :sd_bw2, :float
      column :sd_bw3, :float
      column :sd_bw4, :float
      column :sd_bw5, :float
      column :sd_bd1, :float
      column :sd_bd2, :float
      column :sd_bd3, :float
      column :sd_bd4, :float
      column :sd_bd5, :float
    end
  end
end
