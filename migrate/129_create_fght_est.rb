# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:fght_est) do
      column :fe_id, :varchar, size: 10
      column :fe_dest_zi, :varchar, size: 5
      column :fe_desc, :varchar, size: 30
      column :fe_min_cha, :float
      column :fe_miles, :integer
      column :fe_per_mil, :float
    end
  end
end
