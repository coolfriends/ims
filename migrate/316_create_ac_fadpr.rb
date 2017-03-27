# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_fadpr) do
      column :fd_id, :varchar, size: 10
      column :fd_fa_id, :varchar, size: 10
      column :fd_period, :varchar, size: 2
      column :fd_year, :varchar, size: 4
      column :fd_deprec_, :decimal, precision: 15, scale: 4
      column :fd_accum_a, :decimal, precision: 15, scale: 4
      column :fd_book_va, :decimal, precision: 15, scale: 4
      column :fd_gj_id, :varchar, size: 10
      column :fd_basis_r, :float
      column :fd_lyear, :integer
      column :fd_lperiod, :integer
      column :fd_lper_ye, :integer
      column :fd_fs_id, :varchar, size: 10
      column :fd_fj_id, :varchar, size: 10
      column :fd_capital, :decimal, precision: 15, scale: 4
      column :fd_type, :varchar, size: 1
      column :fd_entry_d, :date
      column :fd_clearin, :decimal, precision: 15, scale: 4
      column :fd_incloss, :decimal, precision: 15, scale: 4
    end
  end
end
