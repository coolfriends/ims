# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:oplib_op) do
      column :oo_id, :integer
      column :oo_op_num, :integer
      column :oo_type, :varchar, size: 1
      column :oo_mach_co, :varchar, size: 5
      column :oo_suhr, :float
      column :oo_sur, :float
      column :oo_su, :float
      column :oo_gp, :float
      column :oo_pop, :integer
      column :oo_np, :float
      column :oo_hpu, :float
      column :oo_hr, :float
      column :oo_cpu, :float
      column :oo_note, :text
      column :oo_current, :integer
      column :oo_attend, :integer
      column :oo_queue, :float
      column :oo_dist_co, :varchar, size: 2
      column :oo_supp_co, :varchar, size: 6
      column :oo_unit_co, :float
      column :oo_quantit, :integer
      column :oo_ext_cos, :float
      column :oo_mark_up, :integer
      column :oo_tot_cos, :float
      column :oo_distrib, :boolean
      column :oo_cost1, :float
      column :oo_cost2, :float
      column :oo_cost3, :float
      column :oo_cost4, :float
      column :oo_cost5, :float
      column :oo_cost6, :float
      column :oo_cost7, :float
      column :oo_cost8, :float
      column :oo_cost9, :float
      column :oo_cost10, :float
      column :oo_recalc, :boolean
      column :oo_in_inve, :varchar, size: 30
      column :oo_out_inv, :varchar, size: 30
      column :oo_sched, :boolean
      column :oo_force, :boolean
      column :oo_rewflag, :boolean
      column :oo_perc_co, :integer
      column :oo_g_code, :varchar, size: 10
      column :oo_move_st, :boolean
      column :oo_ol_id, :integer
      column :oo_oplib_n, :text
      column :oo_hpp, :float
      column :oo_mpp, :float
      column :oo_spp, :float
      column :oo_burden, :float
      column :oo_pc_cost, :float
      column :oo_st_id, :varchar, size: 10
      column :oo_specnot, :boolean
    end
  end
end
