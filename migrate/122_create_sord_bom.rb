Sequel.migration do
  change do
     create_table(:sord_bom) do
      column :sb_sord_nu, :varchar, :size => 7
      column :sb_line_nu, :integer
      column :parent, :varchar, :size => 30
      column :part_num, :varchar, :size => 30
      column :sb_quote_n, :varchar, :size => 15
      column :sb_order_n, :varchar, :size => 12
      column :sb_pr_id, :integer
      column :count, :float
      column :nocost, :boolean
    end
  end
end
