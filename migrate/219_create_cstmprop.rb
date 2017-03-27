# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:cstmprop) do
      column :pr_id, :varchar, size: 10
      column :pr_label, :varchar, size: 40
      column :pr_cc_id, :varchar, size: 10
      column :pr_type, :varchar, size: 5
      column :pr_seq, :integer
      column :pr_note, :text
      column :pr_field_t, :integer
      column :pr_show, :boolean
      column :pr_cf_id, :varchar, size: 10
    end
  end
end
