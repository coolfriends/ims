# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:cv_type) do
      column :cv_code, :varchar, size: 5
      column :cv_desc, :varchar, size: 30
      column :cv_rgb, :integer
      column :cv_forewhi, :boolean
      column :cv_po_memo, :text
      column :cv_pricebr, :integer
    end
  end
end
