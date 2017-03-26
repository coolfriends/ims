Sequel.migration do
  change do
     create_table(:datelog) do
      column :dl_order_n, :varchar, :size => 12
      column :dl_datetim, DateTime
      column :dl_old_dat, :date
      column :dl_new_dat, :date
      column :dl_user_id, :varchar, :size => 5
    end
  end
end
