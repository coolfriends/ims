Sequel.migration do
  change do
     create_table(:vshop) do
      column :vt_id, :integer
      column :vt_fullnam, :varchar, :size => 100
      column :vt_nodenam, :varchar, :size => 100
      column :vt_x, :binary
      column :vt_y, :binary
      column :vt_width, :binary
      column :vt_height, :binary
    end
  end
end
