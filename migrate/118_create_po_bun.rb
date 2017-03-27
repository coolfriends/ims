# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:po_bun) do
      column :pb_po_num, :varchar, size: 7
      column :pb_line_nu, :integer
      column :pb_rec_no, :integer
      column :pb_bun_num, :integer
      column :pb_qty, :float
      column :pb_il_id, :varchar, size: 10
      column :pb_ib_id, :varchar, size: 10
      column :pb_lot_num, :varchar, size: 20
    end
  end
end
