Sequel.migration do
  change do
     create_table(:inv_rec) do
      column :ir_month, :integer
      column :ir_year, :integer
      column :ir_raw_bal, :float
      column :ir_wip_bal, :float
      column :ir_fin_bal, :float
      column :ir_dv_code, :varchar, :size => 2
      column :ir_dp_code, :varchar, :size => 2
      column :ir_gl_raw_, :varchar, :size => 12
      column :ir_gl_wip_, :varchar, :size => 12
      column :ir_gl_fin_, :varchar, :size => 12
      column :ir_gl_pur_, :varchar, :size => 12
      column :ir_gl_pur2, :varchar, :size => 12
      column :ir_gl_prd_, :varchar, :size => 12
      column :ir_gl_prd2, :varchar, :size => 12
      column :ir_gl_prd3, :varchar, :size => 12
      column :ir_gl_cgs_, :varchar, :size => 12
      column :ir_gl_cgs2, :varchar, :size => 12
      column :ir_gl_cgs3, :varchar, :size => 12
      column :ir_gl_cgs4, :varchar, :size => 12
      column :ir_gl_scra, :varchar, :size => 12
      column :ir_gl_inv_, :varchar, :size => 12
      column :ir_pur_to_, :boolean
      column :ir_wip_to_, :boolean
      column :ir_adj_div, :boolean
      column :ir_last_mo, :integer
      column :ir_last_ye, :integer
      column :ir_inv_div, :boolean
      column :ir_cgs_div, :boolean
      column :ir_entry_n, :text
      column :ir_gj_id, :varchar, :size => 10
      column :ir_last_dv, :varchar, :size => 2
      column :ir_last_dp, :varchar, :size => 2
      column :ir_gl_crw_, :varchar, :size => 12
      column :ir_gl_crw2, :varchar, :size => 12
      column :ir_gl_crw3, :varchar, :size => 12
      column :ir_gl_crw4, :varchar, :size => 12
      column :ir_split_r, :boolean
      column :ir_split_2, :boolean
      column :ir_split_f, :boolean
      column :ir_split_c, :boolean
      column :ir_oth_bal, :float
      column :ir_gl_oth_, :varchar, :size => 12
      column :ir_split_o, :boolean
      column :ir_ex_oth_, :boolean
      column :ir_pd_by_t, :boolean
      column :ir_use_div, :boolean
      column :ir_split_s, :boolean
    end
  end
end
