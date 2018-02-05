Sequel.migration do
  change do
     create_table(:execsum) do
      column :es_ar_agin, :float
      column :es_ar_agi2, :float
      column :es_ar_agi3, :float
      column :es_ar_agi4, :float
      column :es_ar_agi5, :float
      column :es_ap_agin, :float
      column :es_ap_agi2, :float
      column :es_ap_agi3, :float
      column :es_ap_agi4, :float
      column :es_ap_agi5, :float
      column :es_ar_tota, :float
      column :es_ar_tot2, :float
      column :es_ar_tot3, :float
      column :es_ar_tot4, :float
      column :es_ar_tot5, :float
      column :es_ap_tota, :float
      column :es_ap_tot2, :float
      column :es_ap_tot3, :float
      column :es_ap_tot4, :float
      column :es_ap_tot5, :float
      column :es_py_tota, :float
      column :es_py_tot2, :float
      column :es_py_tot3, :float
      column :es_py_tot4, :float
      column :es_py_tot5, :float
      column :es_cr_tota, :float
      column :es_cr_tot2, :float
      column :es_cr_tot3, :float
      column :es_cr_tot4, :float
      column :es_cr_tot5, :float
      column :es_cd_tota, :float
      column :es_cd_tot2, :float
      column :es_cd_tot3, :float
      column :es_cd_tot4, :float
      column :es_cd_tot5, :float
      column :es_ar_c, :float
      column :es_us_c, :float
      column :es_so_c, :float
      column :es_ap_c, :float
      column :es_ur_c, :float
      column :es_po_c, :float
      column :es_py_c, :float
      column :es_ca_c, :float
      column :es_ar_1, :float
      column :es_us_1, :float
      column :es_so_1, :float
      column :es_ap_1, :float
      column :es_ur_1, :float
      column :es_po_1, :float
      column :es_py_1, :float
      column :es_ca_1, :float
      column :es_ar_2, :float
      column :es_us_2, :float
      column :es_so_2, :float
      column :es_ap_2, :float
      column :es_ur_2, :float
      column :es_po_2, :float
      column :es_py_2, :float
      column :es_ca_2, :float
      column :es_ar_3, :float
      column :es_us_3, :float
      column :es_so_3, :float
      column :es_ap_3, :float
      column :es_ur_3, :float
      column :es_po_3, :float
      column :es_py_3, :float
      column :es_ca_3, :float
      column :es_asof_da, :date
      column :es_type, :varchar, :size => 1
      column :es_ca_tota, :float
    end
  end
end
