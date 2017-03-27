# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:emp_req) do
      column :er_id, :varchar, size: 10
      column :er_emp_id, :varchar, size: 5
      column :er_ca_code, :varchar, size: 12
    end
  end
end
