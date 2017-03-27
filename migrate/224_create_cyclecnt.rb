# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:cyclecnt) do
      column :cc_id, :varchar, size: 10
      column :cc_batch, :integer
      column :cc_il_id, :varchar, size: 10
      column :cc_ib_id, :varchar, size: 10
      column :cc_ic_tag_, :integer
      column :cc_ic_id, :varchar, size: 10
      column :cc_emp_id, :varchar, size: 5
      column :cc_date, :date
      column :cc_quantit, :float
    end
  end
end
