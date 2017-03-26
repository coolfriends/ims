Sequel.migration do
  change do
     create_table(:ac_gsctg) do
      column :gc_id, :varchar, :size => 10
      column :gc_desc, :varchar, :size => 50
      column :gc_print_o, :integer
      column :gc_horizon, :boolean
      column :gc_math, :text
    end
  end
end
