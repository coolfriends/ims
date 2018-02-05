Sequel.migration do
  change do
     create_table(:schedule) do
      column :sd_run_cod, :varchar, :size => 20
      column :sd_mach_co, :varchar, :size => 5
      column :sd_order_n, :varchar, :size => 12
      column :sd_operati, :integer
      column :sd_rel_num, :integer
      column :sd_qty_sch, :float
      column :sd_start_d, :date
      column :sd_new_sta, :date
      column :sd_inc_su, :varchar, :size => 1
      column :sd_slip_da, :integer
      column :sd_est_net, :float
      column :sd_act_net, :float
      column :sd_end_dat, :date
      column :sd_rev_eda, :date
      column :sd_parts_p, :float
      column :sd_qty_bal, :float
      column :sd_hrs_nee, :float
      column :sd_su_rema, :float
      column :sd_hrs_rem, :float
      column :sd_hrs_ava, :float
      column :sd_hrs_set, :float
      column :sd_hrs_tot, :float
      column :sd_hrs_tdo, :float
      column :sd_hrs_odo, :float
      column :sd_hrs_pro, :float
      column :sd_parts_g, :float
      column :sd_parts_b, :float
      column :sd_gp, :float
      column :sd_np, :float
      column :sd_act_phr, :float
      column :sd_adj_phr, :float
      column :sd_go_eff, :integer
      column :sd_p_eff, :integer
      column :sd_su_eff, :integer
      column :sd_ppbar, :float
      column :sd_act_ppb, :integer
      column :sd_in_inve, :varchar, :size => 30
      column :sd_out_inv, :varchar, :size => 30
      column :sd_req_bar, :integer
      column :sd_rework, :float
      column :sd_scrap, :float
      column :sd_notes, :text
      column :sd_sl, :text
      column :sd_ph, :varchar, :size => 1
      column :sd_lock, :boolean
      column :sd_status, :varchar, :size => 1
      column :sd_ss_sord, :varchar, :size => 7
      column :sd_ss_line, :integer
      column :sd_ss_rel_, :integer
      column :sd_ss_due_, :date
      column :sd_emp_id, :varchar, :size => 5
      column :sd_quote_n, :varchar, :size => 15
      column :sd_op_op_n, :integer
      column :sd_type, :integer
      column :sd_bufferh, :float
      column :sd_isnewqu, :boolean
      column :sd_isorder, :boolean
      column :sd_isquote, :boolean
      column :sd_isfroze, :boolean
      column :sd_tools, :boolean
      column :sd_materia, :boolean
      column :sd_fai, :boolean
      column :sd_qualtit, :boolean
      column :sd_custome, :boolean
      column :sd_late, :boolean
      column :sd_latecus, :boolean
      column :sd_oreleas, :varchar, :size => 15
      column :sd_is_froz, :boolean
      column :sd_mats, :text
    end
  end
end
