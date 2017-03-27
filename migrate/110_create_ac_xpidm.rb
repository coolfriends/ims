# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_xpidm) do
      column :im_supp_co, :varchar, size: 6
      column :im_ap_id, :varchar, size: 10
      column :im_mn_id, :varchar, size: 10
      column :im_inv_num, :varchar, size: 30
      column :im_cred_am, :decimal, precision: 15, scale: 4
    end
  end
end
