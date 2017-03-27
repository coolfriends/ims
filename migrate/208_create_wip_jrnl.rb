# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:wip_jrnl) do
      column :wp_id, :varchar, size: 10
      column :wp_order_n, :varchar, size: 12
      column :wp_date, :date
      column :wp_type, :varchar, size: 1
      column :wp_key, :varchar, size: 20
      column :wp_labor, :float
      column :wp_burden, :float
      column :wp_materia, :float
      column :wp_other, :float
      column :wp_total, :float
      column :wp_referen, :varchar, size: 50
      column :wp_invent_, :varchar, size: 30
      column :wp_quantit, :float
      column :wp_user_id, :varchar, size: 5
      column :wp_unit_la, :float
      column :wp_unit_bu, :float
      column :wp_unit_ma, :float
      column :wp_unit_ot, :float
      column :wp_datetim, DateTime
      column :wp_prod_co, :varchar, size: 2
      column :wp_dist_co, :varchar, size: 2
      column :wp_unit_to, :float
      column :wp_op_num, :integer
    end
  end
end
