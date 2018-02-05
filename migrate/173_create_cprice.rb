Sequel.migration do
  change do
     create_table(:cprice) do
      column :cp_id, :varchar, :size => 6
      column :cp_st_id, :varchar, :size => 6
      column :cp_ma_id, :varchar, :size => 6
      column :cp_cust_co, :varchar, :size => 6
      column :cp_unit_pr, :float
      column :cp_emp_id, :varchar, :size => 5
      column :cp_eff_dat, :date
      column :cp_notes, :text
    end
  end
end
