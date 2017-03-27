# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_regri) do
      column :ri_id, :varchar, size: 10
      column :ri_rg_id, :varchar, size: 10
      column :ri_gl_num, :varchar, size: 12
      column :ri_type, :varchar, size: 1
      column :ri_code, :varchar, size: 10
      column :ri_amount, :float
    end
  end
end
