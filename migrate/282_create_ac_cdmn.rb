Sequel.migration do
  change do
     create_table(:ac_cdmn) do
      column :mn_id, :varchar, :size => 10
      column :mn_type, :varchar, :size => 1
      column :mn_ca_code, :varchar, :size => 12
      column :mn_date, :date
      column :mn_cknum, :varchar, :size => 10
      column :mn_supp_co, :varchar, :size => 6
      column :mn_supp_na, :varchar, :size => 30
      column :mn_rem_add, :text
      column :mn_dr_amou, :decimal, :precision => 15, :scale => 4
      column :mn_cr_amou, :decimal, :precision => 15, :scale => 4
      column :mn_user, :varchar, :size => 5
      column :mn_entry_d, :date
      column :mn_reconci, :varchar, :size => 1
      column :mn_post, :boolean
      column :mn_post_da, :date
      column :mn_amount, :decimal, :precision => 15, :scale => 4
      column :mn_gl_id, :varchar, :size => 10
      column :mn_entry_t, :varchar, :size => 1
      column :mn_referen, :varchar, :size => 30
      column :mn_status, :varchar, :size => 1
      column :mn_ca_cod2, :varchar, :size => 12
      column :mn_print_d, :date
      column :mn_gl_id_2, :varchar, :size => 10
      column :mn_oc_amou, :decimal, :precision => 15, :scale => 4
      column :mn_oc_bala, :decimal, :precision => 15, :scale => 4
      column :mn_mn_id, :varchar, :size => 10
      column :mn_rg_id, :varchar, :size => 10
      column :mn_marked, :boolean
      column :mn_1099, :boolean
      column :mn_new_for, :boolean
      column :mn_st_id_1, :varchar, :size => 10
      column :mn_st_id_2, :varchar, :size => 10
      column :mn_stax_id, :varchar, :size => 25
      column :mn_tax_exe, :boolean
      column :mn_exempt_, :varchar, :size => 30
      column :mn_cur_cod, :varchar, :size => 10
      column :mn_cur_rat, :float
      column :mn_cur, :float
      column :mn_dr_cur, :float
      column :mn_cr_cur, :float
      column :mn_ap_id, :varchar, :size => 10
      column :mn_po_num, :varchar, :size => 7
      column :mn_lo_code, :varchar, :size => 10
      column :mn_number, :varchar, :size => 30
      column :mn_1099_box, :varchar, :size => 2
      column :mn_cur_amo, :decimal, :precision => 15, :scale => 4
      column :mn_ca_cur_, :varchar, :size => 12
      column :mn_gl_id_c, :varchar, :size => 10
      column :mn_check_m, :varchar, :size => 30
      column :mn_manual, :boolean
      column :mn_dm_dd_i, :varchar, :size => 10
      column :mn_cc_supp, :varchar, :size => 6
      column :mn_cust_co, :varchar, :size => 6
      column :mn_rec_dat, :date
      column :mn_emp_id, :varchar, :size => 5
      column :mn_user_id, :varchar, :size => 5
      column :mn_exclude, :boolean
      column :mn_lm_user, :varchar, :size => 5
      column :mn_lm_date, :datetime
    end
  end
end
