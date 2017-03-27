# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:certhead) do
      column :ch_id, :varchar, size: 10
      column :ch_ship_co, :varchar, size: 8
      column :ch_ship_da, :date
      column :ch_ship_qt, :integer
      column :ch_po_num, :varchar, size: 25
      column :ch_cust_co, :varchar, size: 6
      column :ch_cust_na, :varchar, size: 33
      column :ch_address, :varchar, size: 33
      column :ch_addres2, :varchar, size: 33
      column :ch_addres3, :varchar, size: 33
      column :ch_invent_, :varchar, size: 30
      column :ch_part_nu, :varchar, size: 30
      column :ch_rev_num, :varchar, size: 6
      column :ch_part_de, :varchar, size: 50
      column :ch_mat_fur, :boolean
      column :ch_mat_ref, :varchar, size: 15
      column :ch_mat, :varchar, size: 30
      column :ch_spec, :varchar, size: 30
      column :ch_rev, :varchar, size: 30
      column :ch_amend, :varchar, size: 30
      column :ch_notice, :varchar, size: 30
      column :ch_notes, :text
      column :ch_sig_nam, :varchar, size: 35
      column :ch_sig_tit, :varchar, size: 35
      column :ch_sig_dat, :date
      column :ch_sord_nu, :varchar, size: 7
      column :ch_line_nu, :integer
      column :ch_raw_inv, :varchar, size: 30
      column :ch_line_no, :integer
      column :ch_rel_no, :integer
      column :ch_misc_no, :text
      column :ch_shipped, :boolean
      column :ch_status, :varchar, size: 1
      column :ch_batch, :varchar, size: 30
      column :ch_availab, :boolean
      column :ch_org_qty, :float
      column :ch_order_n, :varchar, size: 12
      column :ch_lots_no, :boolean
    end
  end
end
