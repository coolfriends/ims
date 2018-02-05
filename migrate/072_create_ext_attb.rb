Sequel.migration do
  change do
     create_table(:ext_attb) do
      column :z_cextattb, :varchar, :size => 20
      column :z_cextatt2, :varchar, :size => 20
      column :z_cextatt3, :varchar, :size => 20
      column :z_cextatt4, :varchar, :size => 20
      column :z_cextatt5, :varchar, :size => 20
      column :z_cextatt6, :varchar, :size => 20
      column :z_cextatt7, :varchar, :size => 20
      column :z_cextatt8, :varchar, :size => 20
      column :z_cextatt9, :varchar, :size => 20
      column :z_cextat10, :varchar, :size => 20
      column :z_cextat11, :varchar, :size => 20
      column :z_cextat12, :varchar, :size => 20
      column :z_cextat13, :varchar, :size => 20
      column :z_cextat14, :varchar, :size => 20
    end
  end
end
