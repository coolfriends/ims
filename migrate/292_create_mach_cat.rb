Sequel.migration do
  change do
     create_table(:mach_cat) do
      column :mc_mach_ca, :varchar, :size => 5
      column :mc_cat_des, :varchar, :size => 20
      column :mc_udf_nde, :varchar, :size => 20
      column :mc_udf_nd2, :varchar, :size => 20
      column :mc_udf_nd3, :varchar, :size => 20
      column :mc_udf_nd4, :varchar, :size => 20
      column :mc_udf_cde, :varchar, :size => 20
      column :mc_udf_cd2, :varchar, :size => 20
      column :mc_udf_dde, :varchar, :size => 20
    end
  end
end
