Sequel.migration do
  change do
     create_table(:defmat) do
      column :dm_id, :varchar, :size => 10
      column :dm_supp_co, :varchar, :size => 6
      column :dm_mat_typ, :varchar, :size => 6
      column :dm_shape_c, :varchar, :size => 7
      column :dm_uom, :varchar, :size => 2
      column :dm_cht_siz, :float
      column :dm_wide, :float
    end
  end
end
