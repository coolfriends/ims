Sequel.migration do
  change do
     create_table(:eco_docs) do
      column :ed_id, :varchar, :size => 10
      column :ed_ec_id, :varchar, :size => 10
      column :ed_note, :text
      column :ed_emp_id, :varchar, :size => 5
      column :ed_date, :date
      column :ed_doc_num, :varchar, :size => 30
      column :ed_rev_num, :varchar, :size => 3
      column :ed_doc_mod, :integer
      column :ed_assigne, :varchar, :size => 5
      column :ed_assign2, :date
      column :ed_updated, :boolean
      column :ed_update_, :date
      column :ed_old_doc, :varchar, :size => 30
      column :ed_new_doc, :varchar, :size => 30
      column :ed_state, :varchar, :size => 10
      column :ed_de_id, :varchar, :size => 2
      column :ed_assign3, :varchar, :size => 5
      column :ed_dc_doc_, :varchar, :size => 10
    end
  end
end
