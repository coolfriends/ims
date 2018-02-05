Sequel.migration do
  change do
     create_table(:stylemat) do
      column :sm_id, :varchar, :size => 6
      column :sm_st_id, :varchar, :size => 6
      column :sm_st_code, :varchar, :size => 25
      column :sm_ma_id, :varchar, :size => 6
      column :sm_ma_code, :varchar, :size => 30
      column :sm_seq, :integer
    end
  end
end
