# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_dept) do
      column :de_id, :varchar, size: 2
      column :de_desc, :varchar, size: 30
      column :de_emp_id, :varchar, size: 5
      column :de_printer, :varchar, size: 50
      column :de_chg_app, :boolean
      column :de_gl_num, :varchar, size: 12
      column :de_exp_dep, :varchar, size: 6
      column :de_ra_gl_n, :varchar, size: 12
      column :de_hrs_rat, :float
      column :de_laborra, :float
    end
  end
end
