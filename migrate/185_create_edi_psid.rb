# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:edi_psid) do
      column :ep_code, :varchar, size: 2
      column :ep_desc, :varchar, size: 30
    end
  end
end
