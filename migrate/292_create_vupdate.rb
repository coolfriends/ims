Sequel.migration do
  change do
     create_table(:vupdate) do
      column :up_bom_quo, :date
      column :del_jcbatc, :boolean
      column :doc_man_et, :boolean
      column :up_lot_id, :boolean
      column :dec_so_inv, :boolean
      column :pod_txt, :boolean
      column :fixut, :boolean
      column :uom_add_cy, :boolean
      column :up_cur_cod, :boolean
      column :up_cur_co2, :boolean
      column :add_action, :boolean
      column :fix_inv_ec, :boolean
      column :so_phone_f, :boolean
      column :bf_ca_id, :boolean
      column :lo_po_line, :boolean
      column :check_step, :boolean
      column :set_iv_com, :boolean
      column :set_cc_pos, :boolean
      column :set_fflush, :boolean
      column :fix_unit_t, :boolean
      column :convqtyuom, :boolean
      column :invjrnlord, :boolean
      column :set_encryp, :boolean
      column :set_thdwir, :boolean
    end
  end
end
