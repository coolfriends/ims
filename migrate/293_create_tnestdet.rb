# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:tnestdet) do
      column :nd_id, :varchar, size: 10
      column :nd_runcode, :varchar, size: 20
      column :nd_order_n, :varchar, size: 12
      column :nd_op_num, :integer
      column :nd_pcs_raw, :integer
      column :nd_tot_sq_, :float
      column :nd_percent, :integer
      column :nd_pcs_pro, :integer
      column :nd_pcs_scr, :integer
      column :nd_pcs_goo, :integer
      column :nd_time, :float
      column :nd_materia, :float
      column :nd_part_nu, :varchar, size: 25
      column :nd_fg_inve, :varchar, size: 30
      column :nd_aj_id, :varchar, size: 10
      column :nd_rel_num, :integer
      column :nd_pcs_rev, :integer
      column :nd_pcs_rew, :integer
      column :nd_attend, :integer
      column :nd_trackin, :varchar, size: 10
      column :nd_op_comp, :boolean
      column :nd_qi_line, :integer
      column :nd_qi_item, :integer
      column :nd_np, :float
      column :nd_de_id, :varchar, size: 10
      column :nd_notes, :text
    end
  end
end
