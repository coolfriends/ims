Sequel.migration do
  change do
     create_table(:aoperate) do
      column :ao_order_n, :varchar, :size => 12
      column :ao_op_num, :integer
      column :ao_type, :varchar, :size => 1
      column :ao_mach_co, :varchar, :size => 5
      column :ao_suhr, :float
      column :ao_sur, :float
      column :ao_su, :float
      column :ao_gp, :float
      column :ao_pop, :float
      column :ao_np, :float
      column :ao_hpu, :float
      column :ao_hr, :float
      column :ao_cpu, :float
      column :ao_note, :text
      column :ao_current, :integer
      column :ao_attend, :integer
      column :ao_queue, :float
      column :ao_dist_co, :varchar, :size => 2
      column :ao_supp_co, :varchar, :size => 6
      column :ao_unit_co, :float
      column :ao_quantit, :integer
      column :ao_ext_cos, :float
      column :ao_mark_up, :integer
      column :ao_tot_cos, :float
      column :ao_distrib, :boolean
      column :ao_cost1, :float
      column :ao_cost2, :float
      column :ao_cost3, :float
      column :ao_cost4, :float
      column :ao_cost5, :float
      column :ao_cost6, :float
      column :ao_cost7, :float
      column :ao_cost8, :float
      column :ao_cost9, :float
      column :ao_cost10, :float
      column :ao_recalc, :boolean
      column :ao_tsu, :integer
      column :ao_hrs_od, :float
      column :ao_hrs_td, :float
      column :ao_hrs_tot, :float
      column :ao_hrs_av, :float
      column :ao_p_prod, :float
      column :ao_p_bad, :integer
      column :ao_p_good, :float
      column :ao_qty_bal, :float
      column :ao_hrs_pro, :float
      column :ao_hrs_set, :float
      column :ao_scrap, :integer
      column :ao_rework, :integer
      column :ao_qty_pro, :float
      column :ao_qty_inv, :integer
      column :ao_act_phr, :float
      column :ao_adj_phr, :float
      column :ao_go_eff, :integer
      column :ao_p_eff, :integer
      column :ao_su_eff, :integer
      column :ao_perc_co, :integer
      column :ao_num_mac, :integer
      column :ao_qty_ord, :integer
      column :ao_incl_su, :varchar, :size => 100
      column :ao_end_dat, :text
      column :ao_sc_off, :varchar, :size => 100
      column :ao_labors, :float
      column :ao_burdens, :float
      column :ao_laborp, :float
      column :ao_burdenp, :float
      column :ao_force_m, :varchar, :size => 100
      column :ao_sched_q, :text
      column :ao_in_inve, :varchar, :size => 30
      column :ao_out_inv, :varchar, :size => 30
      column :ao_sched, :boolean
      column :ao_force, :boolean
      column :ao_rewflag, :boolean
      column :ao_g_code, :varchar, :size => 10
      column :ao_review, :integer
      column :ao_move_st, :boolean
      column :ao_complet, :boolean
      column :ao_master_, :integer
      column :ao_parent_, :integer
      column :ao_oplib_n, :text
      column :ao_il_id, :varchar, :size => 10
      column :ao_ib_id, :varchar, :size => 10
      column :ao_pagebre, :boolean
      column :ao_min_cha, :float
      column :ao_infin_m, :float
      column :ao_enforce, :boolean
      column :ao_setup_m, :boolean
      column :ao_setup_c, :integer
      column :ao_aggrega, :integer
      column :ao_last_pr, :boolean
      column :ao_split, :boolean
      column :ao_il_id_i, :varchar, :size => 10
      column :ao_ib_id_i, :varchar, :size => 10
      column :ao_optype, :integer
      column :ao_down, :integer
      column :ao_pc_lbs, :boolean
      column :ao_pc_cost, :float
      column :ao_aw_orde, :varchar, :size => 8
      column :ao_unit_ty, :varchar, :size => 4
      column :ao_infstar, :date
      column :ao_infend_, :date
      column :ao_statnot, :text
      column :ao_minqty, :integer
      column :ao_hpp, :float
      column :ao_mpp, :float
      column :ao_spp, :float
      column :ao_burden, :float
      column :ao_exclude, :boolean
      column :ao_comp_da, :date
      column :ao_sl, :text
      column :ao_pc_per_, :float
      column :ao_unit_ra, :float
      column :ao_need_qt, :float
      column :ao_surchar, :float
      column :ao_simple_, :boolean
      column :ao_lossper, :float
      column :ao_load_ti, :float
      column :ao_rpm, :integer
      column :ao_spindge, :varchar, :size => 15
      column :ao_changeg, :varchar, :size => 15
      column :ao_threadg, :varchar, :size => 15
      column :ao_st_id, :varchar, :size => 10
      column :ao_signifi, :boolean
      column :ao_post_pc, :boolean
      column :ao_sa_id, :varchar, :size => 10
      column :ao_donotor, :boolean
      column :ao_casting, :boolean
      column :ao_spindle, :integer
      column :ao_feed_rp, :integer
      column :ao_eff_thr, :integer
      column :ao_mtsc, :float
      column :ao_opqty, :float
      column :ao_freight, :float
      column :ao_freigh2, :float
      column :ao_lotqty, :float
      column :ao_infsta2, DateTime
      column :ao_infend2, DateTime
    end
  end
end
