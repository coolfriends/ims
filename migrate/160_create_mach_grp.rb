# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:mach_grp) do
      column :mg_mach_co, :varchar, size: 5
      column :mg_g_code, :varchar, size: 10
      column :mg_default, :boolean
    end
  end
end
