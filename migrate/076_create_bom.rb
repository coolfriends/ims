# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:bom) do
      column :parent, :varchar, size: 30
      column :part_num, :varchar, size: 30
      column :count, :float
      column :length, :float
      column :width, :float
      column :qty_per, :float
      column :quote_num, :varchar, size: 15
      column :op_num, :integer
      column :usesuom, :boolean
      column :phantom, :boolean
      column :in_mm, :integer
      column :descriptio, :varchar, size: 30
      column :option_gro, :boolean
      column :group_desc, :varchar, size: 50
      column :default_op, :boolean
      column :option_not, :text
      column :sort_chars, :varchar, size: 10
      column :node_note, :text
      column :shipsepera, :boolean
      column :bom_id, :varchar, size: 10
      column :include_on, :boolean
      column :scrap_perc, :integer
      column :seq_num, :integer
      column :chipweight, :float
      column :chip_cost, :float
      column :scraprecov, :float
      column :disable, :boolean
      column :noprice, :boolean
    end
  end
end
