Sequel.migration do
  change do
     create_table(:supplier) do
      column :sp_supp_co, :varchar, :size => 6
      column :sp_supp_na, :varchar, :size => 35
      column :sp_contact, :varchar, :size => 20
      column :sp_address, :varchar, :size => 35
      column :sp_addres2, :varchar, :size => 35
      column :sp_city, :varchar, :size => 30
      column :sp_state, :varchar, :size => 3
      column :sp_zip, :varchar, :size => 10
      column :sp_phone, :varchar, :size => 14
      column :sp_fax, :varchar, :size => 14
      column :sp_memo, :text
      column :sp_def_mu, :integer
      column :sp_tax, :float
      column :sp_account, :varchar, :size => 12
      column :sp_issuppl, :boolean
      column :sp_status, :varchar, :size => 1
      column :sp_crlimit, :decimal, :precision => 15, :scale => 4
      column :sp_1099, :boolean
      column :sp_1099_box, :varchar, :size => 2
      column :sp_fedid, :varchar, :size => 15
      column :sp_terms, :varchar, :size => 20
      column :sp_poreqd, :boolean
      column :sp_email, :varchar, :size => 40
      column :sp_min_cha, :float
      column :sp_supp_ty, :varchar, :size => 4
      column :sp_app_sta, :integer
      column :sp_emp_id, :varchar, :size => 5
      column :sp_app_dat, :date
      column :sp_fob, :varchar, :size => 15
      column :sp_ship_vi, :varchar, :size => 20
      column :sp_website, :varchar, :size => 100
      column :sp_dday_1, :boolean
      column :sp_dday_2, :boolean
      column :sp_dday_3, :boolean
      column :sp_dday_4, :boolean
      column :sp_dday_5, :boolean
      column :sp_dday_6, :boolean
      column :sp_dday_7, :boolean
      column :sp_credit_, :boolean
      column :sp_acct_nu, :varchar, :size => 30
      column :sp_rec_bal, :decimal, :precision => 15, :scale => 4
      column :sp_rec_dat, :date
      column :sp_cur_cod, :varchar, :size => 10
      column :sp_st_id_1, :varchar, :size => 10
      column :sp_st_id_2, :varchar, :size => 10
      column :sp_stax_id, :varchar, :size => 25
      column :sp_tax_exe, :boolean
      column :sp_exempt_, :varchar, :size => 30
      column :sp_cust_co, :varchar, :size => 20
      column :sp_def_per, :boolean
      column :sp_beg_bal, :date
      column :sp_beg_ba2, :decimal, :precision => 15, :scale => 4
      column :sp_create_, :date
      column :sp_exp_dat, :date
      column :sp_cntry, :varchar, :size => 25
      column :sp_lead_ti, :integer
      column :sp_blanket, :varchar, :size => 20
      column :sp_electro, :boolean
      column :sp_cc_due_, :date
      column :sp_cc_bala, :decimal, :precision => 15, :scale => 4
      column :sp_cc_ca_c, :varchar, :size => 12
      column :sp_cc_limi, :float
      column :sp_fc_ca_c, :varchar, :size => 12
      column :sp_exp_sup, :varchar, :size => 12
      column :su_vet_cus, :varchar, :size => 6
      column :sp_cc_due2, :decimal, :precision => 15, :scale => 4
      column :sp_cs_rec_, :date
      column :sp_cs_rec2, :decimal, :precision => 15, :scale => 4
      column :sp_cs_due_, :date
      column :sp_cs_due2, :decimal, :precision => 15, :scale => 4
      column :sp_obsolet, :boolean
      column :sp_uses_po, :boolean
      column :sp_docktos, :boolean
      column :sp_email_p, :boolean
      column :sp_email_2, :varchar, :size => 40
      column :sp_freight, :float
      column :sp_freigh2, :float
      column :sp_critica, :boolean
      column :sp_poalert, :text
      column :sp_poaler2, :integer
      column :sp_nopoale, :boolean
      column :sp_revisio, :text
      column :sp_tier, :varchar, :size => 20
      column :sp_late_al, :integer
      column :sp_autocri, :varchar, :size => 20
    end
  end
end
