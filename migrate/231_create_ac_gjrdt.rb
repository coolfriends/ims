# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_gjrdt) do
      column :rd_id, :varchar, size: 10
      column :rd_sort, :integer
      column :rd_rc_id, :varchar, size: 10
      column :rd_type, :integer
      column :rd_ca_numb, :varchar, size: 12
      column :rd_amount, :decimal, precision: 15, scale: 4
      column :rd_memo, :text
    end
  end
end
