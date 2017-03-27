# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:stdsab) do
      column :sb_id, :varchar, size: 10
      column :sb_type, :varchar, size: 1
      column :sb_po_sord, :varchar, size: 7
      column :sb_line_nu, :integer
      column :sb_st_id, :varchar, size: 10
      column :sb_display, :boolean
    end
  end
end
