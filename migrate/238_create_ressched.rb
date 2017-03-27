# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ressched) do
      column :rs_sched_d, :date
      column :rs_order_n, :varchar, size: 12
      column :rs_rel_num, :integer
      column :rs_mat_cod, :varchar, size: 6
      column :rs_pour_nu, :integer
      column :rs_cust_co, :varchar, size: 6
      column :rs_mach_co, :varchar, size: 5
      column :rs_invent_, :varchar, size: 30
      column :rs_flow_ra, :integer
      column :rs_totalgp, :integer
      column :rs_resingp, :integer
      column :rs_cav_ppo, :integer
      column :rs_duro, :varchar, size: 3
      column :rs_pigment, :varchar, size: 20
      column :rs_qty_pro, :float
      column :rs_qty_sch, :float
      column :rs_mpp, :float
      column :rs_ph, :float
      column :rs_mach_c2, :varchar, size: 5
      column :rs_mach_c3, :varchar, size: 5
      column :rs_mach_c4, :varchar, size: 5
      column :rs_mach_c5, :varchar, size: 5
      column :rs_mpp1, :float
      column :rs_mpp2, :float
      column :rs_mpp3, :float
      column :rs_mpp4, :float
      column :rs_ph1, :float
      column :rs_ph2, :float
      column :rs_ph3, :float
      column :rs_ph4, :float
      column :rs_emp_id, :varchar, size: 5
      column :rs_emp_id1, :varchar, size: 5
      column :rs_emp_id2, :varchar, size: 5
      column :rs_emp_id3, :varchar, size: 5
      column :rs_emp_id4, :varchar, size: 5
      column :rs_shift, :varchar, size: 2
      column :rs_id, :integer
      column :rs_cast_op, :integer
      column :rs_ppop1, :integer
      column :rs_ppop2, :integer
      column :rs_ppop3, :integer
      column :rs_ppop4, :integer
      column :rs_qi_item, :integer
      column :rs_emp_id5, :varchar, size: 5
      column :rs_emp_id6, :varchar, size: 5
      column :rs_emp_id7, :varchar, size: 5
      column :rs_emp_id8, :varchar, size: 5
      column :rs_emp_id9, :varchar, size: 5
      column :rs_emp_i10, :varchar, size: 5
      column :rs_emp_i11, :varchar, size: 5
      column :rs_emp_i12, :varchar, size: 5
      column :rs_emp1_qt, :float
      column :rs_emp1_q2, :float
      column :rs_emp1_q3, :float
      column :rs_emp2_qt, :float
      column :rs_emp2_q2, :float
      column :rs_emp2_q3, :float
      column :rs_emp3_qt, :float
      column :rs_emp3_q2, :float
      column :rs_emp3_q3, :float
      column :rs_emp4_qt, :float
      column :rs_emp4_q2, :float
      column :rs_emp4_q3, :float
      column :rs_priorit, :integer
    end
  end
end
