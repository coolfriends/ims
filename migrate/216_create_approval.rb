Sequel.migration do
  change do
     create_table(:approval) do
      column :ap_id, :varchar, :size => 10
      column :ap_source, :varchar, :size => 20
      column :ap_source_, :varchar, :size => 20
      column :ap_choice, :integer
      column :ap_emp_id, :varchar, :size => 5
      column :ap_notes, :text
      column :ap_date, :date
      column :ap_time, :varchar, :size => 10
      column :ap_de_id, :varchar, :size => 10
      column :ap_uber_us, :boolean
      column :ap_uber_u2, :text
      column :ap_checksu, :integer
      column :ap_rev, :varchar, :size => 3
      column :ap_source2, :varchar, :size => 20
    end
  end
end
