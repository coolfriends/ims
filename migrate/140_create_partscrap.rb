Sequel.migration do
  change do
     create_table(:partscrap) do
      column :psc_id, :integer
      column :invent_num, :varchar, :size => 30
      column :invent_des, :varchar, :size => 50
      column :cust_code, :varchar, :size => 6
      column :numsu52, :integer
      column :numsuem, :integer
      column :numsuq, :integer
      column :year1, :integer
      column :year2, :integer
      column :year3, :integer
      column :year4, :integer
      column :last52, :integer
      column :last26, :integer
      column :last13, :integer
      column :last5, :integer
      column :ofi, :float
    end
  end
end
