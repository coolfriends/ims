Sequel.migration do
  change do
     create_table(:inventor) do
      column :iv_invent_, :varchar, :size => 30
      column :iv_invent2, :varchar, :size => 50
      column :iv_invent3, :varchar, :size => 5
      column :iv_heat_la, :integer
      column :iv_order_n, :varchar, :size => 12
      column :iv_operati, :varchar, :size => 3
      column :iv_date_re, :date
      column :iv_mat_cod, :varchar, :size => 6
      column :iv_shape_c, :varchar, :size => 7
      column :iv_chart_s, :varchar, :size => 7
      column :iv_tol_p, :float
      column :iv_tol_m, :float
      column :iv_mat_len, :float
      column :iv_tot_bar, :float
      column :iv_supp_co, :varchar, :size => 6
      column :iv_quantit, :float
      column :iv_cost_un, :float
      column :iv_tot_val, :float
      column :iv_locatio, :varchar, :size => 20
      column :iv_finish, :varchar, :size => 5
      column :iv_qty_rec, :float
      column :iv_bar_wei, :float
      column :iv_part_nu, :varchar, :size => 30
      column :iv_rev_num, :varchar, :size => 6
      column :iv_ppbar, :float
      column :iv_bars_re, :float
      column :iv_qty_bal, :float
      column :iv_bar_bal, :float
      column :iv_unit_ty, :integer
      column :iv_q_type, :varchar, :size => 5
      column :iv_q_type1, :varchar, :size => 6
      column :iv_part_le, :float
      column :iv_barend_, :integer
      column :iv_qty_sch, :float
      column :iv_qty_pro, :float
      column :iv_width, :varchar, :size => 7
      column :iv_calc_ty, :varchar, :size => 2
      column :iv_msquare, :float
      column :iv_price, :float
      column :iv_reo_lev, :float
      column :iv_reo_qty, :float
      column :iv_lead_ti, :integer
      column :iv_alloc_q, :float
      column :iv_need_qt, :float
      column :iv_sup_par, :varchar, :size => 30
      column :iv_sup_cod, :varchar, :size => 6
      column :iv_prod_co, :varchar, :size => 2
      column :iv_used_qt, :float
      column :iv_cht_siz, :float
      column :iv_wide, :float
      column :iv_notes, :text
      column :iv_aver_co, :float
      column :iv_convert, :float
      column :iv_purch_u, :varchar, :size => 2
      column :iv_len_uom, :varchar, :size => 2
      column :iv_last_co, :float
      column :iv_cost_me, :varchar, :size => 1
      column :iv_pupdate, :date
      column :iv_cupdate, :date
      column :iv_markup, :integer
      column :iv_misc_mu, :integer
      column :iv_mat_mu, :integer
      column :iv_mat_cos, :float
      column :iv_misc_co, :float
      column :iv_man_cos, :float
      column :iv_comp_as, :varchar, :size => 1
      column :iv_make_bu, :varchar, :size => 1
      column :iv_setup_c, :float
      column :iv_sub_cos, :float
      column :iv_quote_n, :varchar, :size => 15
      column :iv_ext_des, :text
      column :iv_part_ty, :varchar, :size => 1
      column :iv_lot_siz, :float
      column :iv_il_id, :varchar, :size => 10
      column :iv_ib_id, :varchar, :size => 10
      column :iv_box_typ, :text
      column :iv_box_qty, :float
      column :iv_bt_code, :varchar, :size => 3
      column :iv_fin_wei, :float
      column :iv_alloc, :boolean
      column :iv_draw_nu, :varchar, :size => 30
      column :iv_draw_re, :varchar, :size => 6
      column :iv_usesuom, :boolean
      column :iv_dist_co, :varchar, :size => 2
      column :iv_qtq, :integer
      column :iv_weeks_o, :float
      column :iv_height, :float
      column :iv_in_lowc, :boolean
      column :iv_purge_d, :date
      column :iv_app_onl, :boolean
      column :iv_abc_typ, :varchar, :size => 1
      column :iv_count_d, :date
      column :iv_count_2, :integer
      column :iv_unit_ma, :float
      column :iv_unit_la, :float
      column :iv_unit_bu, :float
      column :iv_unit_ot, :float
      column :iv_user_id, :varchar, :size => 5
      column :iv_last_mo, DateTime
      column :iv_stepup, :integer
      column :iv_web_thi, :float
      column :iv_lock_ba, :boolean
      column :iv_master, :boolean
      column :iv_master_, :varchar, :size => 30
      column :iv_old_box, :text
      column :iv_req_mac, :varchar, :size => 5
      column :iv_req_fg_, :varchar, :size => 30
      column :iv_req_tg_, :varchar, :size => 10
      column :iv_req_too, :varchar, :size => 20
      column :iv_lo_code, :varchar, :size => 10
      column :iv_class_t, :varchar, :size => 5
      column :iv_mat_spe, :varchar, :size => 50
      column :iv_extatrb, :varchar, :size => 20
      column :iv_extatr2, :varchar, :size => 20
      column :iv_extatr3, :varchar, :size => 20
      column :iv_extatr4, :varchar, :size => 20
      column :iv_extatr5, :varchar, :size => 20
      column :iv_extatr6, :varchar, :size => 20
      column :iv_extatr7, :varchar, :size => 20
      column :iv_extatr8, :varchar, :size => 20
      column :iv_extatr9, :varchar, :size => 20
      column :iv_extat10, :varchar, :size => 20
      column :iv_cust_co, :varchar, :size => 6
      column :iv_bf_ship, :boolean
      column :iv_pfep, :integer
      column :iv_wts_buf, :integer
      column :iv_fg_buf, :integer
      column :iv_exp_day, :boolean
      column :iv_so_stan, :varchar, :size => 8
      column :iv_contain, :date
      column :iv_contai2, :varchar, :size => 10
      column :iv_contai3, :text
      column :iv_family, :varchar, :size => 5
      column :iv_wip, :boolean
      column :iv_tare_we, :float
      column :iv_qty_low, :float
      column :iv_qty_upp, :float
      column :iv_wght_lo, :float
      column :iv_wght_up, :float
      column :iv_lr_id, :varchar, :size => 10
      column :iv_tickets, :float
      column :iv_lr_id_m, :varchar, :size => 10
      column :iv_gage_od, :float
      column :iv_gage_o2, :float
      column :iv_gage_do, :float
      column :iv_gage_hv, :float
      column :iv_gage_le, :float
      column :iv_gage_bf, :float
      column :iv_gage_pd, :float
      column :iv_gage_hn, :varchar, :size => 5
      column :iv_gage_ty, :varchar, :size => 5
      column :iv_gage_tf, :varchar, :size => 5
      column :iv_gage_cl, :varchar, :size => 5
      column :iv_gage_nd, :float
      column :iv_gage_pi, :float
      column :iv_gage_md, :float
      column :iv_apw_upp, :float
      column :iv_apw_low, :float
      column :iv_seriali, :boolean
      column :iv_ep_code, :varchar, :size => 2
      column :iv_ser_typ, :integer
      column :iv_exp_tar, :varchar, :size => 20
      column :iv_exp_cnt, :varchar, :size => 20
      column :iv_non_sto, :boolean
      column :iv_nm_code, :varchar, :size => 10
      column :iv_invent4, :varchar, :size => 1
      column :iv_pallet_, :float
      column :iv_pallet2, :float
      column :iv_eau, :integer
      column :iv_skip_au, :boolean
      column :iv_cert_nu, :varchar, :size => 15
      column :iv_planner, :varchar, :size => 5
      column :iv_obsolet, :boolean
      column :iv_parts_p, :integer
      column :iv_surchar, :float
      column :iv_no_subo, :boolean
      column :iv_ppap_da, :date
      column :iv_scrap_p, :integer
      column :iv_bulk_lo, :float
      column :iv_bulk_hi, :float
      column :iv_feature, :varchar, :size => 20
      column :iv_conv_fa, :float
      column :iv_max_qty, :float
      column :iv_extat11, :varchar, :size => 20
      column :iv_bulk2_l, :float
      column :iv_bulk2_h, :float
      column :iv_created, :varchar, :size => 5
      column :iv_dt_pric, :date
      column :iv_no_subt, :boolean
      column :iv_hcc, :float
      column :iv_extat12, :varchar, :size => 10
      column :iv_extat13, :varchar, :size => 5
      column :iv_extat14, :varchar, :size => 5
      column :iv_pack_st, :varchar, :size => 10
      column :iv_pcs_rac, :integer
      column :iv_num_ski, :integer
      column :iv_num_car, :integer
      column :iv_commiss, :float
      column :iv_excl_sc, :boolean
      column :iv_paintfa, :float
      column :iv_inspect, :boolean
      column :iv_exclude, :boolean
      column :iv_serial_, :integer
      column :iv_minweek, :float
      column :iv_maxweek, :float
      column :iv_turns, :integer
      column :iv_continu, :boolean
      column :iv_eau_quo, :varchar, :size => 15
      column :iv_price1, :float
      column :iv_price2, :float
      column :iv_price3, :float
      column :iv_price4, :float
      column :iv_de_id, :varchar, :size => 2
      column :iv_small, :boolean
      column :iv_picpath, :text
      column :iv_date_cr, :date
      column :iv_lotspec, :boolean
      column :iv_datecre, :date
      column :iv_pantick, :varchar, :size => 20
      column :iv_manufac, :varchar, :size => 30
      column :iv_upc, :varchar, :size => 12
      column :iv_ff_il_i, :varchar, :size => 10
      column :iv_ff_ib_i, :varchar, :size => 10
    end
  end
end
