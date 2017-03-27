# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:inv_pkg) do
      column :ig_id, :varchar, size: 10
      column :ig_invent_, :varchar, size: 30
      column :ig_length, :integer
      column :ig_width, :integer
      column :ig_height, :integer
      column :ig_weight, :integer
      column :ig_quantit, :integer
    end
  end
end
