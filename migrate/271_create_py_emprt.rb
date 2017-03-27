# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_emprt) do
      column :er_id, :varchar, size: 10
      column :er_emp_id, :varchar, size: 5
      column :er_pr_id, :varchar, size: 10
      column :er_rate_re, :float
      column :er_rate_ot, :float
      column :er_rate_do, :float
      column :er_hour_re, :float
      column :er_hour_ot, :float
      column :er_hour_do, :float
      column :er_overrid, :boolean
      column :er_ex_hour, :boolean
      column :er_reg_gl_, :varchar, size: 12
      column :er_ot_gl_n, :varchar, size: 12
      column :er_dot_gl_, :varchar, size: 12
      column :er_delete, :boolean
      column :er_vac_gl_, :varchar, size: 12
      column :er_pto_gl_, :varchar, size: 12
      column :er_hol_gl_, :varchar, size: 12
      column :er_suta, :boolean
      column :er_sit, :boolean
      column :er_sot, :boolean
      column :er_lit1, :boolean
      column :er_lit2, :boolean
    end
  end
end
