# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:zone) do
      column :zo_carrier, :varchar, size: 10
      column :zo_origin_, :varchar, size: 10
      column :zo_dest_zi, :varchar, size: 10
      column :zo_dest_z2, :varchar, size: 10
      column :zo_zone, :varchar, size: 10
      column :zo_ship_ty, :varchar, size: 20
    end
  end
end
