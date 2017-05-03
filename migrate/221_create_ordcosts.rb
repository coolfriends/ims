Sequel.migration do
  change do
     create_table(:ordcosts) do
      column :order_num, :varchar, :size => 12
      column :part_num, :varchar, :size => 30
      column :invent_num, :varchar, :size => 30
      column :qty_prod, :integer
      column :status, :varchar, :size => 1
      column :hours, :float
      column :labor, :float
      column :burden, :float
      column :material, :float
      column :other, :float
      column :perpiece, :float
    end
  end
end
