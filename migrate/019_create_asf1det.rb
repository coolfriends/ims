# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:asf1det) do
      column :f1_det_id, :varchar, size: 10
      column :part_num, :varchar, size: 30
      column :part_name, :varchar, size: 50
      column :serial_num, :varchar, size: 30
      column :fai_report, :varchar, size: 50
      column :as_id, :varchar, size: 10
    end
  end
end
