# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:op_lots) do
      column :ol_id, :varchar, size: 10
      column :ol_quote_n, :varchar, size: 15
      column :ol_order_n, :varchar, size: 12
      column :ol_op_num, :integer
      column :ol_vend_in, :integer
      column :ol_exclude, :boolean
      column :ol_desc, :varchar, size: 40
      column :ol_amt, :float
      column :ol_note, :text
      column :ol_invent_, :varchar, size: 30
    end
  end
end
