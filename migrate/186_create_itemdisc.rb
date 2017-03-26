Sequel.migration do
  change do
     create_table(:itemdisc) do
      column :id_invent_, :varchar, :size => 30
      column :id_start_q, :float
      column :id_end_qty, :float
      column :id_amount, :float
      column :id_is_cost, :boolean
      column :id_option, :boolean
      column :id_percent, :boolean
      column :id_cust_co, :varchar, :size => 6
    end
  end
end
