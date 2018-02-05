Sequel.migration do
  change do
     create_table(:ac_crde) do
      column :dr_id, :varchar, :size => 10
      column :dr_mr_id, :varchar, :size => 10
      column :dr_inv_num, :varchar, :size => 7
      column :dr_referen, :varchar, :size => 10
      column :dr_dr_ca_c, :varchar, :size => 12
      column :dr_cr_ca_c, :varchar, :size => 12
      column :dr_amount, :float
      column :dr_dr_amou, :float
      column :dr_cr_amou, :float
      column :dr_type, :varchar, :size => 1
      column :dr_gl_id, :varchar, :size => 10
      column :dr_dr_gl_i, :varchar, :size => 10
      column :dr_cr_gl_i, :varchar, :size => 10
      column :dr_ca_code, :varchar, :size => 12
      column :dr_notes, :text
      column :dr_apply_d, :date
      column :dr_cur_amo, :float
      column :dr_cm_mr_i, :varchar, :size => 10
      column :dr_cm_new, :boolean
      column :dr_dm_mn_i, :varchar, :size => 10
    end
  end
end
