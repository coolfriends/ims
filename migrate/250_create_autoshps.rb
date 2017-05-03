Sequel.migration do
  change do
     create_table(:autoshps) do
      column :as_id, :varchar, :size => 10
      column :as_invent_, :varchar, :size => 30
      column :as_quantit, :float
      column :as_importe, :boolean
      column :as_user_id, :varchar, :size => 5
      column :as_date, :date
      column :as_cust_co, :varchar, :size => 6
    end
  end
end
