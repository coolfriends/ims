# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:srelease) do
      column :sr_id, :varchar, size: 10
      column :sr_ship_co, :varchar, size: 8
      column :sr_sd_id, :integer
      column :sr_type, :varchar, size: 1
      column :sr_order_n, :varchar, size: 12
      column :sr_rel_num, :integer
      column :sr_sord_nu, :varchar, size: 7
      column :sr_sord_re, :integer
      column :sr_sord_r2, :integer
      column :sr_quantit, :float
    end
  end
end
