Sequel.migration do
  change do
     create_table(:ac_faloc) do
      column :fl_id, :varchar, :size => 10
      column :fl_code, :varchar, :size => 10
      column :fl_desc, :varchar, :size => 40
      column :fl_notes, :text
    end
  end
end
