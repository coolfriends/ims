Sequel.migration do
  change do
     create_table(:ac_xcust) do
      column :cu_cust_co, :varchar, :size => 6
      column :cu_referen, :varchar, :size => 30
      column :cu_total_r, :decimal, :precision => 15, :scale => 4
      column :cu_applied, :decimal, :precision => 15, :scale => 4
      column :cu_open_cr, :decimal, :precision => 15, :scale => 4
    end
  end
end
