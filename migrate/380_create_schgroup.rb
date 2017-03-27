# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:schgroup) do
      column :sg_g_code, :varchar, size: 10
      column :sg_g_desc, :varchar, size: 30
      column :sg_file, :varchar, size: 80
      column :sg_mach_op, :boolean
      column :sg_rate, :float
      column :sg_indexti, :float
      column :sg_toothco, :integer
      column :sg_toothc2, :integer
      column :sg_toothc3, :integer
    end
  end
end
