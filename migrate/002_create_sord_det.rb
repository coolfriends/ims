# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:sord_det) do
      column :sd_sord_nu, :varchar, size: 7
      column :sd_inv_num, :varchar, size: 7
      column :sd_line_nu, :integer
      column :sd_tran_ty, :varchar, size: 2
      column :sd_quote_n, :varchar, size: 15
      column :sd_invent_, :varchar, size: 30
      column :sd_ship_co, :varchar, size: 8
      column :sd_desc, :varchar, size: 50
      column :sd_prod_co, :varchar, size: 2
      column :sd_qty_ord, :float
      column :sd_qty_shi, :float
      column :sd_qty_bo, :float
      column :sd_unit_ty, :varchar, size: 4
      column :sd_unit_pr, :float
      column :sd_discoun, :float
      column :sd_disc_pr, :float
      column :sd_ext_pri, :float
      column :sd_te, :varchar, size: 1
      column :sd_note, :text
      column :sd_note_fl, :varchar, size: 1
      column :sd_order_n, :varchar, size: 12
      column :sd_rel_dat, :date
      column :sd_po_num, :varchar, size: 15
      column :sd_rel_qty, :float
      column :sd_qty_all, :float
      column :sd_qq, :integer
      column :sd_part_nu, :varchar, size: 30
      column :sd_rev_num, :varchar, size: 6
      column :sd_ext_uni, :float
      column :sd_pmemo, :text
      column :sd_tax_rat, :float
      column :sd_contact, :varchar, size: 25
      column :sd_st_id, :varchar, size: 10
      column :sd_emp_id, :varchar, size: 5
      column :sd_comm_fl, :boolean
      column :sd_comm_pe, :float
      column :sd_comm_am, :float
      column :sd_user_id, :varchar, size: 5
      column :sd_last_mo, DateTime
      column :sd_unit_cu, :float
      column :sd_disc_cu, :float
      column :sd_ext_cur, :float
      column :sd_extu_cu, :float
      column :sd_gm_dock, :varchar, size: 12
      column :sd_gm_math, :varchar, size: 10
      column :sd_gm_ref, :varchar, size: 10
      column :sd_gm_cont, :varchar, size: 15
      column :sd_gm_z13, :varchar, size: 20
      column :sd_gm_z14, :varchar, size: 20
      column :sd_gm_z15, :varchar, size: 20
      column :sd_gm_z16, :varchar, size: 20
      column :sd_gm_z17, :varchar, size: 20
      column :sd_gm_lice, :varchar, size: 30
      column :sd_gm_gros, :varchar, size: 15
      column :sd_gm_pcs_, :varchar, size: 15
      column :sd_il_id, :varchar, size: 10
      column :sd_ib_id, :varchar, size: 10
      column :sd_lot_num, :varchar, size: 20
      column :sd_heat_nu, :varchar, size: 30
      column :sd_backflu, :boolean
      column :sd_decimal, :integer
      column :sd_roll_in, :float
      column :sd_roll_ou, :float
      column :sd_sheet_w, :float
      column :sd_sheet_l, :float
      column :sd_sheet_c, :float
      column :sd_price_p, :float
      column :sd_sheet_g, :varchar, size: 1
      column :sd_dont_as, :boolean
      column :sd_emp_id2, :varchar, size: 5
      column :sd_comm_p2, :float
      column :sd_comm_a2, :float
      column :sd_lo_code, :varchar, size: 10
      column :sd_overrid, :boolean
      column :sd_req_cof, :boolean
      column :sd_req_mat, :boolean
      column :sd_req_plc, :boolean
      column :sd_req_htc, :boolean
      column :sd_surchar, :float
      column :sd_surch_c, :float
      column :sd_multi_r, :boolean
      column :sd_serial_, :varchar, size: 20
      column :sd_ser_typ, :integer
      column :sd_seriali, :boolean
      column :sd_exp_pro, :varchar, size: 40
      column :sd_exp_tar, :varchar, size: 20
      column :sd_exp_cnt, :varchar, size: 20
      column :sd_exp_par, :boolean
      column :sd_exp_con, :boolean
      column :sd_exp_dut, :integer
      column :sd_exp_exp, :varchar, size: 80
      column :sd_exp_pri, :boolean
      column :sd_exp_pr2, :boolean
      column :sd_exp_pr3, :boolean
      column :sd_prod_li, :varchar, size: 30
      column :sd_exclude, :boolean
      column :sd_customi, :float
      column :sd_comp_na, :varchar, size: 33
      column :sd_address, :varchar, size: 33
      column :sd_addres2, :varchar, size: 33
      column :sd_addres3, :varchar, size: 33
      column :sd_addres4, :varchar, size: 33
      column :sd_ca_id, :varchar, size: 10
      column :sd_length, :float
      column :sd_width, :float
      column :sd_quantit, :float
      column :sd_wght, :float
      column :sd_po_line, :varchar, size: 7
      column :sd_complet, :boolean
      column :sd_rev_lev, :varchar, size: 3
      column :sd_recurri, :boolean
      column :sd_mu_gm, :integer
      column :sd_confcos, :boolean
      column :sd_dont_po, :boolean
      column :sd_holes, :integer
      column :sd_stock_i, :boolean
      column :sd_pr_inst, :varchar, size: 30
      column :sd_alterna, :float
      column :sd_edi_ack, :varchar, size: 2
      column :sd_edi_qty, :float
      column :sd_return_, :float
      column :sd_return, :boolean
      column :sd_return2, :float
      column :sd_rma, :varchar, size: 10
      column :sd_return3, :text
      column :sd_return4, :varchar, size: 8
      column :sd_gm_tran, :boolean
      column :sd_qtyuom, :varchar, size: 4
      column :sd_ccnote, :text
      column :sd_receive, :varchar, size: 12
    end
  end
end
