# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:vbdocman) do
      column :dm_id, :varchar, size: 10
      column :dm_doc_typ, :varchar, size: 10
      column :dm_desc, :varchar, size: 50
      column :dm_last_up, :date
      column :dm_file, :varchar, size: 254
      column :dm_memo, :text
      column :dm_view_wi, :integer
      column :dm_protect, :boolean
      column :dm_cust_co, :varchar, size: 6
      column :dm_supp_co, :varchar, size: 6
      column :dm_emp_id, :varchar, size: 5
      column :dm_ca_code, :varchar, size: 12
      column :dm_fa_code, :varchar, size: 10
      column :dm_ar_inv_, :varchar, size: 7
      column :dm_ap_inv_, :varchar, size: 30
      column :dm_cmemo_n, :varchar, size: 7
      column :dm_dmemo_n, :varchar, size: 30
      column :dm_chk_acc, :varchar, size: 15
      column :dm_chk_num, :varchar, size: 10
      column :dm_dep_num, :varchar, size: 7
      column :dm_gj_id, :varchar, size: 10
      column :dm_referen, :varchar, size: 40
      column :dm_user_id, :varchar, size: 5
      column :dm_entry_t, :varchar, size: 2
    end
  end
end
