# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:thdwire) do
      column :tw_threads, :varchar, size: 10
      column :tw_wire_mm, :float
      column :tw_wire_in, :float
      column :tw_correct, :float
      column :tw_mmle4, :float
      column :tw_mmgt4, :float
      column :tw_pdle1_pt, :float
      column :tw_pdto4, :float
    end
  end
end
