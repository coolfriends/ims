Sequel.migration do
  change do
     create_table(:pantick) do
      column :pt_id, :integer
      column :pt_run_cod, :varchar, :size => 20
      column :pt_order_n, :varchar, :size => 12
      column :pt_rel_num, :integer
      column :pt_op_num, :integer
      column :pt_mach_co, :varchar, :size => 5
      column :pt_num_tic, :integer
      column :pt_iss_dat, :date
      column :pt_part_nu, :varchar, :size => 30
      column :pt_rev_num, :varchar, :size => 3
      column :pt_part_de, :varchar, :size => 50
      column :pt_emp_nam, :varchar, :size => 30
      column :pt_emp_id, :varchar, :size => 5
      column :pt_invent_, :varchar, :size => 30
      column :pt_lot, :varchar, :size => 10
      column :pt_ps, :varchar, :size => 1
      column :pt_begin, :integer
      column :pt_asm_cou, :integer
      column :pt_jc_id, :varchar, :size => 10
      column :pt_run_dat, :date
      column :pt_qty_pro, :float
      column :pt_qty_scr, :float
      column :pt_qty_goo, :float
      column :pt_qty_rev, :float
    end
  end
end
