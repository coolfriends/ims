Sequel.migration do
  change do
     create_table(:inv_log) do
      column :il_date_ti, :datetime
      column :il_user_id, :varchar, :size => 5
      column :il_old_dat, :date
      column :il_new_dat, :date
    end
  end
end
