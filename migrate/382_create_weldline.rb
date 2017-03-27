# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:weldline) do
      column :wl_id, :varchar, size: 10
      column :wl_code, :varchar, size: 2
      column :wl_desc, :varchar, size: 30
    end
  end
end
