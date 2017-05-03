Sequel.migration do
  change do
     create_table(:da_notcm) do
      column :nc_id, :varchar, :size => 10
      column :nc_ns_id, :varchar, :size => 10
      column :nc_desc, :varchar, :size => 35
      column :nc_last_lo, :varchar, :size => 10
      column :nc_last_up, DateTime
    end
  end
end
