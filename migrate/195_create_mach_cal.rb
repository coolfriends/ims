Sequel.migration do
  change do
     create_table(:mach_cal) do
      column :ml_mach_co, :varchar, :size => 5
      column :ml_sch_dat, :date
      column :ml_load_hr, :varchar, :size => 124
      column :ml_ot_hrs, :varchar, :size => 124
      column :ml_max_hrs, :varchar, :size => 124
    end
  end
end
