# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:sord_ds) do
      column :ss_sord_nu, :varchar, size: 7
      column :ss_line_nu, :integer
      column :ss_rel_num, :integer
      column :ss_due_dat, :date
      column :ss_status, :varchar, size: 1
      column :ss_qty_rel, :float
      column :ss_prom_da, :date
      column :ss_qty_pro, :float
      column :ss_qty_shi, :float
      column :ss_qty_bal, :float
      column :ss_po_num, :varchar, size: 25
      column :ss_confirm, :boolean
      column :ss_qty_cum, :float
      column :ss_red_sta, :varchar, size: 1
      column :ss_reviewe, :boolean
      column :ss_note, :text
      column :ss_modifie, :boolean
      column :ss_shipby_, :date
      column :ss_reset_c, :boolean
      column :ss_reset_2, :float
      column :ss_earlies, :date
      column :ss_latest_, :date
      column :ss_auth_co, :varchar, size: 5
      column :ss_dock_co, :varchar, size: 5
      column :ss_comp_na, :varchar, size: 35
      column :ss_address, :varchar, size: 35
      column :ss_addres2, :varchar, size: 35
      column :ss_addres3, :varchar, size: 35
      column :ss_addres4, :varchar, size: 35
      column :ss_cust_co, :varchar, size: 6
      column :ss_ca_id, :varchar, size: 10
      column :ss_ca_stor, :varchar, size: 20
      column :ss_fab_dat, :date
      column :ss_order_n, :varchar, size: 12
      column :ss_eng_sda, :date
      column :ss_eng_eda, :date
      column :ss_fab_sda, :date
      column :ss_fab_eda, :date
      column :ss_est_hrs, :float
      column :ss_clevel, :integer
      column :ss_receive, :date
      column :ss_cust_re, :integer
    end
  end
end
