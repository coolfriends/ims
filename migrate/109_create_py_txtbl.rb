# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_txtbl) do
      column :tt_id, :varchar, size: 10
      column :tt_tx_id, :varchar, size: 10
      column :tt_type, :varchar, size: 1
      column :tt_over, :float
      column :tt_not_ove, :float
      column :tt_tax_wit, :float
      column :tt_plus_pe, :float
      column :tt_code, :varchar, size: 10
      column :tt_desc, :varchar, size: 35
      column :tt_rate, :float
      column :tt_ts_id, :varchar, size: 10
      column :tt_pos, :varchar, size: 1
    end
  end
end
