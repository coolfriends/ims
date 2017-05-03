Sequel.migration do
  change do
     create_table(:schboard) do
      column :sb_name, :varchar, :size => 30
      column :sb_is_edit, :boolean
      column :sb_needs_r, :boolean
    end
  end
end
