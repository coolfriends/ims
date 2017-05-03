Sequel.migration do
  change do
     create_table(:material) do
      column :ma_id, :varchar, :size => 6
      column :ma_code, :varchar, :size => 30
      column :ma_compos, :text
      column :ma_colors, :text
      column :ma_arc_rat, :text
      column :ma_desc, :text
    end
  end
end
