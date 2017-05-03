Sequel.migration do
  change do
     create_table(:mattime) do
      column :mt_quote_n, :varchar, :size => 15
      column :mt_order_n, :varchar, :size => 12
      column :mt_item, :integer
      column :mt_cut_qty, :float
      column :mt_fit_qty, :float
      column :mt_drill_q, :float
      column :mt_weld_qt, :float
      column :mt_other_q, :float
      column :mt_fit_min, :float
      column :mt_drill_m, :float
      column :mt_weld_mi, :float
      column :mt_cut_min, :float
      column :mt_other_m, :float
      column :mt_cut_tot, :float
      column :mt_fit_tot, :float
      column :mt_drill_t, :float
      column :mt_weld_to, :float
      column :mt_other_t, :float
      column :mt_time, :float
    end
  end
end
