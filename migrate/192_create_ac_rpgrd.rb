# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_rpgrd) do
      column :rd_id, :varchar, size: 10
      column :rd_rg_code, :varchar, size: 10
      column :rd_dv_code, :varchar, size: 2
      column :rd_dp_code, :varchar, size: 2
    end
  end
end
