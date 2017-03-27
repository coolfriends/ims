# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:voltrend) do
      column :vt_invent_, :varchar, size: 30
      column :vt_eau, :integer
      column :vt_aau, :integer
      column :vt_aau_52, :integer
      column :vt_aau_26, :integer
      column :vt_aau_13, :integer
      column :vt_aau_4, :integer
      column :vt_aau1, :integer
      column :vt_aau2, :integer
      column :vt_aau3, :integer
      column :vt_aau4, :integer
      column :vt_aau5, :integer
      column :vt_aau6, :integer
      column :vt_aau7, :integer
      column :vt_aau8, :integer
      column :vt_aau9, :integer
      column :vt_aau10, :integer
      column :vt_aau11, :integer
      column :vt_aau12, :integer
      column :vt_pe1, :float
      column :vt_pe2, :float
      column :vt_pe3, :float
      column :vt_pe4, :float
      column :vt_pe5, :float
      column :vt_pe6, :float
      column :vt_pe7, :float
      column :vt_pe8, :float
      column :vt_pe9, :float
      column :vt_pe10, :float
      column :vt_pe11, :float
      column :vt_pe12, :float
      column :vt_eff52, :float
      column :vt_eff26, :float
      column :vt_eff13, :float
      column :vt_eff4, :float
      column :vt_est_set, :float
      column :vt_act_set, :float
      column :vt_cust_co, :varchar, size: 6
    end
  end
end
