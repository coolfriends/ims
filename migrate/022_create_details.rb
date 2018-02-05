Sequel.migration do
  change do
     create_table(:details) do
      column :de_id, :varchar, :size => 10
      column :de_quote_n, :varchar, :size => 15
      column :de_order_n, :varchar, :size => 12
      column :de_seq_num, :integer
      column :de_desc, :varchar, :size => 60
      column :de_pr_id, :integer
      column :de_op_num, :integer
      column :de_hours, :float
      column :de_default, :boolean
    end
  end
end
