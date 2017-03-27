# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:as9102f1) do
      column :as_id, :varchar, size: 10
      column :part_num, :varchar, size: 30
      column :part_name, :varchar, size: 50
      column :serial_num, :varchar, size: 30
      column :fai_report, :varchar, size: 50
      column :rev_num, :varchar, size: 10
      column :draw_num, :varchar, size: 30
      column :draw_rev_l, :varchar, size: 10
      column :addition_c, :text
      column :man_proces, :varchar, size: 30
      column :organizati, :varchar, size: 50
      column :supplier_c, :varchar, size: 20
      column :po_number, :varchar, size: 30
      column :detail_fai, :varchar, size: 30
      column :full_parti, :integer
      column :parial_fai, :text
      column :signature_, :varchar, size: 5
      column :signature2, :date
      column :reviewedby, :varchar, size: 5
      column :reviewedb2, :date
      column :customer_a, :varchar, size: 30
      column :approval_d, :date
      column :fai_comple, :boolean
      column :invent_num, :varchar, size: 30
      column :cust_code, :varchar, size: 6
      column :order_num, :varchar, size: 12
      column :as_date, :date
    end
  end
end
