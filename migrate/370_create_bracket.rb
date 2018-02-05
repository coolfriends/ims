Sequel.migration do
  change do
     create_table(:bracket) do
      column :br_id, :varchar, :size => 10
      column :br_high_cn, :float
      column :br_unit_ty, :varchar, :size => 4
      column :br_desc, :varchar, :size => 25
      column :br_low_cnt, :float
    end
  end
end
