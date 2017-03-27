# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:sodetlot) do
      column :sl_sord_nu, :varchar, size: 7
      column :sl_line_nu, :integer
      column :sl_ic_id, :varchar, size: 10
      column :sl_ic_quan, :float
    end
  end
end
