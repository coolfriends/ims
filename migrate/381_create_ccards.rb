# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ccards) do
      column :cc_id, :varchar, size: 10
      column :cc_cust_co, :varchar, size: 6
      column :cc_type, :varchar, size: 1
      column :cc_credit_, :varchar, size: 40
      column :cc_cardhol, :varchar, size: 40
      column :cc_expirat, :varchar, size: 40
      column :cc_notes, :text
    end
  end
end
