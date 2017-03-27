# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_darap) do
      column :da_code, :varchar, size: 12
      column :da_type, :integer
    end
  end
end
