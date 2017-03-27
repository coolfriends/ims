# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:corrdet) do
      column :cd_id, :varchar, size: 10
      column :cd_ca_id, :varchar, size: 10
      column :cd_emp_id, :varchar, size: 5
      column :cd_positio, :varchar, size: 30
      column :cd_desc, :text
      column :cd_comp_da, :date
      column :cd_status, :varchar, size: 1
      column :cd_type, :varchar, size: 10
      column :cd_phone, :varchar, size: 20
    end
  end
end
