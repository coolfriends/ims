Sequel.migration do
  change do
     create_table(:grpquote) do
      column :gq_id, :varchar, :size => 10
      column :gq_date, :date
      column :gq_status, :varchar, :size => 1
      column :gq_folup_d, :date
      column :gq_prep_by, :varchar, :size => 30
      column :gq_req_num, :varchar, :size => 20
      column :gq_sent_da, :date
      column :gq_valid_d, :varchar, :size => 10
      column :gq_cust_co, :varchar, :size => 6
      column :gq_cust_c2, :varchar, :size => 30
      column :gq_deliver, :varchar, :size => 50
      column :gq_ship_vi, :varchar, :size => 20
      column :gq_fob, :varchar, :size => 15
      column :gq_pay_ter, :varchar, :size => 20
      column :gq_memo, :text
      column :gq_comp_na, :varchar, :size => 35
      column :gq_address, :varchar, :size => 35
      column :gq_addres2, :varchar, :size => 35
      column :gq_addres3, :varchar, :size => 35
      column :gq_ship_co, :varchar, :size => 35
      column :gq_sh_ad1, :varchar, :size => 35
      column :gq_sh_ad2, :varchar, :size => 35
      column :gq_sh_ad3, :varchar, :size => 35
      column :gq_sh_ad4, :varchar, :size => 35
      column :gq_cust_ph, :varchar, :size => 14
      column :gq_cust_fa, :varchar, :size => 14
      column :gq_req_dat, :date
      column :gq_addres4, :varchar, :size => 35
      column :gq_last_up, :date
      column :gq_lo_code, :varchar, :size => 10
      column :gq_empby, :varchar, :size => 5
      column :gq_due_dat, :date
      column :gq_empto, :varchar, :size => 5
      column :gq_unit_ty, :varchar, :size => 4
      column :gq_stepup, :integer
      column :gq_sord_nu, :varchar, :size => 7
      column :gq_foblabe, :varchar, :size => 3
      column :gq_est_hrs, :float
      column :gq_eng_sda, :date
      column :gq_eng_eda, :date
      column :gq_fab_sda, :date
      column :gq_fab_eda, :date
      column :gq_sord_n2, :varchar, :size => 7
    end
  end
end
