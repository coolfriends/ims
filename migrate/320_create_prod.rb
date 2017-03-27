# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:prod) do
      column :pr_prod_co, :varchar, size: 2
      column :pr_prod_de, :varchar, size: 40
      column :pr_gl_num, :varchar, size: 12
      column :pr_pc_prod, :varchar, size: 5
      column :pr_commiss, :boolean
      column :pr_non_tax, :boolean
      column :pr_dv_code, :varchar, size: 2
      column :pr_dp_code, :varchar, size: 2
      column :pr_dist_co, :varchar, size: 2
      column :pr_gl_num_, :varchar, size: 12
      column :pr_gl_num2, :varchar, size: 12
      column :pr_gl_num3, :varchar, size: 12
      column :pr_gl_num4, :varchar, size: 12
      column :pr_gl_num5, :varchar, size: 12
      column :pr_ex_tonn, :boolean
      column :pr_exclude, :boolean
      column :pr_gl_num6, :varchar, size: 12
      column :pr_gl_num7, :varchar, size: 12
      column :pr_gl_num8, :varchar, size: 12
      column :pr_export, :varchar, size: 5
      column :pr_gl_abs_, :varchar, size: 12
      column :pr_gl_abs2, :varchar, size: 12
      column :pr_gl_abs3, :varchar, size: 12
      column :pr_ship_no, :text
      column :pr_freight, :varchar, size: 2
      column :pr_gl_num9, :varchar, size: 12
      column :pr_lo_code, :varchar, size: 10
      column :pr_il_id, :varchar, size: 10
      column :pr_hideopc, :boolean
      column :pr_excl_di, :boolean
      column :pr_obsolet, :boolean
    end
  end
end
