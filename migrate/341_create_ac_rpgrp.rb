Sequel.migration do
  change do
     create_table(:ac_rpgrp) do
      column :rg_code, :varchar, :size => 10
      column :rg_desc, :varchar, :size => 40
    end
  end
end
