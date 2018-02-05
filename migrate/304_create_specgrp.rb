Sequel.migration do
  change do
     create_table(:specgrp) do
      column :sg_id, :varchar, :size => 10
      column :sg_spec_gr, :varchar, :size => 20
    end
  end
end
