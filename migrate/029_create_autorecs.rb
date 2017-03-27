# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:autorecs) do
      column :ar_id, :varchar, size: 10
      column :ar_invent_, :varchar, size: 30
      column :ar_quantit, :float
      column :ar_importe, :boolean
      column :ar_user_id, :varchar, size: 5
      column :ar_date, :date
    end
  end
end
