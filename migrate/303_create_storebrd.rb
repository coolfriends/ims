# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:storebrd) do
      column :sb_id, :varchar, size: 10
      column :sb_store, :varchar, size: 20
      column :sb_ca_id, :varchar, size: 10
      column :sb_brand, :varchar, size: 40
      column :sb_style, :varchar, size: 40
      column :sb_backpan, :varchar, size: 20
      column :sb_active_, :date
      column :sb_inactiv, :date
    end
  end
end
