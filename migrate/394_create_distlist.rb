Sequel.migration do
  change do
     create_table(:distlist) do
      column :dl_id, :integer
      column :dl_desc, :varchar, :size => 50
    end
  end
end
