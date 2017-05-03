Sequel.migration do
  change do
     create_table(:ppprmg) do
      column :pp_minimum, :float
      column :pp_maximum, :float
      column :pp_xx_tol, :float
      column :pp_x_tol, :float
      column :pp_y_tol, :float
      column :pp_z_tol, :float
      column :pp_zz_tol, :float
    end
  end
end
