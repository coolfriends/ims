# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_dctns) do
      column :dc_id, :varchar, size: 10
      column :dc_code, :varchar, size: 10
      column :dc_type, :varchar, size: 1
      column :dc_desc, :varchar, size: 35
      column :dc_name, :varchar, size: 35
      column :dc_address, :varchar, size: 35
      column :dc_addres2, :varchar, size: 35
      column :dc_addres3, :varchar, size: 35
      column :dc_id_no, :varchar, size: 15
      column :dc_e_type, :varchar, size: 1
      column :dc_e_rate, :float
      column :dc_r_type, :varchar, size: 1
      column :dc_r_rate, :float
      column :dc_pay_gl_, :varchar, size: 12
      column :dc_fed, :boolean
      column :dc_fica, :boolean
      column :dc_med, :boolean
      column :dc_futa, :boolean
      column :dc_empec, :float
      column :dc_exp_gl_, :varchar, size: 12
      column :dc_emprc, :float
      column :dc_after_b, :integer
      column :dc_frequen, :varchar, size: 1
      column :dc_suta, :boolean
      column :dc_sit, :boolean
      column :dc_lit1, :boolean
      column :dc_lit2, :boolean
      column :dc_w2_box, :boolean
      column :dc_w2_box_, :varchar, size: 2
      column :dc_e_amoun, :float
      column :dc_r_amoun, :float
      column :dc_e_date, :date
      column :dc_beg_dat, :date
      column :dc_beg_bal, :float
      column :dc_w2_box2, :boolean
      column :dc_round_d, :boolean
      column :dc_e_rate_, :float
      column :dc_r_rate_, :float
      column :dc_e_max_p, :boolean
      column :dc_r_max_p, :boolean
      column :dc_taxable, :boolean
      column :dc_e_calc, :varchar, size: 1
      column :dc_r_calc, :varchar, size: 1
    end
  end
end
