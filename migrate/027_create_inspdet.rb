Sequel.migration do
  change do
     create_table(:inspdet) do
      column :id_id, :varchar, :size => 10
      column :id_ih_id, :varchar, :size => 10
      column :id_line_nu, :integer
      column :id_dimen, :varchar, :size => 35
      column :id_im_id, :varchar, :size => 10
      column :id_device_, :varchar, :size => 10
      column :id_aql, :varchar, :size => 10
      column :id_samp, :integer
      column :id_acc, :integer
      column :id_rej, :integer
      column :id_actual, :varchar, :size => 10
      column :id_note, :text
      column :id_id1, :float
      column :id_id2, :float
      column :id_id3, :float
      column :id_id4, :float
      column :id_id5, :float
      column :id_id6, :float
      column :id_td1, :float
      column :id_td2, :float
      column :id_td3, :float
      column :id_td4, :float
      column :id_td5, :float
      column :id_td6, :float
      column :id_thread, :varchar, :size => 10
      column :id_thd_plu, :float
      column :id_thd_min, :float
      column :id_item_di, :float
      column :id_plus_to, :float
      column :id_min_tol, :float
      column :id_arspec, :varchar, :size => 35
      column :id_ar1, :varchar, :size => 1
      column :id_ar2, :varchar, :size => 1
      column :id_ar3, :varchar, :size => 1
      column :id_ar4, :varchar, :size => 1
      column :id_ar5, :varchar, :size => 1
      column :id_ar6, :varchar, :size => 1
    end
  end
end
