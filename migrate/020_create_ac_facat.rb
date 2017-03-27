# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_facat) do
      column :fc_id, :varchar, size: 10
      column :fc_code, :varchar, size: 10
      column :fc_desc, :varchar, size: 40
      column :fc_ca_code, :varchar, size: 12
      column :fc_ad_ca_c, :varchar, size: 12
      column :fc_de_ca_c, :varchar, size: 12
    end
  end
end
