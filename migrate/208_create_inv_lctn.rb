Sequel.migration do
  change do
     create_table(:inv_lctn) do
      column :il_id, :varchar, :size => 10
      column :il_lo_code, :varchar, :size => 10
      column :il_code, :varchar, :size => 10
      column :il_desc, :varchar, :size => 30
      column :il_ship, :boolean
      column :il_de_id, :varchar, :size => 2
      column :il_no_usag, :boolean
      column :il_supp_co, :varchar, :size => 6
      column :il_consign, :boolean
      column :il_hold, :boolean
      column :il_wip, :boolean
      column :il_rawloc, :boolean
      column :il_dv_code, :varchar, :size => 2
      column :il_dp_code, :varchar, :size => 2
      column :il_exclude, :boolean
    end
  end
end
