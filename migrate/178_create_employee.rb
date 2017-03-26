Sequel.migration do
  change do
     create_table(:employee) do
      column :em_emp_id, :varchar, :size => 5
      column :em_emp_nam, :varchar, :size => 20
      column :em_positio, :varchar, :size => 30
      column :em_hrly_ra, :float
      column :em_dept_co, :varchar, :size => 2
      column :em_shift, :varchar, :size => 2
      column :em_salespe, :boolean
      column :em_picture, :varchar, :size => 254
      column :em_ci, :varchar, :size => 8
      column :em_co, :varchar, :size => 8
      column :em_lo, :varchar, :size => 8
      column :em_li, :varchar, :size => 8
      column :em_r_limit, :integer
      column :em_jc_use, :boolean
      column :em_tc_use, :boolean
      column :em_minlunc, :integer
      column :em_gl_numb, :varchar, :size => 12
      column :em_last_na, :varchar, :size => 20
      column :em_first_n, :varchar, :size => 15
      column :em_middle_, :varchar, :size => 12
      column :em_address, :varchar, :size => 35
      column :em_addres2, :varchar, :size => 35
      column :em_city, :varchar, :size => 20
      column :em_state, :varchar, :size => 2
      column :em_zip_cod, :varchar, :size => 10
      column :em_phone, :varchar, :size => 14
      column :em_soc_sec, :varchar, :size => 20
      column :em_birth_d, :varchar, :size => 20
      column :em_sex, :varchar, :size => 1
      column :em_marital, :varchar, :size => 1
      column :em_exempts, :integer
      column :em_pay_typ, :varchar, :size => 1
      column :em_pay_fre, :varchar, :size => 1
      column :em_date_hi, :date
      column :em_date_le, :date
      column :em_reason_, :text
      column :em_notes, :text
      column :em_ad_tax_, :float
      column :em_ad_tax2, :float
      column :em_ad_tax3, :float
      column :em_adv_rec, :float
      column :em_st_id_s, :varchar, :size => 2
      column :em_tt_id_s, :varchar, :size => 10
      column :em_tx_id_l, :varchar, :size => 10
      column :em_tx_id_2, :varchar, :size => 10
      column :em_vac_ava, :float
      column :em_vac_use, :float
      column :em_vac_rem, :float
      column :em_pto_ava, :float
      column :em_pto_use, :float
      column :em_pto_rem, :float
      column :em_fax, :varchar, :size => 14
      column :em_email, :varchar, :size => 35
      column :em_benefit, :date
      column :em_vac_ann, :float
      column :em_pto_ann, :float
      column :em_ad_tax4, :float
      column :em_use_tca, :boolean
      column :em_w2_stat, :boolean
      column :em_w2_942_, :boolean
      column :em_w2_def_, :boolean
      column :em_w2_lega, :boolean
      column :em_w2_pens, :boolean
      column :em_w2_dece, :boolean
      column :em_as_fica, :boolean
      column :em_as_medi, :boolean
      column :em_as_futa, :boolean
      column :em_as_suta, :boolean
      column :em_vac_bas, :varchar, :size => 1
      column :em_vac_acc, :varchar, :size => 1
      column :em_pto_bas, :varchar, :size => 1
      column :em_pto_acc, :varchar, :size => 1
      column :em_exempt2, :integer
      column :em_exempt3, :integer
      column :em_exempt4, :integer
      column :em_filing_, :varchar, :size => 1
      column :em_filing2, :varchar, :size => 1
      column :em_filing3, :varchar, :size => 1
      column :em_filing4, :varchar, :size => 1
      column :em_st_id_l, :varchar, :size => 2
      column :em_st_id_2, :varchar, :size => 2
      column :em_vac_ac2, :float
      column :em_pto_ac2, :float
      column :em_electro, :boolean
      column :em_no_etr, :boolean
      column :em_fed_res, :varchar, :size => 30
      column :em_inactiv, :boolean
      column :em_supp_co, :varchar, :size => 6
      column :em_use_jca, :boolean
      column :em_supervi, :boolean
      column :em_emp_id_, :varchar, :size => 5
      column :em_commiss, :float
      column :em_shift_o, :boolean
      column :em_vac_esc, :float
      column :em_pto_esc, :float
      column :em_w2_3_rd_, :boolean
      column :em_use_sca, :boolean
      column :em_sell_ra, :float
      column :em_ad_calc, :boolean
      column :em_ad_cal2, :boolean
      column :em_ad_cal3, :boolean
      column :em_ad_cal4, :boolean
      column :em_sc_dow, :integer
      column :em_tempora, :boolean
      column :em_pe_code, :varchar, :size => 6
      column :em_use_rca, :boolean
      column :em_ex_gain, :boolean
      column :em_product, :boolean
      column :em_signatu, :varchar, :size => 40
      column :em_fit_py_, :varchar, :size => 12
      column :em_fica_py, :varchar, :size => 12
      column :em_fica_ex, :varchar, :size => 12
      column :em_mc_py_g, :varchar, :size => 12
      column :em_mc_ex_g, :varchar, :size => 12
      column :em_futa_py, :varchar, :size => 12
      column :em_futa_ex, :varchar, :size => 12
      column :em_suta_py, :varchar, :size => 12
      column :em_suta_ex, :varchar, :size => 12
      column :em_sii_py_, :varchar, :size => 12
      column :em_sii_ex_, :varchar, :size => 12
      column :em_sit_py_, :varchar, :size => 12
      column :em_sit_ex_, :varchar, :size => 12
      column :em_lit1_py, :varchar, :size => 12
      column :em_lit1_ex, :varchar, :size => 12
      column :em_lit2_py, :varchar, :size => 12
      column :em_lit2_ex, :varchar, :size => 12
      column :em_tax_ove, :boolean
      column :em_suponly, :boolean
      column :em_spec_re, :boolean
      column :em_inspect, :boolean
      column :em_trans_c, :varchar, :size => 2
      column :em_routing, :varchar, :size => 9
      column :em_account, :varchar, :size => 35
      column :em_tc_note, :text
      column :em_mgr_qua, :boolean
      column :em_mgr_pm, :boolean
      column :em_mgr_eng, :boolean
      column :em_app_req, :boolean
      column :em_spouse_, :varchar, :size => 20
      column :em_unatten, :boolean
      column :em_exp_dep, :varchar, :size => 6
      column :em_exp_cod, :varchar, :size => 8
      column :em_hr_note, :text
      column :em_da_note, :text
      column :em_pr_note, :text
      column :em_pr_next, :date
      column :em_ps_id, :varchar, :size => 10
      column :em_hours_a, :float
      column :em_cert_tr, :boolean
      column :em_filing5, :varchar, :size => 1
      column :em_eic_rc_, :varchar, :size => 12
      column :em_setup, :boolean
      column :em_emerg_n, :varchar, :size => 25
      column :em_emerg_p, :varchar, :size => 14
      column :em_can_iss, :boolean
      column :em_can_ass, :boolean
      column :em_as_soth, :boolean
      column :em_sot_py_, :varchar, :size => 12
      column :em_sot_ex_, :varchar, :size => 12
      column :em_filing6, :varchar, :size => 1
      column :em_federal, :boolean
      column :em_state_1, :boolean
      column :em_local_1, :boolean
      column :em_local_2, :boolean
      column :em_arbitra, :boolean
      column :em_ex_holi, :boolean
      column :em_split_p, :integer
      column :em_electr2, :boolean
      column :em_trans_2, :varchar, :size => 2
      column :em_routin2, :varchar, :size => 9
      column :em_accoun2, :varchar, :size => 35
      column :em_split_2, :integer
      column :em_split_t, :integer
      column :em_split_a, :float
      column :em_split_3, :float
      column :em_requisi, :boolean
      column :em_lc_id_l, :varchar, :size => 10
      column :em_lc_id_2, :varchar, :size => 10
      column :em_as_loth, :boolean
      column :em_as_lot2, :boolean
      column :em_lot1_py, :varchar, :size => 12
      column :em_lot1_ex, :varchar, :size => 12
      column :em_lot2_py, :varchar, :size => 12
      column :em_lot2_ex, :varchar, :size => 12
      column :em_srt_py_, :varchar, :size => 12
      column :em_srt_ex_, :varchar, :size => 12
      column :em_depends, :integer
      column :em_inside, :boolean
      column :em_id_code, :varchar, :size => 10
      column :em_qualifi, :boolean
      column :em_sell_r2, :float
      column :em_sell_r3, :float
      column :em_gl_com_, :varchar, :size => 12
      column :em_check_m, :varchar, :size => 30
      column :em_gl_com2, :varchar, :size => 12
      column :em_passwrd, :varchar, :size => 7
      column :em_approve, :boolean
      column :em_car_res, :boolean
      column :em_1099, :boolean
      column :em_1099_box, :varchar, :size => 2
      column :em_lm_user, :varchar, :size => 5
      column :em_lm_date, DateTime
      column :em_email_p, :boolean
      column :em_portalo, :boolean
      column :em_birth_2, :varchar, :size => 20
      column :em_soc_se2, :varchar, :size => 11
      column :em_numofma, :integer
      column :em_prevent, :boolean
      column :em_pdf_pay, :boolean
      column :em_pdf_dir, :varchar, :size => 40
      column :em_aca_fte, :float
    end
  end
end
