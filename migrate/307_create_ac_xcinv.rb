# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_xcinv) do
      column :in_emp_id, :varchar, size: 5
      column :in_inv_num, :varchar, size: 7
      column :in_line_nu, :integer
      column :in_entry_d, :date
      column :in_inv_dat, :date
      column :in_cust_co, :varchar, size: 6
      column :in_inv_sta, :varchar, size: 1
      column :in_sord_nu, :varchar, size: 7
      column :in_po_num, :varchar, size: 25
      column :in_ext_pri, :float
      column :in_comm_pe, :float
      column :in_comm_am, :float
      column :in_comm_pa, :float
      column :in_comm_ba, :float
      column :in_comm_gl, :varchar, size: 12
      column :in_sc_id, :varchar, size: 10
      column :in_pay_mem, :varchar, size: 30
    end
  end
end
