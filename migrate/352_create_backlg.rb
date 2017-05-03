Sequel.migration do
  change do
     create_table(:backlg) do
      column :bl_userid, :varchar, :size => 5
      column :bl_date, :date
      column :bl_complet, :boolean
      column :bl_ship_da, :date
      column :bl_qtytoma, :integer
      column :bl_qtyallo, :integer
      column :bl_part_nu, :varchar, :size => 30
      column :bl_invent_, :varchar, :size => 30
      column :bl_leadtim, :integer
      column :bl_custome, :varchar, :size => 50
      column :bl_comp_da, :date
      column :bl_id, :varchar, :size => 10
    end
  end
end
