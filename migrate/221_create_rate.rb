# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:rate) do
      column :ra_carrier, :varchar, size: 10
      column :ra_ship_ty, :varchar, size: 20
      column :ra_commerc, :boolean
      column :ra_zone, :varchar, size: 10
      column :ra_max_wei, :varchar, size: 10
      column :ra_hundred, :boolean
      column :ra_rate, :float
      column :ra_residen, :boolean
    end
  end
end
