Sequel.migration do
  change do
     create_table(:ac_cdrec) do
      column :mn_id, :varchar, :size => 10
      column :mn_type, :varchar, :size => 1
      column :mn_entry_t, :varchar, :size => 1
      column :mn_frequen, :varchar, :size => 1
      column :mn_day, :integer
      column :mn_next_da, :date
      column :mn_last_da, :date
      column :mn_ca_code, :varchar, :size => 12
      column :mn_supp_co, :varchar, :size => 6
      column :mn_supp_na, :varchar, :size => 30
      column :mn_rem_add, :text
      column :mn_dr_amou, :decimal, :precision => 15, :scale => 4
      column :mn_cr_amou, :decimal, :precision => 15, :scale => 4
      column :mn_amount, :decimal, :precision => 15, :scale => 4
      column :mn_referen, :varchar, :size => 30
      column :mn_cur_cod, :varchar, :size => 10
      column :mn_ca_cur_, :varchar, :size => 12
      column :mn_manual, :boolean
      column :mn_1099, :boolean
      column :mn_1099_box, :varchar, :size => 2
      column :mn_check_m, :varchar, :size => 30
      column :mn_cur_amo, :decimal, :precision => 15, :scale => 4
      column :mn_dom, :integer
    end
  end
end
