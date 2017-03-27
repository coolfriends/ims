# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:nestdet) do
      column :nd_id, :varchar, size: 10
      column :nd_nh_id, :varchar, size: 10
      column :nd_qty_per, :integer
      column :nd_percent, :integer
      column :nd_invent_, :varchar, size: 30
      column :nd_mat_per, :integer
      column :nd_wgtperp, :float
    end
  end
end
