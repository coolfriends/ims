# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:shifts) do
      column :sf_code, :varchar, size: 2
      column :sf_desc, :varchar, size: 40
      column :sf_shift_s, :varchar, size: 8
      column :sf_shift_e, :varchar, size: 8
      column :sf_shift_t, :float
      column :sf_group, :varchar, size: 1
      column :sf_start_e, :varchar, size: 8
      column :sf_start_l, :varchar, size: 8
      column :sf_end_ear, :varchar, size: 8
      column :sf_end_lat, :varchar, size: 8
      column :sf_daily_o, :float
      column :sf_daily_d, :float
      column :sf_weekly_, :float
      column :sf_weekly2, :float
      column :sf_lunch_s, :varchar, size: 8
      column :sf_lunch_e, :varchar, size: 8
      column :sf_break1_, :varchar, size: 8
      column :sf_break12, :varchar, size: 8
      column :sf_break2_, :varchar, size: 8
      column :sf_break22, :varchar, size: 8
      column :sf_break3_, :varchar, size: 8
      column :sf_break32, :varchar, size: 8
      column :sf_break4_, :varchar, size: 8
      column :sf_break42, :varchar, size: 8
      column :sf_break5_, :varchar, size: 8
      column :sf_break52, :varchar, size: 8
      column :sf_break13, :varchar, size: 2
      column :sf_break23, :varchar, size: 2
      column :sf_break33, :varchar, size: 2
      column :sf_break43, :varchar, size: 2
      column :sf_break53, :varchar, size: 2
      column :sf_r_lim, :integer
      column :sf_min_lun, :float
      column :sf_auto_lu, :boolean
      column :sf_mon, :boolean
      column :sf_tue, :boolean
      column :sf_wed, :boolean
      column :sf_thu, :boolean
      column :sf_fri, :boolean
      column :sf_sat, :boolean
      column :sf_sun, :boolean
      column :sf_hol, :boolean
      column :sf_mon_rat, :varchar, size: 1
      column :sf_tue_rat, :varchar, size: 1
      column :sf_wed_rat, :varchar, size: 1
      column :sf_thu_rat, :varchar, size: 1
      column :sf_fri_rat, :varchar, size: 1
      column :sf_sat_rat, :varchar, size: 1
      column :sf_sun_rat, :varchar, size: 1
      column :sf_hol_rat, :varchar, size: 1
      column :sf_inactiv, :boolean
      column :sf_lunch_t, :boolean
      column :sf_lunch_j, :boolean
      column :sf_biweekl, :boolean
      column :sf_biweek2, :float
      column :sf_biweek3, :float
      column :sf_pr_id_1, :varchar, size: 10
      column :sf_pr_id_2, :varchar, size: 10
      column :sf_sun_ot, :float
      column :sf_sun_dot, :float
      column :sf_mon_ot, :float
      column :sf_mon_dot, :float
      column :sf_tue_ot, :float
      column :sf_tue_dot, :float
      column :sf_wed_ot, :float
      column :sf_wed_dot, :float
      column :sf_thu_ot, :float
      column :sf_thu_dot, :float
      column :sf_fri_ot, :float
      column :sf_fri_dot, :float
      column :sf_sat_ot, :float
      column :sf_sat_dot, :float
      column :sf_hol_ot, :float
      column :sf_hol_dot, :float
      column :sf_mon_sta, :varchar, size: 8
      column :sf_tue_sta, :varchar, size: 8
      column :sf_wed_sta, :varchar, size: 8
      column :sf_thu_sta, :varchar, size: 8
      column :sf_fri_sta, :varchar, size: 8
      column :sf_sat_sta, :varchar, size: 8
      column :sf_sun_sta, :varchar, size: 8
      column :sf_hol_sta, :varchar, size: 8
      column :sf_mon_end, :varchar, size: 8
      column :sf_tue_end, :varchar, size: 8
      column :sf_wed_end, :varchar, size: 8
      column :sf_thu_end, :varchar, size: 8
      column :sf_fri_end, :varchar, size: 8
      column :sf_sat_end, :varchar, size: 8
      column :sf_sun_end, :varchar, size: 8
      column :sf_hol_end, :varchar, size: 8
      column :sf_grace_s, :float
      column :sf_grace_2, :float
      column :sf_grace_e, :float
      column :sf_grace_3, :float
      column :sf_grace_l, :float
      column :sf_nightsh, :boolean
    end
  end
end
