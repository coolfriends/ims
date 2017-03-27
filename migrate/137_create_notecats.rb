# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:notecats) do
      column :nc_id, :varchar, size: 10
      column :nc_desc, :varchar, size: 30
      column :nc_inactiv, :boolean
    end
  end
end
