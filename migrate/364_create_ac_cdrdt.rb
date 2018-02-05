Sequel.migration do
  change do
     create_table(:ac_cdrdt) do
      column :dd_id, :varchar, :size => 10
      column :dd_mn_id, :varchar, :size => 10
      column :dd_type, :varchar, :size => 1
      column :dd_dr_amou, :decimal, :precision => 15, :scale => 4
      column :dd_cr_amou, :decimal, :precision => 15, :scale => 4
      column :dd_amount, :decimal, :precision => 15, :scale => 4
      column :dd_dr_ca_c, :varchar, :size => 12
      column :dd_cr_ca_c, :varchar, :size => 12
      column :dd_ca_code, :varchar, :size => 12
      column :dd_cur_amo, :decimal, :precision => 15, :scale => 4
      column :dd_discoun, :boolean
    end
  end
end
