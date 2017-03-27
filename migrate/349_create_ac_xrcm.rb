# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_xrcm) do
      column :mr_cust_co, :varchar, size: 6
      column :mr_id, :varchar, size: 10
      column :mr_number, :varchar, size: 10
      column :mr_date, :date
      column :mr_inv_num, :varchar, size: 7
      column :mr_ship_co, :varchar, size: 8
      column :mr_referen, :varchar, size: 30
      column :mr_oc_amt, :decimal, precision: 15, scale: 4
      column :mr_oc_bal, :decimal, precision: 15, scale: 4
      column :mr_cred_am, :decimal, precision: 15, scale: 4
      column :mr_oc_new, :decimal, precision: 15, scale: 4
    end
  end
end
