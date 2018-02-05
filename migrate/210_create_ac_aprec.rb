Sequel.migration do
  change do
     create_table(:ac_aprec) do
      column :pr_id, :varchar, :size => 10
      column :pr_ca_code, :varchar, :size => 12
      column :pr_supp_co, :varchar, :size => 6
      column :pr_type, :varchar, :size => 1
      column :pr_desc, :varchar, :size => 30
      column :pr_longdes, :text
      column :pr_status, :varchar, :size => 1
      column :pr_terms, :varchar, :size => 20
      column :pr_inv_amt, :decimal, :precision => 15, :scale => 4
      column :pr_inv_bal, :decimal, :precision => 15, :scale => 4
      column :pr_ch_num, :varchar, :size => 10
      column :pr_cash_ap, :decimal, :precision => 15, :scale => 4
      column :pr_lo_code, :varchar, :size => 10
      column :pr_user, :varchar, :size => 5
      column :pr_gl_id, :varchar, :size => 10
      column :pr_last_in, :date
      column :pr_freq, :varchar, :size => 1
      column :pr_selind, :varchar, :size => 1
      column :pr_next, :date
      column :pr_dom, :integer
      column :pr_day, :integer
      column :pr_inv_num, :varchar, :size => 30
      column :pr_post, :boolean
      column :pr_net_amt, :decimal, :precision => 15, :scale => 4
      column :pr_taxes, :decimal, :precision => 15, :scale => 4
    end
  end
end
