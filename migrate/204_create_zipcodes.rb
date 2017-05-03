Sequel.migration do
  change do
     create_table(:zipcodes) do
      column :zc_id, :varchar, :size => 10
      column :zc_lo_id, :varchar, :size => 10
      column :zc_code, :varchar, :size => 5
      column :zc_mailcod, :varchar, :size => 10
    end
  end
end
