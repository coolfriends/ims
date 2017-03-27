# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:mixer) do
      column :mi_id, :varchar, size: 10
      column :mi_desc, :varchar, size: 50
    end
  end
end
