Sequel.migration do
  change do
     create_table(:contanpo) do
      column :cp_id, :varchar, :size => 10
      column :cp_po_num, :varchar, :size => 7
      column :cp_line_nu, :integer
      column :cp_ct_id, :varchar, :size => 10
    end
  end
end
