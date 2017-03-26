Sequel.migration do
  change do
     create_table(:jcmobile) do
      column :ddate, :date
      column :cemp, :varchar, :size => 5
      column :cruncode, :varchar, :size => 20
      column :ncount, :integer
      column :nscrap, :integer
      column :nproduced, :integer
      column :nhours, :float
      column :cdown_reas, :varchar, :size => 60
      column :nsuhours, :float
      column :ndnhours, :float
      column :cdtcode, :varchar, :size => 5
      column :validrec, :varchar, :size => 1
      column :imported, :boolean
      column :dateimport, :date
      column :jm_id, :varchar, :size => 10
      column :jm_inproce, :boolean
      column :jm_state, :varchar, :size => 20
    end
  end
end
