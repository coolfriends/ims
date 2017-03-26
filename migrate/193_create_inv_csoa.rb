Sequel.migration do
  change do
     create_table(:inv_csoa) do
      column :io_id, :varchar, :size => 10
      column :io_ie_id, :varchar, :size => 10
      column :io_adj_dat, :date
      column :io_adj_uni, :float
      column :io_adj_ext, :float
      column :io_org_uni, :float
      column :io_org_ext, :float
      column :io_unit_co, :float
      column :io_ext_cos, :float
      column :io_invent_, :varchar, :size => 30
      column :io_type, :varchar, :size => 1
      column :io_adj_mat, :float
      column :io_adj_lab, :float
      column :io_adj_bur, :float
      column :io_adj_oth, :float
      column :io_unit_ma, :float
      column :io_unit_la, :float
      column :io_unit_bu, :float
      column :io_unit_ot, :float
      column :io_org_mat, :float
      column :io_org_lab, :float
      column :io_org_bur, :float
      column :io_org_oth, :float
      column :io_ext_mat, :float
      column :io_ext_lab, :float
      column :io_ext_bur, :float
      column :io_ext_oth, :float
      column :io_order_n, :varchar, :size => 12
      column :io_order_2, :varchar, :size => 12
      column :io_act_dat, DateTime
      column :io_user_id, :varchar, :size => 5
    end
  end
end
