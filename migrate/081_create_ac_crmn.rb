# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_crmn) do
      column :mr_id, :varchar, size: 10
      column :mr_type, :varchar, size: 1
      column :mr_ca_code, :varchar, size: 12
      column :mr_date, :date
      column :mr_referen, :varchar, size: 30
      column :mr_cust_co, :varchar, size: 6
      column :mr_cust_na, :varchar, size: 30
      column :mr_rem_add, :text
      column :mr_amount, :float
      column :mr_dr_amou, :float
      column :mr_cr_amou, :float
      column :mr_user, :varchar, size: 5
      column :mr_entry_d, :date
      column :mr_reconci, :varchar, size: 1
      column :mr_post, :boolean
      column :mr_post_da, :date
      column :mr_entry_t, :varchar, size: 1
      column :mr_gl_id, :varchar, size: 10
      column :mr_dep_id, :varchar, size: 10
      column :mr_status, :varchar, size: 1
      column :mr_ca_cod2, :varchar, size: 12
      column :mr_gl_id_2, :varchar, size: 10
      column :mr_oc_amou, :float
      column :mr_oc_bala, :float
      column :mr_mr_id, :varchar, size: 10
      column :mr_status_, :varchar, size: 1
      column :mr_reconc2, :varchar, size: 1
      column :mr_marked, :boolean
      column :mr_marked_, :boolean
      column :mr_ship_to, :varchar, size: 3
      column :mr_emp_id, :varchar, size: 5
      column :mr_lo_code, :varchar, size: 10
      column :mr_number, :varchar, size: 7
      column :mr_new_for, :boolean
      column :mr_st_id_1, :varchar, size: 10
      column :mr_st_id_2, :varchar, size: 10
      column :mr_stax_id, :varchar, size: 25
      column :mr_tax_exe, :boolean
      column :mr_exempt_, :varchar, size: 30
      column :mr_cur_cod, :varchar, size: 10
      column :mr_cur_rat, :float
      column :mr_cur, :float
      column :mr_dr_cur, :float
      column :mr_cr_cur, :float
      column :mr_inv_num, :varchar, size: 7
      column :mr_ship_co, :varchar, size: 8
      column :mr_cur_amo, :float
      column :mr_ca_cur_, :varchar, size: 12
      column :mr_gl_id_c, :varchar, size: 10
      column :mr_sord_nu, :varchar, size: 7
      column :mr_cm_dr_i, :varchar, size: 10
      column :mr_billto_, :varchar, size: 10
      column :mr_supp_co, :varchar, size: 6
      column :mr_rec_dat, :date
      column :mr_rec_da2, :date
      column :mr_credit_, :boolean
      column :mr_destina, :varchar, size: 4
      column :mr_zero_ba, :boolean
      column :mr_lm_user, :varchar, size: 5
      column :mr_lm_date, DateTime
    end
  end
end
