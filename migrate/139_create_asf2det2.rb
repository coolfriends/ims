# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:asf2det2) do
      column :f2_det2_id, :varchar, size: 10
      column :funct_test, :varchar, size: 50
      column :accept_tes, :varchar, size: 50
      column :asf2_id, :varchar, size: 10
      column :as_id, :varchar, size: 10
    end
  end
end
