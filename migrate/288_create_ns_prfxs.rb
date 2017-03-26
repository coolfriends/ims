Sequel.migration do
  change do
     create_table(:ns_prfxs) do
      column :np_prefix, :varchar, :size => 3
      column :np_noun, :varchar, :size => 15
      column :np_counter, :integer
      column :np_digits, :integer
      column :np_inactiv, :boolean
    end
  end
end
