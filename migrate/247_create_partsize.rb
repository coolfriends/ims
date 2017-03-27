# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:partsize) do
      column :ps_id, :varchar, size: 10
      column :ps_size, :varchar, size: 3
    end
  end
end
