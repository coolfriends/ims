# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_fajnl) do
      column :fj_id, :varchar, size: 10
      column :fj_fa_id, :varchar, size: 10
      column :fj_date, :date
      column :fj_entry_d, :date
      column :fj_type, :varchar, size: 1
      column :fj_ca_code, :varchar, size: 12
      column :fj_ca_dr_c, :varchar, size: 12
      column :fj_ca_cr_c, :varchar, size: 12
      column :fj_amount, :decimal, precision: 15, scale: 4
      column :fj_dr_amou, :decimal, precision: 15, scale: 4
      column :fj_cr_amou, :decimal, precision: 15, scale: 4
      column :fj_gl_id, :varchar, size: 10
      column :fj_dr_gl_i, :varchar, size: 10
      column :fj_cr_gl_i, :varchar, size: 10
      column :fj_post, :boolean
      column :fj_post_da, :date
      column :fj_referen, :varchar, size: 40
      column :fj_ca_pl_c, :varchar, size: 12
      column :fj_pl_gl_i, :varchar, size: 10
      column :fj_pl_amou, :decimal, precision: 15, scale: 4
      column :fj_supp_co, :varchar, size: 6
    end
  end
end
