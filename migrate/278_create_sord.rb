Sequel.migration do
  change do
     create_table(:sord) do
      column :so_sord_nu, :varchar, :size => 7
      column :so_inv_num, :varchar, :size => 7
      column :so_inv_dat, :date
      column :so_cust_co, :varchar, :size => 6
      column :so_batch, :varchar, :size => 1
      column :so_print_d, :date
      column :so_ship_vi, :varchar, :size => 40
      column :so_net_amt, :float
      column :so_taxes, :float
      column :so_tot_amt, :float
      column :so_post, :varchar, :size => 1
      column :so_post_da, :date
      column :so_comp_na, :varchar, :size => 33
      column :so_address, :varchar, :size => 33
      column :so_addres2, :varchar, :size => 33
      column :so_addres3, :varchar, :size => 33
      column :so_ship_da, :date
      column :so_po_num, :varchar, :size => 25
      column :so_inv_sta, :varchar, :size => 1
      column :so_contact, :varchar, :size => 25
      column :so_emp_id, :varchar, :size => 5
      column :so_pay_ter, :varchar, :size => 20
      column :so_lo_code, :varchar, :size => 10
      column :so_prepaid, :boolean
      column :so_discoun, :float
      column :so_isquote, :boolean
      column :so_rec_dat, :date
      column :so_consign, :boolean
      column :so_entered, :varchar, :size => 5
      column :so_note, :text
      column :so_ship_co, :boolean
      column :so_consig2, :boolean
      column :so_consig3, :integer
      column :so_consig4, :varchar, :size => 10
      column :so_ship_to, :varchar, :size => 3
      column :so_ship_ty, :varchar, :size => 1
      column :so_progres, :boolean
      column :so_user_id, :varchar, :size => 5
      column :so_last_mo, DateTime
      column :so_st_id_1, :varchar, :size => 10
      column :so_st_id_2, :varchar, :size => 10
      column :so_stax_id, :varchar, :size => 25
      column :so_tax_exe, :boolean
      column :so_exempt_, :varchar, :size => 30
      column :so_cur_cod, :varchar, :size => 10
      column :so_cur_rat, :float
      column :so_net_cur, :float
      column :so_tax_cur, :float
      column :so_tot_cur, :float
      column :so_disc_cu, :float
      column :so_prepay_, :integer
      column :so_abbr_na, :varchar, :size => 15
      column :so_addres4, :varchar, :size => 33
      column :so_rev_ste, :integer
      column :so_type, :integer
      column :so_ca_id, :varchar, :size => 10
      column :so_surchar, :float
      column :so_surch_c, :float
      column :so_grs_amt, :float
      column :so_grs_cur, :float
      column :so_rec_sor, :boolean
      column :so_standin, :varchar, :size => 7
      column :so_rev, :integer
      column :so_phone, :varchar, :size => 14
      column :so_fax, :varchar, :size => 14
      column :so_backlog, :boolean
      column :so_expire_, :date
      column :so_enforce, :boolean
      column :so_use_sur, :boolean
      column :so_fob, :varchar, :size => 15
      column :so_billto_, :varchar, :size => 10
      column :so_sumbill, :boolean
      column :so_ch_over, :boolean
      column :so_foblabe, :varchar, :size => 3
      column :so_closed_, :date
      column :so_exc_jhr, :boolean
      column :so_approve, :boolean
      column :so_edi_co_, :varchar, :size => 25
      column :so_edi_855, :date
      column :so_collect, :varchar, :size => 30
      column :so_forecas, :boolean
      column :so_apprv_b, :varchar, :size => 5
      column :so_apprv_s, :varchar, :size => 1
      column :so_appr_da, :date
      column :so_appr_me, :text
      column :so_asnemai, :text
    end
  end
end
