# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:lab_rpt) do
      column :lr_id, :varchar, size: 10
      column :lr_name, :varchar, size: 20
      column :lr_desc, :varchar, size: 50
      column :lr_filenam, :varchar, size: 8
      column :lr_type, :varchar, size: 1
      column :lr_donor, :varchar, size: 8
      column :lr_user_id, :varchar, size: 5
      column :lr_date, :date
      column :lr_no_copi, :integer
      column :lr_cust_co, :varchar, size: 6
    end
  end
end
