Sequel.migration do
  change do
     create_table(:weight) do
      column :wt_mat_cod, :varchar, :size => 3
      column :wt_desc, :varchar, :size => 20
      column :wt_weight, :float
      column :wt_bol_lin, :varchar, :size => 30
      column :wt_bol_li2, :varchar, :size => 30
      column :wt_scrap, :float
      column :wt_rgb, :integer
      column :wt_ca_code, :varchar, :size => 12
      column :wt_nburden, :float
      column :wt_o2_burde, :float
    end
  end
end
