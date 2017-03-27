# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:truckdet) do
      column :td_id, :varchar, size: 10
      column :td_tr_id, :varchar, size: 10
      column :td_seq, :integer
      column :td_sord_nu, :varchar, size: 7
      column :td_line_nu, :integer
      column :td_rel_num, :integer
      column :td_invent_, :varchar, size: 30
      column :td_quantit, :float
      column :td_ship_co, :varchar, size: 8
      column :td_ship_li, :integer
      column :td_tarp, :boolean
      column :td_priorit, :integer
    end
  end
end
