# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:q_cust) do
      column :cu_cust_co, :varchar, size: 6
      column :cu_cust_na, :varchar, size: 35
      column :cu_mail_ad, :varchar, size: 35
      column :cu_mail_a2, :varchar, size: 35
      column :cu_mail_ci, :varchar, size: 30
      column :cu_mail_st, :varchar, size: 3
      column :cu_mail_cn, :varchar, size: 25
      column :cu_mail_zi, :varchar, size: 10
      column :cu_contact, :varchar, size: 25
      column :cu_cust_ph, :varchar, size: 14
      column :cu_cust_fa, :varchar, size: 14
      column :cu_cust_me, :text
      column :cu_pay_ter, :varchar, size: 20
      column :cu_ship_vi, :varchar, size: 20
      column :cu_emp_id, :varchar, size: 5
      column :cu_commiss, :float
      column :cu_cust_ty, :varchar, size: 4
      column :cu_disc_co, :varchar, size: 6
      column :cu_ship_na, :varchar, size: 35
      column :cu_vend_co, :varchar, size: 20
      column :cu_tax, :float
      column :cu_status, :varchar, size: 1
      column :cu_bcp_po, :varchar, size: 5
      column :cu_bcp_qty, :varchar, size: 5
      column :cu_bcp_par, :varchar, size: 5
      column :cu_bcp_ven, :varchar, size: 5
      column :cu_gl_num, :varchar, size: 12
      column :cu_st_id_1, :varchar, size: 10
      column :cu_st_id_2, :varchar, size: 10
      column :cu_stax_id, :varchar, size: 25
      column :cu_login, :varchar, size: 8
      column :cu_pw, :varchar, size: 8
      column :cu_broadca, :text
      column :cu_lview_s, :boolean
      column :cu_lview_2, :boolean
      column :cu_lcreate, :boolean
      column :cu_lview_i, :boolean
      column :cu_ship_cn, :integer
      column :cu_vso_cnt, :integer
      column :cu_cso_cnt, :integer
      column :cu_vinv_cn, :integer
      column :cu_ship_da, :date
      column :cu_vso_dat, :date
      column :cu_cso_dat, :date
      column :cu_vinv_da, :date
      column :cu_bcp_inv, :varchar, size: 5
      column :cu_bcp_doc, :varchar, size: 5
      column :cu_fob, :varchar, size: 15
      column :cu_consign, :integer
      column :cu_consig2, :varchar, size: 10
      column :cu_hold_il, :varchar, size: 10
      column :cu_bcp_ser, :varchar, size: 5
      column :cu_credit_, :float
      column :cu_credit2, :varchar, size: 40
      column :cu_credit3, :boolean
      column :cu_tax_exe, :boolean
      column :cu_exempt_, :varchar, size: 30
      column :cu_website, :varchar, size: 60
      column :cu_cur_cod, :varchar, size: 10
      column :cu_edi_thr, :integer
      column :cu_edi_id, :varchar, size: 20
      column :cu_label, :integer
      column :cu_spec_gr, :varchar, size: 20
      column :cu_ship_co, :boolean
      column :cu_packhol, :boolean
      column :cu_prod_co, :varchar, size: 2
      column :cu_cust_ex, :varchar, size: 5
      column :cu_bcp_uom, :varchar, size: 5
      column :cu_bcp_po_, :varchar, size: 5
      column :cu_exc_so_, :boolean
      column :cu_beg_bal, :date
      column :cu_beg_ba2, :decimal, precision: 15, scale: 4
      column :cu_so_pref, :varchar, size: 3
      column :cu_ship_wi, :integer
      column :cu_create_, :date
      column :cu_exp_dat, :date
      column :cu_emp_id2, :varchar, size: 5
      column :cu_salesta, :integer
      column :cu_lo_code, :varchar, size: 10
      column :cu_prospec, :boolean
      column :cu_mailcod, :varchar, size: 10
      column :cu_markup, :float
      column :cu_shipnot, :text
      column :cu_vet_sup, :varchar, size: 6
      column :cu_st_excl, :boolean
      column :cu_st_no_f, :boolean
      column :cu_st_fc_r, :float
      column :cu_st_mo_d, :integer
      column :cu_st_date, :date
      column :cu_st_amou, :decimal, precision: 15, scale: 4
      column :cu_prepay_, :integer
      column :cu_enforce, :boolean
      column :cu_arnote, :varchar, size: 10
      column :cu_split_s, :boolean
      column :cu_bill_na, :varchar, size: 35
      column :cu_bill_ad, :varchar, size: 35
      column :cu_bill_a2, :varchar, size: 35
      column :cu_bill_ci, :varchar, size: 30
      column :cu_bill_st, :varchar, size: 3
      column :cu_bill_zi, :varchar, size: 10
      column :cu_bill_cn, :varchar, size: 25
      column :cu_bill_ph, :varchar, size: 14
      column :cu_bill_ex, :varchar, size: 5
      column :cu_bill_fa, :varchar, size: 14
      column :cu_bill_co, :varchar, size: 25
      column :cu_inv_hdr, :varchar, size: 25
      column :cu_inv_hd2, :varchar, size: 25
      column :cu_inv_hd3, :varchar, size: 25
      column :cu_inv_hd4, :varchar, size: 25
      column :cu_inv_hd5, :varchar, size: 25
      column :cu_teritor, :integer
      column :cu_mail_a3, :varchar, size: 35
      column :cu_bill_a3, :varchar, size: 35
      column :cu_comm_pe, :float
      column :cu_prod_no, :text
      column :cu_email_i, :boolean
      column :cu_email_2, :varchar, size: 250
      column :cu_email_a, :boolean
      column :cu_email_3, :varchar, size: 250
      column :cu_reg_rat, :float
      column :cu_ot_rate, :float
      column :cu_dot_rat, :float
      column :cu_foblabe, :varchar, size: 3
      column :cu_sco_att, :varchar, size: 30
      column :cu_price_e, :varchar, size: 5
      column :cu_price_2, :date
      column :cu_price_s, :date
      column :cu_obsolet, :boolean
      column :cu_sepcofc, :boolean
      column :cu_distrib, :varchar, size: 10
      column :cu_gs_st, :boolean
      column :cu_no_over, :boolean
      column :cu_email_s, :boolean
      column :cu_email_4, :varchar, size: 250
      column :cu_no_prin, :boolean
      column :cu_print_i, :text
      column :cu_po_ln_o, :boolean
      column :cu_defcons, :boolean
      column :cu_late_al, :integer
      column :cu_collect, :text
      column :cu_ex_coll, :boolean
      column :cu_cn_leve, :integer
      column :cu_excel_i, :boolean
      column :cu_excel_2, :boolean
      column :cu_color, :varchar, size: 10
    end
  end
end
