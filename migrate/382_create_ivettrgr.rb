Sequel.migration do
  change do
     create_table(:ivettrgr) do
      column :tr_invent_, :varchar, :size => 30
      column :tr_fromil_, :varchar, :size => 10
      column :tr_fromib_, :varchar, :size => 10
      column :tr_toil_id, :varchar, :size => 10
      column :tr_toib_id, :varchar, :size => 10
      column :tr_box1, :integer
      column :tr_qty1, :float
      column :tr_box2, :integer
      column :tr_qty2, :float
      column :tr_user, :varchar, :size => 10
      column :tr_guid, :varchar, :size => 36
      column :tr_quantit, :float
      column :tr_print, :boolean
    end
  end
end
