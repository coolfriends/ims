Sequel.migration do
  change do
     create_table(:ac_glrpt) do
      column :gr_id, :varchar, :size => 10
      column :gr_code, :varchar, :size => 10
      column :gr_name, :varchar, :size => 80
      column :gr_type, :varchar, :size => 1
      column :gr_title, :varchar, :size => 80
      column :gr_name_ti, :boolean
      column :gr_title_t, :boolean
      column :gr_title_n, :boolean
      column :gr_title_2, :boolean
      column :gr_title_m, :text
      column :gr_head_ti, :boolean
      column :gr_head_na, :boolean
      column :gr_head_pa, :boolean
      column :gr_head_da, :boolean
      column :gr_head_no, :boolean
      column :gr_head_me, :text
      column :gr_foot_ti, :boolean
      column :gr_foot_na, :boolean
      column :gr_foot_pa, :boolean
      column :gr_foot_da, :boolean
      column :gr_foot_no, :boolean
      column :gr_foot_me, :text
      column :gr_summ_ti, :boolean
      column :gr_summ_na, :boolean
      column :gr_summ_no, :boolean
      column :gr_summ_me, :text
      column :gr_acct_nu, :boolean
      column :gr_title_d, :boolean
      column :gr_head_de, :boolean
      column :gr_foot_de, :boolean
      column :gr_summ_de, :boolean
      column :gr_title_3, :boolean
      column :gr_summ_da, :boolean
      column :gr_title_4, :boolean
      column :gr_title_b, :boolean
      column :gr_head_t_, :boolean
      column :gr_head_b_, :boolean
      column :gr_foot_t_, :boolean
      column :gr_foot_b_, :boolean
      column :gr_summ_t_, :boolean
      column :gr_summ_b_, :boolean
      column :gr_acct_no, :boolean
      column :gr_acct_su, :boolean
      column :gr_acct_he, :boolean
      column :gr_acct_de, :boolean
      column :gr_acct_di, :boolean
      column :gr_acct_dv, :varchar, :size => 2
      column :gr_acct_dp, :varchar, :size => 2
      column :gr_acct_se, :boolean
      column :gr_acct_s2, :integer
      column :gr_acct_s3, :varchar, :size => 2
      column :gr_acct_d2, :boolean
      column :gr_acct_d3, :boolean
      column :gr_round_d, :boolean
    end
  end
end
