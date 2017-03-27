# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:proj_po) do
      column :pp_id, :integer
      column :pp_pr_id, :integer
      column :pp_po_num, :varchar, size: 7
      column :pp_po_line, :integer
    end
  end
end
