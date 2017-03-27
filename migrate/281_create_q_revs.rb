# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:q_revs) do
      column :qv_id, :varchar, size: 10
      column :qv_quote_n, :varchar, size: 15
      column :qv_number, :integer
      column :qv_qr_code, :varchar, size: 6
      column :qv_sales_p, :varchar, size: 5
      column :qv_enter_b, :varchar, size: 5
      column :qv_enter_d, :date
      column :qv_desc, :text
      column :qv_sord_nu, :varchar, size: 7
      column :qv_order_n, :varchar, size: 12
      column :qv_pr_id, :integer
      column :qv_po_num, :varchar, size: 7
      column :qv_sordq, :varchar, size: 7
    end
  end
end
