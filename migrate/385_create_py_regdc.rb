# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_regdc) do
      column :rd_id, :varchar, size: 10
      column :rd_rg_id, :varchar, size: 10
      column :rd_dc_id, :varchar, size: 10
      column :rd_e_type, :varchar, size: 1
      column :rd_r_type, :varchar, size: 1
      column :rd_e_rate, :float
      column :rd_r_rate, :float
      column :rd_suta, :boolean
      column :rd_sit, :boolean
      column :rd_lit1, :boolean
      column :rd_lit2, :boolean
      column :rd_pay_gl_, :varchar, size: 12
      column :rd_exp_gl_, :varchar, size: 12
      column :rd_e_amoun, :float
      column :rd_r_amoun, :float
      column :rd_e_max_a, :float
      column :rd_r_max_a, :float
      column :rd_fit, :boolean
      column :rd_mc, :boolean
      column :rd_fica, :boolean
      column :rd_futa, :boolean
      column :rd_before_, :integer
      column :rd_or_calc, :boolean
      column :rd_e_deduc, :float
      column :rd_r_deduc, :float
      column :rd_e_date, :date
      column :rd_e_rate_, :float
      column :rd_r_rate_, :float
      column :rd_e_max_p, :boolean
      column :rd_r_max_p, :boolean
      column :rd_sot, :boolean
      column :rd_e_calc, :varchar, size: 1
      column :rd_r_calc, :varchar, size: 1
    end
  end
end
