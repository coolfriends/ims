# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:feas) do
      column :fe_id, :varchar, size: 10
      column :fe_type, :integer
      column :fe_text, :varchar, size: 80
      column :fe_order, :integer
      column :fe_textonl, :boolean
      column :fe_feas_no, :integer
      column :fe_general, :boolean
    end
  end
end
