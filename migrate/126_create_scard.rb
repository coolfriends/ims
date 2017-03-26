Sequel.migration do
  change do
     create_table(:scard) do
      column :sc_run_dat, :date
      column :sc_card_st, :varchar, :size => 1
      column :sc_emp_id, :varchar, :size => 5
      column :sc_tot_tim, :float
      column :sc_time_ca, :varchar, :size => 2
      column :sc_time_c2, :varchar, :size => 2
      column :sc_time_c3, :varchar, :size => 2
      column :sc_time_c4, :varchar, :size => 2
      column :sc_time_c5, :varchar, :size => 2
      column :sc_time_c6, :varchar, :size => 2
      column :sc_time_c7, :varchar, :size => 2
      column :sc_time_c8, :varchar, :size => 2
      column :sc_time_c9, :varchar, :size => 2
      column :sc_time_10, :varchar, :size => 2
      column :sc_time_11, :varchar, :size => 2
      column :sc_time_12, :varchar, :size => 2
      column :sc_time_13, :varchar, :size => 2
      column :sc_time_14, :varchar, :size => 2
      column :sc_time_15, :varchar, :size => 2
      column :sc_time1, :varchar, :size => 10
      column :sc_time2, :varchar, :size => 10
      column :sc_time3, :varchar, :size => 10
      column :sc_time4, :varchar, :size => 10
      column :sc_time5, :varchar, :size => 10
      column :sc_time6, :varchar, :size => 10
      column :sc_time7, :varchar, :size => 10
      column :sc_time8, :varchar, :size => 10
      column :sc_time9, :varchar, :size => 10
      column :sc_time10, :varchar, :size => 10
      column :sc_time11, :varchar, :size => 10
      column :sc_time12, :varchar, :size => 10
      column :sc_time13, :varchar, :size => 10
      column :sc_time14, :varchar, :size => 10
      column :sc_time15, :varchar, :size => 10
      column :sc_date1, :date
      column :sc_date2, :date
      column :sc_date3, :date
      column :sc_date4, :date
      column :sc_date5, :date
      column :sc_date6, :date
      column :sc_date7, :date
      column :sc_date8, :date
      column :sc_date9, :date
      column :sc_date10, :date
      column :sc_date11, :date
      column :sc_date12, :date
      column :sc_date13, :date
      column :sc_date14, :date
      column :sc_date15, :date
      column :sc_sec1, :integer
      column :sc_sec2, :integer
      column :sc_sec3, :integer
      column :sc_sec4, :integer
      column :sc_sec5, :integer
      column :sc_sec6, :integer
      column :sc_sec7, :integer
      column :sc_sec8, :integer
      column :sc_sec9, :integer
      column :sc_sec10, :integer
      column :sc_sec11, :integer
      column :sc_sec12, :integer
      column :sc_sec13, :integer
      column :sc_sec14, :integer
      column :sc_sec15, :integer
      column :sc_elap1, :float
      column :sc_elap2, :float
      column :sc_elap3, :float
      column :sc_elap4, :float
      column :sc_elap5, :float
      column :sc_elap6, :float
      column :sc_elap7, :float
      column :sc_elap8, :float
      column :sc_elap9, :float
      column :sc_elap10, :float
      column :sc_elap11, :float
      column :sc_elap12, :float
      column :sc_elap13, :float
      column :sc_elap14, :float
      column :sc_elap15, :float
      column :sc_shift, :varchar, :size => 2
      column :sc_time_mi, :float
      column :sc_er_code, :varchar, :size => 3
      column :sc_da_id_1, :varchar, :size => 10
      column :sc_date_is, :date
      column :sc_issued_, :varchar, :size => 5
      column :sc_da_id_2, :varchar, :size => 10
      column :sc_date_i2, :date
      column :sc_issued2, :varchar, :size => 5
      column :sc_note_1, :text
      column :sc_note_2, :text
      column :sc_da_id_3, :varchar, :size => 10
      column :sc_date_i3, :date
      column :sc_issued3, :varchar, :size => 5
      column :sc_note_3, :text
      column :sc_er_cod2, :varchar, :size => 3
      column :sc_er_cod3, :varchar, :size => 3
      column :sc_da_id_0, :varchar, :size => 10
      column :sc_date_i4, :date
      column :sc_issued4, :varchar, :size => 5
      column :sc_note_0, :text
    end
  end
end
