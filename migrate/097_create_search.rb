# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:search) do
      column :sc_form, :varchar, size: 15
      column :sc_user, :varchar, size: 5
      column :sc_criteri, :text
    end
  end
end
