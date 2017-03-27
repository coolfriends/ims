# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:can_aprv) do
      column :ca_id, :varchar, size: 10
      column :ca_emp_id, :varchar, size: 5
      column :ca_de_id, :varchar, size: 10
      column :ca_canchan, :boolean
      column :ca_canappr, :boolean
    end
  end
end
