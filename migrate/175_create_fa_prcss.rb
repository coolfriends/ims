# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:fa_prcss) do
      column :fa_order_n, :varchar, size: 12
      column :fa_date, :date
      column :fa_emp_nam, :varchar, size: 20
      column :fa_resin1, :varchar, size: 30
      column :fa_resin2, :varchar, size: 30
      column :fa_cur, :varchar, size: 20
      column :fa_duro, :varchar, size: 3
      column :fa_resin1_, :varchar, size: 3
      column :fa_resin2_, :varchar, size: 3
      column :fa_cure_te, :varchar, size: 3
      column :fa_pigment, :varchar, size: 20
      column :fa_totalgp, :integer
      column :fa_oven_te, :varchar, size: 3
      column :fa_moldtem, :varchar, size: 3
      column :fa_moldte2, :varchar, size: 3
      column :fa_moldte3, :varchar, size: 3
      column :fa_moldte4, :varchar, size: 3
      column :fa_moldte5, :varchar, size: 3
      column :fa_moldte6, :varchar, size: 3
      column :fa_mat_cod, :varchar, size: 6
      column :fa_overrid, :integer
      column :fa_hose_si, :varchar, size: 30
      column :fa_hose_le, :integer
      column :fa_cast_ty, :integer
      column :fa_flow_ra, :varchar, size: 20
      column :fa_fr1_tgs, :integer
      column :fa_flow_r2, :varchar, size: 20
      column :fa_fr2_tgs, :integer
      column :fa_colorpe, :integer
      column :fa_pour_ti, :varchar, size: 6
      column :fa_breakou, :varchar, size: 6
      column :fa_partwei, :integer
      column :fa_flashin, :integer
      column :fa_hosewei, :integer
      column :fa_pressti, :varchar, size: 6
      column :fa_bo_note, :text
      column :fa_sp_note, :text
      column :fa_shrinku, :float
      column :fa_shrinka, :float
      column :fa_notes_d, :text
      column :fa_quote_n, :varchar, size: 15
    end
  end
end
