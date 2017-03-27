# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:pm_group) do
      column :pg_group, :varchar, size: 10
      column :pg_desc, :varchar, size: 50
      column :pg_task, :text
    end
  end
end
