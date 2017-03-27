# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:pricbrkt) do
      column :pb_mat_cod, :varchar, size: 6
      column :pb_br_id, :varchar, size: 10
      column :pb_price, :float
    end
  end
end
