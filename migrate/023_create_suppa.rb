# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:suppa) do
      column :sa_id, :varchar, size: 10
      column :sa_supp_co, :varchar, size: 6
      column :sa_name, :varchar, size: 35
      column :sa_address, :varchar, size: 35
      column :sa_addres2, :varchar, size: 35
      column :sa_city, :varchar, size: 30
      column :sa_state, :varchar, size: 2
      column :sa_zip, :varchar, size: 10
      column :sa_cntry, :varchar, size: 15
      column :sa_isremit, :boolean
      column :sa_phone, :varchar, size: 14
      column :sa_fax, :varchar, size: 14
      column :sa_contact, :varchar, size: 20
      column :sa_email, :varchar, size: 40
    end
  end
end
