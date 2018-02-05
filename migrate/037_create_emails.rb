Sequel.migration do
  change do
     create_table(:emails) do
      column :em_id, :varchar, :size => 10
      column :em_datecre, DateTime
      column :em_fromnam, :varchar, :size => 40
      column :em_toname, :varchar, :size => 40
      column :em_subject, :varchar, :size => 250
      column :em_filenam, :varchar, :size => 250
      column :em_mailima, :varchar, :size => 4
      column :em_cust_co, :varchar, :size => 6
      column :em_supp_co, :varchar, :size => 6
      column :em_cc_id, :varchar, :size => 10
      column :em_sord_nu, :varchar, :size => 7
      column :em_order_n, :varchar, :size => 15
      column :em_po_num, :varchar, :size => 7
      column :em_quote_n, :varchar, :size => 30
      column :em_nc_id, :varchar, :size => 10
      column :em_sordq_s, :varchar, :size => 7
      column :em_inv_num, :varchar, :size => 7
      column :em_ap_id, :varchar, :size => 10
      column :em_mr_id, :varchar, :size => 10
      column :em_mn_id, :varchar, :size => 10
    end
  end
end
