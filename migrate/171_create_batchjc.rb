Sequel.migration do
  change do
     create_table(:batchjc) do
      column :cemp, :varchar, :size => 5
      column :nop, :integer
      column :ncount, :integer
      column :nscrap, :integer
      column :nreview, :integer
      column :nhours, :float
      column :ddate, :date
      column :cwc, :varchar, :size => 5
      column :corder, :varchar, :size => 12
      column :cdefects, :varchar, :size => 20
      column :clot, :varchar, :size => 20
      column :nrework, :float
      column :nsuhours, :float
      column :ndnhours, :float
      column :cshift, :varchar, :size => 2
      column :nrel, :integer
      column :nnomach, :integer
      column :serial_num, :float
      column :iscomplete, :boolean
      column :cid_code, :varchar, :size => 10
      column :cdown_reas, :varchar, :size => 80
      column :ot_hrs_s, :float
      column :dot_hrs_s, :float
      column :ot_hrs_p, :float
      column :dot_hrs_p, :float
      column :cdtcode, :varchar, :size => 5
      column :cruncode, :varchar, :size => 20
      column :imported, :boolean
      column :bj_id, :varchar, :size => 10
    end
  end
end
