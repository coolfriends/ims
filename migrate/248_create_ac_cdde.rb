Sequel.migration do
  change do
     create_table(:ac_cdde) do
      column :dd_id, :varchar, :size => 10
      column :dd_mn_id, :varchar, :size => 10
      column :dd_ap_id, :varchar, :size => 10
      column :dd_ap_inv_, :varchar, :size => 30
      column :dd_dr_ca_c, :varchar, :size => 12
      column :dd_dr_amou, :decimal, :precision => 15, :scale => 4
      column :dd_cr_ca_c, :varchar, :size => 12
      column :dd_cr_amou, :decimal, :precision => 15, :scale => 4
      column :dd_amount, :decimal, :precision => 15, :scale => 4
      column :dd_dr_gl_i, :varchar, :size => 10
      column :dd_cr_gl_i, :varchar, :size => 10
      column :dd_type, :varchar, :size => 1
      column :dd_ca_code, :varchar, :size => 12
      column :dd_gl_id, :varchar, :size => 10
      column :dd_apply_d, :date
      column :dd_cur_amo, :decimal, :precision => 15, :scale => 4
      column :dd_status, :varchar, :size => 1
      column :dd_marked, :boolean
      column :dd_dm_mn_i, :varchar, :size => 10
      column :dd_cm_mr_i, :varchar, :size => 10
      column :dd_sc_id, :varchar, :size => 10
    end
  end
end
