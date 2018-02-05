Sequel.migration do
  change do
     create_table(:shipping) do
      column :sh_ship_co, :varchar, :size => 8
      column :sh_ship_da, :date
      column :sh_cust_co, :varchar, :size => 6
      column :sh_sord_nu, :varchar, :size => 7
      column :sh_tot_box, :integer
      column :sh_tot_wei, :integer
      column :sh_tot_car, :integer
      column :sh_tot_qty, :integer
      column :sh_emp_id, :varchar, :size => 5
      column :sh_ship_vi, :varchar, :size => 40
      column :sh_inv_fla, :varchar, :size => 1
      column :sh_ship_no, :text
      column :sh_gt_skid, :integer
      column :sh_gt_cart, :integer
      column :sh_gt_boxe, :integer
      column :sh_gt_qty, :integer
      column :sh_gt_w, :float
      column :sh_gt_tare, :float
      column :sh_gt_gtw, :float
      column :sh_inv_num, :varchar, :size => 7
      column :sh_comp_na, :varchar, :size => 35
      column :sh_address, :varchar, :size => 35
      column :sh_addres2, :varchar, :size => 35
      column :sh_addres3, :varchar, :size => 35
      column :sh_track_n, :varchar, :size => 40
      column :sh_bol_num, :varchar, :size => 10
      column :sh_prepaid, :boolean
      column :sh_lo_code, :varchar, :size => 10
      column :sh_positio, :varchar, :size => 12
      column :sh_ship_ch, :float
      column :sh_consign, :boolean
      column :sh_consig2, :integer
      column :sh_consig3, :date
      column :sh_consig4, :boolean
      column :sh_consig5, :varchar, :size => 10
      column :sh_ship_ty, :varchar, :size => 1
      column :sh_dest_zi, :varchar, :size => 10
      column :sh_ship_me, :varchar, :size => 20
      column :sh_misc_de, :varchar, :size => 30
      column :sh_misc_am, :float
      column :sh_residen, :boolean
      column :sh_hundred, :boolean
      column :sh_user_id, :varchar, :size => 5
      column :sh_last_mo, DateTime
      column :sh_prepay_, :integer
      column :sh_plist_p, :boolean
      column :sh_prem_fr, :float
      column :sh_premf_n, :text
      column :sh_markup, :integer
      column :sh_fr_pric, :float
      column :sh_addres4, :varchar, :size => 35
      column :sh_ca_id, :varchar, :size => 10
      column :sh_edi_pur, :varchar, :size => 2
      column :sh_edi_gw, :float
      column :sh_edi_gw_, :varchar, :size => 2
      column :sh_edi_nw, :float
      column :sh_edi_nw_, :varchar, :size => 2
      column :sh_edi_pkg, :varchar, :size => 5
      column :sh_edi_lad, :integer
      column :sh_edi_sca, :varchar, :size => 17
      column :sh_edi_mod, :varchar, :size => 2
      column :sh_edi_loc, :varchar, :size => 2
      column :sh_edi_lo2, :varchar, :size => 5
      column :sh_edi_shi, :date
      column :sh_edi_sh2, :varchar, :size => 5
      column :sh_edi_asn, :integer
      column :sh_edi_as2, :date
      column :sh_edi_as3, :varchar, :size => 5
      column :sh_edi_eq_, :varchar, :size => 2
      column :sh_edi_eq2, :varchar, :size => 4
      column :sh_edi_eq3, :varchar, :size => 10
      column :sh_edi_rq_, :varchar, :size => 2
      column :sh_edi_rq2, :varchar, :size => 2
      column :sh_edi_rq3, :varchar, :size => 2
      column :sh_edi_rq4, :varchar, :size => 2
      column :sh_edi_ref, :varchar, :size => 30
      column :sh_edi_re2, :varchar, :size => 30
      column :sh_edi_re3, :varchar, :size => 30
      column :sh_edi_re4, :varchar, :size => 30
      column :sh_edi_ic_, :boolean
      column :sh_edi_ic2, :varchar, :size => 5
      column :sh_edi_ic3, :varchar, :size => 2
      column :sh_edi_fob, :varchar, :size => 2
      column :sh_edi_fo2, :varchar, :size => 6
      column :sh_edi_fo3, :varchar, :size => 2
      column :sh_line, :varchar, :size => 7
      column :sh_auth, :varchar, :size => 5
      column :sh_inv_nu2, :varchar, :size => 7
      column :sh_nc_id, :varchar, :size => 10
      column :sh_class, :varchar, :size => 10
      column :sh_qty_not, :text
      column :sh_bol_not, :text
      column :sh_cod_amo, :float
      column :sh_hot, :boolean
      column :sh_asn_gen, :boolean
      column :sh_void, :boolean
      column :sh_collect, :varchar, :size => 30
      column :sh_credith, :boolean
      column :sh_approve, :boolean
      column :alt_comp_n, :varchar, :size => 35
      column :alt_addres, :varchar, :size => 35
      column :alt_addre2, :varchar, :size => 35
      column :alt_addre3, :varchar, :size => 35
      column :alt_addre4, :varchar, :size => 35
      column :third_comp, :varchar, :size => 35
      column :third_addr, :varchar, :size => 35
      column :third_add2, :varchar, :size => 35
      column :third_add3, :varchar, :size => 35
      column :third_add4, :varchar, :size => 35
      column :sh_transfe, :varchar, :size => 10
      column :sh_suffixs, :integer
      column :sh_import_, :date
      column :sh_bol_exp, :date
    end
  end
end
