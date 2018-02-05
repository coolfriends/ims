Sequel.migration do
  change do
     create_table(:certaval) do
      column :ca_id, :varchar, :size => 10
      column :ca_ch_id, :varchar, :size => 10
      column :ca_cert_ch, :varchar, :size => 10
      column :ca_ship_co, :varchar, :size => 8
      column :ca_shipped, :boolean
    end
  end
end
