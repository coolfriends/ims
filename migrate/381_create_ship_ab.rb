Sequel.migration do
  change do
     create_table(:ship_ab) do
      column :sb_ship_co, :varchar, :size => 6
      column :sb_carrier, :varchar, :size => 10
      column :sb_descrip, :varchar, :size => 60
      column :sb_fee, :float
      column :sb_per, :varchar, :size => 10
    end
  end
end
