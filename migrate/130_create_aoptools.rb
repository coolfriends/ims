# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:aoptools) do
      column :at_order_n, :varchar, size: 12
      column :at_op_num, :integer
      column :at_tool_nu, :integer
      column :at_mach_ca, :varchar, size: 5
      column :at_tool_ty, :varchar, size: 20
      column :at_speed, :float
      column :at_sp_adj, :integer
      column :at_adj_spe, :float
      column :at_feed, :float
      column :at_fe_adj, :integer
      column :at_adj_fee, :float
      column :at_sfm, :float
      column :at_ipr, :float
      column :at_gp, :float
      column :at_note, :text
      column :at_loc, :float
      column :at_passes, :integer
      column :at_work_di, :float
      column :at_current, :integer
      column :at_tool_di, :float
      column :at_num_flu, :integer
      column :at_const_v, :float
      column :at_mat_cod, :varchar, size: 6
      column :at_quantit, :integer
      column :at_desc, :varchar, size: 50
      column :at_positio, :integer
      column :at_endside, :integer
      column :at_unit_co, :float
      column :at_ext_cos, :float
      column :at_gp_sec, :float
      column :at_index_m, :float
      column :at_index_s, :float
      column :at_total_c, :float
      column :at_total_2, :float
      column :at_cam, :float
      column :at_cycle, :float
    end
  end
end
