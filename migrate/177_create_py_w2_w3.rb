Sequel.migration do
  change do
     create_table(:py_w2_w3) do
      column :w2_id, :varchar, :size => 10
      column :w2_type, :varchar, :size => 1
      column :w2_emp_id, :varchar, :size => 5
      column :w2_year, :integer
      column :w2_control, :varchar, :size => 8
      column :w2_soc_sec, :varchar, :size => 20
      column :w2_name, :varchar, :size => 40
      column :w2_address, :varchar, :size => 40
      column :w2_addres2, :varchar, :size => 40
      column :w2_addres3, :varchar, :size => 40
      column :w2_tot_wag, :float
      column :w2_fit_wit, :float
      column :w2_ss_wage, :float
      column :w2_ss_with, :float
      column :w2_mc_wage, :float
      column :w2_mc_with, :float
      column :w2_ss_tips, :float
      column :w2_alloc_t, :float
      column :w2_advance, :float
      column :w2_dc_bene, :float
      column :w2_nq_plan, :float
      column :w2_b1_bene, :float
      column :w2_box_13, :text
      column :w2_box_oth, :text
      column :w2_stat_em, :boolean
      column :w2_decease, :boolean
      column :w2_pension, :boolean
      column :w2_legal_r, :boolean
      column :w2_def_com, :boolean
      column :w2_st1_id, :varchar, :size => 2
      column :w2_st1_no, :varchar, :size => 15
      column :w2_st1_wag, :float
      column :w2_st1_wit, :float
      column :w2_st2_id, :varchar, :size => 2
      column :w2_st2_no, :varchar, :size => 15
      column :w2_st2_wag, :float
      column :w2_st2_wit, :float
      column :w2_lc1_nam, :varchar, :size => 10
      column :w2_lc1_wag, :float
      column :w2_lc1_wit, :float
      column :w2_lc2_nam, :varchar, :size => 10
      column :w2_lc2_wag, :float
      column :w2_lc2_wit, :float
      column :w2_void, :boolean
      column :w3_941, :boolean
      column :w3_militar, :boolean
      column :w3_943, :boolean
      column :w3_ct1, :boolean
      column :w3_househo, :boolean
      column :w3_medicar, :boolean
      column :w3_establi, :varchar, :size => 15
      column :w3_ein, :varchar, :size => 20
      column :w3_ein_oth, :varchar, :size => 20
      column :w3_tp_with, :float
      column :w3_contact, :varchar, :size => 40
      column :w3_phone_a, :varchar, :size => 3
      column :w3_phone, :varchar, :size => 8
      column :w3_fax_ac, :varchar, :size => 3
      column :w3_fax, :varchar, :size => 8
      column :w3_email, :varchar, :size => 50
      column :w3_total_w, :integer
      column :w2_alpha, :varchar, :size => 40
      column :w2_3_rd_sic, :boolean
      column :w2_first_n, :varchar, :size => 18
      column :w2_last_na, :varchar, :size => 20
      column :w2_ma_code, :varchar, :size => 2
      column :w2_ma_amou, :float
      column :w2_mb_code, :varchar, :size => 2
      column :w2_mb_amou, :float
      column :w2_mc_code, :varchar, :size => 2
      column :w2_mc_amou, :float
      column :w2_md_code, :varchar, :size => 2
      column :w2_md_amou, :float
      column :w2_suffix_, :varchar, :size => 3
      column :w3_944, :boolean
      column :w2_multipl, :boolean
      column :w2_hire_ex, :float
      column :w3_none_ap, :boolean
      column :w3_501_c_no, :boolean
      column :w3_501_c_n2, :boolean
      column :w3_501_c_sl, :boolean
      column :w3_fed_gov, :boolean
    end
  end
end
