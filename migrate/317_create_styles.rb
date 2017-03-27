# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:styles) do
      column :st_id, :varchar, size: 6
      column :st_code, :varchar, size: 25
      column :st_desc, :text
    end
  end
end
