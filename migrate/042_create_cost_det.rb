Sequel.migration do
  change do
     create_table(:cost_det) do
      column :ct_quote_n, :varchar, :size => 15
      column :ct_order_n, :varchar, :size => 12
      column :ct_id, :integer
      column :ct_supp, :varchar, :size => 6
      column :ct_desc, :varchar, :size => 60
      column :ct_cost, :float
      column :ct_q, :float
      column :ct_uc, :float
      column :ct_dist_co, :varchar, :size => 2
      column :ct_inc_quo, :boolean
      column :ct_invoice, :boolean
      column :ct_inv_num, :varchar, :size => 7
      column :ct_entry_d, :date
      column :ct_unit_ty, :varchar, :size => 4
      column :ct_id_code, :varchar, :size => 10
      column :ct_de_id, :varchar, :size => 10
      column :ct_freight, :boolean
      column :ct_ad_id, :varchar, :size => 10
      column :ct_wp_id, :varchar, :size => 10
    end
  end
end
