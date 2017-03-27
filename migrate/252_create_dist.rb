# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:dist) do
      column :dt_dist_co, :varchar, size: 2
      column :dt_dist_de, :varchar, size: 40
      column :dt_gl_numb, :varchar, size: 12
      column :dt_editabl, :boolean
      column :dt_one_tim, :boolean
      column :dt_po_note, :text
      column :dt_rawmate, :integer
      column :dt_non_tax, :boolean
      column :dt_de_id, :varchar, size: 2
      column :dt_po_ws, :integer
      column :dt_excl_di, :boolean
      column :dt_raw_gl_, :varchar, size: 12
      column :dt_pur_to_, :boolean
      column :dt_tooling, :boolean
      column :dt_lb_cost, :float
      column :dt_prod_co, :varchar, size: 2
    end
  end
end
