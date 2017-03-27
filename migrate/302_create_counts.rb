# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:counts) do
      column :co_id, :varchar, size: 10
      column :co_aj_id, :varchar, size: 10
      column :co_date_ti, DateTime
      column :co_user, :varchar, size: 5
      column :co_prod, :float
      column :co_review, :float
      column :co_scrap, :float
      column :co_good, :float
      column :co_notes, :text
      column :co_down_re, :varchar, size: 80
      column :co_weight, :float
      column :co_lot_num, :varchar, size: 20
      column :co_il_id, :varchar, size: 10
      column :co_ib_id, :varchar, size: 10
      column :co_ij_id, :varchar, size: 10
      column :co_invent_, :varchar, size: 30
      column :co_sc_ij_i, :varchar, size: 10
    end
  end
end
