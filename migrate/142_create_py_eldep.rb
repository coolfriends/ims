# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_eldep) do
      column :el_id, :varchar, size: 10
      column :el_im_dest, :varchar, size: 10
      column :el_im_orig, :varchar, size: 10
      column :el_im_des2, :varchar, size: 23
      column :el_im_ori2, :varchar, size: 23
      column :el_ref_cod, :varchar, size: 8
      column :el_file_da, :varchar, size: 6
      column :el_file_ti, :varchar, size: 4
      column :el_prior_c, :varchar, size: 2
      column :el_file_id, :varchar, size: 1
      column :el_record_, :varchar, size: 3
      column :el_block_f, :varchar, size: 2
      column :el_format_, :varchar, size: 1
      column :el_ser_cla, :varchar, size: 3
      column :el_comp_na, :varchar, size: 36
      column :el_comp_id, :varchar, size: 10
      column :el_ent_cla, :varchar, size: 3
      column :el_comp_en, :varchar, size: 10
      column :el_comp_de, :varchar, size: 6
      column :el_comp_ef, :varchar, size: 6
      column :el_julian_, :varchar, size: 3
      column :el_orig_st, :varchar, size: 1
      column :el_orig_df, :varchar, size: 8
      column :el_batch_n, :varchar, size: 7
      column :el_login_s, :varchar, size: 80
      column :el_balance, :boolean
      column :el_trans_c, :varchar, size: 2
      column :el_routing, :varchar, size: 9
      column :el_account, :varchar, size: 17
    end
  end
end
