Sequel.migration do
  change do
     create_table(:specstds) do
      column :ss_id, :varchar, :size => 10
      column :ss_sg_id, :varchar, :size => 10
      column :ss_st_id, :varchar, :size => 10
    end
  end
end
