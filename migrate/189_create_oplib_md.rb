Sequel.migration do
  change do
     create_table(:oplib_md) do
      column :ol_id, :integer
      column :ol_code, :varchar, :size => 15
      column :ol_descrip, :varchar, :size => 140
      column :ol_ea1, :varchar, :size => 30
      column :ol_ea2, :varchar, :size => 30
      column :ol_ea3, :varchar, :size => 30
      column :ol_ea4, :varchar, :size => 30
      column :ol_ea5, :varchar, :size => 30
      column :ol_ea6, :varchar, :size => 30
      column :ol_ea7, :varchar, :size => 30
      column :ol_ea8, :varchar, :size => 30
      column :ol_ea9, :varchar, :size => 30
      column :ol_ea10, :varchar, :size => 30
      column :ol_notes, :text
      column :ol_unit_ty, :varchar, :size => 4
    end
  end
end
