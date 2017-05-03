Sequel.migration do
  change do
     create_table(:ac_range) do
      column :rn_id, :varchar, :size => 10
      column :rn_code, :varchar, :size => 3
      column :rn_desc, :varchar, :size => 40
      column :rn_lo, :varchar, :size => 12
      column :rn_hi, :varchar, :size => 12
      column :rn_type, :varchar, :size => 1
      column :rn_categor, :integer
      column :rn_reverse, :boolean
    end
  end
end
