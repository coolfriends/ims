Sequel.migration do
  change do
     create_table(:ac_gjrnl) do
      column :gj_id, :varchar, :size => 10
      column :gj_date, :date
      column :gj_type, :integer
      column :gj_desc, :varchar, :size => 35
      column :gj_amount, :decimal, :precision => 15, :scale => 4
      column :gj_post, :boolean
      column :gj_ptdate, :date
      column :gj_rev_gj_, :varchar, :size => 10
      column :gj_rev_dat, :date
      column :gj_out_of_, :boolean
      column :gj_user_id, :varchar, :size => 5
      column :gj_last_mo, DateTime
    end
  end
end
