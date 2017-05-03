Sequel.migration do
  change do
     create_table(:gageass) do
      column :ga_id, :varchar, :size => 10
      column :ga_pm_id, :varchar, :size => 20
      column :ga_outdate, :date
      column :ga_indate, :date
      column :ga_order_n, :varchar, :size => 12
      column :ga_op_num, :integer
      column :ga_emp_id, :varchar, :size => 5
      column :ga_mach_co, :varchar, :size => 5
      column :ga_notes, :text
      column :ga_invent_, :varchar, :size => 30
      column :ga_il_id, :varchar, :size => 10
      column :ga_ib_id, :varchar, :size => 10
    end
  end
end
