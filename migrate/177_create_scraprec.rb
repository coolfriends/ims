Sequel.migration do
  change do
     create_table(:scraprec) do
      column :sr_id, :varchar, :size => 10
      column :sr_order_n, :varchar, :size => 12
      column :sr_date, :date
      column :sr_desc, :varchar, :size => 60
      column :sr_amount, :float
      column :sr_weight, :float
      column :sr_value, :float
      column :sr_jc_id, :varchar, :size => 10
      column :sr_item, :integer
    end
  end
end
