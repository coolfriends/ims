# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:q_draws) do
      column :qd_id, :varchar, size: 10
      column :qd_quote_n, :varchar, size: 15
      column :qd_number, :varchar, size: 15
      column :qd_revisio, :varchar, size: 3
      column :qd_desc, :varchar, size: 30
    end
  end
end
