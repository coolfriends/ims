# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_chkac) do
      column :ck_ca_code, :varchar, size: 12
      column :ck_desc, :varchar, size: 35
      column :ck_acct_no, :varchar, size: 15
      column :ck_next_no, :integer
      column :ck_bank, :varchar, size: 35
      column :ck_status, :varchar, size: 1
      column :ck_address, :varchar, size: 30
      column :ck_addres2, :varchar, size: 30
      column :ck_city, :varchar, size: 25
      column :ck_state, :varchar, size: 2
      column :ck_zip, :varchar, size: 10
      column :ck_routing, :varchar, size: 15
      column :ck_phone, :varchar, size: 20
      column :ck_bf_ca_c, :varchar, size: 12
      column :ck_beg_bal, :float
      column :ck_beg_dat, :date
      column :ck_rec_bal, :float
      column :ck_rec_dat, :date
      column :ck_ses_end, :float
      column :ck_ses_en2, :date
      column :ck_ed_next, :integer
      column :ck_payroll, :boolean
      column :ck_cur_cod, :varchar, size: 10
      column :ck_ce_ca_c, :varchar, size: 12
      column :ck_nc_ca_c, :varchar, size: 12
      column :ck_ur_ca_c, :varchar, size: 12
      column :ck_dep_nex, :integer
      column :ck_man_nex, :integer
      column :ck_prev_ba, :float
      column :ck_prev_da, :date
      column :ck_inactiv, :boolean
    end
  end
end
