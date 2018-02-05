Sequel.migration do
  change do
     create_table(:partkpi) do
      column :invent_num, :varchar, :size => 30
      column :invent_des, :varchar, :size => 50
      column :cust_code, :varchar, :size => 6
      column :valperpart, :float
      column :valaccum, :float
      column :volaau, :integer
      column :voleau, :integer
      column :numsu52, :integer
      column :numsuem, :integer
      column :numsuq, :integer
      column :sut52, :float
      column :sutem, :float
      column :sutq, :float
      column :ct52, :float
      column :ctem, :float
      column :ctq, :float
      column :peff52, :integer
      column :peffem, :integer
      column :peffq, :integer
      column :rate52, :integer
      column :rateem, :integer
      column :rateq, :integer
      column :scrap52, :float
      column :scrapem, :float
      column :scrapq, :float
      column :ptactual, :float
      column :ptem, :float
      column :ptq, :float
      column :partkpiid, :integer
      column :mach_code, :varchar, :size => 5
      column :de_id, :varchar, :size => 2
      column :numsu52_col, :varchar, :size => 1
      column :numsuemcol, :varchar, :size => 1
      column :sut52_color, :varchar, :size => 1
      column :sutemcolor, :varchar, :size => 1
      column :ct52_color, :varchar, :size => 1
      column :ctemcolor, :varchar, :size => 1
      column :peff52_colo, :varchar, :size => 1
      column :peffemcolo, :varchar, :size => 1
      column :rate52_colo, :varchar, :size => 1
      column :rateemcolo, :varchar, :size => 1
      column :scrap52_col, :varchar, :size => 1
      column :scrapemcol, :varchar, :size => 1
      column :ptactualco, :varchar, :size => 1
      column :ofi, :float
      column :vapercent, :integer
    end
  end
end
