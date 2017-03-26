Sequel.migration do
  change do
     create_table(:invoice) do
      column :in_inv_num, :varchar, :size => 7
      column :in_inv_typ, :varchar, :size => 1
      column :in_inv_dat, :date
      column :in_cust_co, :varchar, :size => 6
      column :in_batch, :varchar, :size => 1
      column :in_print_d, :date
      column :in_ship_vi, :varchar, :size => 40
      column :in_net_amt, :float
      column :in_taxes, :float
      column :in_tot_amt, :float
      column :in_exp_dat, :date
      column :in_post, :boolean
      column :in_post_da, :date
      column :in_comp_na, :varchar, :size => 33
      column :in_address, :varchar, :size => 33
      column :in_addres2, :varchar, :size => 33
      column :in_addres3, :varchar, :size => 33
      column :in_ship_co, :varchar, :size => 8
      column :in_ship_da, :date
      column :in_po_num, :varchar, :size => 25
      column :in_inv_sta, :varchar, :size => 1
      column :in_contact, :varchar, :size => 25
      column :in_sord_nu, :varchar, :size => 7
      column :in_emp_id, :varchar, :size => 5
      column :in_pay_ter, :varchar, :size => 20
      column :in_due_dat, :date
      column :in_disc_da, :date
      column :in_lo_code, :varchar, :size => 10
      column :in_type, :varchar, :size => 1
      column :in_inv_bal, :decimal, :precision => 15, :scale => 4
      column :in_ch_num, :varchar, :size => 10
      column :in_ch_date, :date
      column :in_cash_ap, :decimal, :precision => 15, :scale => 4
      column :in_stmt, :boolean
      column :in_gl_num, :varchar, :size => 12
      column :in_gl_id, :varchar, :size => 10
      column :in_startmo, :boolean
      column :in_entry_d, :date
      column :in_ship_to, :varchar, :size => 3
      column :in_st_id_1, :varchar, :size => 10
      column :in_st_id_2, :varchar, :size => 10
      column :in_stax_id, :varchar, :size => 25
      column :in_tax_exe, :boolean
      column :in_exempt_, :varchar, :size => 30
      column :in_cur_cod, :varchar, :size => 10
      column :in_cur_rat, :float
      column :in_net_cur, :float
      column :in_tax_cur, :float
      column :in_tot_cur, :float
      column :in_addres4, :varchar, :size => 33
      column :in_ca_id, :varchar, :size => 10
      column :in_discoun, :float
      column :in_disc_cu, :float
      column :in_surchar, :float
      column :in_surch_c, :float
      column :in_grs_amt, :float
      column :in_grs_cur, :float
      column :in_note, :text
      column :in_use_sur, :boolean
      column :in_split_s, :boolean
      column :in_only_su, :boolean
      column :in_fob, :varchar, :size => 15
      column :in_billto_, :varchar, :size => 10
      column :in_foblabe, :varchar, :size => 3
      column :in_edi_810, :date
      column :in_edi_812, :varchar, :size => 5
      column :in_deldate, :date
      column :in_destina, :varchar, :size => 4
      column :in_noncoll, :boolean
      column :in_nc_inv_, :varchar, :size => 7
      column :in_nc_date, :date
      column :in_nc_mast, :boolean
      column :in_lm_user, :varchar, :size => 5
      column :in_lm_date, :datetime
      column :in_ex_coll, :boolean
    end
  end
end
