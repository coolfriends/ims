# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:sv_atrb) do
      column :sc_id, :varchar, size: 10
      column :sc_ship_vi, :varchar, size: 20
      column :sc_vc_id, :varchar, size: 10
      column :sc_approve, :boolean
      column :sc_expires, :date
      column :sc_desc, :varchar, size: 100
      column :sc_notes, :text
    end
  end
end
