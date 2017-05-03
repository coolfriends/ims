Sequel.migration do
  change do
     create_table(:box) do
      column :bx_id, :varchar, :size => 10
      column :bx_invent_, :varchar, :size => 30
      column :bx_ct_id, :varchar, :size => 10
      column :bx_il_id, :varchar, :size => 10
      column :bx_ib_id, :varchar, :size => 10
      column :bx_type, :varchar, :size => 3
      column :bx_quantit, :float
      column :bx_net_wgh, :float
      column :bx_tare_wg, :float
      column :bx_gross_w, :float
      column :bx_po_num, :varchar, :size => 25
      column :bx_sord_nu, :varchar, :size => 7
      column :bx_op_num, :integer
      column :bx_date_pa, :date
      column :bx_bulkbox, :integer
      column :bx_order_n, :varchar, :size => 12
      column :bx_box_lot, :varchar, :size => 25
    end
  end
end
