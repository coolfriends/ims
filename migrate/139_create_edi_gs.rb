Sequel.migration do
  change do
     create_table(:edi_gs) do
      column :eg_cust_co, :varchar, :size => 6
      column :eg_qs_id, :varchar, :size => 10
      column :eg_resp_ag, :varchar, :size => 2
      column :eg_version, :varchar, :size => 12
      column :eg_fgid_cu, :varchar, :size => 12
      column :eg_fgid_co, :varchar, :size => 12
      column :eg_grp_ctr, :integer
      column :eg_grp_ct2, :integer
      column :eg_ca_id, :varchar, :size => 10
    end
  end
end
