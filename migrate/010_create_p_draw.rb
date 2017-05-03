Sequel.migration do
  change do
     create_table(:p_draw) do
      column :pd_id, :integer
      column :pd_pr_id, :integer
      column :pd_number, :varchar, :size => 15
      column :pd_revisio, :varchar, :size => 3
      column :pd_desc, :varchar, :size => 30
    end
  end
end
