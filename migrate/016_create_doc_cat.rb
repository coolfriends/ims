Sequel.migration do
  change do
     create_table(:doc_cat) do
      column :dc_doc_typ, :varchar, :size => 10
      column :dc_doc_des, :varchar, :size => 30
      column :dc_applica, :varchar, :size => 30
      column :dc_approve, :varchar, :size => 20
      column :dc_process, :varchar, :size => 30
      column :dc_outside, :varchar, :size => 60
      column :dc_control, :boolean
      column :dc_prefix, :varchar, :size => 2
      column :dc_emp_id, :varchar, :size => 5
      column :dc_doc_gro, :integer
      column :dc_de_id, :varchar, :size => 2
      column :dc_multipl, :boolean
      column :dc_docpath, :varchar, :size => 100
    end
  end
end
