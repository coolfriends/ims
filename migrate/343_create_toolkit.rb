Sequel.migration do
  change do
     create_table(:toolkit) do
      column :tk_id, :varchar, :size => 10
      column :tk_parent_, :varchar, :size => 30
      column :tk_child_i, :varchar, :size => 30
      column :tk_quantit, :integer
    end
  end
end
