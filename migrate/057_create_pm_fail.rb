# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:pm_fail) do
      column :pf_id, :varchar, size: 10
      column :pf_po_id, :varchar, size: 10
      column :pf_fa_code, :varchar, size: 10
      column :pf_part_nu, :varchar, size: 30
      column :pf_part_de, :varchar, size: 50
      column :pf_notes, :text
    end
  end
end
