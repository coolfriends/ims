Sequel.migration do
  change do
     create_table(:da_notpc) do
      column :ni_id, :varchar, :size => 10
      column :ni_desc, :varchar, :size => 35
      column :ni_last_lo, :varchar, :size => 10
      column :ni_last_up, :datetime
    end
  end
end
