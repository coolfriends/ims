# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_xpdm) do
      column :mn_supp_co, :varchar, size: 6
      column :mn_id, :varchar, size: 10
      column :mn_number, :varchar, size: 10
      column :mn_date, :date
      column :mn_inv_num, :varchar, size: 30
      column :mn_po_num, :varchar, size: 7
      column :mn_referen, :varchar, size: 30
      column :mn_oc_amt, :decimal, precision: 15, scale: 4
      column :mn_oc_bal, :decimal, precision: 15, scale: 4
      column :mn_cred_am, :decimal, precision: 15, scale: 4
      column :mn_oc_new, :decimal, precision: 15, scale: 4
    end
  end
end
