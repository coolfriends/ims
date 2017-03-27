# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_regtx) do
      column :rt_id, :varchar, size: 10
      column :rt_rg_id, :varchar, size: 10
      column :rt_tx_id, :varchar, size: 10
      column :rt_ts_id, :varchar, size: 10
      column :rt_or_calc, :boolean
      column :rt_tax_py_, :varchar, size: 12
      column :rt_tax_ex_, :varchar, size: 12
      column :rt_ee_ti_a, :float
      column :rt_ee_ri_a, :float
      column :rt_ee_tax_, :float
      column :rt_er_ti_a, :float
      column :rt_er_ri_a, :float
      column :rt_er_tax_, :float
      column :rt_not_cal, :boolean
      column :rt_ts_type, :varchar, size: 1
      column :rt_exempti, :integer
      column :rt_depende, :integer
      column :rt_ad_tax_, :float
      column :rt_ad_tax2, :varchar, size: 1
      column :rt_ad_tax3, :boolean
      column :rt_or_tax, :boolean
      column :rt_or_emp, :boolean
      column :rt_superce, :boolean
      column :rt_ns_type, :varchar, size: 1
      column :rt_ns_amt, :float
    end
  end
end
