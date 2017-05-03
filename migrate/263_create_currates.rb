Sequel.migration do
  change do
     create_table(:currates) do
      column :cr_id, :varchar, :size => 10
      column :cr_code, :varchar, :size => 10
      column :cr_buy, :float
      column :cr_sell, :float
      column :cr_date, :date
      column :cr_inact, :boolean
    end
  end
end
