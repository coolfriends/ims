# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_fasch) do
      column :fs_id, :varchar, size: 10
      column :fs_fa_id, :varchar, size: 10
      column :fs_order, :integer
      column :fs_type, :varchar, size: 1
      column :fs_status, :varchar, size: 1
      column :fs_desc, :varchar, size: 40
      column :fs_supp_co, :varchar, size: 6
      column :fs_cost, :decimal, precision: 15, scale: 4
      column :fs_residua, :decimal, precision: 15, scale: 4
      column :fs_life_ye, :integer
      column :fs_life_mo, :integer
      column :fs_depr_me, :varchar, size: 1
      column :fs_acqrd_d, :date
      column :fs_beg_yea, :integer
      column :fs_beg_mon, :varchar, size: 2
      column :fs_id_numb, :varchar, size: 40
      column :fs_beg_qrt, :integer
      column :fs_basis_r, :float
      column :fs_units_d, :varchar, size: 12
      column :fs_life_un, :float
      column :fs_depr_va, :decimal, precision: 15, scale: 4
      column :fs_mach_co, :varchar, size: 5
      column :fs_model, :varchar, size: 40
      column :fs_dspsd_d, :date
      column :fs_beg_bal, :boolean
      column :fs_accum_d, :decimal, precision: 15, scale: 4
      column :fs_book_va, :decimal, precision: 15, scale: 4
      column :fs_beg_ba2, :integer
      column :fs_beg_ba3, :varchar, size: 2
      column :fs_dspsd_v, :decimal, precision: 15, scale: 4
      column :fs_income_, :decimal, precision: 15, scale: 4
      column :fs_fj_id, :varchar, size: 10
      column :fs_fj_id_2, :varchar, size: 10
    end
  end
end
