# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:jcardman) do
      column :jc_id, :varchar, size: 10
      column :jc_run_dat, :date
      column :jc_shift, :varchar, size: 2
      column :jc_order_n, :varchar, size: 12
      column :jc_operati, :integer
      column :jc_mach_co, :varchar, size: 5
      column :jc_emp_id, :varchar, size: 5
      column :jc_in_inve, :varchar, size: 30
      column :jc_in_qty, :float
      column :jc_hrs_ava, :float
      column :jc_hrs_set, :float
      column :jc_hrs_tot, :float
      column :jc_hrs_tdo, :float
      column :jc_hrs_odo, :float
      column :jc_hrs_pro, :float
      column :jc_down_re, :varchar, size: 80
      column :jc_parts_p, :float
      column :jc_parts_b, :float
      column :jc_parts_g, :float
      column :jc_out_inv, :varchar, size: 30
      column :jc_gp, :float
      column :jc_np, :float
      column :jc_act_phr, :float
      column :jc_adj_phr, :float
      column :jc_go_eff, :integer
      column :jc_p_eff, :integer
      column :jc_o_eff, :integer
      column :jc_run_cod, :varchar, size: 20
      column :jc_su, :integer
      column :jc_prod1, :float
      column :jc_prod2, :float
      column :jc_prod3, :float
      column :jc_prod4, :float
      column :jc_rework1, :float
      column :jc_rework2, :float
      column :jc_rework3, :float
      column :jc_rework4, :float
      column :jc_rework, :float
      column :jc_scrap1, :float
      column :jc_scrap2, :float
      column :jc_scrap3, :float
      column :jc_scrap4, :float
      column :jc_scrap, :float
      column :jc_track1, :varchar, size: 10
      column :jc_track2, :varchar, size: 10
      column :jc_track3, :varchar, size: 10
      column :jc_track4, :varchar, size: 10
      column :jc_good1, :float
      column :jc_good2, :float
      column :jc_good3, :float
      column :jc_good4, :float
      column :jc_burdenp, :float
      column :jc_burdens, :float
      column :jc_laborp, :float
      column :jc_labors, :float
      column :jc_num_mac, :integer
      column :jc_calc, :varchar, size: 2
      column :jc_ot_hrs_, :float
      column :jc_ot_hrs2, :float
      column :jc_rel_num, :integer
      column :jc_in_inv2, :varchar, size: 30
      column :jc_in_inv3, :varchar, size: 30
      column :jc_in_inv4, :varchar, size: 30
      column :jc_in_inv5, :varchar, size: 30
      column :jc_in_inv6, :varchar, size: 30
      column :jc_in_inv7, :varchar, size: 30
      column :jc_in_inv8, :varchar, size: 30
      column :jc_in_inv9, :varchar, size: 30
      column :jc_in_in10, :varchar, size: 30
      column :jc_in_qty1, :float
      column :jc_in_qty2, :float
      column :jc_in_qty3, :float
      column :jc_in_qty4, :float
      column :jc_in_qty5, :float
      column :jc_in_qty6, :float
      column :jc_in_qty7, :float
      column :jc_in_qty8, :float
      column :jc_in_qty9, :float
      column :jc_calc1, :varchar, size: 2
      column :jc_calc2, :varchar, size: 2
      column :jc_calc3, :varchar, size: 2
      column :jc_calc4, :varchar, size: 2
      column :jc_calc5, :varchar, size: 2
      column :jc_calc6, :varchar, size: 2
      column :jc_calc7, :varchar, size: 2
      column :jc_calc8, :varchar, size: 2
      column :jc_calc9, :varchar, size: 2
      column :jc_heat_nu, :varchar, size: 30
      column :jc_heat_n2, :integer
      column :jc_heat_n3, :integer
      column :jc_heat_n4, :integer
      column :jc_heat_n5, :integer
      column :jc_heat_n6, :integer
      column :jc_heat_n7, :integer
      column :jc_heat_n8, :integer
      column :jc_heat_n9, :integer
      column :jc_heat_10, :integer
      column :jc_ws, :boolean
      column :jc_review1, :float
      column :jc_review2, :float
      column :jc_review3, :float
      column :jc_review, :float
      column :jc_defect, :varchar, size: 10
      column :jc_il_id, :varchar, size: 10
      column :jc_ib_id, :varchar, size: 10
      column :jc_ij_id, :varchar, size: 10
      column :jc_sc_ij_i, :varchar, size: 10
      column :jc_zero_wi, :boolean
      column :jc_move_st, :boolean
      column :jc_dot_hrs, :float
      column :jc_dot_hr2, :float
      column :jc_complet, :boolean
      column :jc_lot_num, :varchar, size: 20
      column :jc_notes, :text
      column :jc_other_d, :varchar, size: 5
      column :jc_perc_at, :integer
      column :jc_inlot_n, :varchar, size: 20
      column :jc_wip_tra, :boolean
      column :jc_resave, :boolean
      column :jc_insp_by, :varchar, size: 5
      column :jc_repost_, :boolean
      column :jc_incl_re, :boolean
      column :jc_reject, :integer
      column :jc_id_code, :varchar, size: 10
      column :jc_de_id, :varchar, size: 10
      column :jc_startup, :boolean
      column :jc_aj_id, :varchar, size: 10
      column :jc_passfai, :integer
      column :jc_tool_ty, :varchar, size: 20
      column :jc_st_id, :varchar, size: 2
      column :jc_lc_id, :varchar, size: 10
      column :jc_rg_id, :varchar, size: 10
      column :jc_wp_id, :varchar, size: 10
    end
  end
end
