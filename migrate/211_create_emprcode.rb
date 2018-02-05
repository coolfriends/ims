Sequel.migration do
  change do
     create_table(:emprcode) do
      column :er_id, :varchar, :size => 10
      column :er_date, :date
      column :er_shift, :varchar, :size => 2
      column :er_run_cod, :varchar, :size => 20
      column :er_emp_id, :varchar, :size => 5
      column :er_note, :text
      column :er_item, :integer
      column :er_prod_se, :integer
      column :er_1_st, :boolean
    end
  end
end
