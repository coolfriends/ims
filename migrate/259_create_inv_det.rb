# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:inv_det) do
      column :id_inv_num, :varchar, size: 7
      column :id_line_nu, :integer
      column :id_tran_ty, :varchar, size: 2
      column :id_invent_, :varchar, size: 30
      column :id_ship_co, :varchar, size: 8
      column :id_desc, :varchar, size: 50
      column :id_prod_co, :varchar, size: 2
      column :id_qty_ord, :float
      column :id_qty_shi, :float
      column :id_qty_bo, :float
      column :id_unit_ty, :varchar, size: 4
      column :id_unit_pr, :float
      column :id_discoun, :float
      column :id_disc_pr, :float
      column :id_ext_pri, :float
      column :id_te, :varchar, size: 1
      column :id_note, :text
      column :id_note_fl, :varchar, size: 1
      column :id_order_n, :varchar, size: 12
      column :id_rel_num, :integer
      column :id_po_num, :varchar, size: 15
      column :id_rel_qty, :float
      column :id_ij_id, :varchar, size: 10
      column :id_sd_id, :integer
      column :id_ar_gl_n, :varchar, size: 12
      column :id_pc_gl_n, :varchar, size: 12
      column :id_gl_id, :varchar, size: 10
      column :id_tax_rat, :float
      column :id_part_nu, :varchar, size: 30
      column :id_rev_num, :varchar, size: 6
      column :id_pmemo, :text
      column :id_lot_shi, :varchar, size: 20
      column :id_st_id, :varchar, size: 10
      column :id_emp_id, :varchar, size: 5
      column :id_comm_fl, :boolean
      column :id_comm_pe, :float
      column :id_comm_am, :float
      column :id_st_tot_, :float
      column :id_st_ex_s, :float
      column :id_st_non_, :float
      column :id_st_tax_, :float
      column :id_st_non2, :float
      column :id_st_tax2, :float
      column :id_st_tax3, :float
      column :id_st_tot2, :float
      column :id_unit_cu, :float
      column :id_disc_cu, :float
      column :id_ext_cur, :float
      column :id_il_id, :varchar, size: 10
      column :id_ib_id, :varchar, size: 10
      column :id_lot_num, :varchar, size: 20
      column :id_heat_nu, :varchar, size: 30
      column :id_decimal, :integer
      column :id_emp_id2, :varchar, size: 5
      column :id_comm_p2, :float
      column :id_comm_a2, :float
      column :id_mr_id, :varchar, size: 10
      column :id_cm_inv_, :varchar, size: 7
      column :id_cm_inv2, :integer
      column :id_cm_ship, :varchar, size: 8
      column :id_cm_shi2, :integer
      column :id_overrid, :boolean
      column :id_surchar, :float
      column :id_surch_c, :float
      column :id_ca_code, :varchar, size: 12
      column :id_ca_cod2, :varchar, size: 12
      column :id_ca_cod3, :varchar, size: 12
      column :id_ca_cod4, :varchar, size: 12
      column :id_gl_id_m, :varchar, size: 10
      column :id_gl_id_l, :varchar, size: 10
      column :id_gl_id_b, :varchar, size: 10
      column :id_gl_id_o, :varchar, size: 10
      column :id_gl_id_f, :varchar, size: 10
      column :id_amt_mat, :float
      column :id_amt_lab, :float
      column :id_amt_bur, :float
      column :id_amt_oth, :float
      column :id_amt_fin, :float
      column :id_ca_cod5, :varchar, size: 12
      column :id_gl_num_, :varchar, size: 12
      column :id_gl_num2, :varchar, size: 12
      column :id_gl_id_d, :varchar, size: 10
      column :id_gl_id_s, :varchar, size: 10
      column :id_amt_dsc, :float
      column :id_amt_sch, :float
      column :id_amt_gro, :float
      column :id_length, :float
      column :id_width, :float
      column :id_quantit, :float
      column :id_wght, :float
      column :id_sc_inv_, :varchar, size: 7
      column :id_sc_line, :integer
      column :id_sc_invo, :boolean
      column :id_sord_nu, :varchar, size: 7
      column :id_sord_li, :integer
      column :id_mu_gm, :integer
      column :id_st_over, :boolean
      column :id_lo_code, :varchar, size: 10
      column :id_qtyuom, :varchar, size: 4
      column :id_comm_ho, :boolean
      column :id_excl_di, :boolean
      column :id_receive, :varchar, size: 12
    end
  end
end
