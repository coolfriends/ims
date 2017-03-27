# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:wcscrap) do
      column :ws_mach_co, :varchar, size: 5
      column :ws_start_q, :float
      column :ws_end_qty, :float
      column :ws_scrap_p, :float
      column :ws_quote_n, :varchar, size: 15
      column :ws_op_num, :integer
    end
  end
end
