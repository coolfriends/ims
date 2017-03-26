Sequel.migration do
  change do
     create_table(:da_noprb) do
      column :np_id, :varchar, :size => 10
      column :np_desc, :varchar, :size => 35
      column :np_last_lo, :varchar, :size => 10
      column :np_last_up, :datetime
    end
  end
end
