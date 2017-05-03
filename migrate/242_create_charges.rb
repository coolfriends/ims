Sequel.migration do
  change do
     create_table(:charges) do
      column :ch_carrier, :varchar, :size => 10
      column :ch_descrip, :varchar, :size => 60
      column :ch_fee, :float
      column :ch_per, :varchar, :size => 10
    end
  end
end
