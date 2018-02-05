Sequel.migration do
  change do
     create_table(:qfreight) do
      column :qf_id, :varchar, :size => 10
      column :qf_quote_n, :varchar, :size => 15
      column :qf_fe_id, :varchar, :size => 10
      column :qf_count, :integer
      column :qf_calc_fr, :float
      column :qf_calc_f2, :float
      column :qf_calc_f3, :float
      column :qf_calc_f4, :float
      column :qf_calc_f5, :float
      column :qf_calc_f6, :float
      column :qf_calc_f7, :float
      column :qf_calc_f8, :float
      column :qf_calc_f9, :float
      column :qf_calc_10, :float
    end
  end
end
