Sequel.migration do
  change do
     create_table(:py_w2_ml) do
      column :ml_id, :varchar, :size => 10
      column :ml_w2_id, :varchar, :size => 10
      column :ml_st1_id, :varchar, :size => 2
      column :ml_st1_no, :varchar, :size => 15
      column :ml_st1_wag, :float
      column :ml_st1_wit, :float
      column :ml_st2_id, :varchar, :size => 2
      column :ml_st2_no, :varchar, :size => 15
      column :ml_st2_wag, :float
      column :ml_st2_wit, :float
      column :ml_lc1_nam, :varchar, :size => 10
      column :ml_lc1_wag, :float
      column :ml_lc1_wit, :float
      column :ml_lc2_nam, :varchar, :size => 10
      column :ml_lc2_wag, :float
      column :ml_lc2_wit, :float
    end
  end
end
