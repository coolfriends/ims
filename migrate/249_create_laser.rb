Sequel.migration do
  change do
     create_table(:laser) do
      column :lz_id, :varchar, :size => 10
      column :lz_mat_cod, :varchar, :size => 3
      column :lz_mat_thk, :float
      column :lz_lg_cont, :float
      column :lz_md_cont, :float
      column :lz_sm_cont, :float
      column :lz_pierce, :float
    end
  end
end
