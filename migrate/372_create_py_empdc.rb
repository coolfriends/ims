Sequel.migration do
  change do
     create_table(:py_empdc) do
      column :ed_id, :varchar, :size => 10
      column :ed_emp_id, :varchar, :size => 5
      column :ed_dc_id, :varchar, :size => 10
      column :ed_dc_e_ty, :varchar, :size => 1
      column :ed_dc_e_ra, :float
      column :ed_dc_r_ty, :varchar, :size => 1
      column :ed_dc_r_ra, :float
      column :ed_dc_empr, :float
      column :ed_dc_empe, :float
      column :ed_overrid, :boolean
      column :ed_suta, :boolean
      column :ed_sit, :boolean
      column :ed_lit1, :boolean
      column :ed_lit2, :boolean
      column :ed_dc_e_am, :float
      column :ed_dc_r_am, :float
      column :ed_dc_e_da, :date
      column :ed_pay_gl_, :varchar, :size => 12
      column :ed_exp_gl_, :varchar, :size => 12
      column :ed_dc_e_r2, :float
      column :ed_dc_r_r2, :float
      column :ed_dc_e_ma, :boolean
      column :ed_dc_r_ma, :boolean
      column :ed_sot, :boolean
      column :ed_dc_e_ca, :varchar, :size => 1
      column :ed_dc_r_ca, :varchar, :size => 1
    end
  end
end
