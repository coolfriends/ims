Sequel.migration do
  change do
     create_table(:req_dept) do
      column :rd_id, :varchar, :size => 10
      column :rd_doc_typ, :varchar, :size => 10
      column :rd_de_id, :varchar, :size => 10
    end
  end
end
