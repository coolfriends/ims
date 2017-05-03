Sequel.migration do
  change do
     create_table(:supp_acc) do
      column :sc_supp_co, :varchar, :size => 6
      column :sc_gl_num, :varchar, :size => 12
      column :sc_percent, :integer
      column :sc_dist_co, :varchar, :size => 2
    end
  end
end
