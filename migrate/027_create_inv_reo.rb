# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:inv_reo) do
      column :ir_id, :varchar, size: 10
      column :ir_invent_, :varchar, size: 30
      column :ir_il_id, :varchar, size: 10
      column :ir_reo_lev, :float
      column :ir_reo_qty, :float
    end
  end
end
