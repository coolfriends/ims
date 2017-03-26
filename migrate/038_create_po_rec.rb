Sequel.migration do
  change do
     create_table(:po_rec) do
      column :pr_po_num, :varchar, :size => 7
      column :pr_line_nu, :integer
      column :pr_rec_num, :integer
      column :pr_invent_, :varchar, :size => 30
      column :pr_rec_dat, :date
      column :pr_qty_rec, :float
      column :pr_distrib, :varchar, :size => 1
      column :pr_heat_nu, :varchar, :size => 30
      column :pr_apinv_i, :varchar, :size => 10
      column :pr_il_id, :varchar, :size => 10
      column :pr_ib_id, :varchar, :size => 10
      column :pr_cert_ch, :varchar, :size => 5
      column :pr_approve, :varchar, :size => 5
      column :pr_weight, :float
      column :pr_bundle, :varchar, :size => 10
      column :pr_ij_id, :varchar, :size => 10
      column :pr_rec_no, :integer
      column :pr_po_comp, :boolean
      column :pr_return, :boolean
      column :pr_lo_code, :varchar, :size => 10
      column :pr_stock, :boolean
      column :pr_jc_id, :varchar, :size => 10
      column :pr_lot_not, :text
      column :pr_lot_num, :varchar, :size => 20
      column :pr_order_n, :varchar, :size => 12
      column :pr_inv_num, :varchar, :size => 7
      column :pr_pcs, :float
      column :pr_unit_co, :float
      column :pr_bol_num, :varchar, :size => 10
      column :pr_rev_num, :varchar, :size => 6
      column :pr_rev_lev, :varchar, :size => 3
      column :pr_cust_co, :varchar, :size => 6
      column :pr_cust_c2, :varchar, :size => 6
      column :pr_melt_co, :text
      column :pr_color_c, :varchar, :size => 10
      column :pr_ad_id, :varchar, :size => 10
      column :pr_passfai, :integer
      column :pr_fail_qt, :float
      column :pr_act_len, :float
      column :pr_act_wid, :float
      column :pr_sord_nu, :varchar, :size => 7
      column :pr_reserve, :boolean
      column :pr_sord_li, :integer
      column :pr_wp_id, :varchar, :size => 10
      column :pr_qty_acc, :float
      column :pr_date_in, :date
      column :pr_inspect, :varchar, :size => 5
      column :pr_mrr, :varchar, :size => 30
      column :pr_qty_rej, :float
      column :pr_qty_ret, :float
      column :pr_ship_vi, :varchar, :size => 20
      column :pr_date_re, :date
      column :pr_debitme, :boolean
      column :pr_rej_not, :text
      column :pr_ret_not, :text
      column :pr_qty_scr, :float
      column :pr_expire_, :date
      column :pr_msg_sen, :boolean
      column :pr_deptrat, :float
      column :pr_unitlab, :float
      column :pr_inspecc, :boolean
      column :pr_totinsp, :float
      column :pr_roll, :varchar, :size => 20
    end
  end
end
