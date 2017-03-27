# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:msg_evnt) do
      column :me_id, :integer
      column :me_action, :integer
      column :me_referen, :varchar, size: 40
      column :me_done, :boolean
      column :me_refere2, :varchar, size: 40
      column :me_refere3, :varchar, size: 40
      column :me_refere4, :varchar, size: 40
      column :me_refere5, :varchar, size: 40
      column :me_owner, :varchar, size: 5
      column :me_reportc, :text
      column :me_timetor, DateTime
      column :me_frequen, :varchar, size: 1
      column :me_kiosk, :boolean
    end
  end
end
