Sequel.migration do
  change do
     create_table(:lzcycle) do
      column :lc_quote_n, :varchar, :size => 15
      column :lc_op_num, :integer
      column :lc_mat_cod, :varchar, :size => 6
      column :lc_desc, :varchar, :size => 60
      column :lc_diam_th, :float
      column :lc_lgc_loc, :float
      column :lc_lgc_tra, :float
      column :lc_lgc_spp, :float
      column :lc_mdc_loc, :float
      column :lc_mdc_tra, :float
      column :lc_mdc_spp, :float
      column :lc_smc_loc, :float
      column :lc_smc_tra, :float
      column :lc_smc_spp, :float
      column :lc_pierces, :integer
      column :lc_pierce_, :float
      column :lc_pierce2, :float
      column :lc_adj_spp, :float
      column :lc_total_s, :float
      column :lc_action, :text
      column :lc_date, :date
      column :lc_emp_id, :varchar, :size => 5
      column :lc_order_n, :varchar, :size => 12
      column :lc_assist_, :integer
      column :lc_burden, :float
    end
  end
end
