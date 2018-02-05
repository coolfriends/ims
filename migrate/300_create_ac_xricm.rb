Sequel.migration do
  change do
     create_table(:ac_xricm) do
      column :im_cust_co, :varchar, :size => 6
      column :im_inv_num, :varchar, :size => 7
      column :im_mr_id, :varchar, :size => 10
      column :im_cred_am, :decimal, :precision => 15, :scale => 4
    end
  end
end
