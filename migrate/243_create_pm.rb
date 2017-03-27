# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:pm) do
      column :pm_id, :varchar, size: 20
      column :pm_task, :varchar, size: 50
      column :pm_date, :date
      column :pm_emp_id, :varchar, size: 5
      column :pm_group, :varchar, size: 10
      column :pm_ext_des, :text
      column :pm_frequen, :integer
      column :pm_last_co, :date
      column :pm_invent_, :varchar, size: 30
      column :pm_next_du, :date
      column :pm_mach_co, :varchar, size: 5
      column :pm_est_hou, :float
      column :pm_gage, :boolean
      column :pm_lot_num, :varchar, size: 20
      column :pm_supp_co, :varchar, size: 6
      column :pm_gt_code, :varchar, size: 10
      column :pm_il_id, :varchar, size: 10
      column :pm_size, :float
      column :pm_metric, :boolean
      column :pm_pitch, :float
      column :pm_pitch_g, :float
      column :pm_pitch_n, :float
      column :pm_poa_go, :float
      column :pm_poa_ng, :float
      column :pm_lop_go, :float
      column :pm_lop_ng, :float
      column :pm_ib_id, :varchar, size: 10
      column :pm_obsolet, :boolean
      column :pm_verifie, :boolean
      column :pm_tt_id, :varchar, size: 10
      column :pm_go_id, :varchar, size: 10
      column :pm_manufac, :varchar, size: 30
      column :pm_status, :varchar, size: 10
      column :pm_range, :varchar, size: 30
      column :pm_cbou, :boolean
      column :pm_gagecat, :integer
      column :pm_gagecla, :varchar, size: 10
      column :pm_diamete, :float
      column :pm_gonogo, :integer
      column :pm_threads, :varchar, size: 10
      column :pm_thdform, :integer
      column :pm_classof, :integer
    end
  end
end
