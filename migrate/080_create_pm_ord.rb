Sequel.migration do
  change do
     create_table(:pm_ord) do
      column :po_id, :varchar, :size => 10
      column :po_emp_id, :varchar, :size => 5
      column :po_task, :text
      column :po_order_n, :varchar, :size => 12
      column :po_comp_da, :date
      column :po_comment, :text
      column :po_pm_id, :varchar, :size => 20
      column :po_passfai, :integer
      column :po_due_dat, :date
    end
  end
end
