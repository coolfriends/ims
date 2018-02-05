Sequel.migration do
  change do
     create_table(:vet_memo) do
      column :vm_id, :varchar, :size => 10
      column :vm_datelas, :date
      column :vm_desc, :varchar, :size => 35
      column :vm_type, :varchar, :size => 15
      column :vm_by, :varchar, :size => 5
      column :vm_memo, :text
      column :vm_seqnum, :integer
      column :vm_nc_id, :varchar, :size => 10
    end
  end
end
