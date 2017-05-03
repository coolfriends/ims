Sequel.migration do
  change do
     create_table(:ivhazmat) do
      column :hm_invent_, :varchar, :size => 30
      column :hm_corrosi, :boolean
      column :hm_environ, :boolean
      column :hm_explbom, :boolean
      column :hm_expoint, :boolean
      column :hm_flame, :boolean
      column :hm_flameov, :boolean
      column :hm_gascyli, :boolean
      column :hm_healthh, :boolean
      column :hm_skullxc, :boolean
    end
  end
end
