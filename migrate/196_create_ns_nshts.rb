Sequel.migration do
  change do
     create_table(:ns_nshts) do
      column :ns_code, :varchar, :size => 5
      column :ns_desc, :varchar, :size => 30
      column :ns_hyperli, :varchar, :size => 100
    end
  end
end
