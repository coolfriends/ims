Sequel.migration do
  change do
     create_table(:auditor) do
      column :au_date_ti, :datetime
      column :au_user_id, :varchar, :size => 5
      column :au_screen_, :varchar, :size => 15
      column :au_table_i, :varchar, :size => 15
      column :au_table_k, :varchar, :size => 15
      column :au_table_f, :varchar, :size => 30
      column :au_val_bef, :varchar, :size => 50
      column :au_val_aft, :varchar, :size => 50
      column :au_overflo, :text
    end
  end
end
