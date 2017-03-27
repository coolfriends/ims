# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:intaudit) do
      column :ia_id, :varchar, size: 10
      column :ia_date, :date
      column :ia_de_id, :varchar, size: 2
      column :ia_emp_by, :varchar, size: 5
      column :ia_lead, :varchar, size: 5
      column :ia_comp_da, :date
      column :ia_areas, :text
      column :ia_questio, :text
      column :ia_results, :text
      column :ia_focus, :text
      column :ia_rating, :integer
      column :ia_prev_ra, :integer
      column :ia_status, :varchar, size: 1
      column :ia_contact, :varchar, size: 5
      column :ia_meet_da, :date
      column :ia_meet_ti, :varchar, size: 10
      column :ia_reaudit, :boolean
    end
  end
end
