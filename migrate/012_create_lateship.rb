Sequel.migration do
  change do
     create_table(:lateship) do
      column :ls_code, :varchar, :size => 10
      column :ls_desc, :varchar, :size => 100
    end
  end
end
