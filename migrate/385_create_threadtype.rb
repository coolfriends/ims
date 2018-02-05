Sequel.migration do
  change do
     create_table(:threadtype) do
      column :tt_id, :varchar, :size => 10
      column :tt_descrip, :varchar, :size => 30
    end
  end
end
