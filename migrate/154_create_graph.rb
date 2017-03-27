# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:graph) do
      column :gr_id, :varchar, size: 10
      column :gr_title, :varchar, size: 50
      column :gr_account, :varchar, size: 10
      column :gr_accoun2, :varchar, size: 10
      column :gr_operati, :varchar, size: 1
      column :gr_type, :integer
    end
  end
end
