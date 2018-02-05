Sequel.migration do
  change do
     create_table(:py_rgstr) do
      column :rg_id, :varchar, :size => 10
      column :rg_number, :integer
      column :rg_type, :varchar, :size => 1
      column :rg_emp_id, :varchar, :size => 5
      column :rg_tax_id, :varchar, :size => 10
      column :rg_begin_d, :date
      column :rg_end_dat, :date
      column :rg_entry_d, :date
      column :rg_referen, :varchar, :size => 35
      column :rg_payee, :varchar, :size => 35
      column :rg_address, :text
      column :rg_pay_typ, :varchar, :size => 1
      column :rg_pay_fre, :varchar, :size => 1
      column :rg_use_tca, :boolean
      column :rg_filing_, :varchar, :size => 1
      column :rg_filing2, :varchar, :size => 1
      column :rg_filing3, :varchar, :size => 1
      column :rg_filing4, :varchar, :size => 1
      column :rg_exempts, :integer
      column :rg_exempt2, :integer
      column :rg_exempt3, :integer
      column :rg_exempt4, :integer
      column :rg_as_fica, :boolean
      column :rg_as_medi, :boolean
      column :rg_as_futa, :boolean
      column :rg_as_suta, :boolean
      column :rg_st_id_s, :varchar, :size => 2
      column :rg_st_id_l, :varchar, :size => 2
      column :rg_st_id_2, :varchar, :size => 2
      column :rg_tx_id_f, :varchar, :size => 10
      column :rg_tx_id_2, :varchar, :size => 10
      column :rg_tx_id_m, :varchar, :size => 10
      column :rg_tx_id_3, :varchar, :size => 10
      column :rg_tx_id_s, :varchar, :size => 10
      column :rg_tx_id_4, :varchar, :size => 10
      column :rg_tx_id_5, :varchar, :size => 10
      column :rg_tt_id_s, :varchar, :size => 10
      column :rg_tx_id_l, :varchar, :size => 10
      column :rg_tx_id_6, :varchar, :size => 10
      column :rg_ad_tax_, :float
      column :rg_ad_tax2, :float
      column :rg_ad_tax3, :float
      column :rg_ad_tax4, :float
      column :rg_vac_bas, :varchar, :size => 1
      column :rg_vac_acc, :varchar, :size => 1
      column :rg_vac_ann, :float
      column :rg_vac_ava, :float
      column :rg_vac_ac2, :float
      column :rg_vac_use, :float
      column :rg_vac_rem, :float
      column :rg_pto_bas, :varchar, :size => 1
      column :rg_pto_acc, :varchar, :size => 1
      column :rg_pto_ann, :float
      column :rg_pto_ava, :float
      column :rg_pto_ac2, :float
      column :rg_pto_use, :float
      column :rg_pto_rem, :float
      column :rg_slry_ho, :float
      column :rg_reg_hou, :float
      column :rg_ot_hour, :float
      column :rg_dot_hou, :float
      column :rg_vac_hou, :float
      column :rg_pto_hou, :float
      column :rg_hol_hou, :float
      column :rg_other_h, :float
      column :rg_total_h, :float
      column :rg_slry_am, :float
      column :rg_reg_amt, :float
      column :rg_ot_amt, :float
      column :rg_dot_amt, :float
      column :rg_vac_amt, :float
      column :rg_pto_amt, :float
      column :rg_hol_amt, :float
      column :rg_other_a, :float
      column :rg_gross_a, :float
      column :rg_ee_fit_, :float
      column :rg_ee_fica, :float
      column :rg_ee_mc_a, :float
      column :rg_ee_sit_, :float
      column :rg_ee_lit1, :float
      column :rg_ee_lit2, :float
      column :rg_ee_ded_, :float
      column :rg_ded_tot, :float
      column :rg_net_pay, :float
      column :rg_sub_pay, :float
      column :rg_reimb_a, :float
      column :rg_check_a, :float
      column :rg_er_fica, :float
      column :rg_er_mc_a, :float
      column :rg_er_futa, :float
      column :rg_er_suta, :float
      column :rg_er_sii_, :float
      column :rg_er_sit_, :float
      column :rg_er_lit1, :float
      column :rg_er_lit2, :float
      column :rg_er_ded_, :float
      column :rg_er_tot_, :float
      column :rg_ee_fit2, :float
      column :rg_ee_fic2, :float
      column :rg_ee_mc_t, :float
      column :rg_ee_sit2, :float
      column :rg_ee_lit3, :float
      column :rg_ee_lit4, :float
      column :rg_er_fic2, :float
      column :rg_er_mc_t, :float
      column :rg_er_fut2, :float
      column :rg_er_sut2, :float
      column :rg_er_sii2, :float
      column :rg_er_sit2, :float
      column :rg_er_lit3, :float
      column :rg_er_lit4, :float
      column :rg_fit_py_, :varchar, :size => 12
      column :rg_fica_py, :varchar, :size => 12
      column :rg_fica_ex, :varchar, :size => 12
      column :rg_mc_py_g, :varchar, :size => 12
      column :rg_mc_ex_g, :varchar, :size => 12
      column :rg_futa_py, :varchar, :size => 12
      column :rg_futa_ex, :varchar, :size => 12
      column :rg_suta_py, :varchar, :size => 12
      column :rg_suta_ex, :varchar, :size => 12
      column :rg_sii_py_, :varchar, :size => 12
      column :rg_sii_ex_, :varchar, :size => 12
      column :rg_sit_py_, :varchar, :size => 12
      column :rg_sit_ex_, :varchar, :size => 12
      column :rg_lit1_py, :varchar, :size => 12
      column :rg_lit1_ex, :varchar, :size => 12
      column :rg_lit2_py, :varchar, :size => 12
      column :rg_lit2_ex, :varchar, :size => 12
      column :rg_mn_id, :varchar, :size => 10
      column :rg_or_calc, :boolean
      column :rg_or_vac_, :boolean
      column :rg_base_pa, :float
      column :rg_cknum, :varchar, :size => 10
      column :rg_ckdate, :date
      column :rg_electro, :boolean
      column :rg_ex_pay_, :boolean
      column :rg_use_jca, :boolean
      column :rg_valid, :boolean
      column :rg_excepti, :text
      column :rg_vac_esc, :float
      column :rg_pto_esc, :float
      column :rg_vac_adj, :float
      column :rg_pto_adj, :float
      column :rg_vac_beg, :float
      column :rg_pto_beg, :float
      column :rg_vac_us2, :float
      column :rg_pto_us2, :float
      column :rg_use_sca, :boolean
      column :rg_ad_calc, :boolean
      column :rg_ad_cal2, :boolean
      column :rg_ad_cal3, :boolean
      column :rg_ad_cal4, :boolean
      column :rg_attend_, :float
      column :rg_use_rca, :boolean
      column :rg_gain_sh, :boolean
      column :rg_tax_ove, :boolean
      column :rg_wc_amt, :float
      column :rg_ee_suta, :float
      column :rg_ee_sut2, :float
      column :rg_ee_fit3, :float
      column :rg_ee_fic3, :float
      column :rg_ee_mc_r, :float
      column :rg_ee_sit3, :float
      column :rg_ee_lit5, :float
      column :rg_ee_lit6, :float
      column :rg_er_fic3, :float
      column :rg_er_mc_r, :float
      column :rg_er_fut3, :float
      column :rg_er_sut3, :float
      column :rg_er_sii3, :float
      column :rg_er_sit3, :float
      column :rg_er_lit5, :float
      column :rg_er_lit6, :float
      column :rg_ee_sut3, :float
      column :rg_filing5, :varchar, :size => 1
      column :rg_eic_rc_, :varchar, :size => 12
      column :rg_tx_id_e, :varchar, :size => 10
      column :rg_er_eic_, :float
      column :rg_er_eic2, :float
      column :rg_er_eic3, :float
      column :rg_check_m, :varchar, :size => 30
      column :rg_as_soth, :boolean
      column :rg_tx_id_7, :varchar, :size => 10
      column :rg_ee_sot_, :float
      column :rg_er_sot_, :float
      column :rg_ee_sot2, :float
      column :rg_er_sot2, :float
      column :rg_sot_py_, :varchar, :size => 12
      column :rg_sot_ex_, :varchar, :size => 12
      column :rg_ee_sot3, :float
      column :rg_er_sot3, :float
      column :rg_filing6, :varchar, :size => 1
      column :rg_federal, :boolean
      column :rg_state_1, :boolean
      column :rg_local_1, :boolean
      column :rg_local_2, :boolean
      column :rg_lc_id_l, :varchar, :size => 10
      column :rg_lc_id_2, :varchar, :size => 10
      column :rg_as_loth, :boolean
      column :rg_as_lot2, :boolean
      column :rg_lot1_py, :varchar, :size => 12
      column :rg_lot1_ex, :varchar, :size => 12
      column :rg_lot2_py, :varchar, :size => 12
      column :rg_lot2_ex, :varchar, :size => 12
      column :rg_ee_tax_, :float
      column :rg_er_tax_, :float
      column :rg_srt_py_, :varchar, :size => 12
      column :rg_srt_ex_, :varchar, :size => 12
      column :rg_depends, :integer
      column :rg_edep_da, :date
    end
  end
end
