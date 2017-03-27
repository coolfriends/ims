# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:def_cal) do
      column :dc_m1, :float
      column :dc_m2, :float
      column :dc_m3, :float
      column :dc_m4, :float
      column :dc_m5, :float
      column :dc_m6, :float
      column :dc_m7, :float
      column :dc_ot1, :float
      column :dc_ot2, :float
      column :dc_ot3, :float
      column :dc_ot4, :float
      column :dc_ot5, :float
      column :dc_ot6, :float
      column :dc_ot7, :float
    end
  end
end
