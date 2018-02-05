Sequel.migration do
  change do
     create_table(:ns_exmps) do
      column :ne_example, :varchar, :size => 30
      column :ne_noun, :varchar, :size => 15
    end
  end
end
