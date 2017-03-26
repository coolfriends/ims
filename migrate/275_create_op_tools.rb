Sequel.migration do
  change do
     create_table(:op_tools) do
      column :ot_quote_n, :varchar, :size => 15
      column :ot_op_num, :integer
      column :ot_tool_nu, :integer
      column :ot_mach_ca, :varchar, :size => 5
      column :ot_tool_ty, :varchar, :size => 20
      column :ot_speed, :float
      column :ot_sp_adj, :integer
      column :ot_adj_spe, :float
      column :ot_feed, :float
      column :ot_fe_adj, :integer
      column :ot_adj_fee, :float
      column :ot_sfm, :float
      column :ot_ipr, :float
      column :ot_gp, :float
      column :ot_note, :text
      column :ot_loc, :float
      column :ot_passes, :integer
      column :ot_work_di, :float
      column :ot_current, :integer
      column :ot_tool_di, :float
      column :ot_num_flu, :integer
      column :ot_const_v, :float
      column :ot_mat_cod, :varchar, :size => 6
      column :ot_quantit, :integer
      column :ot_desc, :varchar, :size => 50
      column :ot_positio, :integer
      column :ot_endside, :integer
      column :ot_unit_co, :float
      column :ot_ext_cos, :float
      column :ot_gp_sec, :float
      column :ot_index_m, :float
      column :ot_index_s, :float
      column :ot_total_c, :float
      column :ot_total_2, :float
      column :ot_cycle, :float
      column :ot_cam, :float
    end
  end
end
