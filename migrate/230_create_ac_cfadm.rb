# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_cfadm) do
      column :cf_id, :varchar, size: 10
      column :cf_data_pa, :varchar, size: 80
      column :cf_selecte, :boolean
    end
  end
end
