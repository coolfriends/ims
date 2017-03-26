Sequel.migration do
  change do
     create_table(:ac_adiv) do
      column :dv_code, :varchar, :size => 2
      column :dv_desc, :varchar, :size => 40
      column :dv_acct_su, :varchar, :size => 10
    end
  end
end
