# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:empwc) do
      column :ew_emp_id, :varchar, size: 5
      column :ew_mach_co, :varchar, size: 5
      column :ew_hrly_ra, :float
      column :ew_id, :varchar, size: 10
    end
  end
end
