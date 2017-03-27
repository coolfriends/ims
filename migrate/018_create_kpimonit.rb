# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:kpimonit) do
      column :ks_id, :varchar, size: 10
      column :ks_kp_id, :varchar, size: 10
      column :ks_st_code, :varchar, size: 10
      column :ks_kp_targ, :float
      column :ks_kp_grap, :float
      column :ks_kp_redr, :float
      column :ks_kp_yell, :float
      column :ks_kp_gree, :float
    end
  end
end
