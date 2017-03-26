Sequel.migration do
  change do
     create_table(:altroute) do
      column :ar_invent_, :varchar, :size => 30
      column :ar_start_q, :integer
      column :ar_end_qty, :integer
      column :ar_quote_n, :varchar, :size => 15
      column :ar_desc, :varchar, :size => 20
    end
  end
end
