Sequel.migration do
  change do
     create_table(:ac_arrdt) do
      column :rd_rr_id, :varchar, :size => 10
      column :rd_line_nu, :integer
      column :rd_tran_ty, :varchar, :size => 2
      column :rd_invent_, :varchar, :size => 30
      column :rd_qty_ord, :integer
      column :rd_ship_co, :varchar, :size => 8
      column :rd_desc, :varchar, :size => 30
      column :rd_prod_co, :varchar, :size => 2
      column :rd_qty_shi, :integer
      column :rd_qty_bo, :integer
      column :rd_unit_ty, :varchar, :size => 4
      column :rd_unit_pr, :float
      column :rd_discoun, :float
      column :rd_disc_pr, :float
      column :rd_ext_pri, :float
      column :rd_te, :varchar, :size => 1
      column :rd_note, :text
      column :rd_note_fl, :varchar, :size => 1
      column :rd_order_n, :varchar, :size => 12
      column :rd_rel_num, :integer
      column :rd_po_num, :varchar, :size => 15
      column :rd_rel_qty, :integer
      column :rd_sd_id, :integer
      column :rd_ar_gl_n, :varchar, :size => 12
      column :rd_pc_gl_n, :varchar, :size => 12
      column :rd_tax_rat, :float
      column :rd_part_nu, :varchar, :size => 30
      column :rd_rev_num, :varchar, :size => 3
      column :rd_pmemo, :text
    end
  end
end
