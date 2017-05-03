Sequel.migration do
  change do
     create_table(:vacation) do
      column :va_id, :varchar, :size => 10
      column :va_date, :date
      column :va_type, :varchar, :size => 1
      column :va_paid, :boolean
      column :va_emp_id, :varchar, :size => 5
      column :va_mach_co, :varchar, :size => 5
    end
  end
end
