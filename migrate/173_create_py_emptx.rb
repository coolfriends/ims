# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_emptx) do
      column :et_id, :varchar, size: 10
      column :et_emp_id, :varchar, size: 5
      column :et_tx_id, :varchar, size: 10
      column :et_ts_id, :varchar, size: 10
      column :et_ts_type, :varchar, size: 1
      column :et_tax_py_, :varchar, size: 12
      column :et_tax_ex_, :varchar, size: 12
      column :et_exempti, :integer
      column :et_depende, :integer
      column :et_ad_tax_, :float
      column :et_ad_tax2, :varchar, size: 1
      column :et_ad_tax3, :boolean
      column :et_or_tax, :boolean
      column :et_or_emp, :boolean
      column :et_superce, :boolean
      column :et_ns_type, :varchar, size: 1
      column :et_ns_amt, :float
    end
  end
end
