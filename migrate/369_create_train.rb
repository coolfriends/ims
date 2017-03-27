# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:train) do
      column :tr_id, :varchar, size: 10
      column :tr_emp_id, :varchar, size: 5
      column :tr_standar, :varchar, size: 10
      column :tr_trained, :varchar, size: 6
      column :tr_notes, :text
      column :tr_exp_dat, :date
      column :tr_desc, :varchar, size: 50
      column :tr_date, :date
      column :tr_mach_co, :varchar, size: 5
      column :tr_hours, :float
      column :tr_invent_, :varchar, size: 30
      column :tr_dept_co, :varchar, size: 2
      column :tr_score, :integer
      column :tr_pf, :integer
      column :tr_train_c, :float
      column :tr_supp_co, :varchar, size: 6
    end
  end
end
