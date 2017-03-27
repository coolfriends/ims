# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:deviate) do
      column :de_id, :varchar, size: 10
      column :de_cust_co, :varchar, size: 6
      column :de_invent_, :varchar, size: 30
      column :de_part_nu, :varchar, size: 30
      column :de_part_de, :varchar, size: 50
      column :de_cust_c2, :varchar, size: 40
      column :de_phone, :varchar, size: 15
      column :de_type, :integer
      column :de_request, :text
      column :de_reason, :text
      column :de_status, :varchar, size: 1
      column :de_accept, :integer
      column :de_date, :date
      column :de_datesig, :date
      column :de_devnum, :varchar, size: 50
      column :de_empby, :varchar, size: 5
      column :de_expdate, :date
      column :de_ca_id, :varchar, size: 10
      column :de_draw, :boolean
      column :de_ca_need, :boolean
      column :de_desc, :varchar, size: 100
      column :de_comment, :text
      column :de_quantit, :integer
      column :de_nc_id, :varchar, size: 10
      column :de_qty_typ, :integer
    end
  end
end
