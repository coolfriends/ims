Sequel.migration do
  change do
     create_table(:tcard) do
      column :tc_run_dat, :date
      column :tc_card_st, :varchar, :size => 1
      column :tc_emp_id, :varchar, :size => 5
      column :tc_tot_tim, :float
      column :tc_time_ca, :varchar, :size => 2
      column :tc_time_c2, :varchar, :size => 2
      column :tc_time_c3, :varchar, :size => 2
      column :tc_time_c4, :varchar, :size => 2
      column :tc_time_c5, :varchar, :size => 2
      column :tc_time_c6, :varchar, :size => 2
      column :tc_time_c7, :varchar, :size => 2
      column :tc_time_c8, :varchar, :size => 2
      column :tc_time_c9, :varchar, :size => 2
      column :tc_time_10, :varchar, :size => 2
      column :tc_time_11, :varchar, :size => 2
      column :tc_time_12, :varchar, :size => 2
      column :tc_time_13, :varchar, :size => 2
      column :tc_time_14, :varchar, :size => 2
      column :tc_time_15, :varchar, :size => 2
      column :tc_time1, :varchar, :size => 10
      column :tc_time2, :varchar, :size => 10
      column :tc_time3, :varchar, :size => 10
      column :tc_time4, :varchar, :size => 10
      column :tc_time5, :varchar, :size => 10
      column :tc_time6, :varchar, :size => 10
      column :tc_time7, :varchar, :size => 10
      column :tc_time8, :varchar, :size => 10
      column :tc_time9, :varchar, :size => 10
      column :tc_time10, :varchar, :size => 10
      column :tc_time11, :varchar, :size => 10
      column :tc_time12, :varchar, :size => 10
      column :tc_time13, :varchar, :size => 10
      column :tc_time14, :varchar, :size => 10
      column :tc_time15, :varchar, :size => 10
      column :tc_date1, :date
      column :tc_date2, :date
      column :tc_date3, :date
      column :tc_date4, :date
      column :tc_date5, :date
      column :tc_date6, :date
      column :tc_date7, :date
      column :tc_date8, :date
      column :tc_date9, :date
      column :tc_date10, :date
      column :tc_date11, :date
      column :tc_date12, :date
      column :tc_date13, :date
      column :tc_date14, :date
      column :tc_date15, :date
      column :tc_sec1, :integer
      column :tc_sec2, :integer
      column :tc_sec3, :integer
      column :tc_sec4, :integer
      column :tc_sec5, :integer
      column :tc_sec6, :integer
      column :tc_sec7, :integer
      column :tc_sec8, :integer
      column :tc_sec9, :integer
      column :tc_sec10, :integer
      column :tc_sec11, :integer
      column :tc_sec12, :integer
      column :tc_sec13, :integer
      column :tc_sec14, :integer
      column :tc_sec15, :integer
      column :tc_elap1, :float
      column :tc_elap2, :float
      column :tc_elap3, :float
      column :tc_elap4, :float
      column :tc_elap5, :float
      column :tc_elap6, :float
      column :tc_elap7, :float
      column :tc_elap8, :float
      column :tc_elap9, :float
      column :tc_elap10, :float
      column :tc_elap11, :float
      column :tc_elap12, :float
      column :tc_elap13, :float
      column :tc_elap14, :float
      column :tc_elap15, :float
      column :tc_shift_s, :varchar, :size => 10
      column :tc_shift_e, :varchar, :size => 10
      column :tc_lunch_e, :varchar, :size => 10
      column :tc_lunch_s, :varchar, :size => 10
      column :tc_status, :varchar, :size => 20
      column :tc_shift, :varchar, :size => 2
      column :tc_exporte, :boolean
      column :tc_exp_dat, :date
      column :tc_de_id1, :varchar, :size => 2
      column :tc_de_id2, :varchar, :size => 2
      column :tc_de_id3, :varchar, :size => 2
      column :tc_de_id4, :varchar, :size => 2
      column :tc_de_id5, :varchar, :size => 2
      column :tc_de_id6, :varchar, :size => 2
      column :tc_de_id7, :varchar, :size => 2
      column :tc_de_id8, :varchar, :size => 2
      column :tc_de_id9, :varchar, :size => 2
      column :tc_de_id10, :varchar, :size => 2
      column :tc_de_id11, :varchar, :size => 2
      column :tc_de_id12, :varchar, :size => 2
      column :tc_de_id13, :varchar, :size => 2
      column :tc_de_id14, :varchar, :size => 2
      column :tc_de_id15, :varchar, :size => 2
      column :tc_updt_us, :varchar, :size => 5
      column :tc_updt_da, :datetime
      column :tc_act1, :varchar, :size => 10
      column :tc_act2, :varchar, :size => 10
      column :tc_act3, :varchar, :size => 10
      column :tc_act4, :varchar, :size => 10
      column :tc_act5, :varchar, :size => 10
      column :tc_act6, :varchar, :size => 10
      column :tc_act7, :varchar, :size => 10
      column :tc_act8, :varchar, :size => 10
      column :tc_act9, :varchar, :size => 10
      column :tc_act10, :varchar, :size => 10
      column :tc_act11, :varchar, :size => 10
      column :tc_act12, :varchar, :size => 10
      column :tc_act13, :varchar, :size => 10
      column :tc_act14, :varchar, :size => 10
      column :tc_act15, :varchar, :size => 10
    end
  end
end
