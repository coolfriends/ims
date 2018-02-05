Sequel.migration do
  change do
     create_table(:q_custa) do
      column :ca_cust_co, :varchar, :size => 6
      column :ca_ship_ad, :varchar, :size => 35
      column :ca_ship_a2, :varchar, :size => 35
      column :ca_ship_ci, :varchar, :size => 30
      column :ca_ship_st, :varchar, :size => 3
      column :ca_ship_cn, :varchar, :size => 25
      column :ca_ship_zi, :varchar, :size => 10
      column :ca_ship_na, :varchar, :size => 35
      column :ca_default, :boolean
      column :ca_emp_id, :varchar, :size => 5
      column :ca_st_id_1, :varchar, :size => 10
      column :ca_st_id_2, :varchar, :size => 10
      column :ca_stax_id, :varchar, :size => 25
      column :ca_tax_exe, :boolean
      column :ca_exempt_, :varchar, :size => 30
      column :ca_type, :varchar, :size => 10
      column :ca_cur_cod, :varchar, :size => 10
      column :ca_abbr_na, :varchar, :size => 15
      column :ca_bol, :boolean
      column :ca_ship_a3, :varchar, :size => 35
      column :ca_id, :varchar, :size => 10
      column :ca_transit, :integer
      column :ca_multi_p, :boolean
      column :ca_max_pal, :integer
      column :ca_edi_loc, :varchar, :size => 2
      column :ca_edi_lo2, :varchar, :size => 5
      column :ca_box_cnt, :integer
      column :ca_master_, :integer
      column :ca_edi_ic_, :boolean
      column :ca_edi_ic2, :varchar, :size => 2
      column :ca_edi_ic3, :varchar, :size => 5
      column :ca_contact, :varchar, :size => 25
      column :ca_max_con, :integer
      column :ca_emp_id2, :varchar, :size => 5
      column :ca_proposa, :boolean
      column :ca_full_bo, :boolean
      column :ca_req_ps_, :boolean
      column :ca_2_d_barc, :boolean
      column :ca_notes, :text
      column :ca_dock_co, :varchar, :size => 5
      column :ca_comm_pe, :float
      column :ca_comm_p2, :float
      column :ca_fob, :varchar, :size => 15
      column :ca_billto, :boolean
      column :ca_phone, :varchar, :size => 30
      column :ca_store, :varchar, :size => 20
      column :ca_fax, :varchar, :size => 30
      column :ca_foblabe, :varchar, :size => 3
      column :ca_disc_co, :varchar, :size => 6
      column :ca_dealer_, :varchar, :size => 20
    end
  end
end
