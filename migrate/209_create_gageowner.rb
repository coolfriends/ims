Sequel.migration do
  change do
     create_table(:gageowner) do
      column :go_id, :varchar, :size => 10
      column :go_descrip, :varchar, :size => 30
    end
  end
end
