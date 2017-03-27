# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:use_lots) do
      column :ul_id, :varchar, size: 20
      column :ul_ic_id, :varchar, size: 10
      column :ul_quantit, :float
    end
  end
end
