Sequel.migration do
  change do
     create_table(:mem_part) do
      column :mp_id, :varchar, :size => 10
      column :mp_vm_id, :varchar, :size => 10
      column :mp_inv_num, :varchar, :size => 30
      column :mp_supp_co, :varchar, :size => 6
    end
  end
end
