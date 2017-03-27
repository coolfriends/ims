# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:surftrea) do
      column :st_id, :varchar, size: 10
      column :st_code, :varchar, size: 1
      column :st_desc, :varchar, size: 50
    end
  end
end
