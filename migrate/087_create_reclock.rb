Sequel.migration do
  change do
     create_table(:reclock) do
      column :rl_user_id, :varchar, :size => 5
      column :rl_table, :varchar, :size => 10
      column :rl_key, :varchar, :size => 30
      column :rl_app, :varchar, :size => 3
    end
  end
end
