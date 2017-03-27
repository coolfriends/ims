# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:sordcust) do
      column :sc_sord_nu, :varchar, size: 7
      column :sc_line_nu, :integer
      column :sc_cust_co, :varchar, size: 6
      column :sc_quantit, :integer
      column :sc_percent, :float
      column :sc_fixedam, :float
    end
  end
end
