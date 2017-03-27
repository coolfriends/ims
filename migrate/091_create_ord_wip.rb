# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ord_wip) do
      column :ow_id, :varchar, size: 10
      column :ow_order_n, :varchar, size: 12
      column :ow_endrec_, :date
      column :ow_labor, :float
      column :ow_burden, :float
      column :ow_mat, :float
      column :ow_other, :float
      column :ow_prod, :integer
      column :ow_shipped, :integer
    end
  end
end
