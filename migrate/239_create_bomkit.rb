# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:bomkit) do
      column :bk_id, :varchar, size: 10
      column :bk_sord_nu, :varchar, size: 7
      column :bk_line_nu, :integer
      column :bk_invent_, :varchar, size: 15
      column :bk_qty_per, :float
      column :bk_prod_co, :varchar, size: 2
      column :bk_unit_pr, :float
      column :bk_disc_pr, :float
      column :bk_ext_pri, :float
      column :bk_kit_inv, :varchar, size: 15
      column :bk_discoun, :float
    end
  end
end
