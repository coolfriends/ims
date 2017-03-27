# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:jcmobdet) do
      column :id, :varchar, size: 10
      column :jm_id, :varchar, size: 10
      column :timecat, :varchar, size: 2
      column :datetime, DateTime
      column :elapsetime, :float
    end
  end
end
