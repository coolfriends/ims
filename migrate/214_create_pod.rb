# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:pod) do
      column :px_po_num, :varchar, size: 15
      column :px_parts_f, :boolean
      column :px_hardnes, :boolean
      column :px_bars_pc, :boolean
      column :px_bars_ma, :boolean
      column :px_bars_st, :boolean
      column :px_hardne2, :boolean
      column :px_heat_tr, :boolean
      column :px_inert_g, :boolean
      column :px_scales, :boolean
      column :px_pull_te, :boolean
      column :px_line_nu, :integer
      column :px_dist_co, :varchar, size: 2
      column :px_hardne3, :varchar, size: 30
      column :px_bar_tir, :float
      column :px_hard_re, :varchar, size: 30
      column :px_ht_spec, :varchar, size: 30
      column :px_pull_t2, :integer
      column :px_vend_in, :text
      column :px_pack_re, :text
      column :px_print_i, :boolean
      column :px_ht_done, :boolean
      column :px_batch_i, :boolean
      column :px_add_ven, :text
      column :px_mat_har, :boolean
      column :px_mat_ha2, :varchar, size: 30
      column :px_plate_t, :boolean
      column :px_plate_2, :float
      column :px_fillet, :boolean
      column :px_max_fil, :varchar, size: 30
      column :px_conc_re, :text
      column :px_conc_a, :varchar, size: 15
      column :px_conc_b, :varchar, size: 15
      column :px_conc_c, :varchar, size: 15
      column :px_norm_a, :varchar, size: 15
      column :px_norm_b, :varchar, size: 15
      column :px_norm_c, :varchar, size: 15
      column :px_st_id, :varchar, size: 10
      column :px_type, :integer
      column :px_mat_spe, :boolean
      column :px_gages, :boolean
      column :px_gage_go, :varchar, size: 15
      column :px_gage_no, :varchar, size: 15
      column :px_mat_sp2, :varchar, size: 30
      column :px_finish, :boolean
      column :px_finish_, :varchar, size: 30
      column :_null_flags, :varchar, size: 3
    end
  end
end
