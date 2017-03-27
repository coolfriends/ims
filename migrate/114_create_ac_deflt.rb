# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_deflt) do
      column :ap_basedt, :date
      column :ap_dsctdt, :date
      column :ap_discoun, :boolean
      column :ap_ck_acct, :varchar, size: 15
      column :ar_ck_acct, :varchar, size: 15
      column :ar_rec_dat, :date
      column :ar_discoun, :boolean
      column :ar_deposit, :boolean
      column :ar_dep_dat, :date
      column :ar_import, :boolean
      column :ar_import_, :varchar, size: 80
      column :ap_autoapp, :boolean
      column :ec_ck_acct, :varchar, size: 15
      column :ec_basedt, :date
      column :ec_paydt, :date
      column :ec_exunpai, :boolean
      column :ap_acct_no, :varchar, size: 12
      column :ec_exunapp, :boolean
      column :cp_export_, :varchar, size: 80
    end
  end
end
