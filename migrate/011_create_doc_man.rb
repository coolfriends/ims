Sequel.migration do
  change do
     create_table(:doc_man) do
      column :dm_id, :integer
      column :dm_doc_typ, :varchar, :size => 10
      column :dm_desc, :varchar, :size => 50
      column :dm_quote_n, :varchar, :size => 15
      column :dm_order_n, :varchar, :size => 12
      column :dm_cust_co, :varchar, :size => 6
      column :dm_part_nu, :varchar, :size => 30
      column :dm_rev_num, :varchar, :size => 6
      column :dm_last_up, :date
      column :dm_file, :varchar, :size => 254
      column :dm_memo, :text
      column :dm_invent_, :varchar, :size => 30
      column :dm_lot_num, :varchar, :size => 20
      column :dm_rec_no, :integer
      column :dm_on_rout, :boolean
      column :dm_on_pack, :boolean
      column :dm_view_wi, :integer
      column :dm_po_no, :varchar, :size => 25
      column :dm_prompt_, :boolean
      column :dm_doc_num, :varchar, :size => 30
      column :dm_doc_rev, :varchar, :size => 3
      column :dm_de_id, :varchar, :size => 2
      column :dm_appr_re, :boolean
      column :dm_appr_da, :date
      column :dm_iso_sta, :varchar, :size => 10
      column :dm_doc, :varchar, :size => 4
      column :dm_control, :boolean
      column :dm_emp_id, :varchar, :size => 5
      column :dm_status, :varchar, :size => 1
      column :dm_supp_co, :varchar, :size => 6
      column :dm_mach_co, :varchar, :size => 5
      column :dm_op_num, :integer
      column :dm_sord_nu, :varchar, :size => 7
      column :dm_line_nu, :integer
      column :dm_on_em_r, :boolean
      column :dm_tr_id, :varchar, :size => 10
      column :dm_heat_nu, :varchar, :size => 30
      column :dm_dev_id, :varchar, :size => 10
      column :dm_nc_id, :varchar, :size => 10
      column :dm_car_id, :varchar, :size => 10
      column :dm_ch_id, :varchar, :size => 10
      column :dm_st_id, :varchar, :size => 10
      column :dm_gj_id, :varchar, :size => 10
      column :dm_showonc, :boolean
      column :dm_protect, :boolean
      column :dm_defined, :varchar, :size => 5
      column :dm_sordq, :varchar, :size => 7
      column :dm_on_cofc, :boolean
      column :dm_on_po, :boolean
      column :dm_pt_id, :varchar, :size => 10
      column :dm_ps_id, :varchar, :size => 10
      column :dm_pm_id, :varchar, :size => 10
      column :dmst_id, :varchar, :size => 10
      column :dm_wl_id, :varchar, :size => 10
      column :dm_po_id, :varchar, :size => 10
      column :dm_ldratio, :varchar, :size => 10
      column :dm_oal, :varchar, :size => 10
      column :dm_oempart, :varchar, :size => 50
      column :dm_mi_id, :varchar, :size => 10
    end
  end
end
