# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:parttype) do
      column :pt_id, :varchar, size: 10
      column :pt_code, :varchar, size: 1
      column :pt_desc, :varchar, size: 30
    end
  end
end
