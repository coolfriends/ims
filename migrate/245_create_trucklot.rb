# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:trucklot) do
      column :tl_id, :varchar, size: 10
      column :tl_td_id, :varchar, size: 10
      column :tl_invent_, :varchar, size: 30
      column :tl_lot_num, :varchar, size: 20
      column :tl_quantit, :float
    end
  end
end
