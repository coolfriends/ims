Sequel.migration do
  change do
     create_table(:qb_coa) do
      column :qa_code, :varchar, :size => 7
      column :qa_acct_na, :varchar, :size => 31
      column :qa_acct_ty, :varchar, :size => 24
    end
  end
end
