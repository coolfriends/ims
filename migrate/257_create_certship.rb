# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:certship) do
      column :cs_id, :varchar, size: 10
      column :cs_ch_id, :varchar, size: 10
      column :cs_line_nu, :integer
      column :cs_ship_qt, :integer
      column :cs_lot_num, :varchar, size: 20
      column :cs_heat_nu, :varchar, size: 15
      column :cs_supp_co, :varchar, size: 6
      column :cs_supp_na, :varchar, size: 30
      column :cs_meltsou, :varchar, size: 20
      column :cs_tag_num, :integer
    end
  end
end
