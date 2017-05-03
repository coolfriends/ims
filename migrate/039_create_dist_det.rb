Sequel.migration do
  change do
     create_table(:dist_det) do
      column :dd_id, :integer
      column :dd_dl_id, :integer
      column :dd_user_id, :varchar, :size => 5
      column :dd_email, :varchar, :size => 40
      column :dd_name, :varchar, :size => 30
    end
  end
end
