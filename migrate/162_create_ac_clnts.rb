# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_clnts) do
      column :cn_id, :varchar, size: 10
      column :cn_days, :integer
      column :cn_text, :text
    end
  end
end
