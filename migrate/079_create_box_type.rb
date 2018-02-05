Sequel.migration do
  change do
     create_table(:box_type) do
      column :bt_code, :varchar, :size => 3
      column :bt_desc, :varchar, :size => 25
      column :bt_tare_wt, :float
      column :bt_edi_pkg, :varchar, :size => 5
      column :bt_type, :varchar, :size => 1
      column :bt_length, :float
      column :bt_width, :float
      column :bt_height, :float
    end
  end
end
