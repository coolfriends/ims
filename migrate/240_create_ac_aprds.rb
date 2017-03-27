# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_aprds) do
      column :cp_year, :varchar, size: 4
      column :cp_period, :varchar, size: 2
      column :cp_exclude, :boolean
      column :cp_start_d, :date
      column :cp_end_dat, :date
      column :cp_desc, :varchar, size: 10
      column :cp_lock_do, :boolean
    end
  end
end
