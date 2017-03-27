# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:kpidata) do
      column :kd_id, :varchar, size: 10
      column :kd_kp_id, :varchar, size: 10
      column :kd_date, :date
      column :kd_quantit, :float
      column :kd_ks_id, :varchar, size: 10
    end
  end
end
