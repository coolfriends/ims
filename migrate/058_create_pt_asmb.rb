# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:pt_asmb) do
      column :pa_id, :varchar, size: 10
      column :pa_pt_id, :integer
      column :pa_prod_tk, :integer
      column :pa_type, :varchar, size: 1
      column :pa_lot_num, :varchar, size: 20
      column :pa_invent_, :varchar, size: 30
    end
  end
end
