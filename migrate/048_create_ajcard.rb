Sequel.migration do
  change do
     create_table(:ajcard) do
      column :aj_id, :varchar, :size => 10
      column :aj_run_dat, :date
      column :aj_card_st, :varchar, :size => 1
      column :aj_shift, :varchar, :size => 2
      column :aj_order_n, :varchar, :size => 12
      column :aj_operati, :integer
      column :aj_mach_co, :varchar, :size => 5
      column :aj_emp_id, :varchar, :size => 5
      column :aj_in_inve, :varchar, :size => 30
      column :aj_in_inv2, :varchar, :size => 30
      column :aj_in_inv3, :varchar, :size => 30
      column :aj_in_inv4, :varchar, :size => 30
      column :aj_in_inv5, :varchar, :size => 30
      column :aj_in_inv6, :varchar, :size => 30
      column :aj_in_inv7, :varchar, :size => 30
      column :aj_in_inv8, :varchar, :size => 30
      column :aj_in_inv9, :varchar, :size => 30
      column :aj_in_in10, :varchar, :size => 30
      column :aj_in_qty, :float
      column :aj_in_qty1, :float
      column :aj_in_qty2, :float
      column :aj_in_qty3, :float
      column :aj_in_qty4, :float
      column :aj_in_qty5, :float
      column :aj_in_qty6, :float
      column :aj_in_qty7, :float
      column :aj_in_qty8, :float
      column :aj_in_qty9, :float
      column :aj_hrs_ava, :float
      column :aj_hrs_set, :float
      column :aj_hrs_tot, :float
      column :aj_hrs_tdo, :float
      column :aj_hrs_odo, :float
      column :aj_hrs_pro, :float
      column :aj_down_re, :varchar, :size => 40
      column :aj_parts_p, :float
      column :aj_parts_b, :float
      column :aj_parts_g, :float
      column :aj_out_inv, :varchar, :size => 30
      column :aj_down_r2, :varchar, :size => 40
      column :aj_run_cod, :varchar, :size => 20
      column :aj_su, :integer
      column :aj_rework, :float
      column :aj_scrap, :float
      column :aj_track1, :varchar, :size => 6
      column :aj_time_ca, :varchar, :size => 2
      column :aj_time_c2, :varchar, :size => 2
      column :aj_time_c3, :varchar, :size => 2
      column :aj_time_c4, :varchar, :size => 2
      column :aj_time_c5, :varchar, :size => 2
      column :aj_time_c6, :varchar, :size => 2
      column :aj_time_c7, :varchar, :size => 2
      column :aj_time_c8, :varchar, :size => 2
      column :aj_time_c9, :varchar, :size => 2
      column :aj_time_10, :varchar, :size => 2
      column :aj_time_11, :varchar, :size => 2
      column :aj_time_12, :varchar, :size => 2
      column :aj_time_13, :varchar, :size => 2
      column :aj_time_14, :varchar, :size => 2
      column :aj_time_15, :varchar, :size => 2
      column :aj_time1, :varchar, :size => 10
      column :aj_time2, :varchar, :size => 10
      column :aj_time3, :varchar, :size => 10
      column :aj_time4, :varchar, :size => 10
      column :aj_time5, :varchar, :size => 10
      column :aj_time6, :varchar, :size => 10
      column :aj_time7, :varchar, :size => 10
      column :aj_time8, :varchar, :size => 10
      column :aj_time9, :varchar, :size => 10
      column :aj_time10, :varchar, :size => 10
      column :aj_time11, :varchar, :size => 10
      column :aj_time12, :varchar, :size => 10
      column :aj_time13, :varchar, :size => 10
      column :aj_time14, :varchar, :size => 10
      column :aj_time15, :varchar, :size => 10
      column :aj_date1, :date
      column :aj_date2, :date
      column :aj_date3, :date
      column :aj_date4, :date
      column :aj_date5, :date
      column :aj_date6, :date
      column :aj_date7, :date
      column :aj_date8, :date
      column :aj_date9, :date
      column :aj_date10, :date
      column :aj_date11, :date
      column :aj_date12, :date
      column :aj_date13, :date
      column :aj_date14, :date
      column :aj_date15, :date
      column :aj_sec1, :integer
      column :aj_sec2, :integer
      column :aj_sec3, :integer
      column :aj_sec4, :integer
      column :aj_sec5, :integer
      column :aj_sec6, :integer
      column :aj_sec7, :integer
      column :aj_sec8, :integer
      column :aj_sec9, :integer
      column :aj_sec10, :integer
      column :aj_sec11, :integer
      column :aj_sec12, :integer
      column :aj_sec13, :integer
      column :aj_sec14, :integer
      column :aj_sec15, :integer
      column :aj_elap1, :float
      column :aj_elap2, :float
      column :aj_elap3, :float
      column :aj_elap4, :float
      column :aj_elap5, :float
      column :aj_elap6, :float
      column :aj_elap7, :float
      column :aj_elap8, :float
      column :aj_elap9, :float
      column :aj_elap10, :float
      column :aj_elap11, :float
      column :aj_elap12, :float
      column :aj_elap13, :float
      column :aj_elap14, :float
      column :aj_elap15, :float
      column :aj_tot_tim, :float
      column :aj_time_da, :date
      column :aj_ot_hrs_, :float
      column :aj_ot_hrs2, :float
      column :aj_calc, :varchar, :size => 2
      column :aj_calc1, :varchar, :size => 2
      column :aj_calc2, :varchar, :size => 2
      column :aj_calc3, :varchar, :size => 2
      column :aj_calc4, :varchar, :size => 2
      column :aj_calc5, :varchar, :size => 2
      column :aj_calc6, :varchar, :size => 2
      column :aj_calc7, :varchar, :size => 2
      column :aj_calc8, :varchar, :size => 2
      column :aj_calc9, :varchar, :size => 2
      column :aj_heat_nu, :integer
      column :aj_heat_n2, :integer
      column :aj_heat_n3, :integer
      column :aj_heat_n4, :integer
      column :aj_heat_n5, :integer
      column :aj_heat_n6, :integer
      column :aj_heat_n7, :integer
      column :aj_heat_n8, :integer
      column :aj_heat_n9, :integer
      column :aj_heat_10, :integer
      column :aj_num_mac, :integer
      column :aj_rel_num, :integer
      column :aj_notes, :text
      column :aj_complet, :boolean
      column :aj_last_ti, :varchar, :size => 10
      column :aj_last_qt, :float
      column :aj_last_q2, :float
      column :aj_last_q3, :float
      column :aj_last_q4, :float
      column :aj_last_ef, :float
      column :aj_last_e2, :float
      column :aj_op_comp, :boolean
      column :aj_parent_, :varchar, :size => 8
      column :aj_raw_inv, :varchar, :size => 30
      column :aj_is_nest, :boolean
      column :aj_nest_co, :boolean
      column :aj_nest_ot, :integer
      column :aj_inlot_n, :varchar, :size => 20
      column :aj_il_id, :varchar, :size => 10
      column :aj_ib_id, :varchar, :size => 10
      column :aj_id_code, :varchar, :size => 10
      column :aj_de_id, :varchar, :size => 10
      column :aj_nestmod, :integer
      column :aj_nh_id, :varchar, :size => 10
      column :aj_other_d, :varchar, :size => 5
      column :aj_tool_ty, :varchar, :size => 20
      column :aj_st_id, :varchar, :size => 2
      column :aj_lc_id, :varchar, :size => 10
    end
  end
end
