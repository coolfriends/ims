# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:failure) do
      column :fa_code, :varchar, size: 10
      column :fa_desc, :varchar, size: 40
    end
  end
end
