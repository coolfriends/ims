# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_gjrec) do
      column :rc_id, :varchar, size: 10
      column :rc_name, :varchar, size: 40
      column :rc_desc, :varchar, size: 35
      column :rc_type, :integer
      column :rc_amount, :decimal, precision: 15, scale: 4
      column :rc_freq, :varchar, size: 1
      column :rc_date, :date
      column :rc_day_wee, :integer
      column :rc_day_mon, :integer
      column :rc_month_y, :integer
    end
  end
end
