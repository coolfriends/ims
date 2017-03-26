Sequel.migration do
  change do
     create_table(:da_notes) do
      column :no_id, :varchar, :size => 10
      column :no_cust_co, :varchar, :size => 6
      column :no_cc_id, :varchar, :size => 10
      column :no_emp_id, :varchar, :size => 5
      column :no_order_n, :varchar, :size => 12
      column :no_nt_id, :varchar, :size => 10
      column :no_ns_id, :varchar, :size => 10
      column :no_np_id, :varchar, :size => 10
      column :no_nm_id, :varchar, :size => 10
      column :no_nr_id, :varchar, :size => 10
      column :no_status, :varchar, :size => 1
      column :no_date, :date
      column :no_time, :varchar, :size => 5
      column :no_initiat, :integer
      column :no_importa, :integer
      column :no_priorit, :boolean
      column :no_problem, :boolean
      column :no_order, :varchar, :size => 10
      column :no_credit, :float
      column :no_text, :text
      column :no_created, :varchar, :size => 10
      column :no_create2, DateTime
      column :no_last_lo, :varchar, :size => 10
      column :no_last_up, DateTime
      column :no_invent_, :varchar, :size => 30
      column :no_part_nu, :varchar, :size => 30
      column :no_sord_nu, :varchar, :size => 7
      column :no_followu, :date
      column :no_na_ncod, :varchar, :size => 6
      column :no_nk_id, :varchar, :size => 10
      column :no_prod_co, :varchar, :size => 2
    end
  end
end
