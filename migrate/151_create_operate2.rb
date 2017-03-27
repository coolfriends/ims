# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:operate2) do
      column :o2_quote_n, :varchar, size: 15
      column :o2_op_num, :integer
      column :o2_onetime, :float
      column :o2_amort_t, :float
    end
  end
end
