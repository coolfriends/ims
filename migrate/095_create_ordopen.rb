Sequel.migration do
  change do
     create_table(:ordopen) do
      column :oo_id, :varchar, :size => 10
      column :oo_order_n, :varchar, :size => 12
    end
  end
end
