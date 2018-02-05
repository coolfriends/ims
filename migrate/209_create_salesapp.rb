Sequel.migration do
  change do
     create_table(:salesapp) do
      column :sa_id, :varchar, :size => 10
      column :sa_inv_num, :varchar, :size => 7
      column :sa_line_nu, :integer
      column :sa_de_id, :varchar, :size => 2
      column :sa_percent, :float
      column :sa_amount, :float
      column :sa_ca_code, :varchar, :size => 12
      column :sa_gl_id, :varchar, :size => 10
      column :sa_mr_id, :varchar, :size => 10
      column :sa_prod_co, :varchar, :size => 2
    end
  end
end
