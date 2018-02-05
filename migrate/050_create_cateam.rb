Sequel.migration do
  change do
     create_table(:cateam) do
      column :ct_ca_id, :varchar, :size => 10
      column :ct_emp_id, :varchar, :size => 11
    end
  end
end
