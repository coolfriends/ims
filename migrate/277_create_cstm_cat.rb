Sequel.migration do
  change do
     create_table(:cstm_cat) do
      column :cc_id, :varchar, :size => 10
      column :cc_cat, :varchar, :size => 80
      column :cc_type, :varchar, :size => 5
      column :cc_seq, :integer
      column :cc_cf_id, :varchar, :size => 10
    end
  end
end
