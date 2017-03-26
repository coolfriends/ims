Sequel.migration do
  change do
     create_table(:ac_bal) do
      column :cb_number, :varchar, :size => 12
      column :cb_year, :varchar, :size => 4
      column :cb_bal_1, :decimal, :precision => 15, :scale => 4
      column :cb_bal_2, :decimal, :precision => 15, :scale => 4
      column :cb_bal_3, :decimal, :precision => 15, :scale => 4
      column :cb_bal_4, :decimal, :precision => 15, :scale => 4
      column :cb_bal_5, :decimal, :precision => 15, :scale => 4
      column :cb_bal_6, :decimal, :precision => 15, :scale => 4
      column :cb_bal_7, :decimal, :precision => 15, :scale => 4
      column :cb_bal_8, :decimal, :precision => 15, :scale => 4
      column :cb_bal_9, :decimal, :precision => 15, :scale => 4
      column :cb_bal_10, :decimal, :precision => 15, :scale => 4
      column :cb_bal_11, :decimal, :precision => 15, :scale => 4
      column :cb_bal_12, :decimal, :precision => 15, :scale => 4
      column :cb_bal_13, :decimal, :precision => 15, :scale => 4
    end
  end
end
