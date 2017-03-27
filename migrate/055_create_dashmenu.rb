# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:dashmenu) do
      column :dm_id, :varchar, size: 10
      column :dm_option, :varchar, size: 50
      column :dm_orderby, :integer
      column :dm_windown, :varchar, size: 30
    end
  end
end
