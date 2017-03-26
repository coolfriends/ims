Sequel.migration do
  change do
     create_table(:quote) do
      column :q1_quote_n, :varchar, :size => 15
      column :q1_req_num, :varchar, :size => 20
      column :q1_part_nu, :varchar, :size => 30
      column :q1_draw_nu, :varchar, :size => 30
      column :q1_rev_num, :varchar, :size => 6
      column :q1_cust_co, :varchar, :size => 6
      column :q1_unit_ty, :varchar, :size => 4
      column :q1_quote_d, :date
      column :q1_req_dat, :date
      column :q1_sent_da, :date
      column :q1_last_up, :date
      column :q1_q_memo, :text
      column :q1_invent_, :varchar, :size => 30
      column :q1_qq1, :float
      column :q1_qq2, :float
      column :q1_qq3, :float
      column :q1_qq4, :float
      column :q1_qq5, :float
      column :q1_qq6, :float
      column :q1_qq7, :float
      column :q1_qq8, :float
      column :q1_qq9, :float
      column :q1_qq10, :float
      column :q1_setup1, :float
      column :q1_setup2, :float
      column :q1_setup3, :float
      column :q1_setup4, :float
      column :q1_setup5, :float
      column :q1_setup6, :float
      column :q1_setup7, :float
      column :q1_setup8, :float
      column :q1_setup9, :float
      column :q1_setup10, :float
      column :q1_ot_cost, :float
      column :q1_pmemo, :text
      column :q1_mat_cod, :varchar, :size => 6
      column :q1_act_siz, :float
      column :q1_tol_p, :float
      column :q1_tol_m, :float
      column :q1_mat_len, :float
      column :q1_shape_c, :varchar, :size => 7
      column :q1_m_memo, :text
      column :q1_finish, :varchar, :size => 5
      column :q1_part_le, :float
      column :q1_cut_off, :float
      column :q1_face_le, :float
      column :q1_tot_len, :float
      column :q1_part_wi, :float
      column :q1_wcut_of, :float
      column :q1_wface_l, :float
      column :q1_tot_wid, :float
      column :q1_mach_co, :varchar, :size => 5
      column :q1_totbar_, :float
      column :q1_barend_, :float
      column :q1_baruse_, :float
      column :q1_bar_wei, :float
      column :q1_t_bar_w, :float
      column :q1_ppbar, :float
      column :q1_bar_per, :float
      column :q1_perc_ma, :integer
      column :q1_tot_wei, :float
      column :q1_act_we_, :float
      column :q1_supp_co, :varchar, :size => 6
      column :q1_valid_d, :varchar, :size => 10
      column :q1_deliver, :varchar, :size => 50
      column :q1_part_de, :varchar, :size => 50
      column :q1_uom, :varchar, :size => 1
      column :q1_wgtpp, :float
      column :q1_prep_by, :varchar, :size => 30
      column :q1_bom_mat, :float
      column :q1_cht_siz, :float
      column :q1_wide, :float
      column :q1_cust_c2, :varchar, :size => 30
      column :q1_chipwei, :float
      column :q1_chipcos, :float
      column :q1_chipvol, :float
      column :q1_addrl, :varchar, :size => 33
      column :q1_height, :float
      column :q1_fob, :varchar, :size => 15
      column :q1_qr1, :float
      column :q1_qr2, :float
      column :q1_qr3, :float
      column :q1_qr4, :float
      column :q1_qr5, :float
      column :q1_qr6, :float
      column :q1_qr7, :float
      column :q1_qr8, :float
      column :q1_qr9, :float
      column :q1_qr10, :float
      column :q1_partw_u, :varchar, :size => 2
      column :q1_matw_uo, :varchar, :size => 2
      column :q1_len_uom, :varchar, :size => 2
      column :q1_psquare, :float
      column :q1_msquare, :float
      column :q1_inv_cos, :float
      column :q1_icost1, :float
      column :q1_icost2, :float
      column :q1_icost3, :float
      column :q1_icost4, :float
      column :q1_icost5, :float
      column :q1_icost6, :float
      column :q1_icost7, :float
      column :q1_icost8, :float
      column :q1_icost9, :float
      column :q1_icost10, :float
      column :q1_comp_na, :varchar, :size => 35
      column :q1_address, :varchar, :size => 35
      column :q1_addres2, :varchar, :size => 35
      column :q1_addres3, :varchar, :size => 35
      column :q1_folup_d, :date
      column :q1_status, :varchar, :size => 1
      column :q1_nq_equi, :boolean
      column :q1_nq_part, :boolean
      column :q1_nq_par2, :boolean
      column :q1_nq_cfg, :boolean
      column :q1_nq_cfgd, :varchar, :size => 50
      column :q1_nq_tol, :boolean
      column :q1_nq_told, :varchar, :size => 50
      column :q1_nq_oth, :boolean
      column :q1_nq_othd, :varchar, :size => 50
      column :q1_nq_quan, :boolean
      column :q1_nq_engo, :boolean
      column :q1_nq_quot, :date
      column :q1_nq_noti, :boolean
      column :q1_nq_oth2, :boolean
      column :q1_nq_oth3, :text
      column :q1_scrap_p, :integer
      column :q1_fin_wei, :float
      column :q1_lo_code, :varchar, :size => 10
      column :q1_lock, :boolean
      column :q1_draw_re, :varchar, :size => 6
      column :q1_hub_typ, :varchar, :size => 20
      column :q1_sfb_od, :float
      column :q1_sfb_id, :float
      column :q1_sfb_len, :float
      column :q1_sf1_od, :float
      column :q1_sf1_len, :float
      column :q1_sf2_od, :float
      column :q1_sf2_len, :float
      column :q1_addsub, :float
      column :q1_cast_od, :float
      column :q1_cast_id, :float
      column :q1_mold_id, :varchar, :size => 10
      column :q1_cast_ov, :float
      column :q1_ship_co, :varchar, :size => 35
      column :q1_sh_ad1, :varchar, :size => 35
      column :q1_sh_ad2, :varchar, :size => 35
      column :q1_sh_ad3, :varchar, :size => 35
      column :q1_extatrb, :varchar, :size => 30
      column :q1_extatr2, :varchar, :size => 30
      column :q1_extatr3, :varchar, :size => 30
      column :q1_extatr4, :varchar, :size => 30
      column :q1_extatr5, :varchar, :size => 30
      column :q1_extatr6, :varchar, :size => 30
      column :q1_extatr7, :varchar, :size => 30
      column :q1_extatr8, :varchar, :size => 30
      column :q1_extatr9, :varchar, :size => 30
      column :q1_extat10, :varchar, :size => 30
      column :q1_enginee, :varchar, :size => 3
      column :q1_lot, :integer
      column :q1_dqtr, :integer
      column :q1_usesuom, :boolean
      column :q1_setup_m, :float
      column :q1_parent_, :varchar, :size => 15
      column :q1_fg_inve, :varchar, :size => 30
      column :q1_pay_ter, :varchar, :size => 20
      column :q1_ship_vi, :varchar, :size => 40
      column :q1_prod_co, :varchar, :size => 2
      column :q1_qty_per, :integer
      column :q1_overrid, :boolean
      column :q1_cur_cod, :varchar, :size => 10
      column :q1_cur_rat, :float
      column :q1_cot_cos, :float
      column :q1_mat_inc, :integer
      column :q1_std_plt, :varchar, :size => 10
      column :q1_std_pkg, :varchar, :size => 10
      column :q1_op_last, :varchar, :size => 30
      column :q1_op_rev, :varchar, :size => 3
      column :q1_op_las2, :date
      column :q1_doc_typ, :varchar, :size => 10
      column :q1_user_id, :varchar, :size => 5
      column :q1_last_mo, :datetime
      column :q1_cust_ph, :varchar, :size => 14
      column :q1_cust_fa, :varchar, :size => 14
      column :q1_proj_de, :varchar, :size => 50
      column :q1_rev_nex, :integer
      column :q1_dpas, :varchar, :size => 10
      column :q1_sh_ad4, :varchar, :size => 35
      column :q1_ca_id, :varchar, :size => 10
      column :q1_eng_mas, :boolean
      column :q1_eau, :integer
      column :q1_generic, :boolean
      column :q1_autorou, :integer
      column :q1_max_tru, :integer
      column :q1_addres4, :varchar, :size => 35
      column :q1_ex1, :boolean
      column :q1_ex2, :boolean
      column :q1_ex3, :boolean
      column :q1_ex4, :boolean
      column :q1_ex5, :boolean
      column :q1_ex6, :boolean
      column :q1_ex7, :boolean
      column :q1_ex8, :boolean
      column :q1_ex9, :boolean
      column :q1_ex10, :boolean
      column :q1_fab_dat, :date
      column :q1_ship_da, :date
      column :q1_std_gen, :varchar, :size => 10
      column :q1_rev_lev, :varchar, :size => 3
      column :q1_subord_, :varchar, :size => 7
      column :q1_lead_ti, :integer
      column :q1_shipsep, :boolean
      column :q1_due_dat, :date
      column :q1_foblabe, :varchar, :size => 3
      column :q1_install, :varchar, :size => 30
      column :q1_op_num, :integer
      column :q1_op_mu, :float
      column :q1_apr, :float
      column :q1_rel1, :integer
      column :q1_rel2, :integer
      column :q1_rel3, :integer
      column :q1_rel4, :integer
      column :q1_rel5, :integer
      column :q1_rel6, :integer
      column :q1_rel7, :integer
      column :q1_rel8, :integer
      column :q1_rel9, :integer
      column :q1_rel10, :integer
      column :q1_days1, :integer
      column :q1_days2, :integer
      column :q1_days3, :integer
      column :q1_days4, :integer
      column :q1_days5, :integer
      column :q1_days6, :integer
      column :q1_days7, :integer
      column :q1_days8, :integer
      column :q1_days9, :integer
      column :q1_days10, :integer
      column :q1_cc1, :float
      column :q1_cc2, :float
      column :q1_cc3, :float
      column :q1_cc4, :float
      column :q1_cc5, :float
      column :q1_cc6, :float
      column :q1_cc7, :float
      column :q1_cc8, :float
      column :q1_cc9, :float
      column :q1_cc10, :float
      column :q1_bypass_, :boolean
    end
  end
end
