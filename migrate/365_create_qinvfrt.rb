Sequel.migration do
  change do
     create_table(:qinvfrt) do
      column :qf_id, :varchar, :size => 10
      column :qf_ucc_exc, :float
      column :qf_ucc_dol, :float
      column :qf_ucc_frt, :varchar, :size => 20
      column :qf_ucc_fr2, :float
      column :qf_ucc_fr3, :float
      column :qf_ucc_fr4, :float
      column :qf_ucc_add, :float
      column :qf_ucc_eur, :float
      column :qf_ucc_ad2, :float
      column :qf_ucc_ad3, :float
      column :qf_ucc_ad4, :float
      column :qf_ucc_ad5, :float
      column :qf_ucc_ad6, :float
      column :qf_ucc_tot, :float
      column :qf_ucc_cos, :float
      column :qf_quote_n, :varchar, :size => 15
      column :qf_item, :integer
      column :qf_order_n, :varchar, :size => 12
    end
  end
end
