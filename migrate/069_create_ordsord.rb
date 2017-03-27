# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ordsord) do
      column :os_id, :varchar, size: 10
      column :os_order_n, :varchar, size: 15
      column :os_sord_nu, :varchar, size: 7
      column :os_line_nu, :integer
      column :os_quantit, :integer
    end
  end
end
