Sequel.migration do
  change do
     create_table(:pw) do
      column :pw_id, :varchar, :size => 10
      column :pw_quote_n, :varchar, :size => 15
      column :pw_index, :integer
      column :pw_dia1, :float
      column :pw_dia2, :float
      column :pw_length, :float
      column :pw_shape, :varchar, :size => 10
      column :pw_vol, :float
      column :pw_type, :integer
      column :pw_order_n, :varchar, :size => 12
      column :pw_qi_item, :integer
    end
  end
end
