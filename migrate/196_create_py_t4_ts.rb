# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_t4_ts) do
      column :t4_id, :varchar, size: 10
      column :t4_type, :varchar, size: 1
      column :t4_emp_id, :varchar, size: 5
      column :t4_year, :integer
      column :t4_soc_ins, :varchar, size: 11
      column :t4_last_na, :varchar, size: 20
      column :t4_first_n, :varchar, size: 15
      column :t4_initial, :varchar, size: 2
      column :t4_name, :varchar, size: 40
      column :t4_address, :varchar, size: 40
      column :t4_addres2, :varchar, size: 40
      column :t4_addres3, :varchar, size: 40
      column :t4_emp_pro, :varchar, size: 2
      column :t4_emp_cod, :varchar, size: 2
      column :t4_void, :boolean
      column :t4_ex_cpp, :boolean
      column :t4_ex_ei, :boolean
      column :t4_ex_ppip, :boolean
      column :t4_tot_wag, :float
      column :t4_cit_wit, :float
      column :t4_cpp_wag, :float
      column :t4_cpp_wit, :float
      column :t4_ei_wage, :float
      column :t4_ei_with, :float
      column :t4_ppip_wa, :float
      column :t4_ppip_wi, :float
      column :t4_qpp_wit, :float
      column :t4_rpp_wit, :float
      column :t4_rpp_reg, :varchar, size: 15
      column :t4_box1_co, :varchar, size: 2
      column :t4_box1_am, :float
      column :t4_box2_co, :varchar, size: 2
      column :t4_box2_am, :float
      column :t4_box3_co, :varchar, size: 2
      column :t4_box3_am, :float
      column :t4_box4_co, :varchar, size: 2
      column :t4_box4_am, :float
      column :t4_box5_co, :varchar, size: 2
      column :t4_box5_am, :float
      column :t4_box6_co, :varchar, size: 2
      column :t4_box6_am, :float
      column :ts_bin, :varchar, size: 12
      column :ts_total_t, :integer
      column :t4_control, :varchar, size: 8
      column :t4_union_d, :float
      column :t4_donatio, :float
      column :t4_pension, :float
      column :ts_sin_1, :varchar, size: 9
      column :ts_sin_2, :varchar, size: 9
      column :ts_contact, :varchar, size: 30
      column :ts_phone_a, :varchar, size: 3
      column :ts_phone_1, :varchar, size: 3
      column :ts_phone_2, :varchar, size: 4
      column :ts_phone_e, :varchar, size: 4
      column :ts_cpp_wit, :float
      column :ts_ei_with, :float
      column :ts_deducti, :float
      column :ts_remitta, :float
      column :ts_differe, :float
      column :ts_overpay, :float
      column :ts_balance, :float
      column :ts_amt_enc, :float
      column :t4_alpha, :varchar, size: 40
      column :t4_probati, :boolean
    end
  end
end
