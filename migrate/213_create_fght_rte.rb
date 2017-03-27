# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:fght_rte) do
      column :fr_id, :varchar, size: 10
      column :fr_fe_id, :varchar, size: 10
      column :fr_weight, :float
      column :fr_rate, :float
    end
  end
end
