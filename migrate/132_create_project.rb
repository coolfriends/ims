# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:project) do
      column :pr_id, :integer
      column :pr_proj_or, :varchar, size: 12
      column :pr_install, :varchar, size: 30
      column :pr_item_nu, :integer
      column :pr_subitem, :integer
      column :pr_pcpart, :integer
      column :pr_req_sho, :boolean
      column :pr_order_n, :varchar, size: 12
      column :pr_invnon, :integer
      column :pr_invent_, :varchar, size: 30
      column :pr_part_nu, :varchar, size: 30
      column :pr_purch_u, :varchar, size: 2
      column :pr_islot, :boolean
      column :pr_make_bu, :varchar, size: 1
      column :pr_paint, :varchar, size: 20
      column :pr_quantit, :float
      column :pr_unit_co, :float
      column :pr_ext_cos, :float
      column :pr_reserve, :float
      column :pr_bal_nee, :float
      column :pr_part_de, :varchar, size: 60
      column :pr_pmemo, :text
      column :pr_serial_, :varchar, size: 20
      column :pr_dist_co, :varchar, size: 2
      column :pr_prod_co, :varchar, size: 2
      column :pr_require, :date
      column :pr_prepurc, :boolean
      column :pr_supp_co, :varchar, size: 6
      column :pr_sup_par, :varchar, size: 30
      column :pr_cert_nu, :varchar, size: 15
      column :pr_lead_ti, :integer
      column :pr_donotbu, :boolean
      column :pr_non_sto, :boolean
      column :pr_obsolet, :boolean
      column :pr_dir_sto, :integer
      column :pr_po_num, :varchar, size: 7
      column :pr_po_line, :integer
      column :pr_qty_ord, :float
      column :pr_qty_rec, :float
      column :pr_fab_dat, :date
      column :pr_ship_da, :date
      column :pr_due_dat, :date
      column :pr_assigne, :varchar, size: 5
      column :pr_stock_u, :varchar, size: 2
      column :pr_usesuom, :boolean
      column :pr_shape_c, :varchar, size: 7
      column :pr_mat_cod, :varchar, size: 6
      column :pr_cht_siz, :float
      column :pr_mat_len, :float
      column :pr_width, :float
      column :pr_height, :float
      column :pr_web_thi, :float
      column :pr_bar_wei, :float
      column :pr_mat_wid, :float
      column :pr_length, :float
      column :pr_qty_per, :float
      column :pr_wgtpp, :float
      column :pr_ppbar, :float
      column :pr_mach_co, :varchar, size: 5
      column :pr_tot_hrs, :float
      column :pr_draw_nu, :varchar, size: 15
      column :pr_lock_ba, :boolean
      column :pr_rev_ste, :integer
      column :pr_confcos, :boolean
      column :pr_alloc_o, :integer
      column :pr_qinv_it, :integer
      column :pr_from_ex, :boolean
      column :pr_purch_m, :text
      column :pr_purch_q, :float
      column :pr_bom_id, :varchar, size: 10
    end
  end
end
