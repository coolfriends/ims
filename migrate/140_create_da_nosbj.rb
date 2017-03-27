# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:da_nosbj) do
      column :ns_id, :varchar, size: 10
      column :ns_nt_id, :varchar, size: 10
      column :ns_desc, :varchar, size: 35
      column :ns_last_lo, :varchar, size: 10
      column :ns_last_up, DateTime
    end
  end
end
