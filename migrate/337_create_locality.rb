# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:locality) do
      column :lo_id, :varchar, size: 10
      column :lo_st_id, :varchar, size: 10
      column :lo_name, :varchar, size: 25
      column :lo_stx_id, :varchar, size: 10
    end
  end
end
