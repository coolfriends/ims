# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:tcardcat) do
      column :tc_code, :varchar, size: 2
      column :tc_desc, :varchar, size: 20
      column :tc_io, :varchar, size: 1
      column :tc_perm, :boolean
      column :tc_no_ta, :boolean
      column :tc_no_jc, :boolean
      column :tc_type, :integer
    end
  end
end
