Sequel.migration do
  change do
     create_table(:ac_fadef) do
      column :ff_main, :date
      column :ff_check, :varchar, :size => 20
      column :ff_ca_cc_c, :varchar, :size => 12
      column :ff_ca_pl_c, :varchar, :size => 12
    end
  end
end
