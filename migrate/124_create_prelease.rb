# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:prelease) do
      column :pe_id, :varchar, size: 10
      column :pe_po_num, :varchar, size: 7
      column :pe_po_line, :integer
      column :pe_po_rel, :integer
      column :pe_po_rec, :integer
      column :pe_quantit, :float
    end
  end
end
