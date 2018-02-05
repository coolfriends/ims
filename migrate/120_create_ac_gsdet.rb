Sequel.migration do
  change do
     create_table(:ac_gsdet) do
      column :gd_id, :varchar, :size => 10
      column :gd_gc_id, :varchar, :size => 10
      column :gd_gs_date, :date
      column :gd_ca_numb, :varchar, :size => 12
      column :gd_amt, :float
      column :gd_source, :varchar, :size => 20
      column :gd_type, :varchar, :size => 3
      column :gd_inv_num, :varchar, :size => 7
    end
  end
end
