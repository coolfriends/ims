# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ratehist) do
      column :rh_id, :varchar, size: 10
      column :rh_emp_id, :varchar, size: 5
      column :rh_date_ef, :date
      column :rh_hourly, :float
      column :rh_salary, :float
      column :rh_shift_d, :float
    end
  end
end
