# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:aop_pred) do
      column :ao_order_n, :varchar, size: 12
      column :ao_op_num, :integer
      column :ao_parent_, :varchar, size: 12
      column :ao_parent2, :integer
      column :ao_depend_, :integer
      column :ao_lag, :integer
    end
  end
end
