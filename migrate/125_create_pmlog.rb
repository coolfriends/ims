# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:pmlog) do
      column :pl_id, :varchar, size: 10
      column :pl_pm_id, :varchar, size: 20
      column :pl_reading, :float
      column :pl_readin2, :float
      column :pl_action, :text
      column :pl_blk_siz, :float
      column :pl_blk_si2, :float
      column :pl_date, :date
      column :pl_interva, :float
      column :pl_interv2, :float
      column :pl_interv3, :float
      column :pl_interv4, :float
      column :pl_interv5, :float
      column :pl_emp_id, :varchar, size: 5
      column :pl_result, :varchar, size: 4
      column :pl_masteru, :varchar, size: 30
      column :pl_interv6, :float
      column :pl_interv7, :float
      column :pl_paralle, :float
      column :pl_uncerta, :float
      column :pl_screw_w, :varchar, size: 4
      column :pl_result1, :float
      column :pl_result2, :float
      column :pl_result3, :float
      column :pl_result4, :float
      column :pl_result5, :float
      column :pl_result6, :float
      column :pl_result7, :float
      column :pl_result8, :float
      column :pl_result9, :float
      column :pl_resul10, :float
      column :pl_resul11, :float
      column :pl_resul12, :float
      column :pl_resul13, :float
      column :pl_resul14, :float
      column :pl_result_, :varchar, size: 10
      column :pl_cylindr, :float
      column :pl_pass1, :varchar, size: 4
      column :pl_pass2, :varchar, size: 4
      column :pl_pass3, :varchar, size: 4
      column :pl_pass4, :varchar, size: 4
      column :pl_pass5, :varchar, size: 4
      column :pl_pass6, :varchar, size: 4
      column :pl_pass7, :varchar, size: 4
    end
  end
end
