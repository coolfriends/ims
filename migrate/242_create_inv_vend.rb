# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:inv_vend) do
      column :va_id, :varchar, size: 10
      column :va_invent_, :varchar, size: 30
      column :va_supp_co, :varchar, size: 6
      column :va_part_nu, :varchar, size: 30
      column :va_approve, :boolean
      column :va_app_dat, :date
      column :va_app_by, :varchar, size: 5
      column :va_cost, :float
      column :va_purch_u, :varchar, size: 2
      column :va_manufac, :varchar, size: 30
      column :va_notes, :text
    end
  end
end
