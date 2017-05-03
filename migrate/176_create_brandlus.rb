Sequel.migration do
  change do
     create_table(:brandlus) do
      column :bl_type, :integer
      column :bl_desc, :varchar, :size => 40
      column :bl_active, :boolean
    end
  end
end
