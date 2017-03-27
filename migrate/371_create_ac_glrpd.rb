# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ac_glrpd) do
      column :gd_id, :varchar, size: 10
      column :gd_gr_id, :varchar, size: 10
      column :gd_type, :varchar, size: 1
      column :gd_order, :integer
      column :gd_desc, :varchar, size: 80
      column :gd_auto_de, :boolean
      column :gd_col_aut, :boolean
      column :gd_col_hea, :varchar, size: 60
      column :gd_col_he2, :varchar, size: 15
      column :gd_col_he3, :varchar, size: 15
      column :gd_col_he4, :varchar, size: 15
      column :gd_col_typ, :varchar, size: 1
      column :gd_row_typ, :varchar, size: 1
      column :gd_row_acc, :varchar, size: 12
      column :gd_row_ac2, :varchar, size: 12
      column :gd_row_ran, :varchar, size: 10
      column :gd_row_tex, :varchar, size: 40
      column :gd_row_mem, :text
      column :gd_row_ind, :integer
      column :gd_row_pre, :integer
      column :gd_row_pos, :integer
      column :gd_row_pr2, :integer
      column :gd_row_po2, :integer
      column :gd_row_bla, :integer
      column :gd_row_ac3, :varchar, size: 1
      column :gd_row_con, :boolean
      column :gd_row_ove, :boolean
      column :gd_row_top, :boolean
      column :gd_row_bot, :boolean
      column :gd_row_det, :boolean
      column :gd_col_sou, :varchar, size: 1
      column :gd_col_ran, :varchar, size: 1
      column :gd_col_yea, :varchar, size: 1
      column :gd_col_ye2, :integer
      column :gd_col_ye3, :integer
      column :gd_col_qtr, :varchar, size: 1
      column :gd_col_qt2, :varchar, size: 1
      column :gd_col_qt3, :integer
      column :gd_col_prd, :varchar, size: 1
      column :gd_col_pr2, :varchar, size: 2
      column :gd_col_pr3, :integer
      column :gd_col_num, :integer
      column :gd_col_nu2, :integer
      column :gd_row_no_, :boolean
      column :gd_col_deb, :boolean
      column :gd_col_cre, :boolean
      column :gd_col_for, :varchar, size: 1
      column :gd_col_acc, :varchar, size: 1
      column :gd_col_ac2, :varchar, size: 12
      column :gd_col_ac3, :varchar, size: 12
      column :gd_col_pre, :varchar, size: 10
      column :gd_col_no_, :boolean
      column :gd_col_ye4, :varchar, size: 1
      column :gd_col_ye5, :integer
      column :gd_col_ye6, :integer
      column :gd_col_pr4, :varchar, size: 1
      column :gd_col_pr5, :varchar, size: 2
      column :gd_col_pr6, :integer
      column :gd_col_ye7, :varchar, size: 1
      column :gd_col_qt4, :boolean
      column :gd_col_use, :boolean
      column :gd_row_cal, :varchar, size: 1
      column :gd_row_pr3, :varchar, size: 1
      column :gd_row_num, :integer
      column :gd_row_nu2, :integer
      column :gd_row_co2, :decimal, precision: 15, scale: 4
      column :gd_row_for, :varchar, size: 1
    end
  end
end
