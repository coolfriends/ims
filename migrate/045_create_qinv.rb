# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:qinv) do
      column :qi_quote_n, :varchar, size: 15
      column :qi_item, :integer
      column :qi_invent_, :varchar, size: 30
      column :qi_width, :float
      column :qi_length, :float
      column :qi_quantit, :float
      column :qi_unit_co, :float
      column :qi_ext_cos, :float
      column :qi_uom, :varchar, size: 2
      column :qi_price, :float
      column :qi_op_num, :integer
      column :qi_markup, :integer
      column :qi_ppbar, :float
      column :qi_inv_cos, :float
      column :qi_desc, :varchar, size: 60
      column :qi_ext_des, :text
      column :qi_stock_u, :varchar, size: 2
      column :qi_purch_u, :varchar, size: 2
      column :qi_qty1, :float
      column :qi_qty2, :float
      column :qi_qty3, :float
      column :qi_qty4, :float
      column :qi_qty5, :float
      column :qi_qty6, :float
      column :qi_qty7, :float
      column :qi_qty8, :float
      column :qi_qty9, :float
      column :qi_qty10, :float
      column :qi_unitcos, :float
      column :qi_unitco2, :float
      column :qi_unitco3, :float
      column :qi_unitco4, :float
      column :qi_unitco5, :float
      column :qi_unitco6, :float
      column :qi_unitco7, :float
      column :qi_unitco8, :float
      column :qi_unitco9, :float
      column :qi_unitc10, :float
      column :qi_extcost, :float
      column :qi_extcos2, :float
      column :qi_extcos3, :float
      column :qi_extcos4, :float
      column :qi_extcos5, :float
      column :qi_extcos6, :float
      column :qi_extcos7, :float
      column :qi_extcos8, :float
      column :qi_extcos9, :float
      column :qi_extco10, :float
      column :qi_totcost, :float
      column :qi_totcos2, :float
      column :qi_totcos3, :float
      column :qi_totcos4, :float
      column :qi_totcos5, :float
      column :qi_totcos6, :float
      column :qi_totcos7, :float
      column :qi_totcos8, :float
      column :qi_totcos9, :float
      column :qi_totco10, :float
      column :qi_mu1, :integer
      column :qi_mu2, :integer
      column :qi_mu3, :integer
      column :qi_mu4, :integer
      column :qi_mu5, :integer
      column :qi_mu6, :integer
      column :qi_mu7, :integer
      column :qi_mu8, :integer
      column :qi_mu9, :integer
      column :qi_mu10, :integer
      column :qi_shape_c, :varchar, size: 7
      column :qi_diam_th, :float
      column :qi_mat_len, :float
      column :qi_mat_wid, :float
      column :qi_wgt_uni, :float
      column :qi_inv_non, :integer
      column :qi_mat_cod, :varchar, size: 6
      column :qi_usesuom, :boolean
      column :qi_cut_off, :float
      column :qi_face_le, :float
      column :qi_fac_len, :float
      column :qi_tot_len, :float
      column :qi_act_siz, :float
      column :qi_tol_p, :float
      column :qi_tol_m, :float
      column :qi_wcut_of, :float
      column :qi_wface_l, :float
      column :qi_tot_wid, :float
      column :qi_wgtpp, :float
      column :qi_act_we_, :float
      column :qi_perc_ma, :integer
      column :qi_tot_wei, :float
      column :qi_baruse_, :float
      column :qi_msquare, :float
      column :qi_height, :float
      column :qi_psquare, :float
      column :qi_barend_, :float
      column :qi_bar_wei, :float
      column :qi_t_bar_w, :float
      column :qi_bar_per, :float
      column :qi_calc_ty, :varchar, size: 2
      column :qi_mat_lb1, :float
      column :qi_mat_lb2, :float
      column :qi_mat_lb3, :float
      column :qi_mat_lb4, :float
      column :qi_mat_lb5, :float
      column :qi_mat_lb6, :float
      column :qi_mat_lb7, :float
      column :qi_mat_lb8, :float
      column :qi_mat_lb9, :float
      column :qi_mat_l10, :float
      column :qi_supp_co, :varchar, size: 6
      column :qi_part_nu, :varchar, size: 30
      column :qi_sup_par, :varchar, size: 30
      column :qi_matw_uo, :varchar, size: 2
      column :qi_mu_calc, :varchar, size: 1
      column :qi_draw_nu, :varchar, size: 15
      column :qi_partw_u, :varchar, size: 2
      column :qi_ppbdont, :boolean
      column :qi_cav_ppo, :integer
      column :qi_waste_p, :float
      column :qi_part_vo, :float
      column :qi_part_we, :float
      column :qi_order_n, :varchar, size: 12
      column :qi_al_id, :varchar, size: 10
      column :qi_scrap_p, :float
      column :qi_chipwei, :float
      column :qi_chipcos, :float
      column :qi_lead_ti, :integer
      column :qi_status, :varchar, size: 1
      column :qi_require, :date
      column :qi_purch_i, :text
      column :qi_fin_wei, :float
      column :qi_lock, :boolean
      column :qi_area, :float
      column :qi_ftperc, :float
      column :qi_shrinka, :integer
      column :qi_extcutl, :float
      column :qi_extpcsp, :integer
      column :qi_extdrop, :float
      column :qi_extruno, :float
      column :qi_extwpf, :float
      column :qi_extbutt, :float
      column :qi_extbill, :float
      column :qi_web_thi, :float
      column :qi_lock_ba, :boolean
      column :qi_in_mm, :integer
      column :qi_std_cs_, :varchar, size: 10
      column :qi_extuse_, :float
      column :qi_exthole, :integer
      column :qi_extdie_, :varchar, size: 20
      column :qi_lengthw, :integer
      column :qi_misc1, :float
      column :qi_misc2, :float
      column :qi_misc3, :float
      column :qi_misc4, :float
      column :qi_misc5, :float
      column :qi_misc6, :float
      column :qi_misc7, :float
      column :qi_misc8, :float
      column :qi_misc9, :float
      column :qi_misc10, :float
      column :qi_cut_des, :varchar, size: 30
      column :qi_make_bu, :varchar, size: 1
      column :qi_cert_nu, :varchar, size: 15
      column :qi_barend2, :float
      column :qi_mat_inc, :integer
      column :qi_obsolet, :boolean
      column :qi_islot, :boolean
      column :qi_donotbu, :boolean
      column :qi_non_sto, :boolean
      column :qi_mat_ref, :text
      column :qi_grade, :varchar, size: 10
      column :qi_shipsep, :boolean
      column :qi_confcos, :boolean
      column :qi_dist_co, :varchar, size: 2
      column :qi_pour_nu, :integer
      column :qi_ship_st, :integer
      column :qi_de_id, :varchar, size: 10
      column :qi_paintfa, :float
      column :qi_paintar, :float
      column :qi_sequenc, :integer
      column :qi_lockmat, :boolean
    end
  end
end
