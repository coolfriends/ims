Sequel.migration do
  change do
     create_table(:edi_loci) do
      column :li_code, :varchar, :size => 5
      column :li_desc, :varchar, :size => 30
    end
  end
end
