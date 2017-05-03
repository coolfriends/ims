Sequel.migration do
  change do
     create_table(:edi_mode) do
      column :em_code, :varchar, :size => 2
      column :em_desc, :varchar, :size => 30
    end
  end
end
