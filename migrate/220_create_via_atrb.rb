# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:via_atrb) do
      column :vc_id, :varchar, size: 10
      column :vc_desc, :varchar, size: 30
    end
  end
end
