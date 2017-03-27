# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_apinv) do
      column :ap_id, :varchar, size: 10
      column :ap_ca_code, :varchar, size: 12
      column :ap_inv_num, :varchar, size: 30
      column :ap_inv_dat, :date
      column :ap_supp_co, :varchar, size: 6
      column :ap_type, :varchar, size: 1
      column :ap_desc, :varchar, size: 30
      column :ap_longdes, :text
      column :ap_status, :varchar, size: 1
      column :ap_terms, :varchar, size: 20
      column :ap_pay_dat, :date
      column :ap_dc_date, :date
      column :ap_inv_amt, :decimal, precision: 15, scale: 4
      column :ap_inv_bal, :decimal, precision: 15, scale: 4
      column :ap_ch_num, :varchar, size: 10
      column :ap_ch_date, :date
      column :ap_cash_ap, :decimal, precision: 15, scale: 4
      column :ap_lo_code, :varchar, size: 10
      column :ap_user, :varchar, size: 5
      column :ap_entry_d, :date
      column :ap_post, :boolean
      column :ap_post_da, :date
      column :ap_print_d, :date
      column :ap_exp_dat, :date
      column :ap_gl_id, :varchar, size: 10
      column :ap_startmo, :boolean
      column :ap_reconci, :boolean
      column :ap_marked, :boolean
      column :ap_st_id_1, :varchar, size: 10
      column :ap_st_id_2, :varchar, size: 10
      column :ap_stax_id, :varchar, size: 25
      column :ap_tax_exe, :boolean
      column :ap_exempt_, :varchar, size: 30
      column :ap_net_amt, :decimal, precision: 15, scale: 4
      column :ap_taxes, :decimal, precision: 15, scale: 4
      column :ap_cur_cod, :varchar, size: 10
      column :ap_cur_rat, :float
      column :ap_net_cur, :decimal, precision: 15, scale: 4
      column :ap_tax_cur, :decimal, precision: 15, scale: 4
      column :ap_inv_cur, :decimal, precision: 15, scale: 4
      column :ap_po_num, :varchar, size: 7
      column :ap_exclude, :boolean
      column :ap_deliver, :date
      column :ap_user_id, :varchar, size: 5
      column :ap_lm_user, :varchar, size: 5
      column :ap_lm_date, DateTime
      column :ap_cc_deta, :boolean
    end
  end
end
