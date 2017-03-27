# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:cost_tot) do
      column :cl_quote_n, :varchar, size: 15
      column :cl_order_n, :varchar, size: 12
      column :cl_dist_co, :varchar, size: 2
      column :cl_est_cos, :float
      column :cl_act_cos, :float
    end
  end
end
