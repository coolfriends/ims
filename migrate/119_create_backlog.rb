# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:backlog) do
      column :bl_sord_nu, :varchar, size: 7
      column :bl_line_nu, :integer
      column :bl_po_num, :varchar, size: 20
      column :bl_due_dat, :date
      column :bl_cust_co, :varchar, size: 6
      column :bl_invent_, :varchar, size: 30
      column :bl_part_nu, :varchar, size: 30
      column :bl_desc, :varchar, size: 30
      column :bl_qty_ord, :integer
      column :bl_cpu, :float
      column :bl_qty_shi, :integer
      column :bl_qty_bal, :integer
      column :bl_backlog, :float
      column :bl_cust_na, :varchar, size: 35
      column :bl_prom_da, :date
    end
  end
end
