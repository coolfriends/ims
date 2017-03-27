# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:shoploc) do
      column :sl_locatio, :varchar, size: 15
      column :sl_emp_id, :varchar, size: 5
      column :sl_id, :varchar, size: 10
    end
  end
end
