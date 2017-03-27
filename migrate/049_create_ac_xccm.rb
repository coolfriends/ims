# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_xccm) do
      column :mr_emp_id, :varchar, size: 5
      column :mr_number, :varchar, size: 10
      column :mr_line_nu, :integer
      column :mr_entry_d, :date
      column :mr_date, :date
      column :mr_cust_co, :varchar, size: 6
      column :mr_sord_nu, :varchar, size: 7
      column :mr_inv_num, :varchar, size: 7
      column :mr_ext_pri, :float
      column :mr_comm_pe, :float
      column :mr_comm_am, :float
      column :mr_comm_pa, :float
      column :mr_comm_ba, :float
      column :mr_comm_gl, :varchar, size: 12
      column :mr_sc_id, :varchar, size: 10
      column :mr_id, :varchar, size: 10
      column :mr_referen, :varchar, size: 30
    end
  end
end
