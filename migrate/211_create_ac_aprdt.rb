# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_aprdt) do
      column :pd_id, :varchar, size: 10
      column :pd_pr_id, :varchar, size: 10
      column :pd_account, :varchar, size: 12
      column :pd_item_re, :varchar, size: 10
      column :pd_desc, :varchar, size: 30
      column :pd_qty_rec, :integer
      column :pd_unit_co, :decimal, precision: 15, scale: 4
      column :pd_line_nu, :integer
      column :pd_unit_ty, :varchar, size: 4
      column :pd_ext_cos, :decimal, precision: 15, scale: 4
      column :pd_dist_co, :varchar, size: 2
      column :pd_gl_id, :varchar, size: 10
      column :pd_tran_ty, :varchar, size: 2
      column :pd_te, :varchar, size: 1
    end
  end
end
