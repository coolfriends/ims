Sequel.migration do
  change do
     create_table(:py_taxes) do
      column :tx_id, :varchar, :size => 10
      column :tx_code, :varchar, :size => 10
      column :tx_type, :varchar, :size => 1
      column :tx_desc, :varchar, :size => 35
      column :tx_name, :varchar, :size => 35
      column :tx_address, :varchar, :size => 35
      column :tx_addres2, :varchar, :size => 35
      column :tx_addres3, :varchar, :size => 35
      column :tx_id_no, :varchar, :size => 15
      column :tx_exemp_a, :float
      column :tx_tax_typ, :varchar, :size => 1
      column :tx_e_rate, :float
      column :tx_calc_ty, :varchar, :size => 1
      column :tx_level, :varchar, :size => 1
      column :tx_e_max_t, :float
      column :tx_max_fre, :varchar, :size => 1
      column :tx_state, :varchar, :size => 2
      column :tx_gl_paya, :varchar, :size => 12
      column :tx_gl_expe, :varchar, :size => 12
      column :tx_r_rate, :float
      column :tx_cont_ty, :varchar, :size => 1
      column :tx_r_max_t, :float
      column :tx_beg_dat, :date
      column :tx_beg_bal, :float
      column :tx_round_d, :boolean
      column :tx_perc_em, :boolean
      column :tx_use_exe, :boolean
      column :tx_lc_id, :varchar, :size => 10
      column :tx_r_rate_, :float
      column :tx_use_min, :boolean
    end
  end
end
