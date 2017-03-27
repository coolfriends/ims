# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:edi_ed) do
      column :ee_code, :varchar, size: 2
      column :ee_desc, :varchar, size: 30
    end
  end
end
