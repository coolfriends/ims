# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:daystats) do
      column :ds_sorders, :integer
      column :ds_orders, :integer
      column :ds_quotes, :integer
      column :ds_sord_qu, :integer
      column :ds_shipmen, :integer
      column :ds_invoice, :integer
      column :ds_returns, :integer
      column :ds_sorder2, :float
      column :ds_orders_, :float
      column :ds_quotes_, :float
      column :ds_sord_q2, :float
      column :ds_shipme2, :float
      column :ds_invoic2, :float
      column :ds_return2, :float
      column :ds_date, :date
      column :ds_period, :varchar, size: 1
    end
  end
end
