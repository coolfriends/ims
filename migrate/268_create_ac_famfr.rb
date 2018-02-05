Sequel.migration do
  change do
     create_table(:ac_famfr) do
      column :fm_id, :varchar, :size => 10
      column :fm_code, :varchar, :size => 10
      column :fm_name, :varchar, :size => 40
      column :fm_address, :varchar, :size => 35
      column :fm_addres2, :varchar, :size => 35
      column :fm_city, :varchar, :size => 30
      column :fm_state, :varchar, :size => 3
      column :fm_zip_cod, :varchar, :size => 10
      column :fm_phone, :varchar, :size => 14
      column :fm_fax, :varchar, :size => 14
      column :fm_contact, :varchar, :size => 20
      column :fm_website, :varchar, :size => 30
      column :fm_notes, :text
      column :fm_country, :varchar, :size => 25
      column :fm_email, :varchar, :size => 40
    end
  end
end
