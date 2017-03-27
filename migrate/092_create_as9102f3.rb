# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:as9102f3) do
      column :asf3_id, :varchar, size: 10
      column :part_num, :varchar, size: 30
      column :part_name, :varchar, size: 50
      column :serial_num, :varchar, size: 30
      column :fai_report, :varchar, size: 50
      column :preparedby, :varchar, size: 5
      column :preparedb2, :date
      column :as_id, :varchar, size: 10
    end
  end
end
