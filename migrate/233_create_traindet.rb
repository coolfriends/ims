Sequel.migration do
  change do
     create_table(:traindet) do
      column :td_id, :varchar, :size => 10
      column :td_tr_id, :varchar, :size => 10
      column :td_emp_id, :varchar, :size => 10
      column :td_score, :integer
      column :td_passfai, :integer
    end
  end
end
