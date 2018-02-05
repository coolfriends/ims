Sequel.migration do
  change do
     create_table(:shiptype) do
      column :sh_ship_ty, :varchar, :size => 20
      column :sh_carrier, :varchar, :size => 10
    end
  end
end
