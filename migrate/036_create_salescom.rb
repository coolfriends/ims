Sequel.migration do
  change do
     create_table(:salescom) do
      column :sc_id, :varchar, :size => 10
      column :sc_type, :varchar, :size => 1
      column :sc_num, :varchar, :size => 7
      column :sc_mr_id, :varchar, :size => 10
      column :sc_line_nu, :integer
      column :sc_order, :integer
      column :sc_emp_id, :varchar, :size => 5
      column :sc_comm_pe, :float
      column :sc_comm_am, :float
      column :sc_comm_pa, :boolean
      column :sc_paid_am, :float
      column :sc_gl_com_, :varchar, :size => 12
      column :sc_gl_com2, :varchar, :size => 12
      column :sc_ex_gl_i, :varchar, :size => 10
      column :sc_py_gl_i, :varchar, :size => 10
      column :sc_dr_id, :varchar, :size => 10
      column :sc_gl_com3, :varchar, :size => 12
      column :sc_gl_com4, :varchar, :size => 12
      column :sc_ipy_gl_, :varchar, :size => 10
      column :sc_epy_gl_, :varchar, :size => 10
      column :sc_correct, :boolean
      column :sc_correc2, :varchar, :size => 7
    end
  end
end
