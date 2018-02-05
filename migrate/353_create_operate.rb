Sequel.migration do
  change do
     create_table(:operate) do
      column :op_quote_n, :varchar, :size => 15
      column :op_op_num, :integer
      column :op_type, :varchar, :size => 1
      column :op_mach_co, :varchar, :size => 5
      column :op_suhr, :float
      column :op_sur, :float
      column :op_su, :float
      column :op_gp, :float
      column :op_pop, :float
      column :op_np, :float
      column :op_hpu, :float
      column :op_hr, :float
      column :op_cpu, :float
      column :op_note, :text
      column :op_current, :integer
      column :op_attend, :integer
      column :op_queue, :float
      column :op_dist_co, :varchar, :size => 2
      column :op_supp_co, :varchar, :size => 6
      column :op_unit_co, :float
      column :op_quantit, :integer
      column :op_ext_cos, :float
      column :op_mark_up, :integer
      column :op_tot_cos, :float
      column :op_distrib, :boolean
      column :op_cost1, :float
      column :op_cost2, :float
      column :op_cost3, :float
      column :op_cost4, :float
      column :op_cost5, :float
      column :op_cost6, :float
      column :op_cost7, :float
      column :op_cost8, :float
      column :op_cost9, :float
      column :op_cost10, :float
      column :op_recalc, :boolean
      column :op_in_inve, :varchar, :size => 30
      column :op_out_inv, :varchar, :size => 30
      column :op_sched, :boolean
      column :op_force, :boolean
      column :op_rewflag, :boolean
      column :op_perc_co, :integer
      column :op_g_code, :varchar, :size => 10
      column :op_move_st, :boolean
      column :op_master_, :integer
      column :op_parent_, :integer
      column :op_oplib_n, :text
      column :op_il_id, :varchar, :size => 10
      column :op_ib_id, :varchar, :size => 10
      column :op_pagebre, :boolean
      column :op_min_cha, :float
      column :op_min_ch2, :float
      column :op_min_ch3, :float
      column :op_min_ch4, :float
      column :op_min_ch5, :float
      column :op_min_ch6, :float
      column :op_min_ch7, :float
      column :op_min_ch8, :float
      column :op_min_ch9, :float
      column :op_min_c10, :float
      column :op_unit_c2, :float
      column :op_unit_c3, :float
      column :op_unit_c4, :float
      column :op_unit_c5, :float
      column :op_unit_c6, :float
      column :op_unit_c7, :float
      column :op_unit_c8, :float
      column :op_unit_c9, :float
      column :op_unit_10, :float
      column :op_unit_11, :float
      column :op_quanti2, :integer
      column :op_quanti3, :integer
      column :op_quanti4, :integer
      column :op_quanti5, :integer
      column :op_quanti6, :integer
      column :op_quanti7, :integer
      column :op_quanti8, :integer
      column :op_quanti9, :integer
      column :op_quant10, :integer
      column :op_quant11, :integer
      column :op_ext_co2, :float
      column :op_ext_co3, :float
      column :op_ext_co4, :float
      column :op_ext_co5, :float
      column :op_ext_co6, :float
      column :op_ext_co7, :float
      column :op_ext_co8, :float
      column :op_ext_co9, :float
      column :op_ext_c10, :float
      column :op_ext_c11, :float
      column :op_mark_u2, :integer
      column :op_mark_u3, :integer
      column :op_mark_u4, :integer
      column :op_mark_u5, :integer
      column :op_mark_u6, :integer
      column :op_mark_u7, :integer
      column :op_mark_u8, :integer
      column :op_mark_u9, :integer
      column :op_mark_10, :integer
      column :op_mark_11, :integer
      column :op_tot_co2, :float
      column :op_tot_co3, :float
      column :op_tot_co4, :float
      column :op_tot_co5, :float
      column :op_tot_co6, :float
      column :op_tot_co7, :float
      column :op_tot_co8, :float
      column :op_tot_co9, :float
      column :op_tot_c10, :float
      column :op_tot_c11, :float
      column :op_suhr1, :float
      column :op_suhr2, :float
      column :op_suhr3, :float
      column :op_suhr4, :float
      column :op_suhr5, :float
      column :op_suhr6, :float
      column :op_suhr7, :float
      column :op_suhr8, :float
      column :op_suhr9, :float
      column :op_suhr10, :float
      column :op_sur1, :float
      column :op_sur2, :float
      column :op_sur3, :float
      column :op_sur4, :float
      column :op_sur5, :float
      column :op_sur6, :float
      column :op_sur7, :float
      column :op_sur8, :float
      column :op_sur9, :float
      column :op_sur10, :float
      column :op_gp1, :float
      column :op_gp2, :float
      column :op_gp3, :float
      column :op_gp4, :float
      column :op_gp5, :float
      column :op_gp6, :float
      column :op_gp7, :float
      column :op_gp8, :float
      column :op_gp9, :float
      column :op_gp10, :float
      column :op_pop1, :integer
      column :op_pop2, :integer
      column :op_pop3, :integer
      column :op_pop4, :integer
      column :op_pop5, :integer
      column :op_pop6, :integer
      column :op_pop7, :integer
      column :op_pop8, :integer
      column :op_pop9, :integer
      column :op_pop10, :integer
      column :op_np1, :float
      column :op_np2, :float
      column :op_np3, :float
      column :op_np4, :float
      column :op_np5, :float
      column :op_np6, :float
      column :op_np7, :float
      column :op_np8, :float
      column :op_np9, :float
      column :op_np10, :float
      column :op_hpu1, :float
      column :op_hpu2, :float
      column :op_hpu3, :float
      column :op_hpu4, :float
      column :op_hpu5, :float
      column :op_hpu6, :float
      column :op_hpu7, :float
      column :op_hpu8, :float
      column :op_hpu9, :float
      column :op_hpu10, :float
      column :op_hr1, :float
      column :op_hr2, :float
      column :op_hr3, :float
      column :op_hr4, :float
      column :op_hr5, :float
      column :op_hr6, :float
      column :op_hr7, :float
      column :op_hr8, :float
      column :op_hr9, :float
      column :op_hr10, :float
      column :op_attend1, :integer
      column :op_attend2, :integer
      column :op_attend3, :integer
      column :op_attend4, :integer
      column :op_attend5, :integer
      column :op_attend6, :integer
      column :op_attend7, :integer
      column :op_attend8, :integer
      column :op_attend9, :integer
      column :op_atten10, :integer
      column :op_cpu1, :float
      column :op_cpu2, :float
      column :op_cpu3, :float
      column :op_cpu4, :float
      column :op_cpu5, :float
      column :op_cpu6, :float
      column :op_cpu7, :float
      column :op_cpu8, :float
      column :op_cpu9, :float
      column :op_cpu10, :float
      column :op_su1, :float
      column :op_su2, :float
      column :op_su3, :float
      column :op_su4, :float
      column :op_su5, :float
      column :op_su6, :float
      column :op_su7, :float
      column :op_su8, :float
      column :op_su9, :float
      column :op_su10, :float
      column :op_infin_m, :float
      column :op_enforce, :boolean
      column :op_setup_m, :boolean
      column :op_setup_c, :integer
      column :op_aggrega, :integer
      column :op_invent_, :varchar, :size => 30
      column :op_last_pr, :boolean
      column :op_split, :boolean
      column :op_il_id_i, :varchar, :size => 10
      column :op_ib_id_i, :varchar, :size => 10
      column :op_optype, :integer
      column :op_down, :integer
      column :op_pc_lbs, :boolean
      column :op_pc_cost, :float
      column :op_aw_quot, :varchar, :size => 15
      column :op_unit_ty, :varchar, :size => 4
      column :op_minqty, :integer
      column :op_hpp, :float
      column :op_mpp, :float
      column :op_spp, :float
      column :op_burden, :float
      column :op_exclude, :boolean
      column :op_pc_per_, :float
      column :op_unit_ra, :float
      column :op_need_qt, :float
      column :op_surchar, :float
      column :op_simple_, :boolean
      column :op_lossper, :float
      column :op_load_ti, :float
      column :op_rpm, :integer
      column :op_obsolet, :boolean
      column :op_spindge, :varchar, :size => 15
      column :op_changeg, :varchar, :size => 15
      column :op_threadg, :varchar, :size => 15
      column :op_st_id, :varchar, :size => 10
      column :op_signifi, :boolean
      column :op_post_pc, :boolean
      column :op_apw, :float
      column :op_sa_id, :varchar, :size => 10
      column :op_emp_id, :varchar, :size => 5
      column :op_spindle, :integer
      column :op_feed_rp, :integer
      column :op_eff_thr, :integer
      column :op_casting, :boolean
      column :op_mtsc, :float
    end
  end
end
