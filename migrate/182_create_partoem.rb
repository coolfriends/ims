# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:partoem) do
      column :po_id, :varchar, size: 10
      column :po_code, :varchar, size: 2
      column :po_desc, :varchar, size: 50
    end
  end
end
