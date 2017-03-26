Sequel.migration do
  change do
     create_table(:vshop) do
      column :vt_id, :integer
      column :vt_fullnam, :varchar, :size => 100
      column :vt_nodenam, :varchar, :size => 100
      column :vt_x, :bytea
      column :vt_y, :bytea
      column :vt_width, :bytea
      column :vt_height, :bytea
    end
  end
end
