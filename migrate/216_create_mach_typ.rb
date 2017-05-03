Sequel.migration do
  change do
     create_table(:mach_typ) do
      column :mt_mach_co, :varchar, :size => 5
      column :mt_mach_de, :varchar, :size => 20
      column :mt_caltype, :varchar, :size => 1
      column :mt_cut_off, :float
      column :mt_rate, :float
      column :mt_setup_r, :float
      column :mt_max_spe, :float
      column :mt_max_fee, :float
      column :mt_notes, :text
      column :mt_cycle, :varchar, :size => 1
      column :mt_def_hrs, :float
      column :mt_locatio, :varchar, :size => 10
      column :mt_mach_gr, :varchar, :size => 10
      column :mt_sched, :boolean
      column :mt_burd_ra, :float
      column :mt_pop, :integer
      column :mt_de_id, :varchar, :size => 2
      column :mt_sell_ra, :float
      column :mt_cb_rate, :float
      column :mt_usenote, :boolean
      column :mt_infinit, :boolean
      column :mt_positio, :integer
      column :mt_nowork, :boolean
      column :mt_il_id, :varchar, :size => 10
      column :mt_queue, :float
      column :mt_ib_id, :varchar, :size => 10
      column :mt_is_sub, :boolean
      column :mt_supp_co, :varchar, :size => 6
      column :mt_dist_co, :varchar, :size => 2
      column :mt_workcel, :boolean
      column :mt_useburd, :boolean
      column :mt_il_id_w, :varchar, :size => 10
      column :mt_seconda, :boolean
      column :mt_unatten, :float
      column :mt_line, :integer
      column :mt_spindle, :integer
      column :mt_fixed_a, :varchar, :size => 40
      column :mt_minchar, :float
      column :mt_feature, :varchar, :size => 20
      column :mt_inactiv, :boolean
      column :mt_id_code, :varchar, :size => 10
      column :mt_packagi, :boolean
      column :mt_prod_co, :varchar, :size => 2
      column :mt_sortby, :integer
      column :mt_barend_, :float
      column :mt_bufferh, :float
      column :mt_partcou, :integer
      column :mt_hoursco, :float
      column :mt_virtual, :integer
      column :mt_emp_id, :varchar, :size => 5
      column :mt_useinjc, :boolean
      column :mt_setup_q, :integer
      column :mt_maneng_, :varchar, :size => 5
      column :mt_assigne, :varchar, :size => 5
      column :mt_type, :integer
      column :mt_assign2, :varchar, :size => 5
      column :mt_assign3, :varchar, :size => 5
    end
  end
end
