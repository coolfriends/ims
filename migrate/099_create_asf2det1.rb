Sequel.migration do
  change do
     create_table(:asf2det1) do
      column :f2_det1_id, :varchar, :size => 10
      column :process_na, :varchar, :size => 50
      column :spec_numbe, :varchar, :size => 50
      column :code, :varchar, :size => 25
      column :supplier_c, :varchar, :size => 30
      column :cust_appro, :varchar, :size => 10
      column :cofc_numbe, :varchar, :size => 30
      column :as_id, :varchar, :size => 10
      column :asf2_id, :varchar, :size => 10
    end
  end
end
