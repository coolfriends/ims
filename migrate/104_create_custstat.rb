Sequel.migration do
  change do
     create_table(:custstat) do
      column :cs_cust_co, :varchar, :size => 6
      column :cs_freqofs, :integer
      column :cs_datelas, :date
      column :cs_yearhig, :float
      column :cs_creditl, :float
      column :cs_ytdsale, :float
      column :cs_balance, :float
      column :cs_pastdue, :float
      column :cs_avgdays, :integer
      column :cs_uninvsh, :float
      column :cs_unships, :float
      column :cs_opencre, :float
      column :cs_totpend, :float
      column :cs_availcr, :float
      column :cs_credith, :varchar, :size => 30
      column :cs_currbal, :float
    end
  end
end
