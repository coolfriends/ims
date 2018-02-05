Sequel.migration do
  change do
     create_table(:da_notrg) do
      column :nr_id, :varchar, :size => 10
      column :nr_desc, :varchar, :size => 35
      column :nr_last_lo, :varchar, :size => 10
      column :nr_last_up, DateTime
    end
  end
end
