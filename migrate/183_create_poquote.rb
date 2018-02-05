Sequel.migration do
  change do
     create_table(:poquote) do
      column :pq_seq, :integer
      column :pq_quote_n, :varchar, :size => 15
      column :pq_desc, :varchar, :size => 50
    end
  end
end
