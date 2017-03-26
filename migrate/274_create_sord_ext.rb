Sequel.migration do
  change do
     create_table(:sord_ext) do
      column :se_sord_nu, :varchar, :size => 7
      column :se_tag_num, :varchar, :size => 50
      column :se_instruc, :varchar, :size => 25
      column :se_priorit, :varchar, :size => 15
      column :se_contrac, :varchar, :size => 30
      column :se_dd250, :boolean
      column :se_sf1411, :date
      column :se_program, :varchar, :size => 25
      column :se_proposa, :varchar, :size => 25
      column :se_job_def, :varchar, :size => 15
      column :se_ne_type, :varchar, :size => 1
      column :se_order_t, :varchar, :size => 2
    end
  end
end
