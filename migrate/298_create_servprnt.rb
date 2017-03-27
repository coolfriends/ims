# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:servprnt) do
      column :sp_id, :integer
      column :sp_desc, :varchar, size: 40
      column :sp_printer, :varchar, size: 120
    end
  end
end
