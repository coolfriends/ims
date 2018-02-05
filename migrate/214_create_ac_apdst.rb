Sequel.migration do
  change do
     create_table(:ac_apdst) do
      column :ad_id, :varchar, :size => 10
      column :ad_ap_id, :varchar, :size => 10
      column :ad_account, :varchar, :size => 12
      column :ad_item_re, :varchar, :size => 30
      column :ad_desc, :varchar, :size => 30
      column :ad_qty_rec, :float
      column :ad_unit_co, :decimal, :precision => 15, :scale => 4
      column :ad_po_num, :varchar, :size => 7
      column :ad_line_nu, :integer
      column :ad_unit_ty, :varchar, :size => 4
      column :ad_ext_cos, :decimal, :precision => 15, :scale => 4
      column :ad_dist_co, :varchar, :size => 2
      column :ad_gl_id, :varchar, :size => 10
      column :ad_unit_cu, :decimal, :precision => 15, :scale => 4
      column :ad_ext_cur, :decimal, :precision => 15, :scale => 4
      column :ad_tran_ty, :varchar, :size => 2
      column :ad_te, :varchar, :size => 1
      column :ad_po_line, :integer
      column :ad_st_id, :varchar, :size => 10
      column :ad_tax_rat, :float
      column :ad_st_tot_, :decimal, :precision => 15, :scale => 4
      column :ad_st_ex_s, :decimal, :precision => 15, :scale => 4
      column :ad_st_non_, :decimal, :precision => 15, :scale => 4
      column :ad_st_tax_, :decimal, :precision => 15, :scale => 4
      column :ad_st_non2, :decimal, :precision => 15, :scale => 4
      column :ad_st_tax2, :decimal, :precision => 15, :scale => 4
      column :ad_st_tax3, :decimal, :precision => 15, :scale => 4
      column :ad_st_tot2, :decimal, :precision => 15, :scale => 4
      column :ad_overrid, :boolean
      column :ad_excl_di, :boolean
      column :ad_mn_id, :varchar, :size => 10
      column :ad_dm_ap_i, :varchar, :size => 10
      column :ad_dm_ad_i, :varchar, :size => 10
      column :ad_dm_po_n, :varchar, :size => 7
      column :ad_dm_po_l, :integer
      column :ad_cost_ov, :boolean
      column :ad_dm_rec_, :integer
      column :ad_1099, :boolean
      column :ad_lock, :boolean
      column :ad_order_n, :varchar, :size => 12
      column :ad_distrib, :boolean
      column :ad_entry_d, :date
      column :ad_amortiz, :boolean
      column :ad_amort_a, :decimal, :precision => 15, :scale => 4
      column :ad_lot_not, :text
    end
  end
end
