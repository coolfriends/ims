Sequel.migration do
  change do
     create_table(:incoterm) do
      column :ix_id, :varchar, :size => 3
      column :ix_desc, :varchar, :size => 70
    end
  end
end
