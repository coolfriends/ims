Sequel.migration do
  change do
     create_table(:earnhrs) do
      column :jc_run_dat, :date
      column :jc_shift, :varchar, :size => 2
      column :jc_mach_co, :varchar, :size => 5
      column :jc_order_n, :varchar, :size => 12
      column :or_order_r, :varchar, :size => 21
      column :or_quote_n, :varchar, :size => 15
      column :jc_parts_g, :float
      column :jc_setup, :float
      column :jc_run, :float
      column :jc_gp, :float
      column :jc_adj_phr, :float
      column :jc_go_eff, :float
      column :jc_p_eff, :float
      column :jc_o_eff, :float
      column :jc_eff, :float
      column :jc_std_eff, :float
      column :jc_operati, :integer
      column :op_suhr, :float
      column :op_gp, :float
      column :op_np, :float
      column :or_part_nu, :varchar, :size => 30
      column :or_invent_, :varchar, :size => 30
      column :jc_hrs_set, :float
      column :jc_accum_h, :float
      column :jc_hrs_ava, :float
      column :jc_hrs_pro, :float
      column :jc_num_mac, :integer
      column :em_emp_nam, :varchar, :size => 40
      column :em_emp_id, :varchar, :size => 5
      column :spr_code, :varchar, :size => 1
      column :tc_tot_tim, :float
      column :or_cust_co, :varchar, :size => 6
      column :cu_cust_na, :varchar, :size => 35
      column :dept_id, :varchar, :size => 2
      column :std_mpp, :float
      column :act_mpp, :float
      column :rate, :float
      column :earned_hrs, :float
      column :earned_hr2, :float
      column :earned_rat, :float
      column :dept_ratio, :float
      column :mt_mach_de, :varchar, :size => 20
      column :dept_name, :varchar, :size => 30
      column :jc_id, :varchar, :size => 10
    end
  end
end
