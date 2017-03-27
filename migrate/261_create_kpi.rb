# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:kpi) do
      column :kp_id, :varchar, size: 10
      column :kp_legend, :varchar, size: 50
      column :kp_categor, :varchar, size: 10
      column :kp_units, :varchar, size: 20
      column :kp_target_, :float
      column :kp_graphra, :float
      column :kp_lefttor, :boolean
      column :kp_redrang, :float
      column :kp_yellowr, :float
      column :kp_greenra, :float
      column :kp_timefra, :varchar, size: 1
      column :kp_1, :float
      column :kp_2, :float
      column :kp_3, :float
      column :kp_4, :float
      column :kp_5, :float
      column :kp_6, :float
      column :kp_7, :float
      column :kp_8, :float
      column :kp_9, :float
      column :kp_10, :float
      column :kp_11, :float
      column :kp_12, :float
      column :kp_percent, :float
      column :kp_color, :varchar, size: 1
      column :kp_dept, :varchar, size: 20
      column :kp_respons, :varchar, size: 30
      column :kp_graphle, :varchar, size: 30
      column :kp_inactiv, :boolean
      column :kp_subtype, :varchar, size: 1
    end
  end
end
