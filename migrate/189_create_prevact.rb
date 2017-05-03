Sequel.migration do
  change do
     create_table(:prevact) do
      column :pa_id, :varchar, :size => 10
      column :pa_date, :date
      column :pa_invent_, :varchar, :size => 30
      column :pa_part_nu, :varchar, :size => 30
      column :pa_part_de, :varchar, :size => 50
      column :pa_intcirc, :text
      column :pa_prevact, :text
      column :pa_impl, :text
      column :pa_effanal, :text
      column :pa_comm, :text
      column :pa_cust_co, :varchar, :size => 6
      column :pa_supp_co, :varchar, :size => 6
      column :pa_desc, :varchar, :size => 100
      column :pa_emp_by, :varchar, :size => 5
      column :pa_ca_id, :varchar, :size => 10
      column :pa_status, :varchar, :size => 1
      column :pa_nc_id, :varchar, :size => 10
      column :pa_mach_co, :varchar, :size => 5
      column :pa_op_num, :integer
      column :pa_de_id, :varchar, :size => 2
      column :pa_status_, :date
      column :pa_di_id, :varchar, :size => 10
      column :pa_presp, :varchar, :size => 5
      column :pa_iresp, :varchar, :size => 5
      column :pa_eresp, :varchar, :size => 5
      column :pa_cresp, :varchar, :size => 5
      column :pa_pdate, :date
      column :pa_idate, :date
      column :pa_edate, :date
      column :pa_cdate, :date
      column :pa_pstatus, :varchar, :size => 1
      column :pa_istatus, :varchar, :size => 1
      column :pa_estatus, :varchar, :size => 1
      column :pa_cstatus, :varchar, :size => 1
      column :pa_needact, :text
      column :pa_results, :text
      column :pa_team, :text
    end
  end
end
