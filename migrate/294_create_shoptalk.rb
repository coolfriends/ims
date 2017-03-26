Sequel.migration do
  change do
     create_table(:shoptalk) do
      column :st_id, :varchar, :size => 10
      column :st_emp_id, :varchar, :size => 5
      column :st_datetim, DateTime
      column :st_order_n, :varchar, :size => 12
      column :st_invent_, :varchar, :size => 30
      column :st_cust_co, :varchar, :size => 6
      column :st_supp_co, :varchar, :size => 6
      column :st_comment, :text
      column :st_mach_co, :varchar, :size => 5
      column :st_part_nu, :varchar, :size => 30
    end
  end
end
