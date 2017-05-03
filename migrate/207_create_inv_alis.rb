Sequel.migration do
  change do
     create_table(:inv_alis) do
      column :ia_id, :varchar, :size => 10
      column :ia_invent_, :varchar, :size => 30
      column :ia_cust_co, :varchar, :size => 6
      column :ia_part_nu, :varchar, :size => 30
      column :ia_price, :float
      column :ia_eff_dat, :date
      column :ia_status, :varchar, :size => 1
      column :ia_order_n, :varchar, :size => 12
      column :ia_ord_dat, :date
      column :ia_emp_id, :varchar, :size => 5
      column :ia_po_num, :varchar, :size => 20
      column :ia_ppap_le, :varchar, :size => 10
      column :ia_quote_n, :varchar, :size => 15
      column :ia_samp_qt, :integer
      column :ia_samp_da, :date
      column :ia_buyer_n, :varchar, :size => 30
      column :ia_rep_nam, :varchar, :size => 30
      column :ia_ship_ad, :varchar, :size => 50
      column :ia_ship_a2, :varchar, :size => 50
      column :ia_ship_a3, :varchar, :size => 50
      column :ia_ship_a4, :varchar, :size => 50
      column :ia_ship_a5, :varchar, :size => 50
      column :ia_po_date, :date
      column :ia_ship_a6, :varchar, :size => 50
      column :ia_rep_emp, :varchar, :size => 5
      column :ia_rev_num, :varchar, :size => 3
      column :ia_desc, :varchar, :size => 50
      column :ia_ext_des, :text
      column :ia_expire_, :date
    end
  end
end
