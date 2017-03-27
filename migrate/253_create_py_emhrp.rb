# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_emhrp) do
      column :hp_id, :varchar, size: 10
      column :hp_hr_id, :varchar, size: 10
      column :hp_pd_id, :varchar, size: 10
      column :hp_order, :integer
      column :hp_evaluat, :integer
      column :hp_notes, :text
      column :hp_emp_id, :varchar, size: 5
      column :hp_weight, :integer
    end
  end
end
