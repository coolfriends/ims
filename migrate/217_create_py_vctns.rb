Sequel.migration do
  change do
     create_table(:py_vctns) do
      column :vs_id, :varchar, :size => 10
      column :vs_over, :integer
      column :vs_not_ove, :integer
      column :vs_hours, :integer
    end
  end
end
