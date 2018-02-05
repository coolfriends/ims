Sequel.migration do
  change do
     create_table(:pod_txt) do
      column :pw_id, :varchar, :size => 10
      column :pw_type, :integer
      column :pw_field_n, :varchar, :size => 25
      column :pw_true_te, :varchar, :size => 250
      column :pw_false_t, :varchar, :size => 250
      column :pw_null_te, :varchar, :size => 250
    end
  end
end
