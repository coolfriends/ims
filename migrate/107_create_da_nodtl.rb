# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:da_nodtl) do
      column :nd_id, :varchar, size: 10
      column :nd_no_id, :varchar, size: 10
      column :nd_ni_id, :varchar, size: 10
      column :nd_nc_id, :varchar, size: 10
      column :nd_emp_id, :varchar, size: 5
      column :nd_follow_, :date
      column :nd_complet, :integer
      column :nd_outcome, :varchar, size: 35
      column :nd_outcom2, :text
      column :nd_last_lo, :varchar, size: 10
      column :nd_last_up, DateTime
    end
  end
end
