Sequel.migration do
  change do
     create_table(:order) do
      column :or_order_n, :varchar, :size => 12
      column :or_ord_dat, :date
      column :or_quote_n, :varchar, :size => 15
      column :or_unit_ty, :varchar, :size => 4
      column :or_po_num, :varchar, :size => 25
      column :or_ord_sta, :varchar, :size => 1
      column :or_part_nu, :varchar, :size => 30
      column :or_rev_num, :varchar, :size => 6
      column :or_part_de, :varchar, :size => 50
      column :or_pmemo, :text
      column :or_cust_co, :varchar, :size => 6
      column :or_emp_id, :varchar, :size => 5
      column :or_scomm, :float
      column :or_runs, :integer
      column :or_lastop, :integer
      column :or_ord_not, :text
      column :or_up_date, :date
      column :or_qty_ord, :float
      column :or_qty_car, :integer
      column :or_qty_ret, :integer
      column :or_qty_shi, :integer
      column :or_qty_pro, :float
      column :or_qty_bal, :float
      column :or_qty_inv, :float
      column :or_ht, :float
      column :or_pl, :float
      column :or_tool, :float
      column :or_misc, :float
      column :or_ov, :float
      column :or_ottool, :float
      column :or_otgage, :float
      column :or_otcolle, :float
      column :or_otmisc, :float
      column :or_ht_note, :text
      column :or_pl_note, :text
      column :or_ppbar1, :float
      column :or_act_ppb, :integer
      column :or_tsu1, :integer
      column :or_tsu2, :integer
      column :or_tsu3, :integer
      column :or_tsu4, :integer
      column :or_tsu5, :integer
      column :or_tsu6, :integer
      column :or_tsu7, :integer
      column :or_tsu8, :integer
      column :or_tsu9, :integer
      column :or_tsu10, :integer
      column :or_cpu, :float
      column :or_weight, :float
      column :or_change_, :varchar, :size => 15
      column :or_qtq, :integer
      column :or_require, :integer
      column :or_buyer, :varchar, :size => 20
      column :or_spec_po, :text
      column :or_cust_s_, :boolean
      column :or_n_des_t, :boolean
      column :or_n_des_n, :text
      column :or_os_proc, :text
      column :or_spec_pk, :text
      column :or_cert_re, :text
      column :or_mat_spe, :text
      column :or_os_pr_s, :text
      column :or_spec_ma, :text
      column :or_dt_r_po, :date
      column :or_po_type, :integer
      column :or_cor_bp_, :boolean
      column :or_dt_pb_r, :date
      column :or_mat_on_, :boolean
      column :or_dt_moh_, :date
      column :or_dt_moh2, :date
      column :or_sketch_, :boolean
      column :or_rout_bo, :boolean
      column :or_dt_prg_, :date
      column :or_dt_tol_, :date
      column :or_dt_tol2, :date
      column :or_dt_gag_, :date
      column :or_dt_gag2, :date
      column :or_dt_rel_, :date
      column :or_reviewe, :varchar, :size => 30
      column :or_dt_rev, :date
      column :or_mat, :float
      column :or_lot, :varchar, :size => 20
      column :or_induct_, :integer
      column :or_induct2, :integer
      column :or_shard_s, :varchar, :size => 25
      column :or_shard_i, :varchar, :size => 25
      column :or_toteff_, :integer
      column :or_toteff2, :integer
      column :or_case_s, :varchar, :size => 10
      column :or_case_i, :varchar, :size => 10
      column :or_core_s, :varchar, :size => 10
      column :or_core_i, :varchar, :size => 10
      column :or_plen_s, :varchar, :size => 10
      column :or_plen_i, :varchar, :size => 10
      column :or_note_s, :varchar, :size => 40
      column :or_note_i, :text
      column :or_ins_by, :varchar, :size => 40
      column :or_app_by, :varchar, :size => 25
      column :or_ins_dat, :date
      column :or_app_dat, :date
      column :or_qty_ext, :integer
      column :or_mat_cod, :varchar, :size => 6
      column :or_prod_co, :varchar, :size => 2
      column :or_invent_, :varchar, :size => 30
      column :or_raw_num, :varchar, :size => 30
      column :or_sord_nu, :varchar, :size => 7
      column :or_line_nu, :integer
      column :or_est_mat, :float
      column :or_lo_code, :varchar, :size => 10
      column :or_comp_da, :date
      column :or_draw_nu, :varchar, :size => 30
      column :or_draw_re, :varchar, :size => 6
      column :or_non_bil, :boolean
      column :or_interna, :boolean
      column :or_misc_co, :float
      column :or_scrap_a, :float
      column :or_scrap_w, :float
      column :or_scrap_v, :float
      column :or_parent_, :varchar, :size => 12
      column :or_extatrb, :varchar, :size => 30
      column :or_extatr2, :varchar, :size => 30
      column :or_extatr3, :varchar, :size => 30
      column :or_extatr4, :varchar, :size => 30
      column :or_extatr5, :varchar, :size => 30
      column :or_extatr6, :varchar, :size => 30
      column :or_extatr7, :varchar, :size => 30
      column :or_extatr8, :varchar, :size => 30
      column :or_extatr9, :varchar, :size => 30
      column :or_extat10, :varchar, :size => 30
      column :or_contact, :varchar, :size => 25
      column :or_is_lot, :integer
      column :or_cont_cn, :varchar, :size => 10
      column :or_cont_ty, :varchar, :size => 10
      column :or_cont_de, :varchar, :size => 20
      column :or_cont_we, :varchar, :size => 10
      column :or_aggrega, :boolean
      column :or_user_id, :varchar, :size => 5
      column :or_last_mo, DateTime
      column :or_seriali, :boolean
      column :or_op_last, :varchar, :size => 30
      column :or_op_rev, :varchar, :size => 3
      column :or_op_las2, :date
      column :or_doc_typ, :varchar, :size => 10
      column :or_dpas, :varchar, :size => 10
      column :or_rev_ste, :integer
      column :or_wipinfg, :boolean
      column :or_freeze, :boolean
      column :or_ser_typ, :integer
      column :or_ser_ste, :integer
      column :or_serial_, :varchar, :size => 20
      column :or_printed, :date
      column :or_rework, :boolean
      column :or_rev_lev, :varchar, :size => 3
      column :or_markup, :float
      column :or_labor_c, :boolean
      column :or_continu, :boolean
      column :or_loctime, DateTime
      column :or_sl_id, :varchar, :size => 10
      column :or_print_d, :date
      column :or_origina, :varchar, :size => 5
      column :or_st_id, :varchar, :size => 2
      column :or_lc_id, :varchar, :size => 10
      column :or_externa, :boolean
      column :or_adj_dat, :date
      column :or_mat_mu, :integer
      column :or_display, :boolean
      column :or_displa2, :boolean
      column :or_mat_mem, :text
      column :or_overrid, :boolean
      column :or_project, :integer
      column :or_proj_sa, :varchar, :size => 1
      column :or_tag_num, :integer
      column :or_proj_st, :varchar, :size => 3
      column :or_df_id, :varchar, :size => 10
      column :or_stat_no, :text
      column :or_useopqt, :boolean
      column :or_splitpa, :varchar, :size => 12
      column :or_warrant, :boolean
      column :or_scrap_c, :varchar, :size => 12
      column :or_hidecom, :boolean
      column :or_jobnote, :text
      column :or_jobstop, :boolean
      column :or_sigma_s, :integer
      column :or_keepzer, :boolean
      column :or_exclude, :boolean
      column :or_price_c, :boolean
    end
  end
end
