Sequel.migration do
  change do
     create_table(:sopicked) do
      column :sp_sord_nu, :varchar, :size => 7
      column :sp_lo_code, :varchar, :size => 10
      column :sp_date, :date
    end
  end
end
