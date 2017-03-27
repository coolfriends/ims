# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_xrinv) do
      column :in_cust_co, :varchar, size: 6
      column :in_inv_num, :varchar, size: 7
      column :in_pay_dat, :date
      column :in_inv_dat, :date
      column :in_inv_sta, :varchar, size: 1
      column :in_po_num, :varchar, size: 15
      column :in_ship_co, :varchar, size: 8
      column :in_tot_amt, :decimal, precision: 15, scale: 4
      column :in_tot_cur, :decimal, precision: 15, scale: 4
      column :in_inv_bal, :decimal, precision: 15, scale: 4
      column :in_rec_amt, :decimal, precision: 15, scale: 4
      column :in_cur_amt, :decimal, precision: 15, scale: 4
      column :in_disc_am, :decimal, precision: 15, scale: 4
      column :in_cred_am, :decimal, precision: 15, scale: 4
      column :in_inv_new, :decimal, precision: 15, scale: 4
      column :in_gl_num, :varchar, size: 12
      column :in_pay_ter, :varchar, size: 20
      column :in_due_dat, :date
      column :in_disc_da, :date
      column :in_gl_sd, :varchar, size: 12
      column :in_referen, :varchar, size: 30
      column :in_type, :varchar, size: 1
      column :in_excepti, :boolean
      column :in_desc, :varchar, size: 80
    end
  end
end
