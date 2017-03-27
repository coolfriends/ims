# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_empri) do
      column :ei_id, :varchar, size: 10
      column :ei_emp_id, :varchar, size: 5
      column :ei_gl_num, :varchar, size: 12
      column :ei_type, :varchar, size: 1
      column :ei_code, :varchar, size: 10
      column :ei_amount, :float
    end
  end
end
