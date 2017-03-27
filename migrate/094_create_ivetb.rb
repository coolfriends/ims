# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ivetb) do
      column :db_id, :varchar, size: 10
      column :db_user_id, :varchar, size: 5
      column :db_dm_id, :varchar, size: 10
    end
  end
end
