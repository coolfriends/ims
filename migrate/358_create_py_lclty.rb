# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_lclty) do
      column :lc_id, :varchar, size: 10
      column :lc_st_id, :varchar, size: 2
      column :lc_name, :varchar, size: 25
      column :lc_code, :varchar, size: 10
    end
  end
end
