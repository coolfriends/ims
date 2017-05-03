Sequel.migration do
  change do
     create_table(:edi_locq) do
      column :lq_code, :varchar, :size => 2
      column :lq_desc, :varchar, :size => 30
    end
  end
end
