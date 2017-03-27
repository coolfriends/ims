# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:projerng) do
      column :pe_id, :integer
      column :pe_proj_or, :varchar, size: 12
      column :pe_assigne, :varchar, size: 5
      column :pe_inactiv, :boolean
      column :pe_from, :integer
      column :pe_to, :integer
      column :pe_desc, :varchar, size: 30
      column :pe_next, :integer
    end
  end
end
