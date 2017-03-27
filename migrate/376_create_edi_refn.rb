# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:edi_refn) do
      column :er_code, :varchar, size: 2
      column :er_desc, :varchar, size: 30
    end
  end
end
