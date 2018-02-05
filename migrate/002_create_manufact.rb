Sequel.migration do
  change do
     create_table(:manufact) do
      column :ma_id, :varchar, :size => 10
      column :ma_manufac, :varchar, :size => 30
    end
  end
end
