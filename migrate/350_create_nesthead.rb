Sequel.migration do
  change do
     create_table(:nesthead) do
      column :nh_id, :varchar, :size => 10
      column :nh_desc, :varchar, :size => 30
      column :nh_invent_, :varchar, :size => 30
      column :nh_mach_co, :varchar, :size => 5
      column :nh_percent, :integer
    end
  end
end
