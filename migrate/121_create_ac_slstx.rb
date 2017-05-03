Sequel.migration do
  change do
     create_table(:ac_slstx) do
      column :st_id, :varchar, :size => 10
      column :st_tax_id, :varchar, :size => 15
      column :st_desc, :varchar, :size => 35
      column :st_address, :varchar, :size => 30
      column :st_addres2, :varchar, :size => 30
      column :st_city, :varchar, :size => 25
      column :st_state, :varchar, :size => 2
      column :st_zip, :varchar, :size => 10
      column :st_phone, :varchar, :size => 15
      column :st_rate, :float
      column :st_ca_code, :varchar, :size => 12
      column :st_prod_co, :varchar, :size => 2
      column :st_min, :float
      column :st_max, :float
      column :st_taxonta, :boolean
      column :st_parent_, :varchar, :size => 10
      column :st_code, :varchar, :size => 10
      column :st_ex_frei, :boolean
      column :st_ca_cod2, :varchar, :size => 12
      column :st_dist_co, :varchar, :size => 2
      column :st_type, :integer
      column :st_export, :varchar, :size => 5
      column :st_effecti, :date
      column :st_previou, :float
    end
  end
end
