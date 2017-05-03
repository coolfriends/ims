Sequel.migration do
  change do
     create_table(:shop_con) do
      column :sp_mach_na, :varchar, :size => 10
      column :sp_mach_co, :varchar, :size => 5
      column :sp_mach_de, :varchar, :size => 20
      column :sp_il_code, :varchar, :size => 10
      column :sp_type, :varchar, :size => 1
      column :sp_x, :integer
      column :sp_y, :integer
      column :sp_image, :varchar, :size => 80
      column :sp_width, :integer
      column :sp_height, :integer
    end
  end
end
