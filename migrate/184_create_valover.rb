Sequel.migration do
  change do
     create_table(:valover) do
      column :vo_datetim, DateTime
      column :vo_emp_id, :varchar, :size => 5
      column :vo_order_n, :varchar, :size => 12
      column :vo_op_num, :integer
      column :vo_supervi, :varchar, :size => 5
      column :vo_skipped, :integer
    end
  end
end
