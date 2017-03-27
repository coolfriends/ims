# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:terr) do
      column :tr_id, :varchar, size: 10
      column :tr_descrip, :varchar, size: 25
    end
  end
end
