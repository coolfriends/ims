Sequel.migration do
  change do
     create_table(:contain) do
      column :ct_id, :varchar, :size => 10
      column :ct_il_id, :varchar, :size => 10
      column :ct_ib_id, :varchar, :size => 10
      column :ct_ship_co, :varchar, :size => 8
      column :ct_sd_id, :integer
      column :ct_tare_wg, :float
      column :ct_type, :varchar, :size => 3
      column :ct_invent_, :varchar, :size => 30
      column :ct_tot_box, :integer
      column :ct_order_n, :varchar, :size => 12
    end
  end
end
