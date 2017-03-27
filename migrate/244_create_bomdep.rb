# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:bomdep) do
      column :bd_id, :varchar, size: 10
      column :bd_parent_, :varchar, size: 10
      column :bd_child_i, :varchar, size: 10
      column :bd_require, :boolean
      column :bd_childre, :boolean
    end
  end
end
