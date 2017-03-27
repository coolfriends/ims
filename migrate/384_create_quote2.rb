# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:quote2) do
      column :q2_quote_n, :varchar, size: 15
      column :q2_lastop, :integer
      column :q2_tsu, :float
      column :q2_tmc, :float
      column :q2_tsmc_1, :float
      column :q2_tsmc_2, :float
      column :q2_tsmc_3, :float
      column :q2_tsmc_4, :float
      column :q2_tsmc_5, :float
      column :q2_tsmc_6, :float
      column :q2_tsmc_7, :float
      column :q2_tsmc_8, :float
      column :q2_tsmc_9, :float
      column :q2_tsmc_10, :float
      column :q2_mcpu_1, :float
      column :q2_mcpu_2, :float
      column :q2_mcpu_3, :float
      column :q2_mcpu_4, :float
      column :q2_mcpu_5, :float
      column :q2_mcpu_6, :float
      column :q2_mcpu_7, :float
      column :q2_mcpu_8, :float
      column :q2_mcpu_9, :float
      column :q2_mcpu_10, :float
      column :q2_htc_1, :float
      column :q2_htc_2, :float
      column :q2_htc_3, :float
      column :q2_htc_4, :float
      column :q2_htc_5, :float
      column :q2_htc_6, :float
      column :q2_htc_7, :float
      column :q2_htc_8, :float
      column :q2_htc_9, :float
      column :q2_htc_10, :float
      column :q2_pc_1, :float
      column :q2_pc_2, :float
      column :q2_pc_3, :float
      column :q2_pc_4, :float
      column :q2_pc_5, :float
      column :q2_pc_6, :float
      column :q2_pc_7, :float
      column :q2_pc_8, :float
      column :q2_pc_9, :float
      column :q2_pc_10, :float
      column :q2_tc_1, :float
      column :q2_tc_2, :float
      column :q2_tc_3, :float
      column :q2_tc_4, :float
      column :q2_tc_5, :float
      column :q2_tc_6, :float
      column :q2_tc_7, :float
      column :q2_tc_8, :float
      column :q2_tc_9, :float
      column :q2_tc_10, :float
      column :q2_mc_1, :float
      column :q2_mc_2, :float
      column :q2_mc_3, :float
      column :q2_mc_4, :float
      column :q2_mc_5, :float
      column :q2_mc_6, :float
      column :q2_mc_7, :float
      column :q2_mc_8, :float
      column :q2_mc_9, :float
      column :q2_mc_10, :float
      column :q2_mc1, :float
      column :q2_mc2, :float
      column :q2_mc3, :float
      column :q2_mc4, :float
      column :q2_mc5, :float
      column :q2_mc6, :float
      column :q2_mc7, :float
      column :q2_mc8, :float
      column :q2_mc9, :float
      column :q2_mc10, :float
      column :q2_tsu1, :float
      column :q2_tsu2, :float
      column :q2_tsu3, :float
      column :q2_tsu4, :float
      column :q2_tsu5, :float
      column :q2_tsu6, :float
      column :q2_tsu7, :float
      column :q2_tsu8, :float
      column :q2_tsu9, :float
      column :q2_tsu10, :float
      column :q2_sumu1, :integer
      column :q2_sumu2, :integer
      column :q2_sumu3, :integer
      column :q2_sumu4, :integer
      column :q2_sumu5, :integer
      column :q2_sumu6, :integer
      column :q2_sumu7, :integer
      column :q2_sumu8, :integer
      column :q2_sumu9, :integer
      column :q2_sumu10, :integer
      column :q2_tmc1, :float
      column :q2_tmc2, :float
      column :q2_tmc3, :float
      column :q2_tmc4, :float
      column :q2_tmc5, :float
      column :q2_tmc6, :float
      column :q2_tmc7, :float
      column :q2_tmc8, :float
      column :q2_tmc9, :float
      column :q2_tmc10, :float
      column :q2_ov1, :float
      column :q2_ov2, :float
      column :q2_ov3, :float
      column :q2_ov4, :float
      column :q2_ov5, :float
      column :q2_ov6, :float
      column :q2_ov7, :float
      column :q2_ov8, :float
      column :q2_ov9, :float
      column :q2_ov10, :float
      column :q2_ovmu1, :integer
      column :q2_ovmu2, :integer
      column :q2_ovmu3, :integer
      column :q2_ovmu4, :integer
      column :q2_ovmu5, :integer
      column :q2_ovmu6, :integer
      column :q2_ovmu7, :integer
      column :q2_ovmu8, :integer
      column :q2_ovmu9, :integer
      column :q2_ovmu10, :integer
      column :q2_gtmc1, :float
      column :q2_gtmc2, :float
      column :q2_gtmc3, :float
      column :q2_gtmc4, :float
      column :q2_gtmc5, :float
      column :q2_gtmc6, :float
      column :q2_gtmc7, :float
      column :q2_gtmc8, :float
      column :q2_gtmc9, :float
      column :q2_gtmc10, :float
      column :q2_misc1, :float
      column :q2_misc2, :float
      column :q2_misc3, :float
      column :q2_misc4, :float
      column :q2_misc5, :float
      column :q2_misc6, :float
      column :q2_misc7, :float
      column :q2_misc8, :float
      column :q2_misc9, :float
      column :q2_misc10, :float
      column :q2_gt1, :float
      column :q2_gt2, :float
      column :q2_gt3, :float
      column :q2_gt4, :float
      column :q2_gt5, :float
      column :q2_gt6, :float
      column :q2_gt7, :float
      column :q2_gt8, :float
      column :q2_gt9, :float
      column :q2_gt10, :float
      column :q2_sc1, :float
      column :q2_sc2, :float
      column :q2_sc3, :float
      column :q2_sc4, :float
      column :q2_sc5, :float
      column :q2_sc6, :float
      column :q2_sc7, :float
      column :q2_sc8, :float
      column :q2_sc9, :float
      column :q2_sc10, :float
      column :q2_fcpu1, :float
      column :q2_fcpu2, :float
      column :q2_fcpu3, :float
      column :q2_fcpu4, :float
      column :q2_fcpu5, :float
      column :q2_fcpu6, :float
      column :q2_fcpu7, :float
      column :q2_fcpu8, :float
      column :q2_fcpu9, :float
      column :q2_fcpu10, :float
      column :q2_tottc, :float
      column :q2_totgc, :float
      column :q2_totcc, :float
      column :q2_totmc, :float
      column :q2_fenote, :text
      column :q2_mannote, :text
      column :q2_salespe, :float
      column :q2_salesp2, :varchar, size: 5
      column :q2_ht_note, :text
      column :q2_pl_note, :text
      column :q2_no_quot, :varchar, size: 1
      column :q2_induct_, :varchar, size: 1
      column :q2_shard_s, :varchar, size: 25
      column :q2_toteff_, :varchar, size: 1
      column :q2_case_s, :varchar, size: 10
      column :q2_core_s, :varchar, size: 10
      column :q2_plen_s, :varchar, size: 10
      column :q2_note_s, :varchar, size: 40
      column :q2_inc_sub, :varchar, size: 1
      column :q2_misc_no, :text
      column :q2_overrid, :boolean
      column :q2_gtmat1, :float
      column :q2_gtmat2, :float
      column :q2_gtmat3, :float
      column :q2_gtmat4, :float
      column :q2_gtmat5, :float
      column :q2_gtmat6, :float
      column :q2_gtmat7, :float
      column :q2_gtmat8, :float
      column :q2_gtmat9, :float
      column :q2_gtmat10, :float
      column :q2_decimal, :integer
      column :q2_app_by, :varchar, size: 25
      column :q2_ins_by, :varchar, size: 25
      column :q2_shard_i, :varchar, size: 15
      column :q2_note_i, :text
      column :q2_lot, :varchar, size: 20
      column :q2_case_i, :varchar, size: 10
      column :q2_plen_i, :varchar, size: 10
      column :q2_matmu1, :integer
      column :q2_matmu2, :integer
      column :q2_matmu3, :integer
      column :q2_matmu4, :integer
      column :q2_matmu5, :integer
      column :q2_matmu6, :integer
      column :q2_matmu7, :integer
      column :q2_matmu8, :integer
      column :q2_matmu9, :integer
      column :q2_matmu10, :integer
      column :q2_exclcom, :boolean
      column :q2_cfcpu1, :float
      column :q2_cfcpu2, :float
      column :q2_cfcpu3, :float
      column :q2_cfcpu4, :float
      column :q2_cfcpu5, :float
      column :q2_cfcpu6, :float
      column :q2_cfcpu7, :float
      column :q2_cfcpu8, :float
      column :q2_cfcpu9, :float
      column :q2_cfcpu10, :float
      column :q2_excsetu, :boolean
      column :q2_salesp3, :varchar, size: 5
      column :q2_salesp4, :float
      column :q2_excmatl, :boolean
      column :q2_ptools, :float
      column :q2_inc_mis, :boolean
      column :q2_excplat, :boolean
      column :q2_gm, :boolean
      column :q2_qtyuom, :varchar, size: 4
      column :q2_apr1, :float
      column :q2_apr2, :float
      column :q2_apr3, :float
      column :q2_apr4, :float
      column :q2_apr5, :float
      column :q2_apr6, :float
      column :q2_apr7, :float
      column :q2_apr8, :float
      column :q2_apr9, :float
      column :q2_apr10, :float
    end
  end
end
