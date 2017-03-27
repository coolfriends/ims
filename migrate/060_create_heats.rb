# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:heats) do
      column :ht_invent_, :varchar, size: 30
      column :ht_heat_nu, :varchar, size: 30
      column :ht_heat_de, :varchar, size: 35
      column :ht_heat_no, :text
      column :ht_heat_qt, :float
      column :ht_sup_cod, :varchar, size: 6
      column :ht_recdate, :date
      column :ht_imagefi, :varchar, size: 30
      column :ht_po_num, :varchar, size: 7
      column :ht_cust_co, :varchar, size: 6
      column :ht_cust_c2, :varchar, size: 30
      column :ht_cust_po, :varchar, size: 30
      column :ht_eu_cont, :varchar, size: 30
      column :ht_eu_phon, :varchar, size: 20
      column :ht_eu_addr, :text
      column :ht_purch_d, :date
      column :ht_item1, :varchar, size: 30
      column :ht_item2, :varchar, size: 30
      column :ht_item3, :varchar, size: 30
      column :ht_item4, :varchar, size: 30
      column :ht_item5, :varchar, size: 30
      column :ht_item6, :varchar, size: 30
      column :ht_item7, :varchar, size: 30
      column :ht_item8, :varchar, size: 30
      column :ht_item9, :varchar, size: 30
      column :ht_item10, :varchar, size: 30
      column :ht_len1, :integer
      column :ht_len2, :integer
      column :ht_len3, :integer
      column :ht_len4, :integer
      column :ht_len5, :integer
      column :ht_len6, :integer
      column :ht_len7, :integer
      column :ht_len8, :integer
      column :ht_len9, :integer
      column :ht_len10, :integer
      column :ht_exp1, :date
      column :ht_exp2, :date
      column :ht_exp3, :date
      column :ht_exp4, :date
      column :ht_exp5, :date
      column :ht_exp6, :date
      column :ht_exp7, :date
      column :ht_exp8, :date
      column :ht_exp9, :date
      column :ht_exp10, :date
      column :ht_service, :text
      column :ht_c, :float
      column :ht_mn, :float
      column :ht_p, :float
      column :ht_s, :float
      column :ht_si, :float
      column :ht_pb, :float
      column :ht_cu, :float
      column :ht_ni, :float
      column :ht_cr, :float
      column :ht_mo, :float
      column :ht_v, :float
      column :ht_tensile, :varchar, size: 8
      column :ht_yield, :float
      column :ht_enlong, :float
      column :ht_reducti, :float
      column :ht_temp, :float
      column :ht_hardnes, :float
      column :ht_al, :float
      column :ht_fe, :float
      column :ht_sn, :float
      column :ht_zn, :float
      column :ht_specifi, :text
      column :ht_treatme, :varchar, size: 30
      column :ht_treatm2, :varchar, size: 30
      column :ht_treatm3, :varchar, size: 30
      column :ht_treatm4, :varchar, size: 30
      column :ht_treatm5, :varchar, size: 30
      column :ht_temp1, :integer
      column :ht_temp2, :integer
      column :ht_temp3, :integer
      column :ht_temp4, :integer
      column :ht_temp5, :integer
      column :ht_time1, :integer
      column :ht_time2, :integer
      column :ht_time3, :integer
      column :ht_time4, :integer
      column :ht_time5, :integer
      column :ht_media1, :varchar, size: 20
      column :ht_media2, :varchar, size: 20
      column :ht_media3, :varchar, size: 20
      column :ht_media4, :varchar, size: 20
      column :ht_media5, :varchar, size: 20
      column :ht_grainsi, :varchar, size: 10
      column :ht_grain, :varchar, size: 10
      column :ht_source, :text
      column :ht_conditi, :varchar, size: 30
      column :ht_image_p, :varchar, size: 60
      column :ht_image_2, :varchar, size: 60
      column :ht_c_or_f_, :varchar, size: 1
      column :ht_c_or_f2, :varchar, size: 1
      column :ht_c_or_f3, :varchar, size: 1
      column :ht_c_or_f4, :varchar, size: 1
      column :ht_c_or_f5, :varchar, size: 1
      column :ht_fg_size, :float
      column :ht_shape_c, :varchar, size: 7
      column :ht_grade, :varchar, size: 6
      column :ht_hardtyp, :varchar, size: 3
      column :ht_tensil2, :varchar, size: 8
      column :ht_yield2, :float
      column :ht_enlong2, :float
      column :ht_reduct2, :float
      column :ht_hardne2, :float
      column :ht_tempera, :float
      column :ht_grains2, :varchar, size: 10
      column :ht_grain2, :varchar, size: 10
      column :ht_hardty2, :varchar, size: 3
      column :ht_label1, :varchar, size: 20
      column :ht_label2, :varchar, size: 20
      column :ht_label3, :varchar, size: 20
      column :ht_label4, :varchar, size: 20
      column :ht_label5, :varchar, size: 20
      column :ht_element, :float
      column :ht_elemen2, :float
      column :ht_elemen3, :float
      column :ht_elemen4, :float
      column :ht_elemen5, :float
    end
  end
end
