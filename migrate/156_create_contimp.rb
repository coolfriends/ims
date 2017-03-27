# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:contimp) do
      column :ct_id, :varchar, size: 10
      column :ct_date, :date
      column :ct_dept, :varchar, size: 30
      column :ct_area, :varchar, size: 50
      column :ct_emp_id, :varchar, size: 5
      column :ct_title, :varchar, size: 30
      column :ct_improve, :text
      column :ct_just_da, :date
      column :ct_justifi, :text
      column :ct_total_c, :float
      column :ct_cost_de, :varchar, size: 50
      column :ct_savings, :float
      column :ct_saving2, :varchar, size: 50
      column :ct_due_dat, :date
      column :ct_new_due, :date
      column :ct_approve, :boolean
      column :ct_complet, :boolean
      column :ct_date_co, :date
    end
  end
end
