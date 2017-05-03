Sequel.migration do
  change do
     create_table(:ac_fasts) do
      column :fa_id, :varchar, :size => 10
      column :fa_code, :varchar, :size => 10
      column :fa_desc, :varchar, :size => 40
      column :fa_fc_id, :varchar, :size => 10
      column :fa_fm_id, :varchar, :size => 10
      column :fa_supp_co, :varchar, :size => 6
      column :fa_ca_code, :varchar, :size => 12
      column :fa_ad_ca_c, :varchar, :size => 12
      column :fa_notes, :text
      column :fa_de_ca_c, :varchar, :size => 12
      column :fa_depr_fr, :varchar, :size => 1
      column :fa_complet, :boolean
      column :fa_status, :varchar, :size => 1
      column :fa_fl_id, :varchar, :size => 10
    end
  end
end
