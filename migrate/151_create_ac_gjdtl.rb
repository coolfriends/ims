Sequel.migration do
  change do
     create_table(:ac_gjdtl) do
      column :gd_id, :varchar, :size => 10
      column :gd_sort, :integer
      column :gd_gj_id, :varchar, :size => 10
      column :gd_type, :integer
      column :gd_ca_numb, :varchar, :size => 12
      column :gd_amount, :decimal, :precision => 15, :scale => 4
      column :gd_memo, :text
      column :gd_gl_id, :varchar, :size => 10
    end
  end
end
