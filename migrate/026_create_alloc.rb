# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:alloc) do
      column :al_invent_, :varchar, size: 30
      column :al_type, :varchar, size: 1
      column :al_order_n, :varchar, size: 12
      column :al_op, :integer
      column :al_ppb, :float
      column :al_sched_q, :float
      column :al_prod_qt, :float
      column :al_bal_pro, :float
      column :al_need_ba, :float
      column :al_alloc_q, :float
      column :al_psquare, :float
      column :al_part_le, :float
      column :al_barend_, :float
      column :al_qty_use, :float
      column :al_percent, :integer
      column :al_rel_num, :integer
      column :al_aok, :boolean
      column :al_qty_per, :float
      column :al_width, :float
      column :al_length, :float
      column :al_usesuom, :boolean
      column :al_id, :varchar, size: 10
      column :al_qi_item, :integer
      column :al_order_b, :date
      column :al_need_by, :date
      column :al_po_num, :varchar, size: 7
      column :al_po_line, :integer
      column :al_ok_to_o, :boolean
      column :al_po_note, :text
      column :al_emp_id, :varchar, size: 5
      column :al_req_id, :varchar, size: 10
      column :al_req_sup, :varchar, size: 6
      column :al_req_pur, :varchar, size: 2
      column :al_req_des, :varchar, size: 60
      column :al_req_su2, :varchar, size: 30
      column :al_req_ite, :integer
      column :al_req_ext, :text
      column :al_req_uni, :float
      column :al_req_dis, :varchar, size: 2
      column :al_req_gl_, :varchar, size: 12
      column :al_req_mac, :varchar, size: 5
      column :al_req_fg_, :varchar, size: 30
      column :al_req_tg_, :varchar, size: 10
      column :al_req_too, :varchar, size: 20
      column :al_reqorde, :varchar, size: 12
      column :al_app_emp, :varchar, size: 5
      column :al_sord_nu, :varchar, size: 7
      column :al_sord_li, :integer
    end
  end
end
