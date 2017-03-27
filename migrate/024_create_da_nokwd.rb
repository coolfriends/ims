# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:da_nokwd) do
      column :nk_id, :varchar, size: 10
      column :nk_desc, :varchar, size: 35
      column :nk_last_lo, :varchar, size: 10
      column :nk_last_up, DateTime
    end
  end
end
