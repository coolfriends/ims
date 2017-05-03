Sequel.migration do
  change do
     create_table(:certlot) do
      column :cl_id, :varchar, :size => 10
      column :cl_ch_id, :varchar, :size => 10
      column :cl_line_nu, :integer
      column :cl_lot_qty, :integer
      column :cl_process, :varchar, :size => 20
      column :cl_spec, :varchar, :size => 20
      column :cl_rev, :varchar, :size => 3
      column :cl_amd, :varchar, :size => 3
      column :cl_not, :varchar, :size => 3
      column :cl_heat_nu, :varchar, :size => 15
      column :cl_supp_co, :varchar, :size => 6
      column :cl_supp_na, :varchar, :size => 30
      column :cl_date, :date
    end
  end
end
