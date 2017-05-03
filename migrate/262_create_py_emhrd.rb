Sequel.migration do
  change do
     create_table(:py_emhrd) do
      column :hd_id, :varchar, :size => 10
      column :hd_emp_id, :varchar, :size => 5
      column :hd_da_id, :varchar, :size => 10
      column :hd_dd_id, :varchar, :size => 10
      column :hd_date, :date
      column :hd_occurs, :integer
      column :hd_notes, :text
      column :hd_emp_id_, :varchar, :size => 5
    end
  end
end
