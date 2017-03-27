# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:qinv_ops) do
      column :qo_id, :varchar, size: 10
      column :qo_quote_n, :varchar, size: 15
      column :qo_order_n, :varchar, size: 12
      column :qo_item, :integer
      column :qo_parent, :varchar, size: 30
      column :qo_part_nu, :varchar, size: 30
      column :qo_op_num, :integer
      column :qo_order, :integer
      column :qo_quantit, :integer
      column :qo_bom_id, :varchar, size: 10
    end
  end
end
