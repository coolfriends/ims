# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:accumet) do
      column :ac_quote_n, :varchar, size: 15
      column :ac_sord_nu, :varchar, size: 7
      column :ac_order_n, :varchar, size: 12
      column :ac_invent_, :varchar, size: 30
      column :ac_inv_num, :varchar, size: 7
      column :ac_od, :float
      column :ac_odplus, :float
      column :ac_odminus, :float
      column :ac_wall, :float
      column :ac_wallplu, :float
      column :ac_wallmin, :float
      column :ac_id, :float
      column :ac_idplus, :float
      column :ac_idminus, :float
      column :ac_temper, :varchar, size: 30
      column :ac_length, :float
      column :ac_lengthp, :float
      column :ac_lengthm, :float
      column :ac_mat_cod, :varchar, size: 6
      column :ac_alloyki, :varchar, size: 1
      column :ac_form, :varchar, size: 20
      column :ac_specifi, :varchar, size: 10
      column :ac_lenuom, :varchar, size: 10
      column :ac_line_nu, :integer
    end
  end
end
