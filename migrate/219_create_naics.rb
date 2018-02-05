Sequel.migration do
  change do
     create_table(:naics) do
      column :na_ncode, :varchar, :size => 6
      column :na_ndesc, :varchar, :size => 60
    end
  end
end
