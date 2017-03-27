# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_gledg) do
      column :gl_id, :varchar, size: 10
      column :gl_date, :date
      column :gl_jl_type, :varchar, size: 2
      column :gl_jl_id, :varchar, size: 10
      column :gl_ca_numb, :varchar, size: 12
      column :gl_amount, :decimal, precision: 15, scale: 4
      column :gl_jl_desc, :varchar, size: 50
      column :gl_jl_ext_, :varchar, size: 50
    end
  end
end
