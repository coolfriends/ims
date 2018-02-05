Sequel.migration do
  change do
     create_table(:truck) do
      column :tr_id, :varchar, :size => 10
      column :tr_date, :date
      column :tr_status, :varchar, :size => 1
      column :tr_ship_vi, :varchar, :size => 10
      column :tr_created, :varchar, :size => 5
      column :tr_tt_id, :varchar, :size => 10
      column :tr_note, :text
      column :tr_schedby, :varchar, :size => 5
      column :tr_est_cos, :float
      column :tr_contact, :varchar, :size => 30
      column :tr_appdate, DateTime
      column :tr_actdate, DateTime
      column :tr_tarp, :boolean
      column :tr_shiptim, DateTime
      column :tr_bookedd, DateTime
      column :tr_cust_co, :varchar, :size => 6
      column :tr_type, :integer
      column :tr_partial, :boolean
      column :tr_tally_r, :boolean
      column :tr_see_not, :boolean
      column :tr_paperwo, :boolean
      column :tr_pick_pr, :boolean
      column :tr_to_be_r, :boolean
    end
  end
end
