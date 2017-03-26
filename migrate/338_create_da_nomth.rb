Sequel.migration do
  change do
     create_table(:da_nomth) do
      column :nm_id, :varchar, :size => 10
      column :nm_desc, :varchar, :size => 35
      column :nm_abbrev, :varchar, :size => 5
      column :nm_default, :varchar, :size => 1
      column :nm_last_lo, :varchar, :size => 10
      column :nm_last_up, :datetime
    end
  end
end
