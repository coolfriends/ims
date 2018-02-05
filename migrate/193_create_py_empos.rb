Sequel.migration do
  change do
     create_table(:py_empos) do
      column :ps_id, :varchar, :size => 10
      column :ps_desc, :varchar, :size => 30
      column :ps_freq, :varchar, :size => 1
      column :ps_inactiv, :boolean
    end
  end
end
