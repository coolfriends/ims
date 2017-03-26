Sequel.migration do
  change do
     create_table(:orelease) do
      column :ol_order_n, :varchar, :size => 12
      column :ol_rel_dat, :date
      column :ol_rel_num, :integer
      column :ol_rel_qty, :integer
      column :ol_rel_pro, :float
      column :ol_rel_bal, :float
      column :ol_rel_sch, :integer
      column :ol_rel_shi, :integer
      column :ol_quantit, :integer
      column :ol_priorit, :integer
      column :ol_il, :integer
      column :ol_end_dat, :date
      column :ol_fi, :varchar, :size => 1
      column :ol_start_d, :date
      column :ol_po_num, :varchar, :size => 25
      column :ol_sch_qty, :integer
      column :ol_sch_met, :varchar, :size => 1
      column :ol_lead_ti, :integer
      column :ol_ph, :varchar, :size => 1
      column :ol_track_n, :varchar, :size => 15
      column :ol_proj_st, :date
      column :ol_rel_sta, :varchar, :size => 1
      column :ol_sched, :boolean
      column :ol_comp_da, :date
      column :ol_lock, :boolean
      column :ol_cont_cn, :varchar, :size => 10
      column :ol_cont_ty, :varchar, :size => 10
      column :ol_cont_de, :varchar, :size => 20
      column :ol_cont_we, :varchar, :size => 10
      column :ol_lot, :varchar, :size => 20
      column :ol_insp_da, :date
      column :ol_release, :boolean
      column :ol_notes, :text
      column :ol_fab_dat, :date
      column :ol_shipby_, :date
      column :ol_plannin, :date
      column :ol_ordstat, :varchar, :size => 10
      column :ol_expedit, :varchar, :size => 10
      column :ol_owner, :varchar, :size => 5
      column :ol_status1, :varchar, :size => 50
      column :ol_status2, :varchar, :size => 50
      column :ol_matveri, :boolean
    end
  end
end
