Sequel.migration do
  change do
     create_table(:ac_adept) do
      column :dp_code, :varchar, :size => 2
      column :dp_desc, :varchar, :size => 40
      column :dp_acct_su, :varchar, :size => 10
    end
  end
end
