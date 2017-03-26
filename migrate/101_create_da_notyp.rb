Sequel.migration do
  change do
     create_table(:da_notyp) do
      column :nt_id, :varchar, :size => 10
      column :nt_desc, :varchar, :size => 35
      column :nt_abbrev, :varchar, :size => 5
      column :nt_status, :varchar, :size => 1
      column :nt_type, :varchar, :size => 1
      column :nt_default, :varchar, :size => 1
      column :nt_protect, :boolean
      column :nt_last_lo, :varchar, :size => 10
      column :nt_last_up, DateTime
    end
  end
end
