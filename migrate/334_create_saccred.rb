Sequel.migration do
  change do
     create_table(:saccred) do
      column :sd_id, :varchar, :size => 10
      column :sd_sa_desc, :varchar, :size => 30
      column :sd_supp_co, :varchar, :size => 6
      column :sd_expire_, :date
    end
  end
end
