# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:acserial) do
      column :as_id, :varchar, size: 10
      column :as_lot_num, :varchar, size: 20
      column :as_qty, :integer
      column :as_notes, :text
      column :as_aj_id, :varchar, size: 10
      column :as_jc_id, :varchar, size: 10
    end
  end
end
