Sequel.migration do
  change do
     create_table(:q_rsns) do
      column :qr_code, :varchar, :size => 6
      column :qr_desc, :varchar, :size => 25
    end
  end
end
