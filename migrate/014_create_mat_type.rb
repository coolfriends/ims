Sequel.migration do
  change do
     create_table(:mat_type) do
      column :ma_mat_cod, :varchar, :size => 6
      column :ma_mat_nam, :varchar, :size => 30
      column :ma_conv_fa, :float
      column :ma_sfm, :float
      column :ma_alloy_c, :float
      column :ma_resin, :boolean
      column :ma_cpg, :float
      column :ma_bo_time, :float
      column :ma_mix_tem, :varchar, :size => 3
      column :ma_mix_tim, :float
      column :ma_resin_t, :varchar, :size => 3
      column :ma_cat_tem, :varchar, :size => 3
      column :ma_cure_ti, :integer
      column :ma_cure_te, :varchar, :size => 3
      column :ma_pail_si, :varchar, :size => 20
      column :ma_pails_p, :integer
      column :ma_duro, :varchar, :size => 3
      column :ma_duro_lo, :varchar, :size => 3
      column :ma_duro_hi, :varchar, :size => 3
      column :ma_rgb, :integer
      column :mt_c_min, :float
      column :mt_c_max, :float
      column :mt_mn_min, :float
      column :mt_mn_max, :float
      column :mt_p_min, :float
      column :mt_p_max, :float
      column :mt_s_min, :float
      column :mt_s_max, :float
      column :mt_si_min, :float
      column :mt_si_max, :float
      column :mt_pb_min, :float
      column :mt_pb_max, :float
      column :mt_ni_min, :float
      column :mt_ni_max, :float
      column :mt_cr_min, :float
      column :mt_cr_max, :float
      column :mt_mo_min, :float
      column :mt_mo_max, :float
      column :mt_cu_min, :float
      column :mt_cu_max, :float
      column :mt_v_min, :float
      column :mt_v_max, :float
      column :mt_tensile, :float
      column :mt_tensil2, :float
      column :mt_yield_m, :float
      column :mt_yield_2, :float
      column :mt_enlong_, :float
      column :mt_enlong2, :float
      column :mt_reducti, :float
      column :mt_reduct2, :float
      column :mt_hardnes, :float
      column :mt_hardne2, :float
      column :mt_temp_mi, :float
      column :mt_temp_ma, :float
      column :mt_al_min, :float
      column :mt_al_max, :float
      column :mt_fe_min, :float
      column :mt_fe_max, :float
      column :mt_sn_min, :float
      column :mt_sn_max, :float
      column :mt_zn_min, :float
      column :mt_zn_max, :float
      column :mt_hide, :boolean
      column :ma_specifi, :varchar, :size => 30
      column :ma_grade, :varchar, :size => 6
    end
  end
end
