Sequel.migration do
  change do
     create_table(:mymenu) do
      column :mm_id, :varchar, :size => 10
      column :mm_user_id, :varchar, :size => 5
      column :mm_sequenc, :integer
      column :mm_form_na, :varchar, :size => 10
      column :mm_form_ti, :varchar, :size => 40
      column :mm_app, :varchar, :size => 3
    end
  end
end
