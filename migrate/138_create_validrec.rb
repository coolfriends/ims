Sequel.migration do
  change do
     create_table(:validrec) do
      column :va_id, :varchar, :size => 10
      column :va_ship_co, :varchar, :size => 8
      column :va_order_n, :varchar, :size => 12
      column :va_invent_, :varchar, :size => 30
      column :va_contain, :integer
      column :va_box, :integer
      column :va_quantit, :float
      column :va_user_id, :varchar, :size => 5
      column :va_datetim, :datetime
      column :va_sord_nu, :varchar, :size => 7
    end
  end
end
