# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:insthead) do
      column :nh_id, :varchar, size: 10
      column :nh_invent_, :varchar, size: 30
      column :nh_part_nu, :varchar, size: 30
      column :nh_rev_num, :varchar, size: 3
      column :nh_part_de, :varchar, size: 50
      column :nh_qcir_re, :varchar, size: 10
      column :nh_revised, :varchar, size: 40
      column :nh_prep_by, :varchar, size: 40
      column :nh_rev_dat, :date
      column :nh_refer_n, :varchar, size: 20
      column :nh_cid, :varchar, size: 20
      column :nh_order_n, :varchar, size: 12
      column :nh_inv_rev, :varchar, size: 3
      column :nh_rev_lev, :varchar, size: 3
      column :nh_heat_nu, :varchar, size: 20
      column :nh_cust_co, :varchar, size: 6
    end
  end
end
