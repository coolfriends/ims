Sequel.migration do
  change do
     create_table(:salesrep) do
      column :sr_id, :varchar, :size => 10
      column :sr_tr_id, :varchar, :size => 10
      column :sr_emp_id, :varchar, :size => 5
    end
  end
end
