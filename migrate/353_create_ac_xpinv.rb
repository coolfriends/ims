# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_xpinv) do
      column :ap_supp_co, :varchar, size: 6
      column :ap_id, :varchar, size: 10
      column :ap_inv_num, :varchar, size: 30
      column :ap_inv_dat, :date
      column :ap_status, :varchar, size: 1
      column :ap_po_num, :varchar, size: 7
      column :ap_hold, :varchar, size: 8
      column :ap_tot_amt, :decimal, precision: 15, scale: 4
      column :ap_tot_cur, :decimal, precision: 15, scale: 4
      column :ap_inv_bal, :decimal, precision: 15, scale: 4
      column :ap_pay_amt, :decimal, precision: 15, scale: 4
      column :ap_cur_amt, :decimal, precision: 15, scale: 4
      column :ap_disc_am, :decimal, precision: 15, scale: 4
      column :ap_cred_am, :decimal, precision: 15, scale: 4
      column :ap_inv_new, :decimal, precision: 15, scale: 4
      column :ap_gl_num, :varchar, size: 12
      column :ap_pay_ter, :varchar, size: 20
      column :ap_due_dat, :date
      column :ap_disc_da, :date
      column :ap_gl_pd, :varchar, size: 12
      column :ap_desc, :varchar, size: 30
      column :ap_pay_mem, :varchar, size: 30
      column :ap_pay_dat, :date
      column :ap_check_n, :varchar, size: 10
      column :ap_electro, :boolean
      column :ap_discoun, :boolean
      column :ap_type, :varchar, size: 1
      column :ap_min_pay, :decimal, precision: 15, scale: 4
    end
  end
end
