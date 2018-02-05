Sequel.migration do
  change do
     create_table(:q_revnos) do
      column :qn_id, :varchar, :size => 10
      column :qn_qv_id, :varchar, :size => 10
      column :qn_quote_n, :varchar, :size => 15
    end
  end
end
