Sequel.migration do
  change do
     create_table(:ontime) do
      column :ot_date, :date
      column :ot_mach_co, :varchar, :size => 5
      column :ot_de_id, :varchar, :size => 10
      column :ot_total_o, :integer
      column :ot_total_2, :integer
      column :ot_percent, :float
    end
  end
end
