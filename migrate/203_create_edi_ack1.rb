Sequel.migration do
  change do
     create_table(:edi_ack1) do
      column :ek_code, :varchar, :size => 2
      column :ek_desc, :varchar, :size => 45
    end
  end
end
