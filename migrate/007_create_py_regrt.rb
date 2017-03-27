# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_regrt) do
      column :rr_id, :varchar, size: 10
      column :rr_rg_id, :varchar, size: 10
      column :rr_pr_id, :varchar, size: 10
      column :rr_rate_re, :float
      column :rr_rate_ot, :float
      column :rr_rate_do, :float
      column :rr_hour_re, :float
      column :rr_hour_ot, :float
      column :rr_hour_do, :float
      column :rr_reg_gl_, :varchar, size: 12
      column :rr_ot_gl_n, :varchar, size: 12
      column :rr_dot_gl_, :varchar, size: 12
      column :rr_type, :varchar, size: 1
      column :rr_vac_gl_, :varchar, size: 12
      column :rr_pto_gl_, :varchar, size: 12
      column :rr_hol_gl_, :varchar, size: 12
      column :rr_hour_va, :float
      column :rr_hour_pt, :float
      column :rr_hour_ho, :float
      column :rr_amt_reg, :float
      column :rr_amt_ot, :float
      column :rr_amt_dot, :float
      column :rr_amt_vac, :float
      column :rr_amt_pto, :float
      column :rr_amt_hol, :float
      column :rr_amt_tot, :float
      column :rr_hour_to, :float
      column :rr_or_calc, :boolean
      column :rr_ex_hour, :boolean
      column :rr_amt_wc, :float
      column :rr_st_id, :varchar, size: 2
      column :rr_lc_id, :varchar, size: 10
      column :rr_de_id, :varchar, size: 2
      column :rr_jc_id, :varchar, size: 10
      column :rr_id_code, :varchar, size: 10
      column :rr_order_n, :varchar, size: 12
      column :rr_tax_non, :integer
      column :rr_fit, :boolean
      column :rr_fica, :boolean
      column :rr_mc, :boolean
      column :rr_futa, :boolean
      column :rr_suta, :boolean
      column :rr_sit, :boolean
      column :rr_sot, :boolean
      column :rr_lit1, :boolean
      column :rr_lit2, :boolean
    end
  end
end
