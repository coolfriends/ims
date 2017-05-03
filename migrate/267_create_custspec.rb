Sequel.migration do
  change do
     create_table(:custspec) do
      column :cs_id, :varchar, :size => 10
      column :cs_cust_co, :varchar, :size => 6
      column :cs_cust_sp, :varchar, :size => 30
      column :cs_st_id, :varchar, :size => 10
      column :cs_obsolet, :boolean
      column :cs_sg_id, :varchar, :size => 10
      column :cs_supp_co, :varchar, :size => 6
    end
  end
end
