Sequel.migration do
  change do
     create_table(:ship_via) do
      column :sv_id, :varchar, :size => 10
      column :sv_desc, :varchar, :size => 20
      column :sv_bol, :boolean
      column :sv_surchar, :float
      column :sv_parent, :varchar, :size => 10
      column :sv_ship_ty, :varchar, :size => 20
      column :sv_contact, :varchar, :size => 25
      column :sv_phone, :varchar, :size => 14
      column :sv_scac, :varchar, :size => 6
      column :sv_edi_mod, :varchar, :size => 2
      column :sv_edi_eq_, :varchar, :size => 2
      column :sv_markup, :integer
      column :sv_note, :text
      column :sv_obsolet, :boolean
    end
  end
end
