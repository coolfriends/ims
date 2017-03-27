# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:inv_jdtl) do
      column :ie_id, :varchar, size: 10
      column :ie_ij_id, :varchar, size: 10
      column :ie_ic_id, :varchar, size: 10
      column :ie_il_id, :varchar, size: 10
      column :ie_ib_id, :varchar, size: 10
      column :ie_invent_, :varchar, size: 30
      column :ie_supp_co, :varchar, size: 6
      column :ie_heat_nu, :varchar, size: 30
      column :ie_order_n, :varchar, size: 12
      column :ie_date, :date
      column :ie_quantit, :float
      column :ie_unit_co, :float
      column :ie_ext_cos, :float
      column :ie_lot_num, :varchar, size: 20
      column :ie_lo_code, :varchar, size: 10
      column :ie_consign, :boolean
      column :ie_package, :boolean
      column :ie_op_num, :integer
      column :ie_rev_num, :varchar, size: 6
      column :ie_rev_lev, :varchar, size: 3
      column :ie_ext_mat, :float
      column :ie_ext_lab, :float
      column :ie_ext_bur, :float
      column :ie_ext_oth, :float
      column :ie_tag_num, :integer
    end
  end
end
