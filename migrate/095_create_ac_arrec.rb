# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_arrec) do
      column :rr_id, :varchar, size: 10
      column :rr_cust_co, :varchar, size: 6
      column :rr_ship_vi, :varchar, size: 20
      column :rr_net_amt, :float
      column :rr_taxes, :float
      column :rr_tot_amt, :float
      column :rr_comp_na, :varchar, size: 33
      column :rr_address, :varchar, size: 33
      column :rr_addres2, :varchar, size: 33
      column :rr_addres3, :varchar, size: 33
      column :rr_ship_co, :varchar, size: 8
      column :rr_contact, :varchar, size: 25
      column :rr_emp_id, :varchar, size: 5
      column :rr_pay_ter, :varchar, size: 20
      column :rr_lo_code, :varchar, size: 10
      column :rr_type, :varchar, size: 1
      column :rr_gl_num, :varchar, size: 12
      column :rr_freq, :varchar, size: 1
      column :rr_dom, :integer
      column :rr_day, :integer
      column :rr_last_in, :date
      column :rr_next, :date
      column :rr_desc, :varchar, size: 35
      column :rr_selind, :varchar, size: 1
      column :rr_inv_num, :varchar, size: 7
      column :rr_post, :boolean
      column :rr_po_num, :varchar, size: 15
    end
  end
end
