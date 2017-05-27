# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Ac1099(models.Model):
    sc_id = models.CharField(max_length=10, blank=True, null=True)
    sc_type = models.CharField(max_length=1, blank=True, null=True)
    sc_supp_co = models.CharField(max_length=6, blank=True, null=True)
    sc_year = models.IntegerField(blank=True, null=True)
    sc_fedid = models.CharField(max_length=35, blank=True, null=True)
    sc_name = models.CharField(max_length=35, blank=True, null=True)
    sc_address = models.CharField(max_length=35, blank=True, null=True)
    sc_addres2 = models.CharField(max_length=35, blank=True, null=True)
    sc_city = models.CharField(max_length=15, blank=True, null=True)
    sc_state = models.CharField(max_length=3, blank=True, null=True)
    sc_zip = models.CharField(max_length=10, blank=True, null=True)
    sc_phone = models.CharField(max_length=8, blank=True, null=True)
    sc_supp_ac = models.CharField(max_length=12, blank=True, null=True)
    sc_2_nd_tin = models.NullBooleanField()
    sc_rents = models.FloatField(blank=True, null=True)
    sc_royalti = models.FloatField(blank=True, null=True)
    sc_other_i = models.FloatField(blank=True, null=True)
    sc_fit_wit = models.FloatField(blank=True, null=True)
    sc_fishing = models.FloatField(blank=True, null=True)
    sc_medical = models.FloatField(blank=True, null=True)
    sc_nonempl = models.FloatField(blank=True, null=True)
    sc_substit = models.FloatField(blank=True, null=True)
    sc_crop_in = models.FloatField(blank=True, null=True)
    sc_sit_wit = models.FloatField(blank=True, null=True)
    sc_state_n = models.CharField(max_length=15, blank=True, null=True)
    sc_box_13 = models.FloatField(blank=True, null=True)
    sc_resale = models.NullBooleanField()
    sc_void = models.NullBooleanField()
    sc_correct = models.NullBooleanField()
    sc_egp_pay = models.FloatField(blank=True, null=True)
    sc_attorne = models.FloatField(blank=True, null=True)
    sc_st1_wit = models.FloatField(blank=True, null=True)
    sc_st1_inc = models.FloatField(blank=True, null=True)
    sc_st1_sta = models.CharField(max_length=15, blank=True, null=True)
    sc_st2_wit = models.FloatField(blank=True, null=True)
    sc_st2_inc = models.FloatField(blank=True, null=True)
    sc_st2_sta = models.CharField(max_length=15, blank=True, null=True)
    sc_other_1 = models.CharField(max_length=35, blank=True, null=True)
    sc_other_2 = models.CharField(max_length=35, blank=True, null=True)
    sc_1099_bo = models.CharField(max_length=2, blank=True, null=True)
    sc_total_1 = models.IntegerField(blank=True, null=True)
    sc_final_r = models.NullBooleanField()
    sc_contact = models.CharField(max_length=35, blank=True, null=True)
    sc_email = models.CharField(max_length=35, blank=True, null=True)
    sc_phone_a = models.CharField(max_length=3, blank=True, null=True)
    sc_fax = models.CharField(max_length=8, blank=True, null=True)
    sc_fax_ac = models.CharField(max_length=3, blank=True, null=True)
    sc_soc_sec = models.CharField(max_length=11, blank=True, null=True)
    sc_addres3 = models.CharField(max_length=35, blank=True, null=True)
    sc_409_a_de = models.FloatField(blank=True, null=True)
    sc_409_a_in = models.FloatField(blank=True, null=True)
    sc_source = models.CharField(max_length=1, blank=True, null=True)
    sc_foreign = models.FloatField(blank=True, null=True)
    sc_foreig2 = models.CharField(max_length=12, blank=True, null=True)
    sc_fatca_f = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ac_1099'


class AcAdept(models.Model):
    dp_code = models.CharField(max_length=2, blank=True, null=True)
    dp_desc = models.CharField(max_length=40, blank=True, null=True)
    dp_acct_su = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_adept'


class AcAdiv(models.Model):
    dv_code = models.CharField(max_length=2, blank=True, null=True)
    dv_desc = models.CharField(max_length=40, blank=True, null=True)
    dv_acct_su = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_adiv'


class AcApdst(models.Model):
    ad_id = models.CharField(max_length=10, blank=True, null=True)
    ad_ap_id = models.CharField(max_length=10, blank=True, null=True)
    ad_account = models.CharField(max_length=12, blank=True, null=True)
    ad_item_re = models.CharField(max_length=30, blank=True, null=True)
    ad_desc = models.CharField(max_length=30, blank=True, null=True)
    ad_qty_rec = models.FloatField(blank=True, null=True)
    ad_unit_co = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ad_po_num = models.CharField(max_length=7, blank=True, null=True)
    ad_line_nu = models.IntegerField(blank=True, null=True)
    ad_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    ad_ext_cos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ad_dist_co = models.CharField(max_length=2, blank=True, null=True)
    ad_gl_id = models.CharField(max_length=10, blank=True, null=True)
    ad_unit_cu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ad_ext_cur = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ad_tran_ty = models.CharField(max_length=2, blank=True, null=True)
    ad_te = models.CharField(max_length=1, blank=True, null=True)
    ad_po_line = models.IntegerField(blank=True, null=True)
    ad_st_id = models.CharField(max_length=10, blank=True, null=True)
    ad_tax_rat = models.FloatField(blank=True, null=True)
    ad_st_tot_field = models.DecimalField(db_column='ad_st_tot_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    ad_st_ex_s = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ad_st_non_field = models.DecimalField(db_column='ad_st_non_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    ad_st_tax_field = models.DecimalField(db_column='ad_st_tax_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    ad_st_non2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ad_st_tax2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ad_st_tax3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ad_st_tot2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ad_overrid = models.NullBooleanField()
    ad_excl_di = models.NullBooleanField()
    ad_mn_id = models.CharField(max_length=10, blank=True, null=True)
    ad_dm_ap_i = models.CharField(max_length=10, blank=True, null=True)
    ad_dm_ad_i = models.CharField(max_length=10, blank=True, null=True)
    ad_dm_po_n = models.CharField(max_length=7, blank=True, null=True)
    ad_dm_po_l = models.IntegerField(blank=True, null=True)
    ad_cost_ov = models.NullBooleanField()
    ad_dm_rec_field = models.IntegerField(db_column='ad_dm_rec_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ad_1099 = models.NullBooleanField()
    ad_lock = models.NullBooleanField()
    ad_order_n = models.CharField(max_length=12, blank=True, null=True)
    ad_distrib = models.NullBooleanField()
    ad_entry_d = models.DateField(blank=True, null=True)
    ad_amortiz = models.NullBooleanField()
    ad_amort_a = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ad_lot_not = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_apdst'


class AcApinv(models.Model):
    ap_id = models.CharField(max_length=10, blank=True, null=True)
    ap_ca_code = models.CharField(max_length=12, blank=True, null=True)
    ap_inv_num = models.CharField(max_length=30, blank=True, null=True)
    ap_inv_dat = models.DateField(blank=True, null=True)
    ap_supp_co = models.CharField(max_length=6, blank=True, null=True)
    ap_type = models.CharField(max_length=1, blank=True, null=True)
    ap_desc = models.CharField(max_length=30, blank=True, null=True)
    ap_longdes = models.TextField(blank=True, null=True)
    ap_status = models.CharField(max_length=1, blank=True, null=True)
    ap_terms = models.CharField(max_length=20, blank=True, null=True)
    ap_pay_dat = models.DateField(blank=True, null=True)
    ap_dc_date = models.DateField(blank=True, null=True)
    ap_inv_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_inv_bal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_ch_num = models.CharField(max_length=10, blank=True, null=True)
    ap_ch_date = models.DateField(blank=True, null=True)
    ap_cash_ap = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_lo_code = models.CharField(max_length=10, blank=True, null=True)
    ap_user = models.CharField(max_length=5, blank=True, null=True)
    ap_entry_d = models.DateField(blank=True, null=True)
    ap_post = models.NullBooleanField()
    ap_post_da = models.DateField(blank=True, null=True)
    ap_print_d = models.DateField(blank=True, null=True)
    ap_exp_dat = models.DateField(blank=True, null=True)
    ap_gl_id = models.CharField(max_length=10, blank=True, null=True)
    ap_startmo = models.NullBooleanField()
    ap_reconci = models.NullBooleanField()
    ap_marked = models.NullBooleanField()
    ap_st_id_1 = models.CharField(max_length=10, blank=True, null=True)
    ap_st_id_2 = models.CharField(max_length=10, blank=True, null=True)
    ap_stax_id = models.CharField(max_length=25, blank=True, null=True)
    ap_tax_exe = models.NullBooleanField()
    ap_exempt_field = models.CharField(db_column='ap_exempt_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ap_net_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_taxes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    ap_cur_rat = models.FloatField(blank=True, null=True)
    ap_net_cur = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_tax_cur = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_inv_cur = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_po_num = models.CharField(max_length=7, blank=True, null=True)
    ap_exclude = models.NullBooleanField()
    ap_deliver = models.DateField(blank=True, null=True)
    ap_user_id = models.CharField(max_length=5, blank=True, null=True)
    ap_lm_user = models.CharField(max_length=5, blank=True, null=True)
    ap_lm_date = models.DateTimeField(blank=True, null=True)
    ap_cc_deta = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ac_apinv'


class AcAprds(models.Model):
    cp_year = models.CharField(max_length=4, blank=True, null=True)
    cp_period = models.CharField(max_length=2, blank=True, null=True)
    cp_exclude = models.NullBooleanField()
    cp_start_d = models.DateField(blank=True, null=True)
    cp_end_dat = models.DateField(blank=True, null=True)
    cp_desc = models.CharField(max_length=10, blank=True, null=True)
    cp_lock_do = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ac_aprds'


class AcAprdt(models.Model):
    pd_id = models.CharField(max_length=10, blank=True, null=True)
    pd_pr_id = models.CharField(max_length=10, blank=True, null=True)
    pd_account = models.CharField(max_length=12, blank=True, null=True)
    pd_item_re = models.CharField(max_length=10, blank=True, null=True)
    pd_desc = models.CharField(max_length=30, blank=True, null=True)
    pd_qty_rec = models.IntegerField(blank=True, null=True)
    pd_unit_co = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pd_line_nu = models.IntegerField(blank=True, null=True)
    pd_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    pd_ext_cos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pd_dist_co = models.CharField(max_length=2, blank=True, null=True)
    pd_gl_id = models.CharField(max_length=10, blank=True, null=True)
    pd_tran_ty = models.CharField(max_length=2, blank=True, null=True)
    pd_te = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_aprdt'


class AcAprec(models.Model):
    pr_id = models.CharField(max_length=10, blank=True, null=True)
    pr_ca_code = models.CharField(max_length=12, blank=True, null=True)
    pr_supp_co = models.CharField(max_length=6, blank=True, null=True)
    pr_type = models.CharField(max_length=1, blank=True, null=True)
    pr_desc = models.CharField(max_length=30, blank=True, null=True)
    pr_longdes = models.TextField(blank=True, null=True)
    pr_status = models.CharField(max_length=1, blank=True, null=True)
    pr_terms = models.CharField(max_length=20, blank=True, null=True)
    pr_inv_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pr_inv_bal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pr_ch_num = models.CharField(max_length=10, blank=True, null=True)
    pr_cash_ap = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pr_lo_code = models.CharField(max_length=10, blank=True, null=True)
    pr_user = models.CharField(max_length=5, blank=True, null=True)
    pr_gl_id = models.CharField(max_length=10, blank=True, null=True)
    pr_last_in = models.DateField(blank=True, null=True)
    pr_freq = models.CharField(max_length=1, blank=True, null=True)
    pr_selind = models.CharField(max_length=1, blank=True, null=True)
    pr_next = models.DateField(blank=True, null=True)
    pr_dom = models.IntegerField(blank=True, null=True)
    pr_day = models.IntegerField(blank=True, null=True)
    pr_inv_num = models.CharField(max_length=30, blank=True, null=True)
    pr_post = models.NullBooleanField()
    pr_net_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pr_taxes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_aprec'


class AcArrdt(models.Model):
    rd_rr_id = models.CharField(max_length=10, blank=True, null=True)
    rd_line_nu = models.IntegerField(blank=True, null=True)
    rd_tran_ty = models.CharField(max_length=2, blank=True, null=True)
    rd_invent_field = models.CharField(db_column='rd_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    rd_qty_ord = models.IntegerField(blank=True, null=True)
    rd_ship_co = models.CharField(max_length=8, blank=True, null=True)
    rd_desc = models.CharField(max_length=30, blank=True, null=True)
    rd_prod_co = models.CharField(max_length=2, blank=True, null=True)
    rd_qty_shi = models.IntegerField(blank=True, null=True)
    rd_qty_bo = models.IntegerField(blank=True, null=True)
    rd_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    rd_unit_pr = models.FloatField(blank=True, null=True)
    rd_discoun = models.FloatField(blank=True, null=True)
    rd_disc_pr = models.FloatField(blank=True, null=True)
    rd_ext_pri = models.FloatField(blank=True, null=True)
    rd_te = models.CharField(max_length=1, blank=True, null=True)
    rd_note = models.TextField(blank=True, null=True)
    rd_note_fl = models.CharField(max_length=1, blank=True, null=True)
    rd_order_n = models.CharField(max_length=12, blank=True, null=True)
    rd_rel_num = models.IntegerField(blank=True, null=True)
    rd_po_num = models.CharField(max_length=15, blank=True, null=True)
    rd_rel_qty = models.IntegerField(blank=True, null=True)
    rd_sd_id = models.IntegerField(blank=True, null=True)
    rd_ar_gl_n = models.CharField(max_length=12, blank=True, null=True)
    rd_pc_gl_n = models.CharField(max_length=12, blank=True, null=True)
    rd_tax_rat = models.FloatField(blank=True, null=True)
    rd_part_nu = models.CharField(max_length=30, blank=True, null=True)
    rd_rev_num = models.CharField(max_length=3, blank=True, null=True)
    rd_pmemo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_arrdt'


class AcArrec(models.Model):
    rr_id = models.CharField(max_length=10, blank=True, null=True)
    rr_cust_co = models.CharField(max_length=6, blank=True, null=True)
    rr_ship_vi = models.CharField(max_length=20, blank=True, null=True)
    rr_net_amt = models.FloatField(blank=True, null=True)
    rr_taxes = models.FloatField(blank=True, null=True)
    rr_tot_amt = models.FloatField(blank=True, null=True)
    rr_comp_na = models.CharField(max_length=33, blank=True, null=True)
    rr_address = models.CharField(max_length=33, blank=True, null=True)
    rr_addres2 = models.CharField(max_length=33, blank=True, null=True)
    rr_addres3 = models.CharField(max_length=33, blank=True, null=True)
    rr_ship_co = models.CharField(max_length=8, blank=True, null=True)
    rr_contact = models.CharField(max_length=25, blank=True, null=True)
    rr_emp_id = models.CharField(max_length=5, blank=True, null=True)
    rr_pay_ter = models.CharField(max_length=20, blank=True, null=True)
    rr_lo_code = models.CharField(max_length=10, blank=True, null=True)
    rr_type = models.CharField(max_length=1, blank=True, null=True)
    rr_gl_num = models.CharField(max_length=12, blank=True, null=True)
    rr_freq = models.CharField(max_length=1, blank=True, null=True)
    rr_dom = models.IntegerField(blank=True, null=True)
    rr_day = models.IntegerField(blank=True, null=True)
    rr_last_in = models.DateField(blank=True, null=True)
    rr_next = models.DateField(blank=True, null=True)
    rr_desc = models.CharField(max_length=35, blank=True, null=True)
    rr_selind = models.CharField(max_length=1, blank=True, null=True)
    rr_inv_num = models.CharField(max_length=7, blank=True, null=True)
    rr_post = models.NullBooleanField()
    rr_po_num = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_arrec'


class AcBal(models.Model):
    cb_number = models.CharField(max_length=12, blank=True, null=True)
    cb_year = models.CharField(max_length=4, blank=True, null=True)
    cb_bal_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cb_bal_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_bal'


class AcCdde(models.Model):
    dd_id = models.CharField(max_length=10, blank=True, null=True)
    dd_mn_id = models.CharField(max_length=10, blank=True, null=True)
    dd_ap_id = models.CharField(max_length=10, blank=True, null=True)
    dd_ap_inv_field = models.CharField(db_column='dd_ap_inv_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    dd_dr_ca_c = models.CharField(max_length=12, blank=True, null=True)
    dd_dr_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dd_cr_ca_c = models.CharField(max_length=12, blank=True, null=True)
    dd_cr_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dd_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dd_dr_gl_i = models.CharField(max_length=10, blank=True, null=True)
    dd_cr_gl_i = models.CharField(max_length=10, blank=True, null=True)
    dd_type = models.CharField(max_length=1, blank=True, null=True)
    dd_ca_code = models.CharField(max_length=12, blank=True, null=True)
    dd_gl_id = models.CharField(max_length=10, blank=True, null=True)
    dd_apply_d = models.DateField(blank=True, null=True)
    dd_cur_amo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dd_status = models.CharField(max_length=1, blank=True, null=True)
    dd_marked = models.NullBooleanField()
    dd_dm_mn_i = models.CharField(max_length=10, blank=True, null=True)
    dd_cm_mr_i = models.CharField(max_length=10, blank=True, null=True)
    dd_sc_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_cdde'


class AcCdmn(models.Model):
    mn_id = models.CharField(max_length=10, blank=True, null=True)
    mn_type = models.CharField(max_length=1, blank=True, null=True)
    mn_ca_code = models.CharField(max_length=12, blank=True, null=True)
    mn_date = models.DateField(blank=True, null=True)
    mn_cknum = models.CharField(max_length=10, blank=True, null=True)
    mn_supp_co = models.CharField(max_length=6, blank=True, null=True)
    mn_supp_na = models.CharField(max_length=35, blank=True, null=True)
    mn_rem_add = models.TextField(blank=True, null=True)
    mn_dr_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_cr_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_user = models.CharField(max_length=5, blank=True, null=True)
    mn_entry_d = models.DateField(blank=True, null=True)
    mn_reconci = models.CharField(max_length=1, blank=True, null=True)
    mn_post = models.NullBooleanField()
    mn_post_da = models.DateField(blank=True, null=True)
    mn_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_gl_id = models.CharField(max_length=10, blank=True, null=True)
    mn_entry_t = models.CharField(max_length=1, blank=True, null=True)
    mn_referen = models.CharField(max_length=50, blank=True, null=True)
    mn_status = models.CharField(max_length=1, blank=True, null=True)
    mn_ca_cod2 = models.CharField(max_length=12, blank=True, null=True)
    mn_print_d = models.DateField(blank=True, null=True)
    mn_gl_id_2 = models.CharField(max_length=10, blank=True, null=True)
    mn_oc_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_oc_bala = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_mn_id = models.CharField(max_length=10, blank=True, null=True)
    mn_rg_id = models.CharField(max_length=10, blank=True, null=True)
    mn_marked = models.NullBooleanField()
    mn_1099 = models.NullBooleanField()
    mn_new_for = models.NullBooleanField()
    mn_st_id_1 = models.CharField(max_length=10, blank=True, null=True)
    mn_st_id_2 = models.CharField(max_length=10, blank=True, null=True)
    mn_stax_id = models.CharField(max_length=25, blank=True, null=True)
    mn_tax_exe = models.NullBooleanField()
    mn_exempt_field = models.CharField(db_column='mn_exempt_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    mn_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    mn_cur_rat = models.FloatField(blank=True, null=True)
    mn_cur = models.FloatField(blank=True, null=True)
    mn_dr_cur = models.FloatField(blank=True, null=True)
    mn_cr_cur = models.FloatField(blank=True, null=True)
    mn_ap_id = models.CharField(max_length=10, blank=True, null=True)
    mn_po_num = models.CharField(max_length=7, blank=True, null=True)
    mn_lo_code = models.CharField(max_length=10, blank=True, null=True)
    mn_number = models.CharField(max_length=30, blank=True, null=True)
    mn_1099_box = models.CharField(max_length=2, blank=True, null=True)
    mn_cur_amo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_ca_cur_field = models.CharField(db_column='mn_ca_cur_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    mn_gl_id_c = models.CharField(max_length=10, blank=True, null=True)
    mn_check_m = models.CharField(max_length=30, blank=True, null=True)
    mn_manual = models.NullBooleanField()
    mn_dm_dd_i = models.CharField(max_length=10, blank=True, null=True)
    mn_cc_supp = models.CharField(max_length=6, blank=True, null=True)
    mn_cust_co = models.CharField(max_length=6, blank=True, null=True)
    mn_rec_dat = models.DateField(blank=True, null=True)
    mn_emp_id = models.CharField(max_length=5, blank=True, null=True)
    mn_user_id = models.CharField(max_length=5, blank=True, null=True)
    mn_exclude = models.NullBooleanField()
    mn_lm_user = models.CharField(max_length=5, blank=True, null=True)
    mn_lm_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_cdmn'


class AcCdrdt(models.Model):
    dd_id = models.CharField(max_length=10, blank=True, null=True)
    dd_mn_id = models.CharField(max_length=10, blank=True, null=True)
    dd_type = models.CharField(max_length=1, blank=True, null=True)
    dd_dr_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dd_cr_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dd_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dd_dr_ca_c = models.CharField(max_length=12, blank=True, null=True)
    dd_cr_ca_c = models.CharField(max_length=12, blank=True, null=True)
    dd_ca_code = models.CharField(max_length=12, blank=True, null=True)
    dd_cur_amo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dd_discoun = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ac_cdrdt'


class AcCdrec(models.Model):
    mn_id = models.CharField(max_length=10, blank=True, null=True)
    mn_type = models.CharField(max_length=1, blank=True, null=True)
    mn_entry_t = models.CharField(max_length=1, blank=True, null=True)
    mn_frequen = models.CharField(max_length=1, blank=True, null=True)
    mn_day = models.IntegerField(blank=True, null=True)
    mn_next_da = models.DateField(blank=True, null=True)
    mn_last_da = models.DateField(blank=True, null=True)
    mn_ca_code = models.CharField(max_length=12, blank=True, null=True)
    mn_supp_co = models.CharField(max_length=6, blank=True, null=True)
    mn_supp_na = models.CharField(max_length=30, blank=True, null=True)
    mn_rem_add = models.TextField(blank=True, null=True)
    mn_dr_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_cr_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_referen = models.CharField(max_length=30, blank=True, null=True)
    mn_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    mn_ca_cur_field = models.CharField(db_column='mn_ca_cur_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    mn_manual = models.NullBooleanField()
    mn_1099 = models.NullBooleanField()
    mn_1099_box = models.CharField(max_length=2, blank=True, null=True)
    mn_check_m = models.CharField(max_length=30, blank=True, null=True)
    mn_cur_amo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_dom = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_cdrec'


class AcCfadm(models.Model):
    cf_id = models.CharField(max_length=10, blank=True, null=True)
    cf_data_pa = models.CharField(max_length=80, blank=True, null=True)
    cf_selecte = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ac_cfadm'


class AcChkac(models.Model):
    ck_ca_code = models.CharField(max_length=12, blank=True, null=True)
    ck_desc = models.CharField(max_length=35, blank=True, null=True)
    ck_acct_no = models.CharField(max_length=15, blank=True, null=True)
    ck_next_no = models.IntegerField(blank=True, null=True)
    ck_bank = models.CharField(max_length=35, blank=True, null=True)
    ck_status = models.CharField(max_length=1, blank=True, null=True)
    ck_address = models.CharField(max_length=30, blank=True, null=True)
    ck_addres2 = models.CharField(max_length=30, blank=True, null=True)
    ck_city = models.CharField(max_length=25, blank=True, null=True)
    ck_state = models.CharField(max_length=2, blank=True, null=True)
    ck_zip = models.CharField(max_length=10, blank=True, null=True)
    ck_routing = models.CharField(max_length=15, blank=True, null=True)
    ck_phone = models.CharField(max_length=20, blank=True, null=True)
    ck_bf_ca_c = models.CharField(max_length=12, blank=True, null=True)
    ck_beg_bal = models.FloatField(blank=True, null=True)
    ck_beg_dat = models.DateField(blank=True, null=True)
    ck_rec_bal = models.FloatField(blank=True, null=True)
    ck_rec_dat = models.DateField(blank=True, null=True)
    ck_ses_end = models.FloatField(blank=True, null=True)
    ck_ses_en2 = models.DateField(blank=True, null=True)
    ck_ed_next = models.IntegerField(blank=True, null=True)
    ck_payroll = models.NullBooleanField()
    ck_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    ck_ce_ca_c = models.CharField(max_length=12, blank=True, null=True)
    ck_nc_ca_c = models.CharField(max_length=12, blank=True, null=True)
    ck_ur_ca_c = models.CharField(max_length=12, blank=True, null=True)
    ck_dep_nex = models.IntegerField(blank=True, null=True)
    ck_man_nex = models.IntegerField(blank=True, null=True)
    ck_prev_ba = models.FloatField(blank=True, null=True)
    ck_prev_da = models.DateField(blank=True, null=True)
    ck_inactiv = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ac_chkac'


class AcClinc(models.Model):
    ci_id = models.CharField(max_length=10, blank=True, null=True)
    ci_cust_co = models.CharField(max_length=6, blank=True, null=True)
    ci_user_id = models.CharField(max_length=5, blank=True, null=True)
    ci_date = models.DateField(blank=True, null=True)
    ci_type = models.CharField(max_length=1, blank=True, null=True)
    ci_status = models.CharField(max_length=1, blank=True, null=True)
    ci_inv_num = models.CharField(max_length=7, blank=True, null=True)
    ci_cc_id = models.CharField(max_length=10, blank=True, null=True)
    ci_contact = models.CharField(max_length=25, blank=True, null=True)
    ci_promise = models.DateField(blank=True, null=True)
    ci_notes = models.TextField(blank=True, null=True)
    ci_cn_leve = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_clinc'


class AcClnts(models.Model):
    cn_id = models.CharField(max_length=10, blank=True, null=True)
    cn_days = models.IntegerField(blank=True, null=True)
    cn_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_clnts'


class AcCrde(models.Model):
    dr_id = models.CharField(max_length=10, blank=True, null=True)
    dr_mr_id = models.CharField(max_length=10, blank=True, null=True)
    dr_inv_num = models.CharField(max_length=7, blank=True, null=True)
    dr_referen = models.CharField(max_length=10, blank=True, null=True)
    dr_dr_ca_c = models.CharField(max_length=12, blank=True, null=True)
    dr_cr_ca_c = models.CharField(max_length=12, blank=True, null=True)
    dr_amount = models.FloatField(blank=True, null=True)
    dr_dr_amou = models.FloatField(blank=True, null=True)
    dr_cr_amou = models.FloatField(blank=True, null=True)
    dr_type = models.CharField(max_length=1, blank=True, null=True)
    dr_gl_id = models.CharField(max_length=10, blank=True, null=True)
    dr_dr_gl_i = models.CharField(max_length=10, blank=True, null=True)
    dr_cr_gl_i = models.CharField(max_length=10, blank=True, null=True)
    dr_ca_code = models.CharField(max_length=12, blank=True, null=True)
    dr_notes = models.TextField(blank=True, null=True)
    dr_apply_d = models.DateField(blank=True, null=True)
    dr_cur_amo = models.FloatField(blank=True, null=True)
    dr_cm_mr_i = models.CharField(max_length=10, blank=True, null=True)
    dr_cm_new = models.NullBooleanField()
    dr_dm_mn_i = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_crde'


class AcCrmn(models.Model):
    mr_id = models.CharField(max_length=10, blank=True, null=True)
    mr_type = models.CharField(max_length=1, blank=True, null=True)
    mr_ca_code = models.CharField(max_length=12, blank=True, null=True)
    mr_date = models.DateField(blank=True, null=True)
    mr_referen = models.CharField(max_length=30, blank=True, null=True)
    mr_cust_co = models.CharField(max_length=6, blank=True, null=True)
    mr_cust_na = models.CharField(max_length=30, blank=True, null=True)
    mr_rem_add = models.TextField(blank=True, null=True)
    mr_amount = models.FloatField(blank=True, null=True)
    mr_dr_amou = models.FloatField(blank=True, null=True)
    mr_cr_amou = models.FloatField(blank=True, null=True)
    mr_user = models.CharField(max_length=5, blank=True, null=True)
    mr_entry_d = models.DateField(blank=True, null=True)
    mr_reconci = models.CharField(max_length=1, blank=True, null=True)
    mr_post = models.NullBooleanField()
    mr_post_da = models.DateField(blank=True, null=True)
    mr_entry_t = models.CharField(max_length=1, blank=True, null=True)
    mr_gl_id = models.CharField(max_length=10, blank=True, null=True)
    mr_dep_id = models.CharField(max_length=10, blank=True, null=True)
    mr_status = models.CharField(max_length=1, blank=True, null=True)
    mr_ca_cod2 = models.CharField(max_length=12, blank=True, null=True)
    mr_gl_id_2 = models.CharField(max_length=10, blank=True, null=True)
    mr_oc_amou = models.FloatField(blank=True, null=True)
    mr_oc_bala = models.FloatField(blank=True, null=True)
    mr_mr_id = models.CharField(max_length=10, blank=True, null=True)
    mr_status_field = models.CharField(db_column='mr_status_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    mr_reconc2 = models.CharField(max_length=1, blank=True, null=True)
    mr_marked = models.NullBooleanField()
    mr_marked_field = models.NullBooleanField(db_column='mr_marked_')  # Field renamed because it ended with '_'.
    mr_ship_to = models.CharField(max_length=3, blank=True, null=True)
    mr_emp_id = models.CharField(max_length=5, blank=True, null=True)
    mr_lo_code = models.CharField(max_length=10, blank=True, null=True)
    mr_number = models.CharField(max_length=7, blank=True, null=True)
    mr_new_for = models.NullBooleanField()
    mr_st_id_1 = models.CharField(max_length=10, blank=True, null=True)
    mr_st_id_2 = models.CharField(max_length=10, blank=True, null=True)
    mr_stax_id = models.CharField(max_length=25, blank=True, null=True)
    mr_tax_exe = models.NullBooleanField()
    mr_exempt_field = models.CharField(db_column='mr_exempt_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    mr_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    mr_cur_rat = models.FloatField(blank=True, null=True)
    mr_cur = models.FloatField(blank=True, null=True)
    mr_dr_cur = models.FloatField(blank=True, null=True)
    mr_cr_cur = models.FloatField(blank=True, null=True)
    mr_inv_num = models.CharField(max_length=7, blank=True, null=True)
    mr_ship_co = models.CharField(max_length=8, blank=True, null=True)
    mr_cur_amo = models.FloatField(blank=True, null=True)
    mr_ca_cur_field = models.CharField(db_column='mr_ca_cur_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    mr_gl_id_c = models.CharField(max_length=10, blank=True, null=True)
    mr_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    mr_cm_dr_i = models.CharField(max_length=10, blank=True, null=True)
    mr_billto_field = models.CharField(db_column='mr_billto_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    mr_supp_co = models.CharField(max_length=6, blank=True, null=True)
    mr_rec_dat = models.DateField(blank=True, null=True)
    mr_rec_da2 = models.DateField(blank=True, null=True)
    mr_credit_field = models.NullBooleanField(db_column='mr_credit_')  # Field renamed because it ended with '_'.
    mr_destina = models.CharField(max_length=4, blank=True, null=True)
    mr_zero_ba = models.NullBooleanField()
    mr_lm_user = models.CharField(max_length=5, blank=True, null=True)
    mr_lm_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_crmn'


class AcCstra(models.Model):
    cr_id = models.CharField(max_length=10, blank=True, null=True)
    cr_calc = models.CharField(max_length=70, blank=True, null=True)
    cr_name = models.CharField(max_length=35, blank=True, null=True)
    cr_protect = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ac_cstra'


class AcDarap(models.Model):
    da_code = models.CharField(max_length=12, blank=True, null=True)
    da_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_darap'


class AcDeflt(models.Model):
    ap_basedt = models.DateField(blank=True, null=True)
    ap_dsctdt = models.DateField(blank=True, null=True)
    ap_discoun = models.NullBooleanField()
    ap_ck_acct = models.CharField(max_length=15, blank=True, null=True)
    ar_ck_acct = models.CharField(max_length=15, blank=True, null=True)
    ar_rec_dat = models.DateField(blank=True, null=True)
    ar_discoun = models.NullBooleanField()
    ar_deposit = models.NullBooleanField()
    ar_dep_dat = models.DateField(blank=True, null=True)
    ar_import = models.NullBooleanField()
    ar_import_field = models.CharField(db_column='ar_import_', max_length=80, blank=True, null=True)  # Field renamed because it ended with '_'.
    ap_autoapp = models.NullBooleanField()
    ec_ck_acct = models.CharField(max_length=15, blank=True, null=True)
    ec_basedt = models.DateField(blank=True, null=True)
    ec_paydt = models.DateField(blank=True, null=True)
    ec_exunpai = models.NullBooleanField()
    ap_acct_no = models.CharField(max_length=12, blank=True, null=True)
    ec_exunapp = models.NullBooleanField()
    cp_export_field = models.CharField(db_column='cp_export_', max_length=80, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ac_deflt'


class AcDept(models.Model):
    de_id = models.CharField(max_length=2, blank=True, null=True)
    de_desc = models.CharField(max_length=30, blank=True, null=True)
    de_emp_id = models.CharField(max_length=5, blank=True, null=True)
    de_printer = models.CharField(max_length=50, blank=True, null=True)
    de_chg_app = models.NullBooleanField()
    de_gl_num = models.CharField(max_length=12, blank=True, null=True)
    de_exp_dep = models.CharField(max_length=6, blank=True, null=True)
    de_ra_gl_n = models.CharField(max_length=12, blank=True, null=True)
    de_hrs_rat = models.FloatField(blank=True, null=True)
    de_laborra = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_dept'


class AcFacat(models.Model):
    fc_id = models.CharField(max_length=10, blank=True, null=True)
    fc_code = models.CharField(max_length=10, blank=True, null=True)
    fc_desc = models.CharField(max_length=40, blank=True, null=True)
    fc_ca_code = models.CharField(max_length=12, blank=True, null=True)
    fc_ad_ca_c = models.CharField(max_length=12, blank=True, null=True)
    fc_de_ca_c = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_facat'


class AcFadef(models.Model):
    ff_main = models.DateField(blank=True, null=True)
    ff_check = models.CharField(max_length=20, blank=True, null=True)
    ff_ca_cc_c = models.CharField(max_length=12, blank=True, null=True)
    ff_ca_pl_c = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_fadef'


class AcFadpr(models.Model):
    fd_id = models.CharField(max_length=10, blank=True, null=True)
    fd_fa_id = models.CharField(max_length=10, blank=True, null=True)
    fd_period = models.CharField(max_length=2, blank=True, null=True)
    fd_year = models.CharField(max_length=4, blank=True, null=True)
    fd_deprec_field = models.DecimalField(db_column='fd_deprec_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    fd_accum_a = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fd_book_va = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fd_gj_id = models.CharField(max_length=10, blank=True, null=True)
    fd_basis_r = models.FloatField(blank=True, null=True)
    fd_lyear = models.IntegerField(blank=True, null=True)
    fd_lperiod = models.IntegerField(blank=True, null=True)
    fd_lper_ye = models.IntegerField(blank=True, null=True)
    fd_fs_id = models.CharField(max_length=10, blank=True, null=True)
    fd_fj_id = models.CharField(max_length=10, blank=True, null=True)
    fd_capital = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fd_type = models.CharField(max_length=1, blank=True, null=True)
    fd_entry_d = models.DateField(blank=True, null=True)
    fd_clearin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fd_incloss = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_fadpr'


class AcFajnl(models.Model):
    fj_id = models.CharField(max_length=10, blank=True, null=True)
    fj_fa_id = models.CharField(max_length=10, blank=True, null=True)
    fj_date = models.DateField(blank=True, null=True)
    fj_entry_d = models.DateField(blank=True, null=True)
    fj_type = models.CharField(max_length=1, blank=True, null=True)
    fj_ca_code = models.CharField(max_length=12, blank=True, null=True)
    fj_ca_dr_c = models.CharField(max_length=12, blank=True, null=True)
    fj_ca_cr_c = models.CharField(max_length=12, blank=True, null=True)
    fj_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fj_dr_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fj_cr_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fj_gl_id = models.CharField(max_length=10, blank=True, null=True)
    fj_dr_gl_i = models.CharField(max_length=10, blank=True, null=True)
    fj_cr_gl_i = models.CharField(max_length=10, blank=True, null=True)
    fj_post = models.NullBooleanField()
    fj_post_da = models.DateField(blank=True, null=True)
    fj_referen = models.CharField(max_length=40, blank=True, null=True)
    fj_ca_pl_c = models.CharField(max_length=12, blank=True, null=True)
    fj_pl_gl_i = models.CharField(max_length=10, blank=True, null=True)
    fj_pl_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fj_supp_co = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_fajnl'


class AcFaloc(models.Model):
    fl_id = models.CharField(max_length=10, blank=True, null=True)
    fl_code = models.CharField(max_length=10, blank=True, null=True)
    fl_desc = models.CharField(max_length=40, blank=True, null=True)
    fl_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_faloc'


class AcFamfr(models.Model):
    fm_id = models.CharField(max_length=10, blank=True, null=True)
    fm_code = models.CharField(max_length=10, blank=True, null=True)
    fm_name = models.CharField(max_length=40, blank=True, null=True)
    fm_address = models.CharField(max_length=35, blank=True, null=True)
    fm_addres2 = models.CharField(max_length=35, blank=True, null=True)
    fm_city = models.CharField(max_length=30, blank=True, null=True)
    fm_state = models.CharField(max_length=3, blank=True, null=True)
    fm_zip_cod = models.CharField(max_length=10, blank=True, null=True)
    fm_phone = models.CharField(max_length=14, blank=True, null=True)
    fm_fax = models.CharField(max_length=14, blank=True, null=True)
    fm_contact = models.CharField(max_length=20, blank=True, null=True)
    fm_website = models.CharField(max_length=30, blank=True, null=True)
    fm_notes = models.TextField(blank=True, null=True)
    fm_country = models.CharField(max_length=25, blank=True, null=True)
    fm_email = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_famfr'


class AcFasch(models.Model):
    fs_id = models.CharField(max_length=10, blank=True, null=True)
    fs_fa_id = models.CharField(max_length=10, blank=True, null=True)
    fs_order = models.IntegerField(blank=True, null=True)
    fs_type = models.CharField(max_length=1, blank=True, null=True)
    fs_status = models.CharField(max_length=1, blank=True, null=True)
    fs_desc = models.CharField(max_length=40, blank=True, null=True)
    fs_supp_co = models.CharField(max_length=6, blank=True, null=True)
    fs_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fs_residua = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fs_life_ye = models.IntegerField(blank=True, null=True)
    fs_life_mo = models.IntegerField(blank=True, null=True)
    fs_depr_me = models.CharField(max_length=1, blank=True, null=True)
    fs_acqrd_d = models.DateField(blank=True, null=True)
    fs_beg_yea = models.IntegerField(blank=True, null=True)
    fs_beg_mon = models.CharField(max_length=2, blank=True, null=True)
    fs_id_numb = models.CharField(max_length=40, blank=True, null=True)
    fs_beg_qrt = models.IntegerField(blank=True, null=True)
    fs_basis_r = models.FloatField(blank=True, null=True)
    fs_units_d = models.CharField(max_length=12, blank=True, null=True)
    fs_life_un = models.FloatField(blank=True, null=True)
    fs_depr_va = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fs_mach_co = models.CharField(max_length=5, blank=True, null=True)
    fs_model = models.CharField(max_length=40, blank=True, null=True)
    fs_dspsd_d = models.DateField(blank=True, null=True)
    fs_beg_bal = models.NullBooleanField()
    fs_accum_d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fs_book_va = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fs_beg_ba2 = models.IntegerField(blank=True, null=True)
    fs_beg_ba3 = models.CharField(max_length=2, blank=True, null=True)
    fs_dspsd_v = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fs_income_field = models.DecimalField(db_column='fs_income_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    fs_fj_id = models.CharField(max_length=10, blank=True, null=True)
    fs_fj_id_2 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_fasch'


class AcFasts(models.Model):
    fa_id = models.CharField(max_length=10, blank=True, null=True)
    fa_code = models.CharField(max_length=10, blank=True, null=True)
    fa_desc = models.CharField(max_length=40, blank=True, null=True)
    fa_fc_id = models.CharField(max_length=10, blank=True, null=True)
    fa_fm_id = models.CharField(max_length=10, blank=True, null=True)
    fa_supp_co = models.CharField(max_length=6, blank=True, null=True)
    fa_ca_code = models.CharField(max_length=12, blank=True, null=True)
    fa_ad_ca_c = models.CharField(max_length=12, blank=True, null=True)
    fa_notes = models.TextField(blank=True, null=True)
    fa_de_ca_c = models.CharField(max_length=12, blank=True, null=True)
    fa_depr_fr = models.CharField(max_length=1, blank=True, null=True)
    fa_complet = models.NullBooleanField()
    fa_status = models.CharField(max_length=1, blank=True, null=True)
    fa_fl_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_fasts'


class AcGjdtl(models.Model):
    gd_id = models.CharField(max_length=10, blank=True, null=True)
    gd_sort = models.IntegerField(blank=True, null=True)
    gd_gj_id = models.CharField(max_length=10, blank=True, null=True)
    gd_type = models.IntegerField(blank=True, null=True)
    gd_ca_numb = models.CharField(max_length=12, blank=True, null=True)
    gd_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gd_memo = models.TextField(blank=True, null=True)
    gd_gl_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_gjdtl'


class AcGjrdt(models.Model):
    rd_id = models.CharField(max_length=10, blank=True, null=True)
    rd_sort = models.IntegerField(blank=True, null=True)
    rd_rc_id = models.CharField(max_length=10, blank=True, null=True)
    rd_type = models.IntegerField(blank=True, null=True)
    rd_ca_numb = models.CharField(max_length=12, blank=True, null=True)
    rd_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rd_memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_gjrdt'


class AcGjrec(models.Model):
    rc_id = models.CharField(max_length=10, blank=True, null=True)
    rc_name = models.CharField(max_length=40, blank=True, null=True)
    rc_desc = models.CharField(max_length=35, blank=True, null=True)
    rc_type = models.IntegerField(blank=True, null=True)
    rc_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rc_freq = models.CharField(max_length=1, blank=True, null=True)
    rc_date = models.DateField(blank=True, null=True)
    rc_day_wee = models.IntegerField(blank=True, null=True)
    rc_day_mon = models.IntegerField(blank=True, null=True)
    rc_month_y = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_gjrec'


class AcGjrnl(models.Model):
    gj_id = models.CharField(max_length=10, blank=True, null=True)
    gj_date = models.DateField(blank=True, null=True)
    gj_type = models.IntegerField(blank=True, null=True)
    gj_desc = models.CharField(max_length=35, blank=True, null=True)
    gj_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gj_post = models.NullBooleanField()
    gj_ptdate = models.DateField(blank=True, null=True)
    gj_rev_gj_field = models.CharField(db_column='gj_rev_gj_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    gj_rev_dat = models.DateField(blank=True, null=True)
    gj_out_of_field = models.NullBooleanField(db_column='gj_out_of_')  # Field renamed because it ended with '_'.
    gj_user_id = models.CharField(max_length=5, blank=True, null=True)
    gj_last_mo = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_gjrnl'


class AcGledg(models.Model):
    gl_id = models.CharField(max_length=10, blank=True, null=True)
    gl_date = models.DateField(blank=True, null=True)
    gl_jl_type = models.CharField(max_length=2, blank=True, null=True)
    gl_jl_id = models.CharField(max_length=10, blank=True, null=True)
    gl_ca_numb = models.CharField(max_length=12, blank=True, null=True)
    gl_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gl_jl_desc = models.CharField(max_length=50, blank=True, null=True)
    gl_jl_ext_field = models.CharField(db_column='gl_jl_ext_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ac_gledg'


class AcGlrpd(models.Model):
    gd_id = models.CharField(max_length=10, blank=True, null=True)
    gd_gr_id = models.CharField(max_length=10, blank=True, null=True)
    gd_type = models.CharField(max_length=1, blank=True, null=True)
    gd_order = models.IntegerField(blank=True, null=True)
    gd_desc = models.CharField(max_length=80, blank=True, null=True)
    gd_auto_de = models.NullBooleanField()
    gd_col_aut = models.NullBooleanField()
    gd_col_hea = models.CharField(max_length=60, blank=True, null=True)
    gd_col_he2 = models.CharField(max_length=15, blank=True, null=True)
    gd_col_he3 = models.CharField(max_length=15, blank=True, null=True)
    gd_col_he4 = models.CharField(max_length=15, blank=True, null=True)
    gd_col_typ = models.CharField(max_length=1, blank=True, null=True)
    gd_row_typ = models.CharField(max_length=1, blank=True, null=True)
    gd_row_acc = models.CharField(max_length=12, blank=True, null=True)
    gd_row_ac2 = models.CharField(max_length=12, blank=True, null=True)
    gd_row_ran = models.CharField(max_length=10, blank=True, null=True)
    gd_row_tex = models.CharField(max_length=40, blank=True, null=True)
    gd_row_mem = models.TextField(blank=True, null=True)
    gd_row_ind = models.IntegerField(blank=True, null=True)
    gd_row_pre = models.IntegerField(blank=True, null=True)
    gd_row_pos = models.IntegerField(blank=True, null=True)
    gd_row_pr2 = models.IntegerField(blank=True, null=True)
    gd_row_po2 = models.IntegerField(blank=True, null=True)
    gd_row_bla = models.IntegerField(blank=True, null=True)
    gd_row_ac3 = models.CharField(max_length=1, blank=True, null=True)
    gd_row_con = models.NullBooleanField()
    gd_row_ove = models.NullBooleanField()
    gd_row_top = models.NullBooleanField()
    gd_row_bot = models.NullBooleanField()
    gd_row_det = models.NullBooleanField()
    gd_col_sou = models.CharField(max_length=1, blank=True, null=True)
    gd_col_ran = models.CharField(max_length=1, blank=True, null=True)
    gd_col_yea = models.CharField(max_length=1, blank=True, null=True)
    gd_col_ye2 = models.IntegerField(blank=True, null=True)
    gd_col_ye3 = models.IntegerField(blank=True, null=True)
    gd_col_qtr = models.CharField(max_length=1, blank=True, null=True)
    gd_col_qt2 = models.CharField(max_length=1, blank=True, null=True)
    gd_col_qt3 = models.IntegerField(blank=True, null=True)
    gd_col_prd = models.CharField(max_length=1, blank=True, null=True)
    gd_col_pr2 = models.CharField(max_length=2, blank=True, null=True)
    gd_col_pr3 = models.IntegerField(blank=True, null=True)
    gd_col_num = models.IntegerField(blank=True, null=True)
    gd_col_nu2 = models.IntegerField(blank=True, null=True)
    gd_row_no_field = models.NullBooleanField(db_column='gd_row_no_')  # Field renamed because it ended with '_'.
    gd_col_deb = models.NullBooleanField()
    gd_col_cre = models.NullBooleanField()
    gd_col_for = models.CharField(max_length=1, blank=True, null=True)
    gd_col_acc = models.CharField(max_length=1, blank=True, null=True)
    gd_col_ac2 = models.CharField(max_length=12, blank=True, null=True)
    gd_col_ac3 = models.CharField(max_length=12, blank=True, null=True)
    gd_col_pre = models.CharField(max_length=10, blank=True, null=True)
    gd_col_no_field = models.NullBooleanField(db_column='gd_col_no_')  # Field renamed because it ended with '_'.
    gd_col_ye4 = models.CharField(max_length=1, blank=True, null=True)
    gd_col_ye5 = models.IntegerField(blank=True, null=True)
    gd_col_ye6 = models.IntegerField(blank=True, null=True)
    gd_col_pr4 = models.CharField(max_length=1, blank=True, null=True)
    gd_col_pr5 = models.CharField(max_length=2, blank=True, null=True)
    gd_col_pr6 = models.IntegerField(blank=True, null=True)
    gd_col_ye7 = models.CharField(max_length=1, blank=True, null=True)
    gd_col_qt4 = models.NullBooleanField()
    gd_col_use = models.NullBooleanField()
    gd_row_cal = models.CharField(max_length=1, blank=True, null=True)
    gd_row_pr3 = models.CharField(max_length=1, blank=True, null=True)
    gd_row_num = models.IntegerField(blank=True, null=True)
    gd_row_nu2 = models.IntegerField(blank=True, null=True)
    gd_row_co2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gd_row_for = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_glrpd'


class AcGlrpt(models.Model):
    gr_id = models.CharField(max_length=10, blank=True, null=True)
    gr_code = models.CharField(max_length=10, blank=True, null=True)
    gr_name = models.CharField(max_length=80, blank=True, null=True)
    gr_type = models.CharField(max_length=1, blank=True, null=True)
    gr_title = models.CharField(max_length=80, blank=True, null=True)
    gr_name_ti = models.NullBooleanField()
    gr_title_t = models.NullBooleanField()
    gr_title_n = models.NullBooleanField()
    gr_title_2 = models.NullBooleanField()
    gr_title_m = models.TextField(blank=True, null=True)
    gr_head_ti = models.NullBooleanField()
    gr_head_na = models.NullBooleanField()
    gr_head_pa = models.NullBooleanField()
    gr_head_da = models.NullBooleanField()
    gr_head_no = models.NullBooleanField()
    gr_head_me = models.TextField(blank=True, null=True)
    gr_foot_ti = models.NullBooleanField()
    gr_foot_na = models.NullBooleanField()
    gr_foot_pa = models.NullBooleanField()
    gr_foot_da = models.NullBooleanField()
    gr_foot_no = models.NullBooleanField()
    gr_foot_me = models.TextField(blank=True, null=True)
    gr_summ_ti = models.NullBooleanField()
    gr_summ_na = models.NullBooleanField()
    gr_summ_no = models.NullBooleanField()
    gr_summ_me = models.TextField(blank=True, null=True)
    gr_acct_nu = models.NullBooleanField()
    gr_title_d = models.NullBooleanField()
    gr_head_de = models.NullBooleanField()
    gr_foot_de = models.NullBooleanField()
    gr_summ_de = models.NullBooleanField()
    gr_title_3 = models.NullBooleanField()
    gr_summ_da = models.NullBooleanField()
    gr_title_4 = models.NullBooleanField()
    gr_title_b = models.NullBooleanField()
    gr_head_t_field = models.NullBooleanField(db_column='gr_head_t_')  # Field renamed because it ended with '_'.
    gr_head_b_field = models.NullBooleanField(db_column='gr_head_b_')  # Field renamed because it ended with '_'.
    gr_foot_t_field = models.NullBooleanField(db_column='gr_foot_t_')  # Field renamed because it ended with '_'.
    gr_foot_b_field = models.NullBooleanField(db_column='gr_foot_b_')  # Field renamed because it ended with '_'.
    gr_summ_t_field = models.NullBooleanField(db_column='gr_summ_t_')  # Field renamed because it ended with '_'.
    gr_summ_b_field = models.NullBooleanField(db_column='gr_summ_b_')  # Field renamed because it ended with '_'.
    gr_acct_no = models.NullBooleanField()
    gr_acct_su = models.NullBooleanField()
    gr_acct_he = models.NullBooleanField()
    gr_acct_de = models.NullBooleanField()
    gr_acct_di = models.NullBooleanField()
    gr_acct_dv = models.CharField(max_length=2, blank=True, null=True)
    gr_acct_dp = models.CharField(max_length=2, blank=True, null=True)
    gr_acct_se = models.NullBooleanField()
    gr_acct_s2 = models.IntegerField(blank=True, null=True)
    gr_acct_s3 = models.CharField(max_length=2, blank=True, null=True)
    gr_acct_d2 = models.NullBooleanField()
    gr_acct_d3 = models.NullBooleanField()
    gr_round_d = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ac_glrpt'


class AcGsctg(models.Model):
    gc_id = models.CharField(max_length=10, blank=True, null=True)
    gc_desc = models.CharField(max_length=50, blank=True, null=True)
    gc_print_o = models.IntegerField(blank=True, null=True)
    gc_horizon = models.NullBooleanField()
    gc_math = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_gsctg'


class AcGsdet(models.Model):
    gd_id = models.CharField(max_length=10, blank=True, null=True)
    gd_gc_id = models.CharField(max_length=10, blank=True, null=True)
    gd_gs_date = models.DateField(blank=True, null=True)
    gd_ca_numb = models.CharField(max_length=12, blank=True, null=True)
    gd_amt = models.FloatField(blank=True, null=True)
    gd_source = models.CharField(max_length=20, blank=True, null=True)
    gd_type = models.CharField(max_length=3, blank=True, null=True)
    gd_inv_num = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_gsdet'


class AcRange(models.Model):
    rn_id = models.CharField(max_length=10, blank=True, null=True)
    rn_code = models.CharField(max_length=3, blank=True, null=True)
    rn_desc = models.CharField(max_length=40, blank=True, null=True)
    rn_lo = models.CharField(max_length=12, blank=True, null=True)
    rn_hi = models.CharField(max_length=12, blank=True, null=True)
    rn_type = models.CharField(max_length=1, blank=True, null=True)
    rn_categor = models.IntegerField(blank=True, null=True)
    rn_reverse = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ac_range'


class AcRpgrd(models.Model):
    rd_id = models.CharField(max_length=10, blank=True, null=True)
    rd_rg_code = models.CharField(max_length=10, blank=True, null=True)
    rd_dv_code = models.CharField(max_length=2, blank=True, null=True)
    rd_dp_code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_rpgrd'


class AcRpgrp(models.Model):
    rg_code = models.CharField(max_length=10, blank=True, null=True)
    rg_desc = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_rpgrp'


class AcSlstx(models.Model):
    st_id = models.CharField(max_length=10, blank=True, null=True)
    st_tax_id = models.CharField(max_length=15, blank=True, null=True)
    st_desc = models.CharField(max_length=35, blank=True, null=True)
    st_address = models.CharField(max_length=30, blank=True, null=True)
    st_addres2 = models.CharField(max_length=30, blank=True, null=True)
    st_city = models.CharField(max_length=25, blank=True, null=True)
    st_state = models.CharField(max_length=2, blank=True, null=True)
    st_zip = models.CharField(max_length=10, blank=True, null=True)
    st_phone = models.CharField(max_length=15, blank=True, null=True)
    st_rate = models.FloatField(blank=True, null=True)
    st_ca_code = models.CharField(max_length=12, blank=True, null=True)
    st_prod_co = models.CharField(max_length=2, blank=True, null=True)
    st_min = models.FloatField(blank=True, null=True)
    st_max = models.FloatField(blank=True, null=True)
    st_taxonta = models.NullBooleanField()
    st_parent_field = models.CharField(db_column='st_parent_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    st_code = models.CharField(max_length=10, blank=True, null=True)
    st_ex_frei = models.NullBooleanField()
    st_ca_cod2 = models.CharField(max_length=12, blank=True, null=True)
    st_dist_co = models.CharField(max_length=2, blank=True, null=True)
    st_type = models.IntegerField(blank=True, null=True)
    st_export = models.CharField(max_length=5, blank=True, null=True)
    st_effecti = models.DateField(blank=True, null=True)
    st_previou = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_slstx'


class AcTerms(models.Model):
    te_desc = models.CharField(max_length=20, blank=True, null=True)
    te_type = models.IntegerField(blank=True, null=True)
    te_netdays = models.IntegerField(blank=True, null=True)
    te_disdays = models.IntegerField(blank=True, null=True)
    te_disper = models.FloatField(blank=True, null=True)
    te_day = models.IntegerField(blank=True, null=True)
    te_export_field = models.CharField(db_column='te_export_', max_length=31, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ac_terms'


class AcXccm(models.Model):
    mr_emp_id = models.CharField(max_length=5, blank=True, null=True)
    mr_number = models.CharField(max_length=10, blank=True, null=True)
    mr_line_nu = models.IntegerField(blank=True, null=True)
    mr_entry_d = models.DateField(blank=True, null=True)
    mr_date = models.DateField(blank=True, null=True)
    mr_cust_co = models.CharField(max_length=6, blank=True, null=True)
    mr_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    mr_inv_num = models.CharField(max_length=7, blank=True, null=True)
    mr_ext_pri = models.FloatField(blank=True, null=True)
    mr_comm_pe = models.FloatField(blank=True, null=True)
    mr_comm_am = models.FloatField(blank=True, null=True)
    mr_comm_pa = models.FloatField(blank=True, null=True)
    mr_comm_ba = models.FloatField(blank=True, null=True)
    mr_comm_gl = models.CharField(max_length=12, blank=True, null=True)
    mr_sc_id = models.CharField(max_length=10, blank=True, null=True)
    mr_id = models.CharField(max_length=10, blank=True, null=True)
    mr_referen = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_xccm'


class AcXcinv(models.Model):
    in_emp_id = models.CharField(max_length=5, blank=True, null=True)
    in_inv_num = models.CharField(max_length=7, blank=True, null=True)
    in_line_nu = models.IntegerField(blank=True, null=True)
    in_entry_d = models.DateField(blank=True, null=True)
    in_inv_dat = models.DateField(blank=True, null=True)
    in_cust_co = models.CharField(max_length=6, blank=True, null=True)
    in_inv_sta = models.CharField(max_length=1, blank=True, null=True)
    in_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    in_po_num = models.CharField(max_length=25, blank=True, null=True)
    in_ext_pri = models.FloatField(blank=True, null=True)
    in_comm_pe = models.FloatField(blank=True, null=True)
    in_comm_am = models.FloatField(blank=True, null=True)
    in_comm_pa = models.FloatField(blank=True, null=True)
    in_comm_ba = models.FloatField(blank=True, null=True)
    in_comm_gl = models.CharField(max_length=12, blank=True, null=True)
    in_sc_id = models.CharField(max_length=10, blank=True, null=True)
    in_pay_mem = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_xcinv'


class AcXcust(models.Model):
    cu_cust_co = models.CharField(max_length=6, blank=True, null=True)
    cu_referen = models.CharField(max_length=30, blank=True, null=True)
    cu_total_r = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cu_applied = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cu_open_cr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cu_general = models.NullBooleanField()
    cu_genera2 = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_xcust'


class AcXpdm(models.Model):
    mn_supp_co = models.CharField(max_length=6, blank=True, null=True)
    mn_id = models.CharField(max_length=10, blank=True, null=True)
    mn_number = models.CharField(max_length=10, blank=True, null=True)
    mn_date = models.DateField(blank=True, null=True)
    mn_inv_num = models.CharField(max_length=30, blank=True, null=True)
    mn_po_num = models.CharField(max_length=7, blank=True, null=True)
    mn_referen = models.CharField(max_length=30, blank=True, null=True)
    mn_oc_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_oc_bal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_cred_am = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mn_oc_new = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_xpdm'


class AcXpidm(models.Model):
    im_supp_co = models.CharField(max_length=6, blank=True, null=True)
    im_ap_id = models.CharField(max_length=10, blank=True, null=True)
    im_mn_id = models.CharField(max_length=10, blank=True, null=True)
    im_inv_num = models.CharField(max_length=30, blank=True, null=True)
    im_cred_am = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_xpidm'


class AcXpinv(models.Model):
    ap_supp_co = models.CharField(max_length=6, blank=True, null=True)
    ap_id = models.CharField(max_length=10, blank=True, null=True)
    ap_inv_num = models.CharField(max_length=30, blank=True, null=True)
    ap_inv_dat = models.DateField(blank=True, null=True)
    ap_status = models.CharField(max_length=1, blank=True, null=True)
    ap_po_num = models.CharField(max_length=7, blank=True, null=True)
    ap_hold = models.CharField(max_length=8, blank=True, null=True)
    ap_tot_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_tot_cur = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_inv_bal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_pay_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_cur_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_disc_am = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_cred_am = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_inv_new = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ap_gl_num = models.CharField(max_length=12, blank=True, null=True)
    ap_pay_ter = models.CharField(max_length=20, blank=True, null=True)
    ap_due_dat = models.DateField(blank=True, null=True)
    ap_disc_da = models.DateField(blank=True, null=True)
    ap_gl_pd = models.CharField(max_length=12, blank=True, null=True)
    ap_desc = models.CharField(max_length=30, blank=True, null=True)
    ap_pay_mem = models.CharField(max_length=30, blank=True, null=True)
    ap_pay_dat = models.DateField(blank=True, null=True)
    ap_check_n = models.CharField(max_length=10, blank=True, null=True)
    ap_electro = models.NullBooleanField()
    ap_discoun = models.NullBooleanField()
    ap_type = models.CharField(max_length=1, blank=True, null=True)
    ap_min_pay = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_xpinv'


class AcXrcm(models.Model):
    mr_cust_co = models.CharField(max_length=6, blank=True, null=True)
    mr_id = models.CharField(max_length=10, blank=True, null=True)
    mr_number = models.CharField(max_length=10, blank=True, null=True)
    mr_date = models.DateField(blank=True, null=True)
    mr_inv_num = models.CharField(max_length=7, blank=True, null=True)
    mr_ship_co = models.CharField(max_length=8, blank=True, null=True)
    mr_referen = models.CharField(max_length=30, blank=True, null=True)
    mr_oc_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mr_oc_bal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mr_cred_am = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mr_oc_new = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_xrcm'


class AcXricm(models.Model):
    im_cust_co = models.CharField(max_length=6, blank=True, null=True)
    im_inv_num = models.CharField(max_length=7, blank=True, null=True)
    im_mr_id = models.CharField(max_length=10, blank=True, null=True)
    im_cred_am = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_xricm'


class AcXrinv(models.Model):
    in_cust_co = models.CharField(max_length=6, blank=True, null=True)
    in_inv_num = models.CharField(max_length=7, blank=True, null=True)
    in_pay_dat = models.DateField(blank=True, null=True)
    in_inv_dat = models.DateField(blank=True, null=True)
    in_inv_sta = models.CharField(max_length=1, blank=True, null=True)
    in_po_num = models.CharField(max_length=15, blank=True, null=True)
    in_ship_co = models.CharField(max_length=8, blank=True, null=True)
    in_tot_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_tot_cur = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_inv_bal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_rec_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_cur_amt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_disc_am = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_cred_am = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_inv_new = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_gl_num = models.CharField(max_length=12, blank=True, null=True)
    in_pay_ter = models.CharField(max_length=20, blank=True, null=True)
    in_due_dat = models.DateField(blank=True, null=True)
    in_disc_da = models.DateField(blank=True, null=True)
    in_gl_sd = models.CharField(max_length=12, blank=True, null=True)
    in_referen = models.CharField(max_length=30, blank=True, null=True)
    in_type = models.CharField(max_length=1, blank=True, null=True)
    in_excepti = models.NullBooleanField()
    in_desc = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_xrinv'


class Accumet(models.Model):
    ac_quote_n = models.CharField(max_length=15, blank=True, null=True)
    ac_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    ac_order_n = models.CharField(max_length=12, blank=True, null=True)
    ac_invent_field = models.CharField(db_column='ac_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_inv_num = models.CharField(max_length=7, blank=True, null=True)
    ac_od = models.FloatField(blank=True, null=True)
    ac_odplus = models.FloatField(blank=True, null=True)
    ac_odminus = models.FloatField(blank=True, null=True)
    ac_wall = models.FloatField(blank=True, null=True)
    ac_wallplu = models.FloatField(blank=True, null=True)
    ac_wallmin = models.FloatField(blank=True, null=True)
    ac_id = models.FloatField(blank=True, null=True)
    ac_idplus = models.FloatField(blank=True, null=True)
    ac_idminus = models.FloatField(blank=True, null=True)
    ac_temper = models.CharField(max_length=30, blank=True, null=True)
    ac_length = models.FloatField(blank=True, null=True)
    ac_lengthp = models.FloatField(blank=True, null=True)
    ac_lengthm = models.FloatField(blank=True, null=True)
    ac_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    ac_alloyki = models.CharField(max_length=1, blank=True, null=True)
    ac_form = models.CharField(max_length=20, blank=True, null=True)
    ac_specifi = models.CharField(max_length=10, blank=True, null=True)
    ac_lenuom = models.CharField(max_length=10, blank=True, null=True)
    ac_line_nu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accumet'


class Acserial(models.Model):
    as_id = models.CharField(max_length=10, blank=True, null=True)
    as_lot_num = models.CharField(max_length=20, blank=True, null=True)
    as_qty = models.IntegerField(blank=True, null=True)
    as_notes = models.TextField(blank=True, null=True)
    as_aj_id = models.CharField(max_length=10, blank=True, null=True)
    as_jc_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acserial'


class Ajcard(models.Model):
    aj_id = models.CharField(max_length=10, blank=True, null=True)
    aj_run_dat = models.DateField(blank=True, null=True)
    aj_card_st = models.CharField(max_length=1, blank=True, null=True)
    aj_shift = models.CharField(max_length=2, blank=True, null=True)
    aj_order_n = models.CharField(max_length=12, blank=True, null=True)
    aj_operati = models.IntegerField(blank=True, null=True)
    aj_mach_co = models.CharField(max_length=5, blank=True, null=True)
    aj_emp_id = models.CharField(max_length=5, blank=True, null=True)
    aj_in_inve = models.CharField(max_length=30, blank=True, null=True)
    aj_in_inv2 = models.CharField(max_length=30, blank=True, null=True)
    aj_in_inv3 = models.CharField(max_length=30, blank=True, null=True)
    aj_in_inv4 = models.CharField(max_length=30, blank=True, null=True)
    aj_in_inv5 = models.CharField(max_length=30, blank=True, null=True)
    aj_in_inv6 = models.CharField(max_length=30, blank=True, null=True)
    aj_in_inv7 = models.CharField(max_length=30, blank=True, null=True)
    aj_in_inv8 = models.CharField(max_length=30, blank=True, null=True)
    aj_in_inv9 = models.CharField(max_length=30, blank=True, null=True)
    aj_in_in10 = models.CharField(max_length=30, blank=True, null=True)
    aj_in_qty = models.FloatField(blank=True, null=True)
    aj_in_qty1 = models.FloatField(blank=True, null=True)
    aj_in_qty2 = models.FloatField(blank=True, null=True)
    aj_in_qty3 = models.FloatField(blank=True, null=True)
    aj_in_qty4 = models.FloatField(blank=True, null=True)
    aj_in_qty5 = models.FloatField(blank=True, null=True)
    aj_in_qty6 = models.FloatField(blank=True, null=True)
    aj_in_qty7 = models.FloatField(blank=True, null=True)
    aj_in_qty8 = models.FloatField(blank=True, null=True)
    aj_in_qty9 = models.FloatField(blank=True, null=True)
    aj_hrs_ava = models.FloatField(blank=True, null=True)
    aj_hrs_set = models.FloatField(blank=True, null=True)
    aj_hrs_tot = models.FloatField(blank=True, null=True)
    aj_hrs_tdo = models.FloatField(blank=True, null=True)
    aj_hrs_odo = models.FloatField(blank=True, null=True)
    aj_hrs_pro = models.FloatField(blank=True, null=True)
    aj_down_re = models.CharField(max_length=40, blank=True, null=True)
    aj_parts_p = models.FloatField(blank=True, null=True)
    aj_parts_b = models.FloatField(blank=True, null=True)
    aj_parts_g = models.FloatField(blank=True, null=True)
    aj_out_inv = models.CharField(max_length=30, blank=True, null=True)
    aj_down_r2 = models.CharField(max_length=40, blank=True, null=True)
    aj_run_cod = models.CharField(max_length=20, blank=True, null=True)
    aj_su = models.IntegerField(blank=True, null=True)
    aj_rework = models.FloatField(blank=True, null=True)
    aj_scrap = models.FloatField(blank=True, null=True)
    aj_track1 = models.CharField(max_length=6, blank=True, null=True)
    aj_time_ca = models.CharField(max_length=2, blank=True, null=True)
    aj_time_c2 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_c3 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_c4 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_c5 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_c6 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_c7 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_c8 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_c9 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_10 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_11 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_12 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_13 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_14 = models.CharField(max_length=2, blank=True, null=True)
    aj_time_15 = models.CharField(max_length=2, blank=True, null=True)
    aj_time1 = models.CharField(max_length=10, blank=True, null=True)
    aj_time2 = models.CharField(max_length=10, blank=True, null=True)
    aj_time3 = models.CharField(max_length=10, blank=True, null=True)
    aj_time4 = models.CharField(max_length=10, blank=True, null=True)
    aj_time5 = models.CharField(max_length=10, blank=True, null=True)
    aj_time6 = models.CharField(max_length=10, blank=True, null=True)
    aj_time7 = models.CharField(max_length=10, blank=True, null=True)
    aj_time8 = models.CharField(max_length=10, blank=True, null=True)
    aj_time9 = models.CharField(max_length=10, blank=True, null=True)
    aj_time10 = models.CharField(max_length=10, blank=True, null=True)
    aj_time11 = models.CharField(max_length=10, blank=True, null=True)
    aj_time12 = models.CharField(max_length=10, blank=True, null=True)
    aj_time13 = models.CharField(max_length=10, blank=True, null=True)
    aj_time14 = models.CharField(max_length=10, blank=True, null=True)
    aj_time15 = models.CharField(max_length=10, blank=True, null=True)
    aj_date1 = models.DateField(blank=True, null=True)
    aj_date2 = models.DateField(blank=True, null=True)
    aj_date3 = models.DateField(blank=True, null=True)
    aj_date4 = models.DateField(blank=True, null=True)
    aj_date5 = models.DateField(blank=True, null=True)
    aj_date6 = models.DateField(blank=True, null=True)
    aj_date7 = models.DateField(blank=True, null=True)
    aj_date8 = models.DateField(blank=True, null=True)
    aj_date9 = models.DateField(blank=True, null=True)
    aj_date10 = models.DateField(blank=True, null=True)
    aj_date11 = models.DateField(blank=True, null=True)
    aj_date12 = models.DateField(blank=True, null=True)
    aj_date13 = models.DateField(blank=True, null=True)
    aj_date14 = models.DateField(blank=True, null=True)
    aj_date15 = models.DateField(blank=True, null=True)
    aj_sec1 = models.IntegerField(blank=True, null=True)
    aj_sec2 = models.IntegerField(blank=True, null=True)
    aj_sec3 = models.IntegerField(blank=True, null=True)
    aj_sec4 = models.IntegerField(blank=True, null=True)
    aj_sec5 = models.IntegerField(blank=True, null=True)
    aj_sec6 = models.IntegerField(blank=True, null=True)
    aj_sec7 = models.IntegerField(blank=True, null=True)
    aj_sec8 = models.IntegerField(blank=True, null=True)
    aj_sec9 = models.IntegerField(blank=True, null=True)
    aj_sec10 = models.IntegerField(blank=True, null=True)
    aj_sec11 = models.IntegerField(blank=True, null=True)
    aj_sec12 = models.IntegerField(blank=True, null=True)
    aj_sec13 = models.IntegerField(blank=True, null=True)
    aj_sec14 = models.IntegerField(blank=True, null=True)
    aj_sec15 = models.IntegerField(blank=True, null=True)
    aj_elap1 = models.FloatField(blank=True, null=True)
    aj_elap2 = models.FloatField(blank=True, null=True)
    aj_elap3 = models.FloatField(blank=True, null=True)
    aj_elap4 = models.FloatField(blank=True, null=True)
    aj_elap5 = models.FloatField(blank=True, null=True)
    aj_elap6 = models.FloatField(blank=True, null=True)
    aj_elap7 = models.FloatField(blank=True, null=True)
    aj_elap8 = models.FloatField(blank=True, null=True)
    aj_elap9 = models.FloatField(blank=True, null=True)
    aj_elap10 = models.FloatField(blank=True, null=True)
    aj_elap11 = models.FloatField(blank=True, null=True)
    aj_elap12 = models.FloatField(blank=True, null=True)
    aj_elap13 = models.FloatField(blank=True, null=True)
    aj_elap14 = models.FloatField(blank=True, null=True)
    aj_elap15 = models.FloatField(blank=True, null=True)
    aj_tot_tim = models.FloatField(blank=True, null=True)
    aj_time_da = models.DateField(blank=True, null=True)
    aj_ot_hrs_field = models.FloatField(db_column='aj_ot_hrs_', blank=True, null=True)  # Field renamed because it ended with '_'.
    aj_ot_hrs2 = models.FloatField(blank=True, null=True)
    aj_calc = models.CharField(max_length=2, blank=True, null=True)
    aj_calc1 = models.CharField(max_length=2, blank=True, null=True)
    aj_calc2 = models.CharField(max_length=2, blank=True, null=True)
    aj_calc3 = models.CharField(max_length=2, blank=True, null=True)
    aj_calc4 = models.CharField(max_length=2, blank=True, null=True)
    aj_calc5 = models.CharField(max_length=2, blank=True, null=True)
    aj_calc6 = models.CharField(max_length=2, blank=True, null=True)
    aj_calc7 = models.CharField(max_length=2, blank=True, null=True)
    aj_calc8 = models.CharField(max_length=2, blank=True, null=True)
    aj_calc9 = models.CharField(max_length=2, blank=True, null=True)
    aj_heat_nu = models.IntegerField(blank=True, null=True)
    aj_heat_n2 = models.IntegerField(blank=True, null=True)
    aj_heat_n3 = models.IntegerField(blank=True, null=True)
    aj_heat_n4 = models.IntegerField(blank=True, null=True)
    aj_heat_n5 = models.IntegerField(blank=True, null=True)
    aj_heat_n6 = models.IntegerField(blank=True, null=True)
    aj_heat_n7 = models.IntegerField(blank=True, null=True)
    aj_heat_n8 = models.IntegerField(blank=True, null=True)
    aj_heat_n9 = models.IntegerField(blank=True, null=True)
    aj_heat_10 = models.IntegerField(blank=True, null=True)
    aj_num_mac = models.IntegerField(blank=True, null=True)
    aj_rel_num = models.IntegerField(blank=True, null=True)
    aj_notes = models.TextField(blank=True, null=True)
    aj_complet = models.NullBooleanField()
    aj_last_ti = models.CharField(max_length=10, blank=True, null=True)
    aj_last_qt = models.FloatField(blank=True, null=True)
    aj_last_q2 = models.FloatField(blank=True, null=True)
    aj_last_q3 = models.FloatField(blank=True, null=True)
    aj_last_q4 = models.FloatField(blank=True, null=True)
    aj_last_ef = models.FloatField(blank=True, null=True)
    aj_last_e2 = models.FloatField(blank=True, null=True)
    aj_op_comp = models.NullBooleanField()
    aj_parent_field = models.CharField(db_column='aj_parent_', max_length=8, blank=True, null=True)  # Field renamed because it ended with '_'.
    aj_raw_inv = models.CharField(max_length=30, blank=True, null=True)
    aj_is_nest = models.NullBooleanField()
    aj_nest_co = models.NullBooleanField()
    aj_nest_ot = models.IntegerField(blank=True, null=True)
    aj_inlot_n = models.CharField(max_length=20, blank=True, null=True)
    aj_il_id = models.CharField(max_length=10, blank=True, null=True)
    aj_ib_id = models.CharField(max_length=10, blank=True, null=True)
    aj_id_code = models.CharField(max_length=10, blank=True, null=True)
    aj_de_id = models.CharField(max_length=10, blank=True, null=True)
    aj_nestmod = models.IntegerField(blank=True, null=True)
    aj_nh_id = models.CharField(max_length=10, blank=True, null=True)
    aj_other_d = models.CharField(max_length=5, blank=True, null=True)
    aj_tool_ty = models.CharField(max_length=20, blank=True, null=True)
    aj_st_id = models.CharField(max_length=2, blank=True, null=True)
    aj_lc_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ajcard'


class Alloc(models.Model):
    al_invent_field = models.CharField(db_column='al_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    al_type = models.CharField(max_length=1, blank=True, null=True)
    al_order_n = models.CharField(max_length=12, blank=True, null=True)
    al_op = models.IntegerField(blank=True, null=True)
    al_ppb = models.FloatField(blank=True, null=True)
    al_sched_q = models.FloatField(blank=True, null=True)
    al_prod_qt = models.FloatField(blank=True, null=True)
    al_bal_pro = models.FloatField(blank=True, null=True)
    al_need_ba = models.FloatField(blank=True, null=True)
    al_alloc_q = models.FloatField(blank=True, null=True)
    al_psquare = models.FloatField(blank=True, null=True)
    al_part_le = models.FloatField(blank=True, null=True)
    al_barend_field = models.FloatField(db_column='al_barend_', blank=True, null=True)  # Field renamed because it ended with '_'.
    al_qty_use = models.FloatField(blank=True, null=True)
    al_percent = models.IntegerField(blank=True, null=True)
    al_rel_num = models.IntegerField(blank=True, null=True)
    al_aok = models.NullBooleanField()
    al_qty_per = models.FloatField(blank=True, null=True)
    al_width = models.FloatField(blank=True, null=True)
    al_length = models.FloatField(blank=True, null=True)
    al_usesuom = models.NullBooleanField()
    al_id = models.CharField(max_length=10, blank=True, null=True)
    al_qi_item = models.IntegerField(blank=True, null=True)
    al_order_b = models.DateField(blank=True, null=True)
    al_need_by = models.DateField(blank=True, null=True)
    al_po_num = models.CharField(max_length=7, blank=True, null=True)
    al_po_line = models.IntegerField(blank=True, null=True)
    al_ok_to_o = models.NullBooleanField()
    al_po_note = models.TextField(blank=True, null=True)
    al_emp_id = models.CharField(max_length=5, blank=True, null=True)
    al_req_id = models.CharField(max_length=10, blank=True, null=True)
    al_req_sup = models.CharField(max_length=6, blank=True, null=True)
    al_req_pur = models.CharField(max_length=2, blank=True, null=True)
    al_req_des = models.CharField(max_length=60, blank=True, null=True)
    al_req_su2 = models.CharField(max_length=30, blank=True, null=True)
    al_req_ite = models.IntegerField(blank=True, null=True)
    al_req_ext = models.TextField(blank=True, null=True)
    al_req_uni = models.FloatField(blank=True, null=True)
    al_req_dis = models.CharField(max_length=2, blank=True, null=True)
    al_req_gl_field = models.CharField(db_column='al_req_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    al_req_mac = models.CharField(max_length=5, blank=True, null=True)
    al_req_fg_field = models.CharField(db_column='al_req_fg_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    al_req_tg_field = models.CharField(db_column='al_req_tg_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    al_req_too = models.CharField(max_length=20, blank=True, null=True)
    al_reqorde = models.CharField(max_length=12, blank=True, null=True)
    al_app_emp = models.CharField(max_length=5, blank=True, null=True)
    al_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    al_sord_li = models.IntegerField(blank=True, null=True)
    al_quality = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alloc'


class Altroute(models.Model):
    ar_invent_field = models.CharField(db_column='ar_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ar_start_q = models.IntegerField(blank=True, null=True)
    ar_end_qty = models.IntegerField(blank=True, null=True)
    ar_quote_n = models.CharField(max_length=15, blank=True, null=True)
    ar_desc = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'altroute'


class AopPred(models.Model):
    ao_order_n = models.CharField(max_length=12, blank=True, null=True)
    ao_op_num = models.IntegerField(blank=True, null=True)
    ao_parent_field = models.CharField(db_column='ao_parent_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_parent2 = models.IntegerField(blank=True, null=True)
    ao_depend_field = models.IntegerField(db_column='ao_depend_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_lag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aop_pred'


class Aoperate(models.Model):
    ao_order_n = models.CharField(max_length=12, blank=True, null=True)
    ao_op_num = models.IntegerField(blank=True, null=True)
    ao_type = models.CharField(max_length=1, blank=True, null=True)
    ao_mach_co = models.CharField(max_length=5, blank=True, null=True)
    ao_suhr = models.FloatField(blank=True, null=True)
    ao_sur = models.FloatField(blank=True, null=True)
    ao_su = models.FloatField(blank=True, null=True)
    ao_gp = models.FloatField(blank=True, null=True)
    ao_pop = models.FloatField(blank=True, null=True)
    ao_np = models.FloatField(blank=True, null=True)
    ao_hpu = models.FloatField(blank=True, null=True)
    ao_hr = models.FloatField(blank=True, null=True)
    ao_cpu = models.FloatField(blank=True, null=True)
    ao_note = models.TextField(blank=True, null=True)
    ao_current = models.IntegerField(blank=True, null=True)
    ao_attend = models.IntegerField(blank=True, null=True)
    ao_queue = models.FloatField(blank=True, null=True)
    ao_dist_co = models.CharField(max_length=2, blank=True, null=True)
    ao_supp_co = models.CharField(max_length=6, blank=True, null=True)
    ao_unit_co = models.FloatField(blank=True, null=True)
    ao_quantit = models.FloatField(blank=True, null=True)
    ao_ext_cos = models.FloatField(blank=True, null=True)
    ao_mark_up = models.IntegerField(blank=True, null=True)
    ao_tot_cos = models.FloatField(blank=True, null=True)
    ao_distrib = models.NullBooleanField()
    ao_cost1 = models.FloatField(blank=True, null=True)
    ao_cost2 = models.FloatField(blank=True, null=True)
    ao_cost3 = models.FloatField(blank=True, null=True)
    ao_cost4 = models.FloatField(blank=True, null=True)
    ao_cost5 = models.FloatField(blank=True, null=True)
    ao_cost6 = models.FloatField(blank=True, null=True)
    ao_cost7 = models.FloatField(blank=True, null=True)
    ao_cost8 = models.FloatField(blank=True, null=True)
    ao_cost9 = models.FloatField(blank=True, null=True)
    ao_cost10 = models.FloatField(blank=True, null=True)
    ao_recalc = models.NullBooleanField()
    ao_tsu = models.IntegerField(blank=True, null=True)
    ao_hrs_od = models.FloatField(blank=True, null=True)
    ao_hrs_td = models.FloatField(blank=True, null=True)
    ao_hrs_tot = models.FloatField(blank=True, null=True)
    ao_hrs_av = models.FloatField(blank=True, null=True)
    ao_p_prod = models.FloatField(blank=True, null=True)
    ao_p_bad = models.IntegerField(blank=True, null=True)
    ao_p_good = models.FloatField(blank=True, null=True)
    ao_qty_bal = models.FloatField(blank=True, null=True)
    ao_hrs_pro = models.FloatField(blank=True, null=True)
    ao_hrs_set = models.FloatField(blank=True, null=True)
    ao_scrap = models.FloatField(blank=True, null=True)
    ao_rework = models.FloatField(blank=True, null=True)
    ao_qty_pro = models.FloatField(blank=True, null=True)
    ao_qty_inv = models.FloatField(blank=True, null=True)
    ao_act_phr = models.FloatField(blank=True, null=True)
    ao_adj_phr = models.FloatField(blank=True, null=True)
    ao_go_eff = models.IntegerField(blank=True, null=True)
    ao_p_eff = models.IntegerField(blank=True, null=True)
    ao_su_eff = models.IntegerField(blank=True, null=True)
    ao_perc_co = models.IntegerField(blank=True, null=True)
    ao_num_mac = models.IntegerField(blank=True, null=True)
    ao_qty_ord = models.FloatField(blank=True, null=True)
    ao_incl_su = models.CharField(max_length=100, blank=True, null=True)
    ao_end_dat = models.TextField(blank=True, null=True)
    ao_sc_off = models.CharField(max_length=100, blank=True, null=True)
    ao_labors = models.FloatField(blank=True, null=True)
    ao_burdens = models.FloatField(blank=True, null=True)
    ao_laborp = models.FloatField(blank=True, null=True)
    ao_burdenp = models.FloatField(blank=True, null=True)
    ao_force_m = models.CharField(max_length=100, blank=True, null=True)
    ao_sched_q = models.TextField(blank=True, null=True)
    ao_in_inve = models.CharField(max_length=30, blank=True, null=True)
    ao_out_inv = models.CharField(max_length=30, blank=True, null=True)
    ao_sched = models.NullBooleanField()
    ao_force = models.NullBooleanField()
    ao_rewflag = models.NullBooleanField()
    ao_g_code = models.CharField(max_length=10, blank=True, null=True)
    ao_review = models.FloatField(blank=True, null=True)
    ao_move_st = models.NullBooleanField()
    ao_complet = models.NullBooleanField()
    ao_master_field = models.IntegerField(db_column='ao_master_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_parent_field = models.IntegerField(db_column='ao_parent_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_oplib_n = models.TextField(blank=True, null=True)
    ao_il_id = models.CharField(max_length=10, blank=True, null=True)
    ao_ib_id = models.CharField(max_length=10, blank=True, null=True)
    ao_pagebre = models.NullBooleanField()
    ao_min_cha = models.FloatField(blank=True, null=True)
    ao_infin_m = models.FloatField(blank=True, null=True)
    ao_enforce = models.NullBooleanField()
    ao_setup_m = models.NullBooleanField()
    ao_setup_c = models.IntegerField(blank=True, null=True)
    ao_aggrega = models.IntegerField(blank=True, null=True)
    ao_last_pr = models.NullBooleanField()
    ao_split = models.NullBooleanField()
    ao_il_id_i = models.CharField(max_length=10, blank=True, null=True)
    ao_ib_id_i = models.CharField(max_length=10, blank=True, null=True)
    ao_optype = models.IntegerField(blank=True, null=True)
    ao_down = models.IntegerField(blank=True, null=True)
    ao_pc_lbs = models.NullBooleanField()
    ao_pc_cost = models.FloatField(blank=True, null=True)
    ao_aw_orde = models.CharField(max_length=8, blank=True, null=True)
    ao_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    ao_infstar = models.DateField(blank=True, null=True)
    ao_infend_field = models.DateField(db_column='ao_infend_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_statnot = models.TextField(blank=True, null=True)
    ao_minqty = models.IntegerField(blank=True, null=True)
    ao_hpp = models.FloatField(blank=True, null=True)
    ao_mpp = models.FloatField(blank=True, null=True)
    ao_spp = models.FloatField(blank=True, null=True)
    ao_burden = models.FloatField(blank=True, null=True)
    ao_exclude = models.NullBooleanField()
    ao_comp_da = models.DateField(blank=True, null=True)
    ao_sl = models.TextField(blank=True, null=True)
    ao_pc_per_field = models.FloatField(db_column='ao_pc_per_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_unit_ra = models.FloatField(blank=True, null=True)
    ao_need_qt = models.FloatField(blank=True, null=True)
    ao_surchar = models.FloatField(blank=True, null=True)
    ao_simple_field = models.NullBooleanField(db_column='ao_simple_')  # Field renamed because it ended with '_'.
    ao_lossper = models.FloatField(blank=True, null=True)
    ao_load_ti = models.FloatField(blank=True, null=True)
    ao_rpm = models.IntegerField(blank=True, null=True)
    ao_spindge = models.CharField(max_length=15, blank=True, null=True)
    ao_changeg = models.CharField(max_length=15, blank=True, null=True)
    ao_threadg = models.CharField(max_length=15, blank=True, null=True)
    ao_st_id = models.CharField(max_length=10, blank=True, null=True)
    ao_signifi = models.NullBooleanField()
    ao_post_pc = models.NullBooleanField()
    ao_sa_id = models.CharField(max_length=10, blank=True, null=True)
    ao_donotor = models.NullBooleanField()
    ao_casting = models.NullBooleanField()
    ao_spindle = models.IntegerField(blank=True, null=True)
    ao_feed_rp = models.IntegerField(blank=True, null=True)
    ao_eff_thr = models.IntegerField(blank=True, null=True)
    ao_mtsc = models.FloatField(blank=True, null=True)
    ao_opqty = models.FloatField(blank=True, null=True)
    ao_freight = models.FloatField(blank=True, null=True)
    ao_freigh2 = models.FloatField(blank=True, null=True)
    ao_lotqty = models.FloatField(blank=True, null=True)
    ao_infsta2 = models.DateTimeField(blank=True, null=True)
    ao_infend2 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aoperate'


class Aoptools(models.Model):
    at_order_n = models.CharField(max_length=12, blank=True, null=True)
    at_op_num = models.IntegerField(blank=True, null=True)
    at_tool_nu = models.IntegerField(blank=True, null=True)
    at_mach_ca = models.CharField(max_length=5, blank=True, null=True)
    at_tool_ty = models.CharField(max_length=20, blank=True, null=True)
    at_speed = models.FloatField(blank=True, null=True)
    at_sp_adj = models.IntegerField(blank=True, null=True)
    at_adj_spe = models.FloatField(blank=True, null=True)
    at_feed = models.FloatField(blank=True, null=True)
    at_fe_adj = models.IntegerField(blank=True, null=True)
    at_adj_fee = models.FloatField(blank=True, null=True)
    at_sfm = models.FloatField(blank=True, null=True)
    at_ipr = models.FloatField(blank=True, null=True)
    at_gp = models.FloatField(blank=True, null=True)
    at_note = models.TextField(blank=True, null=True)
    at_loc = models.FloatField(blank=True, null=True)
    at_passes = models.IntegerField(blank=True, null=True)
    at_work_di = models.FloatField(blank=True, null=True)
    at_current = models.IntegerField(blank=True, null=True)
    at_tool_di = models.FloatField(blank=True, null=True)
    at_num_flu = models.IntegerField(blank=True, null=True)
    at_const_v = models.FloatField(blank=True, null=True)
    at_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    at_quantit = models.IntegerField(blank=True, null=True)
    at_desc = models.CharField(max_length=50, blank=True, null=True)
    at_positio = models.IntegerField(blank=True, null=True)
    at_endside = models.IntegerField(blank=True, null=True)
    at_unit_co = models.FloatField(blank=True, null=True)
    at_ext_cos = models.FloatField(blank=True, null=True)
    at_gp_sec = models.FloatField(blank=True, null=True)
    at_index_m = models.FloatField(blank=True, null=True)
    at_index_s = models.FloatField(blank=True, null=True)
    at_total_c = models.FloatField(blank=True, null=True)
    at_total_2 = models.FloatField(blank=True, null=True)
    at_cam = models.FloatField(blank=True, null=True)
    at_cycle = models.FloatField(blank=True, null=True)
    at_cycle_s = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aoptools'


class Approval(models.Model):
    ap_id = models.CharField(max_length=10, blank=True, null=True)
    ap_source = models.CharField(max_length=20, blank=True, null=True)
    ap_source_field = models.CharField(db_column='ap_source_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    ap_choice = models.IntegerField(blank=True, null=True)
    ap_emp_id = models.CharField(max_length=5, blank=True, null=True)
    ap_notes = models.TextField(blank=True, null=True)
    ap_date = models.DateField(blank=True, null=True)
    ap_time = models.CharField(max_length=10, blank=True, null=True)
    ap_de_id = models.CharField(max_length=10, blank=True, null=True)
    ap_uber_us = models.NullBooleanField()
    ap_uber_u2 = models.TextField(blank=True, null=True)
    ap_checksu = models.IntegerField(blank=True, null=True)
    ap_rev = models.CharField(max_length=3, blank=True, null=True)
    ap_source2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approval'


class As9102F1(models.Model):
    as_id = models.CharField(max_length=10, blank=True, null=True)
    part_num = models.CharField(max_length=30, blank=True, null=True)
    part_name = models.CharField(max_length=50, blank=True, null=True)
    serial_num = models.CharField(max_length=30, blank=True, null=True)
    fai_report = models.CharField(max_length=50, blank=True, null=True)
    rev_num = models.CharField(max_length=10, blank=True, null=True)
    draw_num = models.CharField(max_length=30, blank=True, null=True)
    draw_rev_l = models.CharField(max_length=10, blank=True, null=True)
    addition_c = models.TextField(blank=True, null=True)
    man_proces = models.CharField(max_length=30, blank=True, null=True)
    organizati = models.CharField(max_length=50, blank=True, null=True)
    supplier_c = models.CharField(max_length=20, blank=True, null=True)
    po_number = models.CharField(max_length=30, blank=True, null=True)
    detail_fai = models.CharField(max_length=30, blank=True, null=True)
    full_parti = models.IntegerField(blank=True, null=True)
    parial_fai = models.TextField(blank=True, null=True)
    signature_field = models.CharField(db_column='signature_', max_length=5, blank=True, null=True)  # Field renamed because it ended with '_'.
    signature2 = models.DateField(blank=True, null=True)
    reviewedby = models.CharField(max_length=5, blank=True, null=True)
    reviewedb2 = models.DateField(blank=True, null=True)
    customer_a = models.CharField(max_length=30, blank=True, null=True)
    approval_d = models.DateField(blank=True, null=True)
    fai_comple = models.NullBooleanField()
    invent_num = models.CharField(max_length=30, blank=True, null=True)
    cust_code = models.CharField(max_length=6, blank=True, null=True)
    order_num = models.CharField(max_length=12, blank=True, null=True)
    as_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'as9102f1'


class As9102F2(models.Model):
    asf2_id = models.CharField(max_length=10, blank=True, null=True)
    part_num = models.CharField(max_length=30, blank=True, null=True)
    part_name = models.CharField(max_length=50, blank=True, null=True)
    serial_num = models.CharField(max_length=30, blank=True, null=True)
    fai_report = models.CharField(max_length=30, blank=True, null=True)
    preparedby = models.CharField(max_length=5, blank=True, null=True)
    preparedb2 = models.DateField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    as_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'as9102f2'


class As9102F3(models.Model):
    asf3_id = models.CharField(max_length=10, blank=True, null=True)
    part_num = models.CharField(max_length=30, blank=True, null=True)
    part_name = models.CharField(max_length=50, blank=True, null=True)
    serial_num = models.CharField(max_length=30, blank=True, null=True)
    fai_report = models.CharField(max_length=50, blank=True, null=True)
    preparedby = models.CharField(max_length=5, blank=True, null=True)
    preparedb2 = models.DateField(blank=True, null=True)
    as_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'as9102f3'


class Asf1Det(models.Model):
    f1_det_id = models.CharField(max_length=10, blank=True, null=True)
    part_num = models.CharField(max_length=30, blank=True, null=True)
    part_name = models.CharField(max_length=50, blank=True, null=True)
    serial_num = models.CharField(max_length=30, blank=True, null=True)
    fai_report = models.CharField(max_length=50, blank=True, null=True)
    as_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asf1det'


class Asf2Det1(models.Model):
    f2_det1_id = models.CharField(max_length=10, blank=True, null=True)
    process_na = models.CharField(max_length=50, blank=True, null=True)
    spec_numbe = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=25, blank=True, null=True)
    supplier_c = models.CharField(max_length=30, blank=True, null=True)
    cust_appro = models.CharField(max_length=10, blank=True, null=True)
    cofc_numbe = models.CharField(max_length=30, blank=True, null=True)
    as_id = models.CharField(max_length=10, blank=True, null=True)
    asf2_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asf2det1'


class Asf2Det2(models.Model):
    f2_det2_id = models.CharField(max_length=10, blank=True, null=True)
    funct_test = models.CharField(max_length=50, blank=True, null=True)
    accept_tes = models.CharField(max_length=50, blank=True, null=True)
    asf2_id = models.CharField(max_length=10, blank=True, null=True)
    as_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asf2det2'


class Asf3Det(models.Model):
    f3_det_id = models.CharField(max_length=10, blank=True, null=True)
    char_num = models.CharField(max_length=10, blank=True, null=True)
    reference_field = models.CharField(db_column='reference_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    char_desig = models.CharField(max_length=30, blank=True, null=True)
    results = models.CharField(max_length=50, blank=True, null=True)
    design_too = models.CharField(max_length=30, blank=True, null=True)
    nonconf_nu = models.CharField(max_length=30, blank=True, null=True)
    meas_gauge = models.CharField(max_length=50, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    as_id = models.CharField(max_length=10, blank=True, null=True)
    asf3_id = models.CharField(max_length=10, blank=True, null=True)
    requiremen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asf3det'


class Auditor(models.Model):
    au_date_ti = models.DateTimeField(blank=True, null=True)
    au_user_id = models.CharField(max_length=5, blank=True, null=True)
    au_screen_field = models.CharField(db_column='au_screen_', max_length=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    au_table_i = models.CharField(max_length=15, blank=True, null=True)
    au_table_k = models.CharField(max_length=15, blank=True, null=True)
    au_table_f = models.CharField(max_length=30, blank=True, null=True)
    au_val_bef = models.CharField(max_length=50, blank=True, null=True)
    au_val_aft = models.CharField(max_length=50, blank=True, null=True)
    au_overflo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditor'


class Autorecs(models.Model):
    ar_id = models.CharField(max_length=10, blank=True, null=True)
    ar_invent_field = models.CharField(db_column='ar_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ar_quantit = models.FloatField(blank=True, null=True)
    ar_importe = models.NullBooleanField()
    ar_user_id = models.CharField(max_length=5, blank=True, null=True)
    ar_date = models.DateField(blank=True, null=True)
    ar_po_num = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autorecs'


class Autoshps(models.Model):
    as_id = models.CharField(max_length=10, blank=True, null=True)
    as_invent_field = models.CharField(db_column='as_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    as_quantit = models.FloatField(blank=True, null=True)
    as_importe = models.NullBooleanField()
    as_user_id = models.CharField(max_length=5, blank=True, null=True)
    as_date = models.DateField(blank=True, null=True)
    as_cust_co = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autoshps'


class Backlg(models.Model):
    bl_userid = models.CharField(max_length=5, blank=True, null=True)
    bl_date = models.DateField(blank=True, null=True)
    bl_complet = models.NullBooleanField()
    bl_ship_da = models.DateField(blank=True, null=True)
    bl_qtytoma = models.IntegerField(blank=True, null=True)
    bl_qtyallo = models.IntegerField(blank=True, null=True)
    bl_part_nu = models.CharField(max_length=30, blank=True, null=True)
    bl_invent_field = models.CharField(db_column='bl_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    bl_leadtim = models.IntegerField(blank=True, null=True)
    bl_custome = models.CharField(max_length=50, blank=True, null=True)
    bl_comp_da = models.DateField(blank=True, null=True)
    bl_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'backlg'


class Backlog(models.Model):
    bl_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    bl_line_nu = models.IntegerField(blank=True, null=True)
    bl_po_num = models.CharField(max_length=20, blank=True, null=True)
    bl_due_dat = models.DateField(blank=True, null=True)
    bl_cust_co = models.CharField(max_length=6, blank=True, null=True)
    bl_invent_field = models.CharField(db_column='bl_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    bl_part_nu = models.CharField(max_length=30, blank=True, null=True)
    bl_desc = models.CharField(max_length=30, blank=True, null=True)
    bl_qty_ord = models.IntegerField(blank=True, null=True)
    bl_cpu = models.FloatField(blank=True, null=True)
    bl_qty_shi = models.IntegerField(blank=True, null=True)
    bl_qty_bal = models.IntegerField(blank=True, null=True)
    bl_backlog = models.FloatField(blank=True, null=True)
    bl_cust_na = models.CharField(max_length=35, blank=True, null=True)
    bl_prom_da = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'backlog'


class Batchjc(models.Model):
    cemp = models.CharField(max_length=5, blank=True, null=True)
    nop = models.IntegerField(blank=True, null=True)
    ncount = models.IntegerField(blank=True, null=True)
    nscrap = models.IntegerField(blank=True, null=True)
    nreview = models.IntegerField(blank=True, null=True)
    nhours = models.FloatField(blank=True, null=True)
    ddate = models.DateField(blank=True, null=True)
    cwc = models.CharField(max_length=5, blank=True, null=True)
    corder = models.CharField(max_length=12, blank=True, null=True)
    cdefects = models.CharField(max_length=20, blank=True, null=True)
    clot = models.CharField(max_length=20, blank=True, null=True)
    nrework = models.FloatField(blank=True, null=True)
    nsuhours = models.FloatField(blank=True, null=True)
    ndnhours = models.FloatField(blank=True, null=True)
    cshift = models.CharField(max_length=2, blank=True, null=True)
    nrel = models.IntegerField(blank=True, null=True)
    nnomach = models.IntegerField(blank=True, null=True)
    serial_num = models.FloatField(blank=True, null=True)
    iscomplete = models.NullBooleanField()
    cid_code = models.CharField(max_length=10, blank=True, null=True)
    cdown_reas = models.CharField(max_length=80, blank=True, null=True)
    ot_hrs_s = models.FloatField(blank=True, null=True)
    dot_hrs_s = models.FloatField(blank=True, null=True)
    ot_hrs_p = models.FloatField(blank=True, null=True)
    dot_hrs_p = models.FloatField(blank=True, null=True)
    cdtcode = models.CharField(max_length=5, blank=True, null=True)
    cruncode = models.CharField(max_length=20, blank=True, null=True)
    imported = models.NullBooleanField()
    bj_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batchjc'


class Bom(models.Model):
    parent = models.CharField(max_length=30, blank=True, null=True)
    part_num = models.CharField(max_length=30, blank=True, null=True)
    count = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    qty_per = models.FloatField(blank=True, null=True)
    quote_num = models.CharField(max_length=15, blank=True, null=True)
    op_num = models.IntegerField(blank=True, null=True)
    usesuom = models.NullBooleanField()
    phantom = models.NullBooleanField()
    in_mm = models.IntegerField(blank=True, null=True)
    descriptio = models.CharField(max_length=30, blank=True, null=True)
    option_gro = models.NullBooleanField()
    group_desc = models.CharField(max_length=50, blank=True, null=True)
    default_op = models.NullBooleanField()
    option_not = models.TextField(blank=True, null=True)
    sort_chars = models.CharField(max_length=10, blank=True, null=True)
    node_note = models.TextField(blank=True, null=True)
    shipsepera = models.NullBooleanField()
    bom_id = models.CharField(max_length=10, blank=True, null=True)
    include_on = models.NullBooleanField()
    scrap_perc = models.IntegerField(blank=True, null=True)
    seq_num = models.IntegerField(blank=True, null=True)
    chipweight = models.FloatField(blank=True, null=True)
    chip_cost = models.FloatField(blank=True, null=True)
    scraprecov = models.FloatField(blank=True, null=True)
    disable = models.NullBooleanField()
    noprice = models.NullBooleanField()
    rollup = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'bom'


class Bomdep(models.Model):
    bd_id = models.CharField(max_length=10, blank=True, null=True)
    bd_parent_field = models.CharField(db_column='bd_parent_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    bd_child_i = models.CharField(max_length=10, blank=True, null=True)
    bd_require = models.NullBooleanField()
    bd_childre = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'bomdep'


class Bomkit(models.Model):
    bk_id = models.CharField(max_length=10, blank=True, null=True)
    bk_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    bk_line_nu = models.IntegerField(blank=True, null=True)
    bk_invent_field = models.CharField(db_column='bk_invent_', max_length=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    bk_qty_per = models.FloatField(blank=True, null=True)
    bk_prod_co = models.CharField(max_length=2, blank=True, null=True)
    bk_unit_pr = models.FloatField(blank=True, null=True)
    bk_disc_pr = models.FloatField(blank=True, null=True)
    bk_ext_pri = models.FloatField(blank=True, null=True)
    bk_kit_inv = models.CharField(max_length=15, blank=True, null=True)
    bk_discoun = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bomkit'


class Box(models.Model):
    bx_id = models.CharField(max_length=10, blank=True, null=True)
    bx_invent_field = models.CharField(db_column='bx_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    bx_ct_id = models.CharField(max_length=10, blank=True, null=True)
    bx_il_id = models.CharField(max_length=10, blank=True, null=True)
    bx_ib_id = models.CharField(max_length=10, blank=True, null=True)
    bx_type = models.CharField(max_length=3, blank=True, null=True)
    bx_quantit = models.FloatField(blank=True, null=True)
    bx_net_wgh = models.FloatField(blank=True, null=True)
    bx_tare_wg = models.FloatField(blank=True, null=True)
    bx_gross_w = models.FloatField(blank=True, null=True)
    bx_po_num = models.CharField(max_length=25, blank=True, null=True)
    bx_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    bx_op_num = models.IntegerField(blank=True, null=True)
    bx_date_pa = models.DateField(blank=True, null=True)
    bx_bulkbox = models.IntegerField(blank=True, null=True)
    bx_order_n = models.CharField(max_length=12, blank=True, null=True)
    bx_box_lot = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'box'


class BoxType(models.Model):
    bt_code = models.CharField(max_length=3, blank=True, null=True)
    bt_desc = models.CharField(max_length=25, blank=True, null=True)
    bt_tare_wt = models.FloatField(blank=True, null=True)
    bt_edi_pkg = models.CharField(max_length=5, blank=True, null=True)
    bt_type = models.CharField(max_length=1, blank=True, null=True)
    bt_length = models.FloatField(blank=True, null=True)
    bt_width = models.FloatField(blank=True, null=True)
    bt_height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'box_type'


class Bracket(models.Model):
    br_id = models.CharField(max_length=10, blank=True, null=True)
    br_high_cn = models.FloatField(blank=True, null=True)
    br_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    br_desc = models.CharField(max_length=25, blank=True, null=True)
    br_low_cnt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bracket'


class Brandlus(models.Model):
    bl_type = models.IntegerField(blank=True, null=True)
    bl_desc = models.CharField(max_length=40, blank=True, null=True)
    bl_active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'brandlus'


class CanAprv(models.Model):
    ca_id = models.CharField(max_length=10, blank=True, null=True)
    ca_emp_id = models.CharField(max_length=5, blank=True, null=True)
    ca_de_id = models.CharField(max_length=10, blank=True, null=True)
    ca_canchan = models.NullBooleanField()
    ca_canappr = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'can_aprv'


class Cateam(models.Model):
    ct_ca_id = models.CharField(max_length=10, blank=True, null=True)
    ct_emp_id = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cateam'


class Ccards(models.Model):
    cc_id = models.CharField(max_length=10, blank=True, null=True)
    cc_cust_co = models.CharField(max_length=6, blank=True, null=True)
    cc_type = models.CharField(max_length=1, blank=True, null=True)
    cc_credit_field = models.CharField(db_column='cc_credit_', max_length=40, blank=True, null=True)  # Field renamed because it ended with '_'.
    cc_cardhol = models.CharField(max_length=40, blank=True, null=True)
    cc_expirat = models.CharField(max_length=40, blank=True, null=True)
    cc_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ccards'


class Certaval(models.Model):
    ca_id = models.CharField(max_length=10, blank=True, null=True)
    ca_ch_id = models.CharField(max_length=10, blank=True, null=True)
    ca_cert_ch = models.CharField(max_length=10, blank=True, null=True)
    ca_ship_co = models.CharField(max_length=8, blank=True, null=True)
    ca_shipped = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'certaval'


class Certhead(models.Model):
    ch_id = models.CharField(max_length=10, blank=True, null=True)
    ch_ship_co = models.CharField(max_length=8, blank=True, null=True)
    ch_ship_da = models.DateField(blank=True, null=True)
    ch_ship_qt = models.IntegerField(blank=True, null=True)
    ch_po_num = models.CharField(max_length=25, blank=True, null=True)
    ch_cust_co = models.CharField(max_length=6, blank=True, null=True)
    ch_cust_na = models.CharField(max_length=33, blank=True, null=True)
    ch_address = models.CharField(max_length=33, blank=True, null=True)
    ch_addres2 = models.CharField(max_length=33, blank=True, null=True)
    ch_addres3 = models.CharField(max_length=33, blank=True, null=True)
    ch_invent_field = models.CharField(db_column='ch_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ch_part_nu = models.CharField(max_length=30, blank=True, null=True)
    ch_rev_num = models.CharField(max_length=6, blank=True, null=True)
    ch_part_de = models.CharField(max_length=50, blank=True, null=True)
    ch_mat_fur = models.NullBooleanField()
    ch_mat_ref = models.CharField(max_length=15, blank=True, null=True)
    ch_mat = models.CharField(max_length=30, blank=True, null=True)
    ch_spec = models.CharField(max_length=30, blank=True, null=True)
    ch_rev = models.CharField(max_length=30, blank=True, null=True)
    ch_amend = models.CharField(max_length=30, blank=True, null=True)
    ch_notice = models.CharField(max_length=30, blank=True, null=True)
    ch_notes = models.TextField(blank=True, null=True)
    ch_sig_nam = models.CharField(max_length=35, blank=True, null=True)
    ch_sig_tit = models.CharField(max_length=35, blank=True, null=True)
    ch_sig_dat = models.DateField(blank=True, null=True)
    ch_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    ch_line_nu = models.IntegerField(blank=True, null=True)
    ch_raw_inv = models.CharField(max_length=30, blank=True, null=True)
    ch_line_no = models.IntegerField(blank=True, null=True)
    ch_rel_no = models.IntegerField(blank=True, null=True)
    ch_misc_no = models.TextField(blank=True, null=True)
    ch_shipped = models.NullBooleanField()
    ch_status = models.CharField(max_length=1, blank=True, null=True)
    ch_batch = models.CharField(max_length=30, blank=True, null=True)
    ch_availab = models.NullBooleanField()
    ch_org_qty = models.FloatField(blank=True, null=True)
    ch_order_n = models.CharField(max_length=12, blank=True, null=True)
    ch_lots_no = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'certhead'


class Certlot(models.Model):
    cl_id = models.CharField(max_length=10, blank=True, null=True)
    cl_ch_id = models.CharField(max_length=10, blank=True, null=True)
    cl_line_nu = models.IntegerField(blank=True, null=True)
    cl_lot_qty = models.IntegerField(blank=True, null=True)
    cl_process = models.CharField(max_length=20, blank=True, null=True)
    cl_spec = models.CharField(max_length=20, blank=True, null=True)
    cl_rev = models.CharField(max_length=3, blank=True, null=True)
    cl_amd = models.CharField(max_length=3, blank=True, null=True)
    cl_not = models.CharField(max_length=3, blank=True, null=True)
    cl_heat_nu = models.CharField(max_length=15, blank=True, null=True)
    cl_supp_co = models.CharField(max_length=6, blank=True, null=True)
    cl_supp_na = models.CharField(max_length=30, blank=True, null=True)
    cl_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certlot'


class Certship(models.Model):
    cs_id = models.CharField(max_length=10, blank=True, null=True)
    cs_ch_id = models.CharField(max_length=10, blank=True, null=True)
    cs_line_nu = models.IntegerField(blank=True, null=True)
    cs_ship_qt = models.IntegerField(blank=True, null=True)
    cs_lot_num = models.CharField(max_length=20, blank=True, null=True)
    cs_heat_nu = models.CharField(max_length=15, blank=True, null=True)
    cs_supp_co = models.CharField(max_length=6, blank=True, null=True)
    cs_supp_na = models.CharField(max_length=30, blank=True, null=True)
    cs_meltsou = models.CharField(max_length=20, blank=True, null=True)
    cs_tag_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certship'


class Charges(models.Model):
    ch_carrier = models.CharField(max_length=10, blank=True, null=True)
    ch_descrip = models.CharField(max_length=60, blank=True, null=True)
    ch_fee = models.FloatField(blank=True, null=True)
    ch_per = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'charges'


class Contacts(models.Model):
    cc_id = models.CharField(max_length=10, blank=True, null=True)
    cc_cust_co = models.CharField(max_length=6, blank=True, null=True)
    cc_emp_id = models.CharField(max_length=5, blank=True, null=True)
    cc_name = models.CharField(max_length=25, blank=True, null=True)
    cc_address = models.NullBooleanField()
    cc_addres2 = models.CharField(max_length=35, blank=True, null=True)
    cc_addres3 = models.CharField(max_length=35, blank=True, null=True)
    cc_city = models.CharField(max_length=20, blank=True, null=True)
    cc_state = models.CharField(max_length=3, blank=True, null=True)
    cc_zip_cod = models.CharField(max_length=10, blank=True, null=True)
    cc_country = models.CharField(max_length=20, blank=True, null=True)
    cc_phone = models.CharField(max_length=14, blank=True, null=True)
    cc_phone_e = models.CharField(max_length=5, blank=True, null=True)
    cc_phone_c = models.CharField(max_length=14, blank=True, null=True)
    cc_fax = models.CharField(max_length=14, blank=True, null=True)
    cc_email = models.CharField(max_length=50, blank=True, null=True)
    cc_prime_c = models.NullBooleanField()
    cc_next_co = models.DateField(blank=True, null=True)
    cc_last_ca = models.DateField(blank=True, null=True)
    cc_departm = models.CharField(max_length=35, blank=True, null=True)
    cc_unit = models.CharField(max_length=35, blank=True, null=True)
    cc_positio = models.CharField(max_length=35, blank=True, null=True)
    cc_title = models.CharField(max_length=35, blank=True, null=True)
    cc_interes = models.IntegerField(blank=True, null=True)
    cc_dont_co = models.NullBooleanField()
    cc_dont_re = models.TextField(blank=True, null=True)
    cc_no_long = models.NullBooleanField()
    cc_left_ab = models.DateField(blank=True, null=True)
    cc_home_ph = models.CharField(max_length=14, blank=True, null=True)
    cc_cell_ph = models.CharField(max_length=14, blank=True, null=True)
    cc_pager = models.CharField(max_length=14, blank=True, null=True)
    cc_em_name = models.CharField(max_length=35, blank=True, null=True)
    cc_em_phon = models.CharField(max_length=14, blank=True, null=True)
    cc_em_fax = models.CharField(max_length=14, blank=True, null=True)
    cc_em_note = models.TextField(blank=True, null=True)
    cc_marital = models.IntegerField(blank=True, null=True)
    cc_childre = models.CharField(max_length=75, blank=True, null=True)
    cc_sex = models.IntegerField(blank=True, null=True)
    cc_age = models.IntegerField(blank=True, null=True)
    cc_age_in = models.IntegerField(blank=True, null=True)
    cc_intere2 = models.TextField(blank=True, null=True)
    cc_eh_name = models.CharField(max_length=35, blank=True, null=True)
    cc_eh_role = models.CharField(max_length=35, blank=True, null=True)
    cc_eh_city = models.CharField(max_length=20, blank=True, null=True)
    cc_eh_stat = models.CharField(max_length=2, blank=True, null=True)
    cc_eh_left = models.DateField(blank=True, null=True)
    cc_eh_note = models.TextField(blank=True, null=True)
    cc_notes = models.TextField(blank=True, null=True)
    cc_created = models.CharField(max_length=5, blank=True, null=True)
    cc_create2 = models.DateTimeField(blank=True, null=True)
    cc_last_lo = models.CharField(max_length=5, blank=True, null=True)
    cc_last_up = models.DateTimeField(blank=True, null=True)
    cc_call_cy = models.CharField(max_length=20, blank=True, null=True)
    cc_salutat = models.CharField(max_length=15, blank=True, null=True)
    cc_supp_co = models.CharField(max_length=6, blank=True, null=True)
    cc_ap_pers = models.NullBooleanField()
    cc_type = models.CharField(max_length=10, blank=True, null=True)
    cc_sales_c = models.NullBooleanField()
    cc_ca_id = models.CharField(max_length=10, blank=True, null=True)
    cc_teritor = models.IntegerField(blank=True, null=True)
    cc_inactiv = models.NullBooleanField()
    cc_email1 = models.CharField(max_length=50, blank=True, null=True)
    cc_email2 = models.CharField(max_length=50, blank=True, null=True)
    cc_email3 = models.CharField(max_length=50, blank=True, null=True)
    cc_email1_d = models.CharField(max_length=20, blank=True, null=True)
    cc_email2_d = models.CharField(max_length=20, blank=True, null=True)
    cc_email3_d = models.CharField(max_length=20, blank=True, null=True)
    cc_locatio = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class Contain(models.Model):
    ct_id = models.CharField(max_length=10, blank=True, null=True)
    ct_il_id = models.CharField(max_length=10, blank=True, null=True)
    ct_ib_id = models.CharField(max_length=10, blank=True, null=True)
    ct_ship_co = models.CharField(max_length=8, blank=True, null=True)
    ct_sd_id = models.IntegerField(blank=True, null=True)
    ct_tare_wg = models.FloatField(blank=True, null=True)
    ct_type = models.CharField(max_length=3, blank=True, null=True)
    ct_invent_field = models.CharField(db_column='ct_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ct_tot_box = models.IntegerField(blank=True, null=True)
    ct_order_n = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contain'


class Contanpo(models.Model):
    cp_id = models.CharField(max_length=10, blank=True, null=True)
    cp_po_num = models.CharField(max_length=7, blank=True, null=True)
    cp_line_nu = models.IntegerField(blank=True, null=True)
    cp_ct_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contanpo'


class Contimp(models.Model):
    ct_id = models.CharField(max_length=10, blank=True, null=True)
    ct_date = models.DateField(blank=True, null=True)
    ct_dept = models.CharField(max_length=30, blank=True, null=True)
    ct_area = models.CharField(max_length=50, blank=True, null=True)
    ct_emp_id = models.CharField(max_length=5, blank=True, null=True)
    ct_title = models.CharField(max_length=30, blank=True, null=True)
    ct_improve = models.TextField(blank=True, null=True)
    ct_just_da = models.DateField(blank=True, null=True)
    ct_justifi = models.TextField(blank=True, null=True)
    ct_total_c = models.FloatField(blank=True, null=True)
    ct_cost_de = models.CharField(max_length=50, blank=True, null=True)
    ct_savings = models.FloatField(blank=True, null=True)
    ct_saving2 = models.CharField(max_length=50, blank=True, null=True)
    ct_due_dat = models.DateField(blank=True, null=True)
    ct_new_due = models.DateField(blank=True, null=True)
    ct_approve = models.NullBooleanField()
    ct_complet = models.NullBooleanField()
    ct_date_co = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contimp'


class Corrdet(models.Model):
    cd_id = models.CharField(max_length=10, blank=True, null=True)
    cd_ca_id = models.CharField(max_length=10, blank=True, null=True)
    cd_emp_id = models.CharField(max_length=5, blank=True, null=True)
    cd_positio = models.CharField(max_length=30, blank=True, null=True)
    cd_desc = models.TextField(blank=True, null=True)
    cd_comp_da = models.DateField(blank=True, null=True)
    cd_status = models.CharField(max_length=1, blank=True, null=True)
    cd_type = models.CharField(max_length=10, blank=True, null=True)
    cd_phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corrdet'


class CostDet(models.Model):
    ct_quote_n = models.CharField(max_length=15, blank=True, null=True)
    ct_order_n = models.CharField(max_length=12, blank=True, null=True)
    ct_id = models.IntegerField(blank=True, null=True)
    ct_supp = models.CharField(max_length=6, blank=True, null=True)
    ct_desc = models.CharField(max_length=60, blank=True, null=True)
    ct_cost = models.FloatField(blank=True, null=True)
    ct_q = models.FloatField(blank=True, null=True)
    ct_uc = models.FloatField(blank=True, null=True)
    ct_dist_co = models.CharField(max_length=2, blank=True, null=True)
    ct_inc_quo = models.NullBooleanField()
    ct_invoice = models.NullBooleanField()
    ct_inv_num = models.CharField(max_length=7, blank=True, null=True)
    ct_entry_d = models.DateField(blank=True, null=True)
    ct_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    ct_id_code = models.CharField(max_length=10, blank=True, null=True)
    ct_de_id = models.CharField(max_length=10, blank=True, null=True)
    ct_freight = models.NullBooleanField()
    ct_ad_id = models.CharField(max_length=10, blank=True, null=True)
    ct_wp_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_det'


class CostTot(models.Model):
    cl_quote_n = models.CharField(max_length=15, blank=True, null=True)
    cl_order_n = models.CharField(max_length=12, blank=True, null=True)
    cl_dist_co = models.CharField(max_length=2, blank=True, null=True)
    cl_est_cos = models.FloatField(blank=True, null=True)
    cl_act_cos = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_tot'


class Country(models.Model):
    co_id = models.CharField(max_length=10, blank=True, null=True)
    co_name = models.CharField(max_length=25, blank=True, null=True)
    co_exclude = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'country'


class Counts(models.Model):
    co_id = models.CharField(max_length=10, blank=True, null=True)
    co_aj_id = models.CharField(max_length=10, blank=True, null=True)
    co_date_ti = models.DateTimeField(blank=True, null=True)
    co_user = models.CharField(max_length=5, blank=True, null=True)
    co_prod = models.FloatField(blank=True, null=True)
    co_review = models.FloatField(blank=True, null=True)
    co_scrap = models.FloatField(blank=True, null=True)
    co_good = models.FloatField(blank=True, null=True)
    co_notes = models.TextField(blank=True, null=True)
    co_down_re = models.CharField(max_length=80, blank=True, null=True)
    co_weight = models.FloatField(blank=True, null=True)
    co_lot_num = models.CharField(max_length=20, blank=True, null=True)
    co_il_id = models.CharField(max_length=10, blank=True, null=True)
    co_ib_id = models.CharField(max_length=10, blank=True, null=True)
    co_ij_id = models.CharField(max_length=10, blank=True, null=True)
    co_invent_field = models.CharField(db_column='co_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    co_sc_ij_i = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counts'


class Cprice(models.Model):
    cp_id = models.CharField(max_length=6, blank=True, null=True)
    cp_st_id = models.CharField(max_length=6, blank=True, null=True)
    cp_ma_id = models.CharField(max_length=6, blank=True, null=True)
    cp_cust_co = models.CharField(max_length=6, blank=True, null=True)
    cp_unit_pr = models.FloatField(blank=True, null=True)
    cp_emp_id = models.CharField(max_length=5, blank=True, null=True)
    cp_eff_dat = models.DateField(blank=True, null=True)
    cp_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cprice'


class CstmCat(models.Model):
    cc_id = models.CharField(max_length=10, blank=True, null=True)
    cc_cat = models.CharField(max_length=80, blank=True, null=True)
    cc_type = models.CharField(max_length=5, blank=True, null=True)
    cc_seq = models.IntegerField(blank=True, null=True)
    cc_cf_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cstm_cat'


class Cstmform(models.Model):
    cf_id = models.CharField(max_length=10, blank=True, null=True)
    cf_report_field = models.CharField(db_column='cf_report_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    cf_referen = models.CharField(max_length=20, blank=True, null=True)
    cf_quote = models.NullBooleanField()
    cf_sord = models.NullBooleanField()
    cf_shop = models.NullBooleanField()
    cf_custome = models.NullBooleanField()
    cf_vendor = models.NullBooleanField()
    cf_invento = models.NullBooleanField()
    cf_action = models.NullBooleanField()
    cf_note = models.TextField(blank=True, null=True)
    cf_invoice = models.NullBooleanField()
    cf_ac_apin = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'cstmform'


class Cstmprop(models.Model):
    pr_id = models.CharField(max_length=10, blank=True, null=True)
    pr_label = models.CharField(max_length=40, blank=True, null=True)
    pr_cc_id = models.CharField(max_length=10, blank=True, null=True)
    pr_type = models.CharField(max_length=5, blank=True, null=True)
    pr_seq = models.IntegerField(blank=True, null=True)
    pr_note = models.TextField(blank=True, null=True)
    pr_field_t = models.IntegerField(blank=True, null=True)
    pr_show = models.NullBooleanField()
    pr_cf_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cstmprop'


class Currates(models.Model):
    cr_id = models.CharField(max_length=10, blank=True, null=True)
    cr_code = models.CharField(max_length=10, blank=True, null=True)
    cr_buy = models.FloatField(blank=True, null=True)
    cr_sell = models.FloatField(blank=True, null=True)
    cr_date = models.DateField(blank=True, null=True)
    cr_inact = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'currates'


class Custspec(models.Model):
    cs_id = models.CharField(max_length=10, blank=True, null=True)
    cs_cust_co = models.CharField(max_length=6, blank=True, null=True)
    cs_cust_sp = models.CharField(max_length=30, blank=True, null=True)
    cs_st_id = models.CharField(max_length=10, blank=True, null=True)
    cs_obsolet = models.NullBooleanField()
    cs_sg_id = models.CharField(max_length=10, blank=True, null=True)
    cs_supp_co = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custspec'


class Custstat(models.Model):
    cs_cust_co = models.CharField(max_length=6, blank=True, null=True)
    cs_freqofs = models.IntegerField(blank=True, null=True)
    cs_datelas = models.DateField(blank=True, null=True)
    cs_yearhig = models.FloatField(blank=True, null=True)
    cs_creditl = models.FloatField(blank=True, null=True)
    cs_ytdsale = models.FloatField(blank=True, null=True)
    cs_balance = models.FloatField(blank=True, null=True)
    cs_pastdue = models.FloatField(blank=True, null=True)
    cs_avgdays = models.IntegerField(blank=True, null=True)
    cs_uninvsh = models.FloatField(blank=True, null=True)
    cs_unships = models.FloatField(blank=True, null=True)
    cs_opencre = models.FloatField(blank=True, null=True)
    cs_totpend = models.FloatField(blank=True, null=True)
    cs_availcr = models.FloatField(blank=True, null=True)
    cs_credith = models.CharField(max_length=30, blank=True, null=True)
    cs_currbal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custstat'


class CvType(models.Model):
    cv_code = models.CharField(max_length=5, blank=True, null=True)
    cv_desc = models.CharField(max_length=30, blank=True, null=True)
    cv_rgb = models.IntegerField(blank=True, null=True)
    cv_forewhi = models.NullBooleanField()
    cv_po_memo = models.TextField(blank=True, null=True)
    cv_pricebr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv_type'


class Cyclecnt(models.Model):
    cc_id = models.CharField(max_length=10, blank=True, null=True)
    cc_batch = models.IntegerField(blank=True, null=True)
    cc_il_id = models.CharField(max_length=10, blank=True, null=True)
    cc_ib_id = models.CharField(max_length=10, blank=True, null=True)
    cc_ic_tag_field = models.IntegerField(db_column='cc_ic_tag_', blank=True, null=True)  # Field renamed because it ended with '_'.
    cc_ic_id = models.CharField(max_length=10, blank=True, null=True)
    cc_emp_id = models.CharField(max_length=5, blank=True, null=True)
    cc_date = models.DateField(blank=True, null=True)
    cc_quantit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cyclecnt'


class DaNodtl(models.Model):
    nd_id = models.CharField(max_length=10, blank=True, null=True)
    nd_no_id = models.CharField(max_length=10, blank=True, null=True)
    nd_ni_id = models.CharField(max_length=10, blank=True, null=True)
    nd_nc_id = models.CharField(max_length=10, blank=True, null=True)
    nd_emp_id = models.CharField(max_length=5, blank=True, null=True)
    nd_follow_field = models.DateField(db_column='nd_follow_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nd_complet = models.IntegerField(blank=True, null=True)
    nd_outcome = models.CharField(max_length=35, blank=True, null=True)
    nd_outcom2 = models.TextField(blank=True, null=True)
    nd_last_lo = models.CharField(max_length=10, blank=True, null=True)
    nd_last_up = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'da_nodtl'


class DaNokwd(models.Model):
    nk_id = models.CharField(max_length=10, blank=True, null=True)
    nk_desc = models.CharField(max_length=35, blank=True, null=True)
    nk_last_lo = models.CharField(max_length=10, blank=True, null=True)
    nk_last_up = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'da_nokwd'


class DaNomth(models.Model):
    nm_id = models.CharField(max_length=10, blank=True, null=True)
    nm_desc = models.CharField(max_length=35, blank=True, null=True)
    nm_abbrev = models.CharField(max_length=5, blank=True, null=True)
    nm_default = models.CharField(max_length=1, blank=True, null=True)
    nm_last_lo = models.CharField(max_length=10, blank=True, null=True)
    nm_last_up = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'da_nomth'


class DaNoprb(models.Model):
    np_id = models.CharField(max_length=10, blank=True, null=True)
    np_desc = models.CharField(max_length=35, blank=True, null=True)
    np_last_lo = models.CharField(max_length=10, blank=True, null=True)
    np_last_up = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'da_noprb'


class DaNosbj(models.Model):
    ns_id = models.CharField(max_length=10, blank=True, null=True)
    ns_nt_id = models.CharField(max_length=10, blank=True, null=True)
    ns_desc = models.CharField(max_length=35, blank=True, null=True)
    ns_last_lo = models.CharField(max_length=10, blank=True, null=True)
    ns_last_up = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'da_nosbj'


class DaNotcm(models.Model):
    nc_id = models.CharField(max_length=10, blank=True, null=True)
    nc_ns_id = models.CharField(max_length=10, blank=True, null=True)
    nc_desc = models.CharField(max_length=35, blank=True, null=True)
    nc_last_lo = models.CharField(max_length=10, blank=True, null=True)
    nc_last_up = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'da_notcm'


class DaNotes(models.Model):
    no_id = models.CharField(max_length=10, blank=True, null=True)
    no_cust_co = models.CharField(max_length=6, blank=True, null=True)
    no_cc_id = models.CharField(max_length=10, blank=True, null=True)
    no_emp_id = models.CharField(max_length=5, blank=True, null=True)
    no_order_n = models.CharField(max_length=12, blank=True, null=True)
    no_nt_id = models.CharField(max_length=10, blank=True, null=True)
    no_ns_id = models.CharField(max_length=10, blank=True, null=True)
    no_np_id = models.CharField(max_length=10, blank=True, null=True)
    no_nm_id = models.CharField(max_length=10, blank=True, null=True)
    no_nr_id = models.CharField(max_length=10, blank=True, null=True)
    no_status = models.CharField(max_length=1, blank=True, null=True)
    no_date = models.DateField(blank=True, null=True)
    no_time = models.CharField(max_length=5, blank=True, null=True)
    no_initiat = models.IntegerField(blank=True, null=True)
    no_importa = models.IntegerField(blank=True, null=True)
    no_priorit = models.NullBooleanField()
    no_problem = models.NullBooleanField()
    no_order = models.CharField(max_length=10, blank=True, null=True)
    no_credit = models.FloatField(blank=True, null=True)
    no_text = models.TextField(blank=True, null=True)
    no_created = models.CharField(max_length=10, blank=True, null=True)
    no_create2 = models.DateTimeField(blank=True, null=True)
    no_last_lo = models.CharField(max_length=10, blank=True, null=True)
    no_last_up = models.DateTimeField(blank=True, null=True)
    no_invent_field = models.CharField(db_column='no_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    no_part_nu = models.CharField(max_length=30, blank=True, null=True)
    no_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    no_followu = models.DateField(blank=True, null=True)
    no_na_ncod = models.CharField(max_length=6, blank=True, null=True)
    no_nk_id = models.CharField(max_length=10, blank=True, null=True)
    no_prod_co = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'da_notes'


class DaNotpc(models.Model):
    ni_id = models.CharField(max_length=10, blank=True, null=True)
    ni_desc = models.CharField(max_length=35, blank=True, null=True)
    ni_last_lo = models.CharField(max_length=10, blank=True, null=True)
    ni_last_up = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'da_notpc'


class DaNotrg(models.Model):
    nr_id = models.CharField(max_length=10, blank=True, null=True)
    nr_desc = models.CharField(max_length=35, blank=True, null=True)
    nr_last_lo = models.CharField(max_length=10, blank=True, null=True)
    nr_last_up = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'da_notrg'


class DaNotyp(models.Model):
    nt_id = models.CharField(max_length=10, blank=True, null=True)
    nt_desc = models.CharField(max_length=35, blank=True, null=True)
    nt_abbrev = models.CharField(max_length=5, blank=True, null=True)
    nt_status = models.CharField(max_length=1, blank=True, null=True)
    nt_type = models.CharField(max_length=1, blank=True, null=True)
    nt_default = models.CharField(max_length=1, blank=True, null=True)
    nt_protect = models.NullBooleanField()
    nt_last_lo = models.CharField(max_length=10, blank=True, null=True)
    nt_last_up = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'da_notyp'


class Dashb(models.Model):
    db_id = models.CharField(max_length=10, blank=True, null=True)
    db_user_id = models.CharField(max_length=5, blank=True, null=True)
    db_dm_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashb'


class Dashmenu(models.Model):
    dm_id = models.CharField(max_length=10, blank=True, null=True)
    dm_option = models.CharField(max_length=50, blank=True, null=True)
    dm_orderby = models.IntegerField(blank=True, null=True)
    dm_windown = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashmenu'


class Datelog(models.Model):
    dl_order_n = models.CharField(max_length=12, blank=True, null=True)
    dl_datetim = models.DateTimeField(blank=True, null=True)
    dl_old_dat = models.DateField(blank=True, null=True)
    dl_new_dat = models.DateField(blank=True, null=True)
    dl_user_id = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datelog'


class Daystats(models.Model):
    ds_sorders = models.IntegerField(blank=True, null=True)
    ds_orders = models.IntegerField(blank=True, null=True)
    ds_quotes = models.IntegerField(blank=True, null=True)
    ds_sord_qu = models.IntegerField(blank=True, null=True)
    ds_shipmen = models.IntegerField(blank=True, null=True)
    ds_invoice = models.IntegerField(blank=True, null=True)
    ds_returns = models.IntegerField(blank=True, null=True)
    ds_sorder2 = models.FloatField(blank=True, null=True)
    ds_orders_field = models.FloatField(db_column='ds_orders_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ds_quotes_field = models.FloatField(db_column='ds_quotes_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ds_sord_q2 = models.FloatField(blank=True, null=True)
    ds_shipme2 = models.FloatField(blank=True, null=True)
    ds_invoic2 = models.FloatField(blank=True, null=True)
    ds_return2 = models.FloatField(blank=True, null=True)
    ds_date = models.DateField(blank=True, null=True)
    ds_period = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daystats'


class DefCal(models.Model):
    dc_m1 = models.FloatField(blank=True, null=True)
    dc_m2 = models.FloatField(blank=True, null=True)
    dc_m3 = models.FloatField(blank=True, null=True)
    dc_m4 = models.FloatField(blank=True, null=True)
    dc_m5 = models.FloatField(blank=True, null=True)
    dc_m6 = models.FloatField(blank=True, null=True)
    dc_m7 = models.FloatField(blank=True, null=True)
    dc_ot1 = models.FloatField(blank=True, null=True)
    dc_ot2 = models.FloatField(blank=True, null=True)
    dc_ot3 = models.FloatField(blank=True, null=True)
    dc_ot4 = models.FloatField(blank=True, null=True)
    dc_ot5 = models.FloatField(blank=True, null=True)
    dc_ot6 = models.FloatField(blank=True, null=True)
    dc_ot7 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'def_cal'


class Defmat(models.Model):
    dm_id = models.CharField(max_length=10, blank=True, null=True)
    dm_supp_co = models.CharField(max_length=6, blank=True, null=True)
    dm_mat_typ = models.CharField(max_length=6, blank=True, null=True)
    dm_shape_c = models.CharField(max_length=7, blank=True, null=True)
    dm_uom = models.CharField(max_length=2, blank=True, null=True)
    dm_cht_siz = models.FloatField(blank=True, null=True)
    dm_wide = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'defmat'


class Deftime(models.Model):
    s1_ci = models.CharField(max_length=10, blank=True, null=True)
    s1_co = models.CharField(max_length=10, blank=True, null=True)
    s1_lo = models.CharField(max_length=10, blank=True, null=True)
    s1_li = models.CharField(max_length=10, blank=True, null=True)
    s2_ci = models.CharField(max_length=10, blank=True, null=True)
    s2_co = models.CharField(max_length=10, blank=True, null=True)
    s2_lo = models.CharField(max_length=10, blank=True, null=True)
    s2_li = models.CharField(max_length=10, blank=True, null=True)
    s3_ci = models.CharField(max_length=10, blank=True, null=True)
    s3_co = models.CharField(max_length=10, blank=True, null=True)
    s3_lo = models.CharField(max_length=10, blank=True, null=True)
    s3_li = models.CharField(max_length=10, blank=True, null=True)
    r_limit = models.IntegerField(blank=True, null=True)
    jc_use = models.CharField(max_length=1, blank=True, null=True)
    tc_use = models.CharField(max_length=1, blank=True, null=True)
    minlunch = models.IntegerField(blank=True, null=True)
    animatetc = models.NullBooleanField()
    s_flag = models.NullBooleanField()
    td_flag = models.NullBooleanField()
    od_flag = models.NullBooleanField()
    bp_flag = models.NullBooleanField()
    bu_flag = models.NullBooleanField()
    lp_flag = models.NullBooleanField()
    lu_flag = models.NullBooleanField()
    qty_only_f = models.NullBooleanField()
    qty_review = models.NullBooleanField()
    qty_rework = models.NullBooleanField()
    qty_scrap = models.NullBooleanField()
    paperless = models.NullBooleanField()
    changetime = models.NullBooleanField()
    swipe_only = models.NullBooleanField()
    use_tscree = models.NullBooleanField()
    use_tcards = models.NullBooleanField()
    use_jcards = models.NullBooleanField()
    allow_shif = models.NullBooleanField()
    select_co_field = models.NullBooleanField(db_column='select_co_')  # Field renamed because it ended with '_'.
    ripple_rel = models.NullBooleanField()
    secure_am = models.NullBooleanField()
    supervisor = models.NullBooleanField()
    disable_jc = models.NullBooleanField()
    secure_exi = models.NullBooleanField()
    round15 = models.NullBooleanField()
    digits_onl = models.NullBooleanField()
    sort_by_la = models.NullBooleanField()
    no_emp_lis = models.NullBooleanField()
    dont_close = models.NullBooleanField()
    tcard_thre = models.IntegerField(blank=True, null=True)
    remove_key = models.NullBooleanField()
    simple_jc = models.NullBooleanField()
    consolidat = models.NullBooleanField()
    at_hours_a = models.FloatField(blank=True, null=True)
    ot_hours_a = models.FloatField(blank=True, null=True)
    le_leaves_field = models.IntegerField(db_column='le_leaves_', blank=True, null=True)  # Field renamed because it ended with '_'.
    manual_jc = models.NullBooleanField()
    timeserver = models.CharField(max_length=30, blank=True, null=True)
    bypassmatr = models.NullBooleanField()
    close_on_l = models.NullBooleanField()
    mon_refres = models.IntegerField(blank=True, null=True)
    wp_export_field = models.CharField(db_column='wp_export_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    wp_export2 = models.CharField(max_length=40, blank=True, null=True)
    remain_in_field = models.NullBooleanField(db_column='remain_in_')  # Field renamed because it ended with '_'.
    le_use_no_field = models.NullBooleanField(db_column='le_use_no_')  # Field renamed because it ended with '_'.
    use_timecl = models.NullBooleanField()
    enforce_30 = models.NullBooleanField()
    deptoverri = models.NullBooleanField()
    use_1_x2_bi = models.NullBooleanField()
    jobonly = models.NullBooleanField()
    eo_hours_a = models.NullBooleanField()
    hide_jc = models.NullBooleanField()
    sublot = models.NullBooleanField()
    round15_lu = models.NullBooleanField()
    hide_add_o = models.NullBooleanField()
    nojcwithou = models.NullBooleanField()
    nojcwithjc = models.NullBooleanField()
    notcwithjc = models.NullBooleanField()
    op_comp_fl = models.NullBooleanField()
    endofshift = models.NullBooleanField()
    quickjob = models.NullBooleanField()
    defaultqty = models.NullBooleanField()
    autojcout = models.IntegerField(blank=True, null=True)
    autooverti = models.NullBooleanField()
    showdie = models.NullBooleanField()
    diereport = models.NullBooleanField()
    showheat = models.NullBooleanField()
    at_include = models.NullBooleanField()
    roundjobca = models.NullBooleanField()
    round78 = models.NullBooleanField()
    clockoutpr = models.NullBooleanField()
    use_small_field = models.NullBooleanField(db_column='use_small_')  # Field renamed because it ended with '_'.
    autosave = models.NullBooleanField()
    nonpmultij = models.NullBooleanField()
    showlot_nu = models.NullBooleanField()
    roundtc15 = models.NullBooleanField()
    always15 = models.NullBooleanField()
    cycleonly = models.NullBooleanField()
    barcodekey = models.NullBooleanField()
    usecounter = models.NullBooleanField()
    showpace = models.NullBooleanField()
    showpaceba = models.TextField(blank=True, null=True)
    showpacego = models.TextField(blank=True, null=True)
    showtag = models.NullBooleanField()
    usetagasbi = models.NullBooleanField()
    teamlogin = models.NullBooleanField()
    hidelaborc = models.NullBooleanField()
    usetcdate = models.NullBooleanField()
    showtrilab = models.NullBooleanField()
    usefactors = models.NullBooleanField()
    alwayslunc = models.NullBooleanField()
    empasteris = models.NullBooleanField()
    jcfirst = models.NullBooleanField()
    nodecimals = models.NullBooleanField()
    stoponhold = models.NullBooleanField()
    autofilllu = models.NullBooleanField()
    simplejc = models.NullBooleanField()
    eci_thresh = models.IntegerField(blank=True, null=True)
    eci_messag = models.TextField(blank=True, null=True)
    defectcode = models.NullBooleanField()
    actionrequ = models.NullBooleanField()
    pausestart = models.NullBooleanField()
    printbinti = models.NullBooleanField()
    calc_perce = models.NullBooleanField()
    defaultmat = models.NullBooleanField()
    passinvent = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'deftime'


class Details(models.Model):
    de_id = models.CharField(max_length=10, blank=True, null=True)
    de_quote_n = models.CharField(max_length=15, blank=True, null=True)
    de_order_n = models.CharField(max_length=12, blank=True, null=True)
    de_seq_num = models.IntegerField(blank=True, null=True)
    de_desc = models.CharField(max_length=60, blank=True, null=True)
    de_pr_id = models.IntegerField(blank=True, null=True)
    de_op_num = models.IntegerField(blank=True, null=True)
    de_hours = models.FloatField(blank=True, null=True)
    de_default = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'details'


class Deviate(models.Model):
    de_id = models.CharField(max_length=10, blank=True, null=True)
    de_cust_co = models.CharField(max_length=6, blank=True, null=True)
    de_invent_field = models.CharField(db_column='de_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    de_part_nu = models.CharField(max_length=30, blank=True, null=True)
    de_part_de = models.CharField(max_length=50, blank=True, null=True)
    de_cust_c2 = models.CharField(max_length=40, blank=True, null=True)
    de_phone = models.CharField(max_length=15, blank=True, null=True)
    de_type = models.IntegerField(blank=True, null=True)
    de_request = models.TextField(blank=True, null=True)
    de_reason = models.TextField(blank=True, null=True)
    de_status = models.CharField(max_length=1, blank=True, null=True)
    de_accept = models.IntegerField(blank=True, null=True)
    de_date = models.DateField(blank=True, null=True)
    de_datesig = models.DateField(blank=True, null=True)
    de_devnum = models.CharField(max_length=50, blank=True, null=True)
    de_empby = models.CharField(max_length=5, blank=True, null=True)
    de_expdate = models.DateField(blank=True, null=True)
    de_ca_id = models.CharField(max_length=10, blank=True, null=True)
    de_draw = models.NullBooleanField()
    de_ca_need = models.NullBooleanField()
    de_desc = models.CharField(max_length=100, blank=True, null=True)
    de_comment = models.TextField(blank=True, null=True)
    de_quantit = models.IntegerField(blank=True, null=True)
    de_nc_id = models.CharField(max_length=10, blank=True, null=True)
    de_qty_typ = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deviate'


class Dist(models.Model):
    dt_dist_co = models.CharField(max_length=2, blank=True, null=True)
    dt_dist_de = models.CharField(max_length=40, blank=True, null=True)
    dt_gl_numb = models.CharField(max_length=12, blank=True, null=True)
    dt_editabl = models.NullBooleanField()
    dt_one_tim = models.NullBooleanField()
    dt_po_note = models.TextField(blank=True, null=True)
    dt_rawmate = models.IntegerField(blank=True, null=True)
    dt_non_tax = models.NullBooleanField()
    dt_de_id = models.CharField(max_length=2, blank=True, null=True)
    dt_po_ws = models.IntegerField(blank=True, null=True)
    dt_excl_di = models.NullBooleanField()
    dt_raw_gl_field = models.CharField(db_column='dt_raw_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    dt_pur_to_field = models.NullBooleanField(db_column='dt_pur_to_')  # Field renamed because it ended with '_'.
    dt_tooling = models.NullBooleanField()
    dt_lb_cost = models.FloatField(blank=True, null=True)
    dt_prod_co = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dist'


class DistDet(models.Model):
    dd_id = models.IntegerField(blank=True, null=True)
    dd_dl_id = models.IntegerField(blank=True, null=True)
    dd_user_id = models.CharField(max_length=5, blank=True, null=True)
    dd_email = models.CharField(max_length=40, blank=True, null=True)
    dd_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dist_det'


class Distlist(models.Model):
    dl_id = models.IntegerField(blank=True, null=True)
    dl_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distlist'


class DocCat(models.Model):
    dc_doc_typ = models.CharField(max_length=10, blank=True, null=True)
    dc_doc_des = models.CharField(max_length=30, blank=True, null=True)
    dc_applica = models.CharField(max_length=30, blank=True, null=True)
    dc_approve = models.CharField(max_length=20, blank=True, null=True)
    dc_process = models.CharField(max_length=30, blank=True, null=True)
    dc_outside = models.CharField(max_length=60, blank=True, null=True)
    dc_control = models.NullBooleanField()
    dc_prefix = models.CharField(max_length=2, blank=True, null=True)
    dc_emp_id = models.CharField(max_length=5, blank=True, null=True)
    dc_doc_gro = models.IntegerField(blank=True, null=True)
    dc_de_id = models.CharField(max_length=2, blank=True, null=True)
    dc_multipl = models.NullBooleanField()
    dc_docpath = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_cat'


class DocMan(models.Model):
    dm_id = models.IntegerField(blank=True, null=True)
    dm_doc_typ = models.CharField(max_length=10, blank=True, null=True)
    dm_desc = models.CharField(max_length=50, blank=True, null=True)
    dm_quote_n = models.CharField(max_length=15, blank=True, null=True)
    dm_order_n = models.CharField(max_length=12, blank=True, null=True)
    dm_cust_co = models.CharField(max_length=6, blank=True, null=True)
    dm_part_nu = models.CharField(max_length=30, blank=True, null=True)
    dm_rev_num = models.CharField(max_length=6, blank=True, null=True)
    dm_last_up = models.DateField(blank=True, null=True)
    dm_file = models.CharField(max_length=254, blank=True, null=True)
    dm_memo = models.TextField(blank=True, null=True)
    dm_invent_field = models.CharField(db_column='dm_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    dm_lot_num = models.CharField(max_length=20, blank=True, null=True)
    dm_rec_no = models.IntegerField(blank=True, null=True)
    dm_on_rout = models.NullBooleanField()
    dm_on_pack = models.NullBooleanField()
    dm_view_wi = models.IntegerField(blank=True, null=True)
    dm_po_no = models.CharField(max_length=25, blank=True, null=True)
    dm_prompt_field = models.NullBooleanField(db_column='dm_prompt_')  # Field renamed because it ended with '_'.
    dm_doc_num = models.CharField(max_length=30, blank=True, null=True)
    dm_doc_rev = models.CharField(max_length=3, blank=True, null=True)
    dm_de_id = models.CharField(max_length=2, blank=True, null=True)
    dm_appr_re = models.NullBooleanField()
    dm_appr_da = models.DateField(blank=True, null=True)
    dm_iso_sta = models.CharField(max_length=10, blank=True, null=True)
    dm_doc = models.CharField(max_length=4, blank=True, null=True)
    dm_control = models.NullBooleanField()
    dm_emp_id = models.CharField(max_length=5, blank=True, null=True)
    dm_status = models.CharField(max_length=1, blank=True, null=True)
    dm_supp_co = models.CharField(max_length=6, blank=True, null=True)
    dm_mach_co = models.CharField(max_length=5, blank=True, null=True)
    dm_op_num = models.IntegerField(blank=True, null=True)
    dm_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    dm_line_nu = models.IntegerField(blank=True, null=True)
    dm_on_em_r = models.NullBooleanField()
    dm_tr_id = models.CharField(max_length=10, blank=True, null=True)
    dm_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    dm_dev_id = models.CharField(max_length=10, blank=True, null=True)
    dm_nc_id = models.CharField(max_length=10, blank=True, null=True)
    dm_car_id = models.CharField(max_length=10, blank=True, null=True)
    dm_ch_id = models.CharField(max_length=10, blank=True, null=True)
    dm_st_id = models.CharField(max_length=10, blank=True, null=True)
    dm_gj_id = models.CharField(max_length=10, blank=True, null=True)
    dm_showonc = models.NullBooleanField()
    dm_protect = models.NullBooleanField()
    dm_defined = models.CharField(max_length=5, blank=True, null=True)
    dm_sordq = models.CharField(max_length=7, blank=True, null=True)
    dm_on_cofc = models.NullBooleanField()
    dm_on_po = models.NullBooleanField()
    dm_pt_id = models.CharField(max_length=10, blank=True, null=True)
    dm_ps_id = models.CharField(max_length=10, blank=True, null=True)
    dm_pm_id = models.CharField(max_length=10, blank=True, null=True)
    dmst_id = models.CharField(max_length=10, blank=True, null=True)
    dm_wl_id = models.CharField(max_length=10, blank=True, null=True)
    dm_po_id = models.CharField(max_length=10, blank=True, null=True)
    dm_ldratio = models.CharField(max_length=10, blank=True, null=True)
    dm_oal = models.CharField(max_length=10, blank=True, null=True)
    dm_oempart = models.CharField(max_length=50, blank=True, null=True)
    dm_mi_id = models.CharField(max_length=10, blank=True, null=True)
    dm_gage_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_man'


class Dtreason(models.Model):
    dr_code = models.CharField(max_length=5, blank=True, null=True)
    dr_desc = models.CharField(max_length=30, blank=True, null=True)
    dr_rgb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dtreason'


class Earnhrs(models.Model):
    jc_run_dat = models.DateField(blank=True, null=True)
    jc_shift = models.CharField(max_length=2, blank=True, null=True)
    jc_mach_co = models.CharField(max_length=5, blank=True, null=True)
    jc_order_n = models.CharField(max_length=12, blank=True, null=True)
    or_order_r = models.CharField(max_length=21, blank=True, null=True)
    or_quote_n = models.CharField(max_length=15, blank=True, null=True)
    jc_parts_g = models.FloatField(blank=True, null=True)
    jc_setup = models.FloatField(blank=True, null=True)
    jc_run = models.FloatField(blank=True, null=True)
    jc_gp = models.FloatField(blank=True, null=True)
    jc_adj_phr = models.FloatField(blank=True, null=True)
    jc_go_eff = models.FloatField(blank=True, null=True)
    jc_p_eff = models.FloatField(blank=True, null=True)
    jc_o_eff = models.FloatField(blank=True, null=True)
    jc_eff = models.FloatField(blank=True, null=True)
    jc_std_eff = models.FloatField(blank=True, null=True)
    jc_operati = models.IntegerField(blank=True, null=True)
    op_suhr = models.FloatField(blank=True, null=True)
    op_gp = models.FloatField(blank=True, null=True)
    op_np = models.FloatField(blank=True, null=True)
    or_part_nu = models.CharField(max_length=30, blank=True, null=True)
    or_invent_field = models.CharField(db_column='or_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    jc_hrs_set = models.FloatField(blank=True, null=True)
    jc_accum_h = models.FloatField(blank=True, null=True)
    jc_hrs_ava = models.FloatField(blank=True, null=True)
    jc_hrs_pro = models.FloatField(blank=True, null=True)
    jc_num_mac = models.IntegerField(blank=True, null=True)
    em_emp_nam = models.CharField(max_length=40, blank=True, null=True)
    em_emp_id = models.CharField(max_length=5, blank=True, null=True)
    spr_code = models.CharField(max_length=1, blank=True, null=True)
    tc_tot_tim = models.FloatField(blank=True, null=True)
    or_cust_co = models.CharField(max_length=6, blank=True, null=True)
    cu_cust_na = models.CharField(max_length=35, blank=True, null=True)
    dept_id = models.CharField(max_length=2, blank=True, null=True)
    std_mpp = models.FloatField(blank=True, null=True)
    act_mpp = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    earned_hrs = models.FloatField(blank=True, null=True)
    earned_hr2 = models.FloatField(blank=True, null=True)
    earned_rat = models.FloatField(blank=True, null=True)
    dept_ratio = models.FloatField(blank=True, null=True)
    mt_mach_de = models.CharField(max_length=20, blank=True, null=True)
    dept_name = models.CharField(max_length=30, blank=True, null=True)
    jc_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'earnhrs'


class EcoDocs(models.Model):
    ed_id = models.CharField(max_length=10, blank=True, null=True)
    ed_ec_id = models.CharField(max_length=10, blank=True, null=True)
    ed_note = models.TextField(blank=True, null=True)
    ed_emp_id = models.CharField(max_length=5, blank=True, null=True)
    ed_date = models.DateField(blank=True, null=True)
    ed_doc_num = models.CharField(max_length=30, blank=True, null=True)
    ed_rev_num = models.CharField(max_length=3, blank=True, null=True)
    ed_doc_mod = models.IntegerField(blank=True, null=True)
    ed_assigne = models.CharField(max_length=5, blank=True, null=True)
    ed_assign2 = models.DateField(blank=True, null=True)
    ed_updated = models.NullBooleanField()
    ed_update_field = models.DateField(db_column='ed_update_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ed_old_doc = models.CharField(max_length=30, blank=True, null=True)
    ed_new_doc = models.CharField(max_length=30, blank=True, null=True)
    ed_state = models.CharField(max_length=10, blank=True, null=True)
    ed_de_id = models.CharField(max_length=2, blank=True, null=True)
    ed_assign3 = models.CharField(max_length=5, blank=True, null=True)
    ed_dc_doc_field = models.CharField(db_column='ed_dc_doc_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'eco_docs'


class EdiAck1(models.Model):
    ek_code = models.CharField(max_length=2, blank=True, null=True)
    ek_desc = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_ack1'


class EdiEd(models.Model):
    ee_code = models.CharField(max_length=2, blank=True, null=True)
    ee_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_ed'


class EdiGs(models.Model):
    eg_cust_co = models.CharField(max_length=6, blank=True, null=True)
    eg_qs_id = models.CharField(max_length=10, blank=True, null=True)
    eg_resp_ag = models.CharField(max_length=2, blank=True, null=True)
    eg_version = models.CharField(max_length=12, blank=True, null=True)
    eg_fgid_cu = models.CharField(max_length=12, blank=True, null=True)
    eg_fgid_co = models.CharField(max_length=12, blank=True, null=True)
    eg_grp_ctr = models.IntegerField(blank=True, null=True)
    eg_grp_ct2 = models.IntegerField(blank=True, null=True)
    eg_ca_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_gs'


class EdiLoci(models.Model):
    li_code = models.CharField(max_length=5, blank=True, null=True)
    li_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_loci'


class EdiLocq(models.Model):
    lq_code = models.CharField(max_length=2, blank=True, null=True)
    lq_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_locq'


class EdiMode(models.Model):
    em_code = models.CharField(max_length=2, blank=True, null=True)
    em_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_mode'


class EdiPsid(models.Model):
    ep_code = models.CharField(max_length=2, blank=True, null=True)
    ep_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_psid'


class EdiRefn(models.Model):
    er_code = models.CharField(max_length=2, blank=True, null=True)
    er_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_refn'


class EdiSt(models.Model):
    es_cust_co = models.CharField(max_length=6, blank=True, null=True)
    es_qs_id = models.CharField(max_length=10, blank=True, null=True)
    es_trans_c = models.CharField(max_length=3, blank=True, null=True)
    es_funct_i = models.CharField(max_length=2, blank=True, null=True)
    es_send_ac = models.NullBooleanField()
    es_set_con = models.IntegerField(blank=True, null=True)
    es_set_co2 = models.IntegerField(blank=True, null=True)
    es_ca_id = models.CharField(max_length=10, blank=True, null=True)
    es_resp_ag = models.CharField(max_length=2, blank=True, null=True)
    es_version = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_st'


class Emails(models.Model):
    em_id = models.CharField(max_length=10, blank=True, null=True)
    em_datecre = models.DateTimeField(blank=True, null=True)
    em_fromnam = models.CharField(max_length=40, blank=True, null=True)
    em_toname = models.CharField(max_length=40, blank=True, null=True)
    em_subject = models.CharField(max_length=250, blank=True, null=True)
    em_filenam = models.CharField(max_length=250, blank=True, null=True)
    em_mailima = models.CharField(max_length=4, blank=True, null=True)
    em_cust_co = models.CharField(max_length=6, blank=True, null=True)
    em_supp_co = models.CharField(max_length=6, blank=True, null=True)
    em_cc_id = models.CharField(max_length=10, blank=True, null=True)
    em_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    em_order_n = models.CharField(max_length=15, blank=True, null=True)
    em_po_num = models.CharField(max_length=7, blank=True, null=True)
    em_quote_n = models.CharField(max_length=30, blank=True, null=True)
    em_nc_id = models.CharField(max_length=10, blank=True, null=True)
    em_sordq_s = models.CharField(max_length=7, blank=True, null=True)
    em_inv_num = models.CharField(max_length=7, blank=True, null=True)
    em_ap_id = models.CharField(max_length=10, blank=True, null=True)
    em_mr_id = models.CharField(max_length=10, blank=True, null=True)
    em_mn_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emails'


class EmpReq(models.Model):
    er_id = models.CharField(max_length=10, blank=True, null=True)
    er_emp_id = models.CharField(max_length=5, blank=True, null=True)
    er_ca_code = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_req'


class Employee(models.Model):
    em_emp_id = models.CharField(max_length=5, blank=True, null=True)
    em_emp_nam = models.CharField(max_length=20, blank=True, null=True)
    em_positio = models.CharField(max_length=30, blank=True, null=True)
    em_hrly_ra = models.FloatField(blank=True, null=True)
    em_dept_co = models.CharField(max_length=2, blank=True, null=True)
    em_shift = models.CharField(max_length=2, blank=True, null=True)
    em_salespe = models.NullBooleanField()
    em_picture = models.CharField(max_length=254, blank=True, null=True)
    em_ci = models.CharField(max_length=8, blank=True, null=True)
    em_co = models.CharField(max_length=8, blank=True, null=True)
    em_lo = models.CharField(max_length=8, blank=True, null=True)
    em_li = models.CharField(max_length=8, blank=True, null=True)
    em_r_limit = models.IntegerField(blank=True, null=True)
    em_jc_use = models.NullBooleanField()
    em_tc_use = models.NullBooleanField()
    em_minlunc = models.IntegerField(blank=True, null=True)
    em_gl_numb = models.CharField(max_length=12, blank=True, null=True)
    em_last_na = models.CharField(max_length=20, blank=True, null=True)
    em_first_n = models.CharField(max_length=15, blank=True, null=True)
    em_middle_field = models.CharField(db_column='em_middle_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_address = models.CharField(max_length=35, blank=True, null=True)
    em_addres2 = models.CharField(max_length=35, blank=True, null=True)
    em_city = models.CharField(max_length=20, blank=True, null=True)
    em_state = models.CharField(max_length=2, blank=True, null=True)
    em_zip_cod = models.CharField(max_length=10, blank=True, null=True)
    em_phone = models.CharField(max_length=14, blank=True, null=True)
    em_soc_sec = models.CharField(max_length=20, blank=True, null=True)
    em_birth_d = models.CharField(max_length=20, blank=True, null=True)
    em_sex = models.CharField(max_length=1, blank=True, null=True)
    em_marital = models.CharField(max_length=1, blank=True, null=True)
    em_exempts = models.IntegerField(blank=True, null=True)
    em_pay_typ = models.CharField(max_length=1, blank=True, null=True)
    em_pay_fre = models.CharField(max_length=1, blank=True, null=True)
    em_date_hi = models.DateField(blank=True, null=True)
    em_date_le = models.DateField(blank=True, null=True)
    em_reason_field = models.TextField(db_column='em_reason_', blank=True, null=True)  # Field renamed because it ended with '_'.
    em_notes = models.TextField(blank=True, null=True)
    em_ad_tax_field = models.FloatField(db_column='em_ad_tax_', blank=True, null=True)  # Field renamed because it ended with '_'.
    em_ad_tax2 = models.FloatField(blank=True, null=True)
    em_ad_tax3 = models.FloatField(blank=True, null=True)
    em_adv_rec = models.FloatField(blank=True, null=True)
    em_st_id_s = models.CharField(max_length=2, blank=True, null=True)
    em_tt_id_s = models.CharField(max_length=10, blank=True, null=True)
    em_tx_id_l = models.CharField(max_length=10, blank=True, null=True)
    em_tx_id_2 = models.CharField(max_length=10, blank=True, null=True)
    em_vac_ava = models.FloatField(blank=True, null=True)
    em_vac_use = models.FloatField(blank=True, null=True)
    em_vac_rem = models.FloatField(blank=True, null=True)
    em_pto_ava = models.FloatField(blank=True, null=True)
    em_pto_use = models.FloatField(blank=True, null=True)
    em_pto_rem = models.FloatField(blank=True, null=True)
    em_fax = models.CharField(max_length=14, blank=True, null=True)
    em_email = models.CharField(max_length=35, blank=True, null=True)
    em_benefit = models.DateField(blank=True, null=True)
    em_vac_ann = models.FloatField(blank=True, null=True)
    em_pto_ann = models.FloatField(blank=True, null=True)
    em_ad_tax4 = models.FloatField(blank=True, null=True)
    em_use_tca = models.NullBooleanField()
    em_w2_stat = models.NullBooleanField()
    em_w2_942_field = models.NullBooleanField(db_column='em_w2_942_')  # Field renamed because it ended with '_'.
    em_w2_def_field = models.NullBooleanField(db_column='em_w2_def_')  # Field renamed because it ended with '_'.
    em_w2_lega = models.NullBooleanField()
    em_w2_pens = models.NullBooleanField()
    em_w2_dece = models.NullBooleanField()
    em_as_fica = models.NullBooleanField()
    em_as_medi = models.NullBooleanField()
    em_as_futa = models.NullBooleanField()
    em_as_suta = models.NullBooleanField()
    em_vac_bas = models.CharField(max_length=1, blank=True, null=True)
    em_vac_acc = models.CharField(max_length=1, blank=True, null=True)
    em_pto_bas = models.CharField(max_length=1, blank=True, null=True)
    em_pto_acc = models.CharField(max_length=1, blank=True, null=True)
    em_exempt2 = models.IntegerField(blank=True, null=True)
    em_exempt3 = models.IntegerField(blank=True, null=True)
    em_exempt4 = models.IntegerField(blank=True, null=True)
    em_filing_field = models.CharField(db_column='em_filing_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_filing2 = models.CharField(max_length=1, blank=True, null=True)
    em_filing3 = models.CharField(max_length=1, blank=True, null=True)
    em_filing4 = models.CharField(max_length=1, blank=True, null=True)
    em_st_id_l = models.CharField(max_length=2, blank=True, null=True)
    em_st_id_2 = models.CharField(max_length=2, blank=True, null=True)
    em_vac_ac2 = models.FloatField(blank=True, null=True)
    em_pto_ac2 = models.FloatField(blank=True, null=True)
    em_electro = models.NullBooleanField()
    em_no_etr = models.NullBooleanField()
    em_fed_res = models.CharField(max_length=30, blank=True, null=True)
    em_inactiv = models.NullBooleanField()
    em_supp_co = models.CharField(max_length=6, blank=True, null=True)
    em_use_jca = models.NullBooleanField()
    em_supervi = models.NullBooleanField()
    em_emp_id_field = models.CharField(db_column='em_emp_id_', max_length=5, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_commiss = models.FloatField(blank=True, null=True)
    em_shift_o = models.NullBooleanField()
    em_vac_esc = models.FloatField(blank=True, null=True)
    em_pto_esc = models.FloatField(blank=True, null=True)
    em_w2_3_rd_field = models.NullBooleanField(db_column='em_w2_3_rd_')  # Field renamed because it ended with '_'.
    em_use_sca = models.NullBooleanField()
    em_sell_ra = models.FloatField(blank=True, null=True)
    em_ad_calc = models.NullBooleanField()
    em_ad_cal2 = models.NullBooleanField()
    em_ad_cal3 = models.NullBooleanField()
    em_ad_cal4 = models.NullBooleanField()
    em_sc_dow = models.IntegerField(blank=True, null=True)
    em_tempora = models.NullBooleanField()
    em_pe_code = models.CharField(max_length=6, blank=True, null=True)
    em_use_rca = models.NullBooleanField()
    em_ex_gain = models.NullBooleanField()
    em_product = models.NullBooleanField()
    em_signatu = models.CharField(max_length=40, blank=True, null=True)
    em_fit_py_field = models.CharField(db_column='em_fit_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_fica_py = models.CharField(max_length=12, blank=True, null=True)
    em_fica_ex = models.CharField(max_length=12, blank=True, null=True)
    em_mc_py_g = models.CharField(max_length=12, blank=True, null=True)
    em_mc_ex_g = models.CharField(max_length=12, blank=True, null=True)
    em_futa_py = models.CharField(max_length=12, blank=True, null=True)
    em_futa_ex = models.CharField(max_length=12, blank=True, null=True)
    em_suta_py = models.CharField(max_length=12, blank=True, null=True)
    em_suta_ex = models.CharField(max_length=12, blank=True, null=True)
    em_sii_py_field = models.CharField(db_column='em_sii_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_sii_ex_field = models.CharField(db_column='em_sii_ex_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_sit_py_field = models.CharField(db_column='em_sit_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_sit_ex_field = models.CharField(db_column='em_sit_ex_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_lit1_py = models.CharField(max_length=12, blank=True, null=True)
    em_lit1_ex = models.CharField(max_length=12, blank=True, null=True)
    em_lit2_py = models.CharField(max_length=12, blank=True, null=True)
    em_lit2_ex = models.CharField(max_length=12, blank=True, null=True)
    em_tax_ove = models.NullBooleanField()
    em_suponly = models.NullBooleanField()
    em_spec_re = models.NullBooleanField()
    em_inspect = models.NullBooleanField()
    em_trans_c = models.CharField(max_length=2, blank=True, null=True)
    em_routing = models.CharField(max_length=9, blank=True, null=True)
    em_account = models.CharField(max_length=35, blank=True, null=True)
    em_tc_note = models.TextField(blank=True, null=True)
    em_mgr_qua = models.NullBooleanField()
    em_mgr_pm = models.NullBooleanField()
    em_mgr_eng = models.NullBooleanField()
    em_app_req = models.NullBooleanField()
    em_spouse_field = models.CharField(db_column='em_spouse_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_unatten = models.NullBooleanField()
    em_exp_dep = models.CharField(max_length=6, blank=True, null=True)
    em_exp_cod = models.CharField(max_length=8, blank=True, null=True)
    em_hr_note = models.TextField(blank=True, null=True)
    em_da_note = models.TextField(blank=True, null=True)
    em_pr_note = models.TextField(blank=True, null=True)
    em_pr_next = models.DateField(blank=True, null=True)
    em_ps_id = models.CharField(max_length=10, blank=True, null=True)
    em_hours_a = models.FloatField(blank=True, null=True)
    em_cert_tr = models.NullBooleanField()
    em_filing5 = models.CharField(max_length=1, blank=True, null=True)
    em_eic_rc_field = models.CharField(db_column='em_eic_rc_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_setup = models.NullBooleanField()
    em_emerg_n = models.CharField(max_length=25, blank=True, null=True)
    em_emerg_p = models.CharField(max_length=14, blank=True, null=True)
    em_can_iss = models.NullBooleanField()
    em_can_ass = models.NullBooleanField()
    em_as_soth = models.NullBooleanField()
    em_sot_py_field = models.CharField(db_column='em_sot_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_sot_ex_field = models.CharField(db_column='em_sot_ex_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_filing6 = models.CharField(max_length=1, blank=True, null=True)
    em_federal = models.NullBooleanField()
    em_state_1 = models.NullBooleanField()
    em_local_1 = models.NullBooleanField()
    em_local_2 = models.NullBooleanField()
    em_arbitra = models.NullBooleanField()
    em_ex_holi = models.NullBooleanField()
    em_split_p = models.IntegerField(blank=True, null=True)
    em_electr2 = models.NullBooleanField()
    em_trans_2 = models.CharField(max_length=2, blank=True, null=True)
    em_routin2 = models.CharField(max_length=9, blank=True, null=True)
    em_accoun2 = models.CharField(max_length=35, blank=True, null=True)
    em_split_2 = models.IntegerField(blank=True, null=True)
    em_split_t = models.IntegerField(blank=True, null=True)
    em_split_a = models.FloatField(blank=True, null=True)
    em_split_3 = models.FloatField(blank=True, null=True)
    em_requisi = models.NullBooleanField()
    em_lc_id_l = models.CharField(max_length=10, blank=True, null=True)
    em_lc_id_2 = models.CharField(max_length=10, blank=True, null=True)
    em_as_loth = models.NullBooleanField()
    em_as_lot2 = models.NullBooleanField()
    em_lot1_py = models.CharField(max_length=12, blank=True, null=True)
    em_lot1_ex = models.CharField(max_length=12, blank=True, null=True)
    em_lot2_py = models.CharField(max_length=12, blank=True, null=True)
    em_lot2_ex = models.CharField(max_length=12, blank=True, null=True)
    em_srt_py_field = models.CharField(db_column='em_srt_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_srt_ex_field = models.CharField(db_column='em_srt_ex_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_depends = models.IntegerField(blank=True, null=True)
    em_inside = models.NullBooleanField()
    em_id_code = models.CharField(max_length=10, blank=True, null=True)
    em_qualifi = models.NullBooleanField()
    em_sell_r2 = models.FloatField(blank=True, null=True)
    em_sell_r3 = models.FloatField(blank=True, null=True)
    em_gl_com_field = models.CharField(db_column='em_gl_com_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    em_check_m = models.CharField(max_length=30, blank=True, null=True)
    em_gl_com2 = models.CharField(max_length=12, blank=True, null=True)
    em_passwrd = models.CharField(max_length=7, blank=True, null=True)
    em_approve = models.NullBooleanField()
    em_car_res = models.NullBooleanField()
    em_1099 = models.NullBooleanField()
    em_1099_box = models.CharField(max_length=2, blank=True, null=True)
    em_lm_user = models.CharField(max_length=5, blank=True, null=True)
    em_lm_date = models.DateTimeField(blank=True, null=True)
    em_email_p = models.NullBooleanField()
    em_portalo = models.NullBooleanField()
    em_birth_2 = models.CharField(max_length=20, blank=True, null=True)
    em_soc_se2 = models.CharField(max_length=11, blank=True, null=True)
    em_numofma = models.IntegerField(blank=True, null=True)
    em_prevent = models.NullBooleanField()
    em_pdf_pay = models.NullBooleanField()
    em_pdf_dir = models.CharField(max_length=40, blank=True, null=True)
    em_aca_fte = models.FloatField(blank=True, null=True)
    em_accoun3 = models.CharField(max_length=17, blank=True, null=True)
    em_accoun4 = models.CharField(max_length=17, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Emprcode(models.Model):
    er_id = models.CharField(max_length=10, blank=True, null=True)
    er_date = models.DateField(blank=True, null=True)
    er_shift = models.CharField(max_length=2, blank=True, null=True)
    er_run_cod = models.CharField(max_length=20, blank=True, null=True)
    er_emp_id = models.CharField(max_length=5, blank=True, null=True)
    er_note = models.TextField(blank=True, null=True)
    er_item = models.IntegerField(blank=True, null=True)
    er_prod_se = models.IntegerField(blank=True, null=True)
    er_1_st = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'emprcode'


class Empwc(models.Model):
    ew_emp_id = models.CharField(max_length=5, blank=True, null=True)
    ew_mach_co = models.CharField(max_length=5, blank=True, null=True)
    ew_hrly_ra = models.FloatField(blank=True, null=True)
    ew_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empwc'


class Ereasons(models.Model):
    er_code = models.CharField(max_length=3, blank=True, null=True)
    er_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ereasons'


class EtSys(models.Model):
    es_group = models.CharField(max_length=10, blank=True, null=True)
    es_counter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'et_sys'


class Execsum(models.Model):
    es_ar_agin = models.FloatField(blank=True, null=True)
    es_ar_agi2 = models.FloatField(blank=True, null=True)
    es_ar_agi3 = models.FloatField(blank=True, null=True)
    es_ar_agi4 = models.FloatField(blank=True, null=True)
    es_ar_agi5 = models.FloatField(blank=True, null=True)
    es_ap_agin = models.FloatField(blank=True, null=True)
    es_ap_agi2 = models.FloatField(blank=True, null=True)
    es_ap_agi3 = models.FloatField(blank=True, null=True)
    es_ap_agi4 = models.FloatField(blank=True, null=True)
    es_ap_agi5 = models.FloatField(blank=True, null=True)
    es_ar_tota = models.FloatField(blank=True, null=True)
    es_ar_tot2 = models.FloatField(blank=True, null=True)
    es_ar_tot3 = models.FloatField(blank=True, null=True)
    es_ar_tot4 = models.FloatField(blank=True, null=True)
    es_ar_tot5 = models.FloatField(blank=True, null=True)
    es_ap_tota = models.FloatField(blank=True, null=True)
    es_ap_tot2 = models.FloatField(blank=True, null=True)
    es_ap_tot3 = models.FloatField(blank=True, null=True)
    es_ap_tot4 = models.FloatField(blank=True, null=True)
    es_ap_tot5 = models.FloatField(blank=True, null=True)
    es_py_tota = models.FloatField(blank=True, null=True)
    es_py_tot2 = models.FloatField(blank=True, null=True)
    es_py_tot3 = models.FloatField(blank=True, null=True)
    es_py_tot4 = models.FloatField(blank=True, null=True)
    es_py_tot5 = models.FloatField(blank=True, null=True)
    es_cr_tota = models.FloatField(blank=True, null=True)
    es_cr_tot2 = models.FloatField(blank=True, null=True)
    es_cr_tot3 = models.FloatField(blank=True, null=True)
    es_cr_tot4 = models.FloatField(blank=True, null=True)
    es_cr_tot5 = models.FloatField(blank=True, null=True)
    es_cd_tota = models.FloatField(blank=True, null=True)
    es_cd_tot2 = models.FloatField(blank=True, null=True)
    es_cd_tot3 = models.FloatField(blank=True, null=True)
    es_cd_tot4 = models.FloatField(blank=True, null=True)
    es_cd_tot5 = models.FloatField(blank=True, null=True)
    es_ar_c = models.FloatField(blank=True, null=True)
    es_us_c = models.FloatField(blank=True, null=True)
    es_so_c = models.FloatField(blank=True, null=True)
    es_ap_c = models.FloatField(blank=True, null=True)
    es_ur_c = models.FloatField(blank=True, null=True)
    es_po_c = models.FloatField(blank=True, null=True)
    es_py_c = models.FloatField(blank=True, null=True)
    es_ca_c = models.FloatField(blank=True, null=True)
    es_ar_1 = models.FloatField(blank=True, null=True)
    es_us_1 = models.FloatField(blank=True, null=True)
    es_so_1 = models.FloatField(blank=True, null=True)
    es_ap_1 = models.FloatField(blank=True, null=True)
    es_ur_1 = models.FloatField(blank=True, null=True)
    es_po_1 = models.FloatField(blank=True, null=True)
    es_py_1 = models.FloatField(blank=True, null=True)
    es_ca_1 = models.FloatField(blank=True, null=True)
    es_ar_2 = models.FloatField(blank=True, null=True)
    es_us_2 = models.FloatField(blank=True, null=True)
    es_so_2 = models.FloatField(blank=True, null=True)
    es_ap_2 = models.FloatField(blank=True, null=True)
    es_ur_2 = models.FloatField(blank=True, null=True)
    es_po_2 = models.FloatField(blank=True, null=True)
    es_py_2 = models.FloatField(blank=True, null=True)
    es_ca_2 = models.FloatField(blank=True, null=True)
    es_ar_3 = models.FloatField(blank=True, null=True)
    es_us_3 = models.FloatField(blank=True, null=True)
    es_so_3 = models.FloatField(blank=True, null=True)
    es_ap_3 = models.FloatField(blank=True, null=True)
    es_ur_3 = models.FloatField(blank=True, null=True)
    es_po_3 = models.FloatField(blank=True, null=True)
    es_py_3 = models.FloatField(blank=True, null=True)
    es_ca_3 = models.FloatField(blank=True, null=True)
    es_asof_da = models.DateField(blank=True, null=True)
    es_type = models.CharField(max_length=1, blank=True, null=True)
    es_ca_tota = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'execsum'


class ExtAttb(models.Model):
    z_cextattb = models.CharField(max_length=20, blank=True, null=True)
    z_cextatt2 = models.CharField(max_length=20, blank=True, null=True)
    z_cextatt3 = models.CharField(max_length=20, blank=True, null=True)
    z_cextatt4 = models.CharField(max_length=20, blank=True, null=True)
    z_cextatt5 = models.CharField(max_length=20, blank=True, null=True)
    z_cextatt6 = models.CharField(max_length=20, blank=True, null=True)
    z_cextatt7 = models.CharField(max_length=20, blank=True, null=True)
    z_cextatt8 = models.CharField(max_length=20, blank=True, null=True)
    z_cextatt9 = models.CharField(max_length=20, blank=True, null=True)
    z_cextat10 = models.CharField(max_length=20, blank=True, null=True)
    z_cextat11 = models.CharField(max_length=20, blank=True, null=True)
    z_cextat12 = models.CharField(max_length=20, blank=True, null=True)
    z_cextat13 = models.CharField(max_length=20, blank=True, null=True)
    z_cextat14 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ext_attb'


class FaPrcss(models.Model):
    fa_order_n = models.CharField(max_length=12, blank=True, null=True)
    fa_date = models.DateField(blank=True, null=True)
    fa_emp_nam = models.CharField(max_length=20, blank=True, null=True)
    fa_resin1 = models.CharField(max_length=30, blank=True, null=True)
    fa_resin2 = models.CharField(max_length=30, blank=True, null=True)
    fa_cur = models.CharField(max_length=20, blank=True, null=True)
    fa_duro = models.CharField(max_length=3, blank=True, null=True)
    fa_resin1_field = models.CharField(db_column='fa_resin1_', max_length=3, blank=True, null=True)  # Field renamed because it ended with '_'.
    fa_resin2_field = models.CharField(db_column='fa_resin2_', max_length=3, blank=True, null=True)  # Field renamed because it ended with '_'.
    fa_cure_te = models.CharField(max_length=3, blank=True, null=True)
    fa_pigment = models.CharField(max_length=20, blank=True, null=True)
    fa_totalgp = models.IntegerField(blank=True, null=True)
    fa_oven_te = models.CharField(max_length=3, blank=True, null=True)
    fa_moldtem = models.CharField(max_length=3, blank=True, null=True)
    fa_moldte2 = models.CharField(max_length=3, blank=True, null=True)
    fa_moldte3 = models.CharField(max_length=3, blank=True, null=True)
    fa_moldte4 = models.CharField(max_length=3, blank=True, null=True)
    fa_moldte5 = models.CharField(max_length=3, blank=True, null=True)
    fa_moldte6 = models.CharField(max_length=3, blank=True, null=True)
    fa_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    fa_overrid = models.IntegerField(blank=True, null=True)
    fa_hose_si = models.CharField(max_length=30, blank=True, null=True)
    fa_hose_le = models.IntegerField(blank=True, null=True)
    fa_cast_ty = models.IntegerField(blank=True, null=True)
    fa_flow_ra = models.CharField(max_length=20, blank=True, null=True)
    fa_fr1_tgs = models.IntegerField(blank=True, null=True)
    fa_flow_r2 = models.CharField(max_length=20, blank=True, null=True)
    fa_fr2_tgs = models.IntegerField(blank=True, null=True)
    fa_colorpe = models.IntegerField(blank=True, null=True)
    fa_pour_ti = models.CharField(max_length=6, blank=True, null=True)
    fa_breakou = models.CharField(max_length=6, blank=True, null=True)
    fa_partwei = models.IntegerField(blank=True, null=True)
    fa_flashin = models.IntegerField(blank=True, null=True)
    fa_hosewei = models.IntegerField(blank=True, null=True)
    fa_pressti = models.CharField(max_length=6, blank=True, null=True)
    fa_bo_note = models.TextField(blank=True, null=True)
    fa_sp_note = models.TextField(blank=True, null=True)
    fa_shrinku = models.FloatField(blank=True, null=True)
    fa_shrinka = models.FloatField(blank=True, null=True)
    fa_notes_d = models.TextField(blank=True, null=True)
    fa_quote_n = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fa_prcss'


class Failure(models.Model):
    fa_code = models.CharField(max_length=10, blank=True, null=True)
    fa_desc = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'failure'


class Feas(models.Model):
    fe_id = models.CharField(max_length=10, blank=True, null=True)
    fe_type = models.IntegerField(blank=True, null=True)
    fe_text = models.CharField(max_length=80, blank=True, null=True)
    fe_order = models.IntegerField(blank=True, null=True)
    fe_textonl = models.NullBooleanField()
    fe_feas_no = models.IntegerField(blank=True, null=True)
    fe_general = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'feas'


class FghtEst(models.Model):
    fe_id = models.CharField(max_length=10, blank=True, null=True)
    fe_dest_zi = models.CharField(max_length=5, blank=True, null=True)
    fe_desc = models.CharField(max_length=30, blank=True, null=True)
    fe_min_cha = models.FloatField(blank=True, null=True)
    fe_miles = models.IntegerField(blank=True, null=True)
    fe_per_mil = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fght_est'


class FghtRte(models.Model):
    fr_id = models.CharField(max_length=10, blank=True, null=True)
    fr_fe_id = models.CharField(max_length=10, blank=True, null=True)
    fr_weight = models.FloatField(blank=True, null=True)
    fr_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fght_rte'


class Gageass(models.Model):
    ga_id = models.CharField(max_length=10, blank=True, null=True)
    ga_pm_id = models.CharField(max_length=20, blank=True, null=True)
    ga_outdate = models.DateField(blank=True, null=True)
    ga_indate = models.DateField(blank=True, null=True)
    ga_order_n = models.CharField(max_length=12, blank=True, null=True)
    ga_op_num = models.IntegerField(blank=True, null=True)
    ga_emp_id = models.CharField(max_length=5, blank=True, null=True)
    ga_mach_co = models.CharField(max_length=5, blank=True, null=True)
    ga_notes = models.TextField(blank=True, null=True)
    ga_invent_field = models.CharField(db_column='ga_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ga_il_id = models.CharField(max_length=10, blank=True, null=True)
    ga_ib_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gageass'


class Gageowner(models.Model):
    go_id = models.CharField(max_length=10, blank=True, null=True)
    go_descrip = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gageowner'


class Gagetype(models.Model):
    gt_code = models.CharField(max_length=10, blank=True, null=True)
    gt_desc = models.CharField(max_length=40, blank=True, null=True)
    gt_toleran = models.FloatField(blank=True, null=True)
    gt_interva = models.FloatField(blank=True, null=True)
    gt_interv2 = models.FloatField(blank=True, null=True)
    gt_interv3 = models.FloatField(blank=True, null=True)
    gt_interv4 = models.FloatField(blank=True, null=True)
    gt_interv5 = models.FloatField(blank=True, null=True)
    gt_note = models.TextField(blank=True, null=True)
    gt_blk_siz = models.FloatField(blank=True, null=True)
    gt_blk_si2 = models.FloatField(blank=True, null=True)
    gt_range = models.CharField(max_length=30, blank=True, null=True)
    gt_interv6 = models.FloatField(blank=True, null=True)
    gt_interv7 = models.FloatField(blank=True, null=True)
    gt_paralle = models.FloatField(blank=True, null=True)
    gt_cylindr = models.FloatField(blank=True, null=True)
    gt_blk_si3 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gagetype'


class Gear(models.Model):
    gr_id = models.CharField(max_length=10, blank=True, null=True)
    gr_schgrp = models.CharField(max_length=10, blank=True, null=True)
    gr_type = models.CharField(max_length=1, blank=True, null=True)
    gr_driver = models.IntegerField(blank=True, null=True)
    gr_driven = models.IntegerField(blank=True, null=True)
    gr_rpm = models.IntegerField(blank=True, null=True)
    gr_mds_rpm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gear'


class Graph(models.Model):
    gr_id = models.CharField(max_length=10, blank=True, null=True)
    gr_title = models.CharField(max_length=50, blank=True, null=True)
    gr_account = models.CharField(max_length=10, blank=True, null=True)
    gr_accoun2 = models.CharField(max_length=10, blank=True, null=True)
    gr_operati = models.CharField(max_length=1, blank=True, null=True)
    gr_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'graph'


class Grpquote(models.Model):
    gq_id = models.CharField(max_length=10, blank=True, null=True)
    gq_date = models.DateField(blank=True, null=True)
    gq_status = models.CharField(max_length=1, blank=True, null=True)
    gq_folup_d = models.DateField(blank=True, null=True)
    gq_prep_by = models.CharField(max_length=30, blank=True, null=True)
    gq_req_num = models.CharField(max_length=20, blank=True, null=True)
    gq_sent_da = models.DateField(blank=True, null=True)
    gq_valid_d = models.CharField(max_length=10, blank=True, null=True)
    gq_cust_co = models.CharField(max_length=6, blank=True, null=True)
    gq_cust_c2 = models.CharField(max_length=30, blank=True, null=True)
    gq_deliver = models.CharField(max_length=50, blank=True, null=True)
    gq_ship_vi = models.CharField(max_length=20, blank=True, null=True)
    gq_fob = models.CharField(max_length=15, blank=True, null=True)
    gq_pay_ter = models.CharField(max_length=20, blank=True, null=True)
    gq_memo = models.TextField(blank=True, null=True)
    gq_comp_na = models.CharField(max_length=35, blank=True, null=True)
    gq_address = models.CharField(max_length=35, blank=True, null=True)
    gq_addres2 = models.CharField(max_length=35, blank=True, null=True)
    gq_addres3 = models.CharField(max_length=35, blank=True, null=True)
    gq_ship_co = models.CharField(max_length=35, blank=True, null=True)
    gq_sh_ad1 = models.CharField(max_length=35, blank=True, null=True)
    gq_sh_ad2 = models.CharField(max_length=35, blank=True, null=True)
    gq_sh_ad3 = models.CharField(max_length=35, blank=True, null=True)
    gq_sh_ad4 = models.CharField(max_length=35, blank=True, null=True)
    gq_cust_ph = models.CharField(max_length=14, blank=True, null=True)
    gq_cust_fa = models.CharField(max_length=14, blank=True, null=True)
    gq_req_dat = models.DateField(blank=True, null=True)
    gq_addres4 = models.CharField(max_length=35, blank=True, null=True)
    gq_last_up = models.DateField(blank=True, null=True)
    gq_lo_code = models.CharField(max_length=10, blank=True, null=True)
    gq_empby = models.CharField(max_length=5, blank=True, null=True)
    gq_due_dat = models.DateField(blank=True, null=True)
    gq_empto = models.CharField(max_length=5, blank=True, null=True)
    gq_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    gq_stepup = models.IntegerField(blank=True, null=True)
    gq_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    gq_foblabe = models.CharField(max_length=3, blank=True, null=True)
    gq_est_hrs = models.FloatField(blank=True, null=True)
    gq_eng_sda = models.DateField(blank=True, null=True)
    gq_eng_eda = models.DateField(blank=True, null=True)
    gq_fab_sda = models.DateField(blank=True, null=True)
    gq_fab_eda = models.DateField(blank=True, null=True)
    gq_sord_n2 = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grpquote'


class Heats(models.Model):
    ht_invent_field = models.CharField(db_column='ht_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ht_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    ht_heat_de = models.CharField(max_length=35, blank=True, null=True)
    ht_heat_no = models.TextField(blank=True, null=True)
    ht_heat_qt = models.FloatField(blank=True, null=True)
    ht_sup_cod = models.CharField(max_length=6, blank=True, null=True)
    ht_recdate = models.DateField(blank=True, null=True)
    ht_imagefi = models.CharField(max_length=30, blank=True, null=True)
    ht_po_num = models.CharField(max_length=7, blank=True, null=True)
    ht_cust_co = models.CharField(max_length=6, blank=True, null=True)
    ht_cust_c2 = models.CharField(max_length=30, blank=True, null=True)
    ht_cust_po = models.CharField(max_length=30, blank=True, null=True)
    ht_eu_cont = models.CharField(max_length=30, blank=True, null=True)
    ht_eu_phon = models.CharField(max_length=20, blank=True, null=True)
    ht_eu_addr = models.TextField(blank=True, null=True)
    ht_purch_d = models.DateField(blank=True, null=True)
    ht_item1 = models.CharField(max_length=30, blank=True, null=True)
    ht_item2 = models.CharField(max_length=30, blank=True, null=True)
    ht_item3 = models.CharField(max_length=30, blank=True, null=True)
    ht_item4 = models.CharField(max_length=30, blank=True, null=True)
    ht_item5 = models.CharField(max_length=30, blank=True, null=True)
    ht_item6 = models.CharField(max_length=30, blank=True, null=True)
    ht_item7 = models.CharField(max_length=30, blank=True, null=True)
    ht_item8 = models.CharField(max_length=30, blank=True, null=True)
    ht_item9 = models.CharField(max_length=30, blank=True, null=True)
    ht_item10 = models.CharField(max_length=30, blank=True, null=True)
    ht_len1 = models.IntegerField(blank=True, null=True)
    ht_len2 = models.IntegerField(blank=True, null=True)
    ht_len3 = models.IntegerField(blank=True, null=True)
    ht_len4 = models.IntegerField(blank=True, null=True)
    ht_len5 = models.IntegerField(blank=True, null=True)
    ht_len6 = models.IntegerField(blank=True, null=True)
    ht_len7 = models.IntegerField(blank=True, null=True)
    ht_len8 = models.IntegerField(blank=True, null=True)
    ht_len9 = models.IntegerField(blank=True, null=True)
    ht_len10 = models.IntegerField(blank=True, null=True)
    ht_exp1 = models.DateField(blank=True, null=True)
    ht_exp2 = models.DateField(blank=True, null=True)
    ht_exp3 = models.DateField(blank=True, null=True)
    ht_exp4 = models.DateField(blank=True, null=True)
    ht_exp5 = models.DateField(blank=True, null=True)
    ht_exp6 = models.DateField(blank=True, null=True)
    ht_exp7 = models.DateField(blank=True, null=True)
    ht_exp8 = models.DateField(blank=True, null=True)
    ht_exp9 = models.DateField(blank=True, null=True)
    ht_exp10 = models.DateField(blank=True, null=True)
    ht_service = models.TextField(blank=True, null=True)
    ht_c = models.FloatField(blank=True, null=True)
    ht_mn = models.FloatField(blank=True, null=True)
    ht_p = models.FloatField(blank=True, null=True)
    ht_s = models.FloatField(blank=True, null=True)
    ht_si = models.FloatField(blank=True, null=True)
    ht_pb = models.FloatField(blank=True, null=True)
    ht_cu = models.FloatField(blank=True, null=True)
    ht_ni = models.FloatField(blank=True, null=True)
    ht_cr = models.FloatField(blank=True, null=True)
    ht_mo = models.FloatField(blank=True, null=True)
    ht_v = models.FloatField(blank=True, null=True)
    ht_tensile = models.CharField(max_length=8, blank=True, null=True)
    ht_yield = models.FloatField(blank=True, null=True)
    ht_enlong = models.FloatField(blank=True, null=True)
    ht_reducti = models.FloatField(blank=True, null=True)
    ht_temp = models.FloatField(blank=True, null=True)
    ht_hardnes = models.FloatField(blank=True, null=True)
    ht_al = models.FloatField(blank=True, null=True)
    ht_fe = models.FloatField(blank=True, null=True)
    ht_sn = models.FloatField(blank=True, null=True)
    ht_zn = models.FloatField(blank=True, null=True)
    ht_specifi = models.TextField(blank=True, null=True)
    ht_treatme = models.CharField(max_length=30, blank=True, null=True)
    ht_treatm2 = models.CharField(max_length=30, blank=True, null=True)
    ht_treatm3 = models.CharField(max_length=30, blank=True, null=True)
    ht_treatm4 = models.CharField(max_length=30, blank=True, null=True)
    ht_treatm5 = models.CharField(max_length=30, blank=True, null=True)
    ht_temp1 = models.IntegerField(blank=True, null=True)
    ht_temp2 = models.IntegerField(blank=True, null=True)
    ht_temp3 = models.IntegerField(blank=True, null=True)
    ht_temp4 = models.IntegerField(blank=True, null=True)
    ht_temp5 = models.IntegerField(blank=True, null=True)
    ht_time1 = models.IntegerField(blank=True, null=True)
    ht_time2 = models.IntegerField(blank=True, null=True)
    ht_time3 = models.IntegerField(blank=True, null=True)
    ht_time4 = models.IntegerField(blank=True, null=True)
    ht_time5 = models.IntegerField(blank=True, null=True)
    ht_media1 = models.CharField(max_length=20, blank=True, null=True)
    ht_media2 = models.CharField(max_length=20, blank=True, null=True)
    ht_media3 = models.CharField(max_length=20, blank=True, null=True)
    ht_media4 = models.CharField(max_length=20, blank=True, null=True)
    ht_media5 = models.CharField(max_length=20, blank=True, null=True)
    ht_grainsi = models.CharField(max_length=10, blank=True, null=True)
    ht_grain = models.CharField(max_length=10, blank=True, null=True)
    ht_source = models.TextField(blank=True, null=True)
    ht_conditi = models.CharField(max_length=30, blank=True, null=True)
    ht_image_p = models.CharField(max_length=60, blank=True, null=True)
    ht_image_2 = models.CharField(max_length=60, blank=True, null=True)
    ht_c_or_f_field = models.CharField(db_column='ht_c_or_f_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    ht_c_or_f2 = models.CharField(max_length=1, blank=True, null=True)
    ht_c_or_f3 = models.CharField(max_length=1, blank=True, null=True)
    ht_c_or_f4 = models.CharField(max_length=1, blank=True, null=True)
    ht_c_or_f5 = models.CharField(max_length=1, blank=True, null=True)
    ht_fg_size = models.FloatField(blank=True, null=True)
    ht_shape_c = models.CharField(max_length=7, blank=True, null=True)
    ht_grade = models.CharField(max_length=6, blank=True, null=True)
    ht_hardtyp = models.CharField(max_length=3, blank=True, null=True)
    ht_tensil2 = models.CharField(max_length=8, blank=True, null=True)
    ht_yield2 = models.FloatField(blank=True, null=True)
    ht_enlong2 = models.FloatField(blank=True, null=True)
    ht_reduct2 = models.FloatField(blank=True, null=True)
    ht_hardne2 = models.FloatField(blank=True, null=True)
    ht_tempera = models.FloatField(blank=True, null=True)
    ht_grains2 = models.CharField(max_length=10, blank=True, null=True)
    ht_grain2 = models.CharField(max_length=10, blank=True, null=True)
    ht_hardty2 = models.CharField(max_length=3, blank=True, null=True)
    ht_label1 = models.CharField(max_length=20, blank=True, null=True)
    ht_label2 = models.CharField(max_length=20, blank=True, null=True)
    ht_label3 = models.CharField(max_length=20, blank=True, null=True)
    ht_label4 = models.CharField(max_length=20, blank=True, null=True)
    ht_label5 = models.CharField(max_length=20, blank=True, null=True)
    ht_element = models.FloatField(blank=True, null=True)
    ht_elemen2 = models.FloatField(blank=True, null=True)
    ht_elemen3 = models.FloatField(blank=True, null=True)
    ht_elemen4 = models.FloatField(blank=True, null=True)
    ht_elemen5 = models.FloatField(blank=True, null=True)
    ht_country = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'heats'


class Incoterm(models.Model):
    ix_id = models.CharField(max_length=3, blank=True, null=True)
    ix_desc = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incoterm'


class Inspdet(models.Model):
    id_id = models.CharField(max_length=10, blank=True, null=True)
    id_ih_id = models.CharField(max_length=10, blank=True, null=True)
    id_line_nu = models.IntegerField(blank=True, null=True)
    id_dimen = models.CharField(max_length=35, blank=True, null=True)
    id_im_id = models.CharField(max_length=10, blank=True, null=True)
    id_device_field = models.CharField(db_column='id_device_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    id_aql = models.CharField(max_length=10, blank=True, null=True)
    id_samp = models.IntegerField(blank=True, null=True)
    id_acc = models.IntegerField(blank=True, null=True)
    id_rej = models.IntegerField(blank=True, null=True)
    id_actual = models.CharField(max_length=10, blank=True, null=True)
    id_note = models.TextField(blank=True, null=True)
    id_id1 = models.FloatField(blank=True, null=True)
    id_id2 = models.FloatField(blank=True, null=True)
    id_id3 = models.FloatField(blank=True, null=True)
    id_id4 = models.FloatField(blank=True, null=True)
    id_id5 = models.FloatField(blank=True, null=True)
    id_id6 = models.FloatField(blank=True, null=True)
    id_td1 = models.FloatField(blank=True, null=True)
    id_td2 = models.FloatField(blank=True, null=True)
    id_td3 = models.FloatField(blank=True, null=True)
    id_td4 = models.FloatField(blank=True, null=True)
    id_td5 = models.FloatField(blank=True, null=True)
    id_td6 = models.FloatField(blank=True, null=True)
    id_thread = models.CharField(max_length=10, blank=True, null=True)
    id_thd_plu = models.FloatField(blank=True, null=True)
    id_thd_min = models.FloatField(blank=True, null=True)
    id_item_di = models.FloatField(blank=True, null=True)
    id_plus_to = models.FloatField(blank=True, null=True)
    id_min_tol = models.FloatField(blank=True, null=True)
    id_arspec = models.CharField(max_length=35, blank=True, null=True)
    id_ar1 = models.CharField(max_length=1, blank=True, null=True)
    id_ar2 = models.CharField(max_length=1, blank=True, null=True)
    id_ar3 = models.CharField(max_length=1, blank=True, null=True)
    id_ar4 = models.CharField(max_length=1, blank=True, null=True)
    id_ar5 = models.CharField(max_length=1, blank=True, null=True)
    id_ar6 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inspdet'


class Insphead(models.Model):
    ih_id = models.CharField(max_length=10, blank=True, null=True)
    ih_type = models.CharField(max_length=1, blank=True, null=True)
    ih_al_id = models.CharField(max_length=10, blank=True, null=True)
    ih_invent_field = models.CharField(db_column='ih_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ih_date = models.DateField(blank=True, null=True)
    ih_part_nu = models.CharField(max_length=30, blank=True, null=True)
    ih_rev_num = models.CharField(max_length=3, blank=True, null=True)
    ih_part_de = models.CharField(max_length=50, blank=True, null=True)
    ih_lot_qty = models.IntegerField(blank=True, null=True)
    ih_lot_num = models.CharField(max_length=20, blank=True, null=True)
    ih_cust_co = models.CharField(max_length=6, blank=True, null=True)
    ih_cust_na = models.CharField(max_length=33, blank=True, null=True)
    ih_po_num = models.CharField(max_length=15, blank=True, null=True)
    ih_order_n = models.CharField(max_length=12, blank=True, null=True)
    ih_inspect = models.CharField(max_length=15, blank=True, null=True)
    ih_inspec2 = models.CharField(max_length=35, blank=True, null=True)
    ih_inv_rev = models.CharField(max_length=3, blank=True, null=True)
    ih_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    ih_heat_nu = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insphead'


class Insthead(models.Model):
    nh_id = models.CharField(max_length=10, blank=True, null=True)
    nh_invent_field = models.CharField(db_column='nh_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    nh_part_nu = models.CharField(max_length=30, blank=True, null=True)
    nh_rev_num = models.CharField(max_length=3, blank=True, null=True)
    nh_part_de = models.CharField(max_length=50, blank=True, null=True)
    nh_qcir_re = models.CharField(max_length=10, blank=True, null=True)
    nh_revised = models.CharField(max_length=40, blank=True, null=True)
    nh_prep_by = models.CharField(max_length=40, blank=True, null=True)
    nh_rev_dat = models.DateField(blank=True, null=True)
    nh_refer_n = models.CharField(max_length=20, blank=True, null=True)
    nh_cid = models.CharField(max_length=20, blank=True, null=True)
    nh_order_n = models.CharField(max_length=12, blank=True, null=True)
    nh_inv_rev = models.CharField(max_length=3, blank=True, null=True)
    nh_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    nh_heat_nu = models.CharField(max_length=20, blank=True, null=True)
    nh_cust_co = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insthead'


class Intaudit(models.Model):
    ia_id = models.CharField(max_length=10, blank=True, null=True)
    ia_date = models.DateField(blank=True, null=True)
    ia_de_id = models.CharField(max_length=2, blank=True, null=True)
    ia_emp_by = models.CharField(max_length=5, blank=True, null=True)
    ia_lead = models.CharField(max_length=5, blank=True, null=True)
    ia_comp_da = models.DateField(blank=True, null=True)
    ia_areas = models.TextField(blank=True, null=True)
    ia_questio = models.TextField(blank=True, null=True)
    ia_results = models.TextField(blank=True, null=True)
    ia_focus = models.TextField(blank=True, null=True)
    ia_rating = models.IntegerField(blank=True, null=True)
    ia_prev_ra = models.IntegerField(blank=True, null=True)
    ia_status = models.CharField(max_length=1, blank=True, null=True)
    ia_contact = models.CharField(max_length=5, blank=True, null=True)
    ia_meet_da = models.DateField(blank=True, null=True)
    ia_meet_ti = models.CharField(max_length=10, blank=True, null=True)
    ia_reaudit = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'intaudit'


class InvAdj(models.Model):
    ia_id = models.CharField(max_length=10, blank=True, null=True)
    ia_invent_field = models.CharField(db_column='ia_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ia_il_id = models.CharField(max_length=10, blank=True, null=True)
    ia_ib_id = models.CharField(max_length=10, blank=True, null=True)
    ia_quantit = models.FloatField(blank=True, null=True)
    ia_count = models.FloatField(blank=True, null=True)
    ia_adjust = models.FloatField(blank=True, null=True)
    ia_type = models.CharField(max_length=1, blank=True, null=True)
    ia_date = models.DateField(blank=True, null=True)
    ia_user_id = models.CharField(max_length=5, blank=True, null=True)
    ia_ij_id = models.CharField(max_length=10, blank=True, null=True)
    ia_batch_n = models.IntegerField(blank=True, null=True)
    ia_uom = models.CharField(max_length=10, blank=True, null=True)
    ia_order_n = models.CharField(max_length=12, blank=True, null=True)
    ia_lot_num = models.CharField(max_length=20, blank=True, null=True)
    ia_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    ia_supp_co = models.CharField(max_length=6, blank=True, null=True)
    ia_op_num = models.IntegerField(blank=True, null=True)
    ia_rev_num = models.CharField(max_length=6, blank=True, null=True)
    ia_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    ia_adj_dat = models.DateField(blank=True, null=True)
    ia_order_2 = models.CharField(max_length=12, blank=True, null=True)
    ia_unit_co = models.FloatField(blank=True, null=True)
    ia_ext_cos = models.FloatField(blank=True, null=True)
    ia_unit_ma = models.FloatField(blank=True, null=True)
    ia_unit_la = models.FloatField(blank=True, null=True)
    ia_unit_bu = models.FloatField(blank=True, null=True)
    ia_unit_ot = models.FloatField(blank=True, null=True)
    ia_po_num = models.CharField(max_length=7, blank=True, null=True)
    ia_notes = models.TextField(blank=True, null=True)
    ia_cust_co = models.CharField(max_length=6, blank=True, null=True)
    ia_cust_c2 = models.CharField(max_length=6, blank=True, null=True)
    ia_melt_co = models.TextField(blank=True, null=True)
    ia_color_c = models.CharField(max_length=10, blank=True, null=True)
    ia_width1 = models.FloatField(blank=True, null=True)
    ia_length1 = models.FloatField(blank=True, null=True)
    ia_tag_num = models.IntegerField(blank=True, null=True)
    ia_unit_ty = models.IntegerField(blank=True, null=True)
    ia_expire_field = models.DateField(db_column='ia_expire_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ia_conditi = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_adj'


class InvAlis(models.Model):
    ia_id = models.CharField(max_length=10, blank=True, null=True)
    ia_invent_field = models.CharField(db_column='ia_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ia_cust_co = models.CharField(max_length=6, blank=True, null=True)
    ia_part_nu = models.CharField(max_length=30, blank=True, null=True)
    ia_price = models.FloatField(blank=True, null=True)
    ia_eff_dat = models.DateField(blank=True, null=True)
    ia_status = models.CharField(max_length=1, blank=True, null=True)
    ia_order_n = models.CharField(max_length=12, blank=True, null=True)
    ia_ord_dat = models.DateField(blank=True, null=True)
    ia_emp_id = models.CharField(max_length=5, blank=True, null=True)
    ia_po_num = models.CharField(max_length=20, blank=True, null=True)
    ia_ppap_le = models.CharField(max_length=10, blank=True, null=True)
    ia_quote_n = models.CharField(max_length=15, blank=True, null=True)
    ia_samp_qt = models.IntegerField(blank=True, null=True)
    ia_samp_da = models.DateField(blank=True, null=True)
    ia_buyer_n = models.CharField(max_length=30, blank=True, null=True)
    ia_rep_nam = models.CharField(max_length=30, blank=True, null=True)
    ia_ship_ad = models.CharField(max_length=50, blank=True, null=True)
    ia_ship_a2 = models.CharField(max_length=50, blank=True, null=True)
    ia_ship_a3 = models.CharField(max_length=50, blank=True, null=True)
    ia_ship_a4 = models.CharField(max_length=50, blank=True, null=True)
    ia_ship_a5 = models.CharField(max_length=50, blank=True, null=True)
    ia_po_date = models.DateField(blank=True, null=True)
    ia_ship_a6 = models.CharField(max_length=50, blank=True, null=True)
    ia_rep_emp = models.CharField(max_length=5, blank=True, null=True)
    ia_rev_num = models.CharField(max_length=3, blank=True, null=True)
    ia_desc = models.CharField(max_length=50, blank=True, null=True)
    ia_ext_des = models.TextField(blank=True, null=True)
    ia_expire_field = models.DateField(db_column='ia_expire_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'inv_alis'


class InvChng(models.Model):
    iy_id = models.CharField(max_length=10, blank=True, null=True)
    iy_invent_field = models.CharField(db_column='iy_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    iy_year = models.CharField(max_length=4, blank=True, null=True)
    iy_month_1 = models.FloatField(blank=True, null=True)
    iy_month_2 = models.FloatField(blank=True, null=True)
    iy_month_3 = models.FloatField(blank=True, null=True)
    iy_month_4 = models.FloatField(blank=True, null=True)
    iy_month_5 = models.FloatField(blank=True, null=True)
    iy_month_6 = models.FloatField(blank=True, null=True)
    iy_month_7 = models.FloatField(blank=True, null=True)
    iy_month_8 = models.FloatField(blank=True, null=True)
    iy_month_9 = models.FloatField(blank=True, null=True)
    iy_month10 = models.FloatField(blank=True, null=True)
    iy_month11 = models.FloatField(blank=True, null=True)
    iy_month12 = models.FloatField(blank=True, null=True)
    iy_quantit = models.FloatField(blank=True, null=True)
    iy_quanti2 = models.FloatField(blank=True, null=True)
    iy_quanti3 = models.FloatField(blank=True, null=True)
    iy_quanti4 = models.FloatField(blank=True, null=True)
    iy_quanti5 = models.FloatField(blank=True, null=True)
    iy_quanti6 = models.FloatField(blank=True, null=True)
    iy_quanti7 = models.FloatField(blank=True, null=True)
    iy_quanti8 = models.FloatField(blank=True, null=True)
    iy_quanti9 = models.FloatField(blank=True, null=True)
    iy_quant10 = models.FloatField(blank=True, null=True)
    iy_quant11 = models.FloatField(blank=True, null=True)
    iy_quant12 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_chng'


class InvCost(models.Model):
    ic_id = models.CharField(max_length=10, blank=True, null=True)
    ic_ij_id = models.CharField(max_length=10, blank=True, null=True)
    ic_il_id = models.CharField(max_length=10, blank=True, null=True)
    ic_ib_id = models.CharField(max_length=10, blank=True, null=True)
    ic_invent_field = models.CharField(db_column='ic_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ic_supp_co = models.CharField(max_length=6, blank=True, null=True)
    ic_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    ic_order_n = models.CharField(max_length=12, blank=True, null=True)
    ic_date = models.DateField(blank=True, null=True)
    ic_notes = models.TextField(blank=True, null=True)
    ic_quantit = models.FloatField(blank=True, null=True)
    ic_unit_co = models.FloatField(blank=True, null=True)
    ic_ext_cos = models.FloatField(blank=True, null=True)
    ic_order_2 = models.CharField(max_length=12, blank=True, null=True)
    ic_tr_date = models.DateField(blank=True, null=True)
    ic_tr_il_i = models.CharField(max_length=10, blank=True, null=True)
    ic_tr_ib_i = models.CharField(max_length=10, blank=True, null=True)
    ic_tr_orde = models.CharField(max_length=12, blank=True, null=True)
    ic_tr_user = models.CharField(max_length=5, blank=True, null=True)
    ic_tr_use2 = models.DateField(blank=True, null=True)
    ic_tr_quan = models.FloatField(blank=True, null=True)
    ic_tr_ship = models.CharField(max_length=8, blank=True, null=True)
    ic_tr_sd_i = models.IntegerField(blank=True, null=True)
    ic_lot_num = models.CharField(max_length=20, blank=True, null=True)
    ic_unit_ma = models.FloatField(blank=True, null=True)
    ic_unit_la = models.FloatField(blank=True, null=True)
    ic_unit_bu = models.FloatField(blank=True, null=True)
    ic_unit_ot = models.FloatField(blank=True, null=True)
    ic_image_p = models.CharField(max_length=60, blank=True, null=True)
    ic_tr_lot_field = models.CharField(db_column='ic_tr_lot_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    ic_op_num = models.IntegerField(blank=True, null=True)
    ic_tr_op_n = models.IntegerField(blank=True, null=True)
    ic_width1 = models.FloatField(blank=True, null=True)
    ic_width2 = models.FloatField(blank=True, null=True)
    ic_length1 = models.FloatField(blank=True, null=True)
    ic_length2 = models.FloatField(blank=True, null=True)
    ic_rev_num = models.CharField(max_length=6, blank=True, null=True)
    ic_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    ic_tr_rev_field = models.CharField(db_column='ic_tr_rev_', max_length=3, blank=True, null=True)  # Field renamed because it ended with '_'.
    ic_tr_rev2 = models.CharField(max_length=3, blank=True, null=True)
    ic_tr_heat = models.CharField(max_length=30, blank=True, null=True)
    ic_std_mat = models.FloatField(blank=True, null=True)
    ic_std_lab = models.FloatField(blank=True, null=True)
    ic_std_bur = models.FloatField(blank=True, null=True)
    ic_std_oth = models.FloatField(blank=True, null=True)
    ic_std_uni = models.FloatField(blank=True, null=True)
    ic_cust_co = models.CharField(max_length=6, blank=True, null=True)
    ic_cust_c2 = models.CharField(max_length=6, blank=True, null=True)
    ic_melt_co = models.TextField(blank=True, null=True)
    ic_color_c = models.CharField(max_length=10, blank=True, null=True)
    ic_po_num = models.CharField(max_length=7, blank=True, null=True)
    ic_tag_num = models.IntegerField(blank=True, null=True)
    ic_conditi = models.CharField(max_length=20, blank=True, null=True)
    ic_expire_field = models.DateField(db_column='ic_expire_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ic_id_pare = models.CharField(max_length=10, blank=True, null=True)
    ic_roll = models.CharField(max_length=20, blank=True, null=True)
    ic_tr_tag_field = models.IntegerField(db_column='ic_tr_tag_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ic_rem_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_cost'


class InvCsoa(models.Model):
    io_id = models.CharField(max_length=10, blank=True, null=True)
    io_ie_id = models.CharField(max_length=10, blank=True, null=True)
    io_adj_dat = models.DateField(blank=True, null=True)
    io_adj_uni = models.FloatField(blank=True, null=True)
    io_adj_ext = models.FloatField(blank=True, null=True)
    io_org_uni = models.FloatField(blank=True, null=True)
    io_org_ext = models.FloatField(blank=True, null=True)
    io_unit_co = models.FloatField(blank=True, null=True)
    io_ext_cos = models.FloatField(blank=True, null=True)
    io_invent_field = models.CharField(db_column='io_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    io_type = models.CharField(max_length=1, blank=True, null=True)
    io_adj_mat = models.FloatField(blank=True, null=True)
    io_adj_lab = models.FloatField(blank=True, null=True)
    io_adj_bur = models.FloatField(blank=True, null=True)
    io_adj_oth = models.FloatField(blank=True, null=True)
    io_unit_ma = models.FloatField(blank=True, null=True)
    io_unit_la = models.FloatField(blank=True, null=True)
    io_unit_bu = models.FloatField(blank=True, null=True)
    io_unit_ot = models.FloatField(blank=True, null=True)
    io_org_mat = models.FloatField(blank=True, null=True)
    io_org_lab = models.FloatField(blank=True, null=True)
    io_org_bur = models.FloatField(blank=True, null=True)
    io_org_oth = models.FloatField(blank=True, null=True)
    io_ext_mat = models.FloatField(blank=True, null=True)
    io_ext_lab = models.FloatField(blank=True, null=True)
    io_ext_bur = models.FloatField(blank=True, null=True)
    io_ext_oth = models.FloatField(blank=True, null=True)
    io_order_n = models.CharField(max_length=12, blank=True, null=True)
    io_order_2 = models.CharField(max_length=12, blank=True, null=True)
    io_act_dat = models.DateTimeField(blank=True, null=True)
    io_user_id = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_csoa'


class InvDet(models.Model):
    id_inv_num = models.CharField(max_length=7, blank=True, null=True)
    id_line_nu = models.IntegerField(blank=True, null=True)
    id_tran_ty = models.CharField(max_length=2, blank=True, null=True)
    id_invent_field = models.CharField(db_column='id_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    id_ship_co = models.CharField(max_length=8, blank=True, null=True)
    id_desc = models.CharField(max_length=50, blank=True, null=True)
    id_prod_co = models.CharField(max_length=2, blank=True, null=True)
    id_qty_ord = models.FloatField(blank=True, null=True)
    id_qty_shi = models.FloatField(blank=True, null=True)
    id_qty_bo = models.FloatField(blank=True, null=True)
    id_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    id_unit_pr = models.FloatField(blank=True, null=True)
    id_discoun = models.FloatField(blank=True, null=True)
    id_disc_pr = models.FloatField(blank=True, null=True)
    id_ext_pri = models.FloatField(blank=True, null=True)
    id_te = models.CharField(max_length=1, blank=True, null=True)
    id_note = models.TextField(blank=True, null=True)
    id_note_fl = models.CharField(max_length=1, blank=True, null=True)
    id_order_n = models.CharField(max_length=12, blank=True, null=True)
    id_rel_num = models.IntegerField(blank=True, null=True)
    id_po_num = models.CharField(max_length=15, blank=True, null=True)
    id_rel_qty = models.FloatField(blank=True, null=True)
    id_ij_id = models.CharField(max_length=10, blank=True, null=True)
    id_sd_id = models.IntegerField(blank=True, null=True)
    id_ar_gl_n = models.CharField(max_length=12, blank=True, null=True)
    id_pc_gl_n = models.CharField(max_length=12, blank=True, null=True)
    id_gl_id = models.CharField(max_length=10, blank=True, null=True)
    id_tax_rat = models.FloatField(blank=True, null=True)
    id_part_nu = models.CharField(max_length=30, blank=True, null=True)
    id_rev_num = models.CharField(max_length=6, blank=True, null=True)
    id_pmemo = models.TextField(blank=True, null=True)
    id_lot_shi = models.CharField(max_length=20, blank=True, null=True)
    id_st_id = models.CharField(max_length=10, blank=True, null=True)
    id_emp_id = models.CharField(max_length=5, blank=True, null=True)
    id_comm_fl = models.NullBooleanField()
    id_comm_pe = models.FloatField(blank=True, null=True)
    id_comm_am = models.FloatField(blank=True, null=True)
    id_st_tot_field = models.FloatField(db_column='id_st_tot_', blank=True, null=True)  # Field renamed because it ended with '_'.
    id_st_ex_s = models.FloatField(blank=True, null=True)
    id_st_non_field = models.FloatField(db_column='id_st_non_', blank=True, null=True)  # Field renamed because it ended with '_'.
    id_st_tax_field = models.FloatField(db_column='id_st_tax_', blank=True, null=True)  # Field renamed because it ended with '_'.
    id_st_non2 = models.FloatField(blank=True, null=True)
    id_st_tax2 = models.FloatField(blank=True, null=True)
    id_st_tax3 = models.FloatField(blank=True, null=True)
    id_st_tot2 = models.FloatField(blank=True, null=True)
    id_unit_cu = models.FloatField(blank=True, null=True)
    id_disc_cu = models.FloatField(blank=True, null=True)
    id_ext_cur = models.FloatField(blank=True, null=True)
    id_il_id = models.CharField(max_length=10, blank=True, null=True)
    id_ib_id = models.CharField(max_length=10, blank=True, null=True)
    id_lot_num = models.CharField(max_length=20, blank=True, null=True)
    id_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    id_decimal = models.IntegerField(blank=True, null=True)
    id_emp_id2 = models.CharField(max_length=5, blank=True, null=True)
    id_comm_p2 = models.FloatField(blank=True, null=True)
    id_comm_a2 = models.FloatField(blank=True, null=True)
    id_mr_id = models.CharField(max_length=10, blank=True, null=True)
    id_cm_inv_field = models.CharField(db_column='id_cm_inv_', max_length=7, blank=True, null=True)  # Field renamed because it ended with '_'.
    id_cm_inv2 = models.IntegerField(blank=True, null=True)
    id_cm_ship = models.CharField(max_length=8, blank=True, null=True)
    id_cm_shi2 = models.IntegerField(blank=True, null=True)
    id_overrid = models.NullBooleanField()
    id_surchar = models.FloatField(blank=True, null=True)
    id_surch_c = models.FloatField(blank=True, null=True)
    id_ca_code = models.CharField(max_length=12, blank=True, null=True)
    id_ca_cod2 = models.CharField(max_length=12, blank=True, null=True)
    id_ca_cod3 = models.CharField(max_length=12, blank=True, null=True)
    id_ca_cod4 = models.CharField(max_length=12, blank=True, null=True)
    id_gl_id_m = models.CharField(max_length=10, blank=True, null=True)
    id_gl_id_l = models.CharField(max_length=10, blank=True, null=True)
    id_gl_id_b = models.CharField(max_length=10, blank=True, null=True)
    id_gl_id_o = models.CharField(max_length=10, blank=True, null=True)
    id_gl_id_f = models.CharField(max_length=10, blank=True, null=True)
    id_amt_mat = models.FloatField(blank=True, null=True)
    id_amt_lab = models.FloatField(blank=True, null=True)
    id_amt_bur = models.FloatField(blank=True, null=True)
    id_amt_oth = models.FloatField(blank=True, null=True)
    id_amt_fin = models.FloatField(blank=True, null=True)
    id_ca_cod5 = models.CharField(max_length=12, blank=True, null=True)
    id_gl_num_field = models.CharField(db_column='id_gl_num_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    id_gl_num2 = models.CharField(max_length=12, blank=True, null=True)
    id_gl_id_d = models.CharField(max_length=10, blank=True, null=True)
    id_gl_id_s = models.CharField(max_length=10, blank=True, null=True)
    id_amt_dsc = models.FloatField(blank=True, null=True)
    id_amt_sch = models.FloatField(blank=True, null=True)
    id_amt_gro = models.FloatField(blank=True, null=True)
    id_length = models.FloatField(blank=True, null=True)
    id_width = models.FloatField(blank=True, null=True)
    id_quantit = models.FloatField(blank=True, null=True)
    id_wght = models.FloatField(blank=True, null=True)
    id_sc_inv_field = models.CharField(db_column='id_sc_inv_', max_length=7, blank=True, null=True)  # Field renamed because it ended with '_'.
    id_sc_line = models.IntegerField(blank=True, null=True)
    id_sc_invo = models.NullBooleanField()
    id_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    id_sord_li = models.IntegerField(blank=True, null=True)
    id_mu_gm = models.IntegerField(blank=True, null=True)
    id_st_over = models.NullBooleanField()
    id_lo_code = models.CharField(max_length=10, blank=True, null=True)
    id_qtyuom = models.CharField(max_length=4, blank=True, null=True)
    id_comm_ho = models.NullBooleanField()
    id_excl_di = models.NullBooleanField()
    id_receive = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_det'


class InvJdtl(models.Model):
    ie_id = models.CharField(max_length=10, blank=True, null=True)
    ie_ij_id = models.CharField(max_length=10, blank=True, null=True)
    ie_ic_id = models.CharField(max_length=10, blank=True, null=True)
    ie_il_id = models.CharField(max_length=10, blank=True, null=True)
    ie_ib_id = models.CharField(max_length=10, blank=True, null=True)
    ie_invent_field = models.CharField(db_column='ie_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ie_supp_co = models.CharField(max_length=6, blank=True, null=True)
    ie_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    ie_order_n = models.CharField(max_length=12, blank=True, null=True)
    ie_date = models.DateField(blank=True, null=True)
    ie_quantit = models.FloatField(blank=True, null=True)
    ie_unit_co = models.FloatField(blank=True, null=True)
    ie_ext_cos = models.FloatField(blank=True, null=True)
    ie_lot_num = models.CharField(max_length=20, blank=True, null=True)
    ie_lo_code = models.CharField(max_length=10, blank=True, null=True)
    ie_consign = models.NullBooleanField()
    ie_package = models.NullBooleanField()
    ie_op_num = models.IntegerField(blank=True, null=True)
    ie_rev_num = models.CharField(max_length=6, blank=True, null=True)
    ie_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    ie_ext_mat = models.FloatField(blank=True, null=True)
    ie_ext_lab = models.FloatField(blank=True, null=True)
    ie_ext_bur = models.FloatField(blank=True, null=True)
    ie_ext_oth = models.FloatField(blank=True, null=True)
    ie_tag_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_jdtl'


class InvJrnl(models.Model):
    ij_id = models.CharField(max_length=10, blank=True, null=True)
    ij_invent_field = models.CharField(db_column='ij_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ij_order_n = models.CharField(max_length=12, blank=True, null=True)
    ij_date = models.DateField(blank=True, null=True)
    ij_type = models.CharField(max_length=1, blank=True, null=True)
    ij_desc = models.CharField(max_length=30, blank=True, null=True)
    ij_notes = models.TextField(blank=True, null=True)
    ij_quantit = models.FloatField(blank=True, null=True)
    ij_unit_co = models.FloatField(blank=True, null=True)
    ij_ext_cos = models.FloatField(blank=True, null=True)
    ij_protect = models.NullBooleanField()
    ij_lo_code = models.CharField(max_length=10, blank=True, null=True)
    ij_user_id = models.CharField(max_length=5, blank=True, null=True)
    ij_last_mo = models.DateTimeField(blank=True, null=True)
    ij_prod_co = models.CharField(max_length=2, blank=True, null=True)
    ij_dist_co = models.CharField(max_length=2, blank=True, null=True)
    ij_order_2 = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_jrnl'


class InvLctn(models.Model):
    il_id = models.CharField(max_length=10, blank=True, null=True)
    il_lo_code = models.CharField(max_length=10, blank=True, null=True)
    il_code = models.CharField(max_length=10, blank=True, null=True)
    il_desc = models.CharField(max_length=30, blank=True, null=True)
    il_ship = models.NullBooleanField()
    il_de_id = models.CharField(max_length=2, blank=True, null=True)
    il_no_usag = models.NullBooleanField()
    il_supp_co = models.CharField(max_length=6, blank=True, null=True)
    il_consign = models.NullBooleanField()
    il_hold = models.NullBooleanField()
    il_wip = models.NullBooleanField()
    il_rawloc = models.NullBooleanField()
    il_dv_code = models.CharField(max_length=2, blank=True, null=True)
    il_dp_code = models.CharField(max_length=2, blank=True, null=True)
    il_exclude = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'inv_lctn'


class InvLog(models.Model):
    il_date_ti = models.DateTimeField(blank=True, null=True)
    il_user_id = models.CharField(max_length=5, blank=True, null=True)
    il_old_dat = models.DateField(blank=True, null=True)
    il_new_dat = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_log'


class InvPkg(models.Model):
    ig_id = models.CharField(max_length=10, blank=True, null=True)
    ig_invent_field = models.CharField(db_column='ig_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ig_length = models.IntegerField(blank=True, null=True)
    ig_width = models.IntegerField(blank=True, null=True)
    ig_height = models.IntegerField(blank=True, null=True)
    ig_weight = models.IntegerField(blank=True, null=True)
    ig_quantit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_pkg'


class InvRec(models.Model):
    ir_month = models.IntegerField(blank=True, null=True)
    ir_year = models.IntegerField(blank=True, null=True)
    ir_raw_bal = models.FloatField(blank=True, null=True)
    ir_wip_bal = models.FloatField(blank=True, null=True)
    ir_fin_bal = models.FloatField(blank=True, null=True)
    ir_dv_code = models.CharField(max_length=2, blank=True, null=True)
    ir_dp_code = models.CharField(max_length=2, blank=True, null=True)
    ir_gl_raw_field = models.CharField(db_column='ir_gl_raw_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ir_gl_wip_field = models.CharField(db_column='ir_gl_wip_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ir_gl_fin_field = models.CharField(db_column='ir_gl_fin_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ir_gl_pur_field = models.CharField(db_column='ir_gl_pur_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ir_gl_pur2 = models.CharField(max_length=12, blank=True, null=True)
    ir_gl_prd_field = models.CharField(db_column='ir_gl_prd_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ir_gl_prd2 = models.CharField(max_length=12, blank=True, null=True)
    ir_gl_prd3 = models.CharField(max_length=12, blank=True, null=True)
    ir_gl_cgs_field = models.CharField(db_column='ir_gl_cgs_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ir_gl_cgs2 = models.CharField(max_length=12, blank=True, null=True)
    ir_gl_cgs3 = models.CharField(max_length=12, blank=True, null=True)
    ir_gl_cgs4 = models.CharField(max_length=12, blank=True, null=True)
    ir_gl_scra = models.CharField(max_length=12, blank=True, null=True)
    ir_gl_inv_field = models.CharField(db_column='ir_gl_inv_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ir_pur_to_field = models.NullBooleanField(db_column='ir_pur_to_')  # Field renamed because it ended with '_'.
    ir_wip_to_field = models.NullBooleanField(db_column='ir_wip_to_')  # Field renamed because it ended with '_'.
    ir_adj_div = models.NullBooleanField()
    ir_last_mo = models.IntegerField(blank=True, null=True)
    ir_last_ye = models.IntegerField(blank=True, null=True)
    ir_inv_div = models.NullBooleanField()
    ir_cgs_div = models.NullBooleanField()
    ir_entry_n = models.TextField(blank=True, null=True)
    ir_gj_id = models.CharField(max_length=10, blank=True, null=True)
    ir_last_dv = models.CharField(max_length=2, blank=True, null=True)
    ir_last_dp = models.CharField(max_length=2, blank=True, null=True)
    ir_gl_crw_field = models.CharField(db_column='ir_gl_crw_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ir_gl_crw2 = models.CharField(max_length=12, blank=True, null=True)
    ir_gl_crw3 = models.CharField(max_length=12, blank=True, null=True)
    ir_gl_crw4 = models.CharField(max_length=12, blank=True, null=True)
    ir_split_r = models.NullBooleanField()
    ir_split_2 = models.NullBooleanField()
    ir_split_f = models.NullBooleanField()
    ir_split_c = models.NullBooleanField()
    ir_oth_bal = models.FloatField(blank=True, null=True)
    ir_gl_oth_field = models.CharField(db_column='ir_gl_oth_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ir_split_o = models.NullBooleanField()
    ir_ex_oth_field = models.NullBooleanField(db_column='ir_ex_oth_')  # Field renamed because it ended with '_'.
    ir_pd_by_t = models.NullBooleanField()
    ir_use_div = models.NullBooleanField()
    ir_split_s = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'inv_rec'


class InvReo(models.Model):
    ir_id = models.CharField(max_length=10, blank=True, null=True)
    ir_invent_field = models.CharField(db_column='ir_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ir_il_id = models.CharField(max_length=10, blank=True, null=True)
    ir_reo_lev = models.FloatField(blank=True, null=True)
    ir_reo_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_reo'


class InvTrfr(models.Model):
    tf_id = models.CharField(max_length=10, blank=True, null=True)
    tf_invent_field = models.CharField(db_column='tf_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    tf_date = models.DateField(blank=True, null=True)
    tf_quantit = models.FloatField(blank=True, null=True)
    tf_il_id = models.CharField(max_length=10, blank=True, null=True)
    tf_il_id_2 = models.CharField(max_length=10, blank=True, null=True)
    tf_ib_id = models.CharField(max_length=10, blank=True, null=True)
    tf_ib_id_2 = models.CharField(max_length=10, blank=True, null=True)
    tf_order_n = models.CharField(max_length=12, blank=True, null=True)
    tf_order_2 = models.CharField(max_length=12, blank=True, null=True)
    tf_lot_num = models.CharField(max_length=20, blank=True, null=True)
    tf_lot_nu2 = models.CharField(max_length=20, blank=True, null=True)
    tf_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    tf_heat_n2 = models.CharField(max_length=30, blank=True, null=True)
    tf_user_id = models.CharField(max_length=5, blank=True, null=True)
    tf_user_da = models.DateField(blank=True, null=True)
    tf_type = models.CharField(max_length=1, blank=True, null=True)
    tf_op_num = models.IntegerField(blank=True, null=True)
    tf_op_num_field = models.IntegerField(db_column='tf_op_num_', blank=True, null=True)  # Field renamed because it ended with '_'.
    tf_jc_id = models.CharField(max_length=10, blank=True, null=True)
    tf_lot_dat = models.DateField(blank=True, null=True)
    tf_lot_da2 = models.DateField(blank=True, null=True)
    tf_unit_co = models.FloatField(blank=True, null=True)
    tf_unit_ma = models.FloatField(blank=True, null=True)
    tf_unit_la = models.FloatField(blank=True, null=True)
    tf_unit_bu = models.FloatField(blank=True, null=True)
    tf_unit_ot = models.FloatField(blank=True, null=True)
    tf_rev_num = models.CharField(max_length=3, blank=True, null=True)
    tf_rev_nu2 = models.CharField(max_length=3, blank=True, null=True)
    tf_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    tf_rev_le2 = models.CharField(max_length=3, blank=True, null=True)
    tf_tag_num = models.IntegerField(blank=True, null=True)
    tf_tag_nu2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_trfr'


class InvUsag(models.Model):
    iu_jc_id = models.CharField(max_length=10, blank=True, null=True)
    iu_item = models.IntegerField(blank=True, null=True)
    iu_invent_field = models.CharField(db_column='iu_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    iu_invent2 = models.CharField(max_length=30, blank=True, null=True)
    iu_qty = models.FloatField(blank=True, null=True)
    iu_calc = models.CharField(max_length=2, blank=True, null=True)
    iu_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    iu_stock_u = models.FloatField(blank=True, null=True)
    iu_ppbar = models.FloatField(blank=True, null=True)
    iu_ij_id = models.CharField(max_length=10, blank=True, null=True)
    iu_mat_cos = models.FloatField(blank=True, null=True)
    iu_ad_ij_i = models.CharField(max_length=10, blank=True, null=True)
    iu_adjust_field = models.FloatField(db_column='iu_adjust_', blank=True, null=True)  # Field renamed because it ended with '_'.
    iu_wip_val = models.FloatField(blank=True, null=True)
    iu_overrid = models.NullBooleanField()
    iu_length = models.FloatField(blank=True, null=True)
    iu_width = models.FloatField(blank=True, null=True)
    iu_il_id = models.CharField(max_length=10, blank=True, null=True)
    iu_ib_id = models.CharField(max_length=10, blank=True, null=True)
    iu_lot_num = models.CharField(max_length=20, blank=True, null=True)
    iu_al_id = models.CharField(max_length=10, blank=True, null=True)
    iu_return = models.NullBooleanField()
    iu_order_n = models.CharField(max_length=12, blank=True, null=True)
    iu_rel_num = models.IntegerField(blank=True, null=True)
    iu_operati = models.IntegerField(blank=True, null=True)
    iu_emp_id = models.CharField(max_length=5, blank=True, null=True)
    iu_run_dat = models.DateField(blank=True, null=True)
    iu_ext_mat = models.FloatField(blank=True, null=True)
    iu_ext_lab = models.FloatField(blank=True, null=True)
    iu_ext_bur = models.FloatField(blank=True, null=True)
    iu_ext_oth = models.FloatField(blank=True, null=True)
    iu_rev_num = models.CharField(max_length=3, blank=True, null=True)
    iu_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    iu_rework = models.NullBooleanField()
    iu_comment = models.CharField(max_length=10, blank=True, null=True)
    iu_offset = models.NullBooleanField()
    iu_wp_id = models.CharField(max_length=10, blank=True, null=True)
    iu_tag_num = models.IntegerField(blank=True, null=True)
    iu_user_id = models.CharField(max_length=5, blank=True, null=True)
    iu_transti = models.DateTimeField(blank=True, null=True)
    iu_remwidt = models.FloatField(blank=True, null=True)
    iu_remleng = models.FloatField(blank=True, null=True)
    iu_remquan = models.IntegerField(blank=True, null=True)
    iu_unit_co = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_usag'


class InvVend(models.Model):
    va_id = models.CharField(max_length=10, blank=True, null=True)
    va_invent_field = models.CharField(db_column='va_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    va_supp_co = models.CharField(max_length=6, blank=True, null=True)
    va_part_nu = models.CharField(max_length=30, blank=True, null=True)
    va_approve = models.NullBooleanField()
    va_app_dat = models.DateField(blank=True, null=True)
    va_app_by = models.CharField(max_length=5, blank=True, null=True)
    va_cost = models.FloatField(blank=True, null=True)
    va_purch_u = models.CharField(max_length=2, blank=True, null=True)
    va_manufac = models.CharField(max_length=30, blank=True, null=True)
    va_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_vend'


class InventT(models.Model):
    it_invent_field = models.CharField(db_column='it_invent_', max_length=5, blank=True, null=True)  # Field renamed because it ended with '_'.
    it_invent2 = models.CharField(max_length=20, blank=True, null=True)
    it_rgb = models.IntegerField(blank=True, null=True)
    it_dontred = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'invent_t'


class Inventor(models.Model):
    iv_invent_field = models.CharField(db_column='iv_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    iv_invent2 = models.CharField(max_length=50, blank=True, null=True)
    iv_invent3 = models.CharField(max_length=5, blank=True, null=True)
    iv_heat_la = models.IntegerField(blank=True, null=True)
    iv_order_n = models.CharField(max_length=12, blank=True, null=True)
    iv_operati = models.CharField(max_length=3, blank=True, null=True)
    iv_date_re = models.DateField(blank=True, null=True)
    iv_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    iv_shape_c = models.CharField(max_length=7, blank=True, null=True)
    iv_chart_s = models.CharField(max_length=7, blank=True, null=True)
    iv_tol_p = models.FloatField(blank=True, null=True)
    iv_tol_m = models.FloatField(blank=True, null=True)
    iv_mat_len = models.FloatField(blank=True, null=True)
    iv_tot_bar = models.FloatField(blank=True, null=True)
    iv_supp_co = models.CharField(max_length=6, blank=True, null=True)
    iv_quantit = models.FloatField(blank=True, null=True)
    iv_cost_un = models.FloatField(blank=True, null=True)
    iv_tot_val = models.FloatField(blank=True, null=True)
    iv_locatio = models.CharField(max_length=20, blank=True, null=True)
    iv_finish = models.CharField(max_length=5, blank=True, null=True)
    iv_qty_rec = models.FloatField(blank=True, null=True)
    iv_bar_wei = models.FloatField(blank=True, null=True)
    iv_part_nu = models.CharField(max_length=30, blank=True, null=True)
    iv_rev_num = models.CharField(max_length=6, blank=True, null=True)
    iv_ppbar = models.FloatField(blank=True, null=True)
    iv_bars_re = models.FloatField(blank=True, null=True)
    iv_qty_bal = models.FloatField(blank=True, null=True)
    iv_bar_bal = models.FloatField(blank=True, null=True)
    iv_unit_ty = models.IntegerField(blank=True, null=True)
    iv_q_type = models.CharField(max_length=5, blank=True, null=True)
    iv_q_type1 = models.CharField(max_length=6, blank=True, null=True)
    iv_part_le = models.FloatField(blank=True, null=True)
    iv_barend_field = models.IntegerField(db_column='iv_barend_', blank=True, null=True)  # Field renamed because it ended with '_'.
    iv_qty_sch = models.FloatField(blank=True, null=True)
    iv_qty_pro = models.FloatField(blank=True, null=True)
    iv_width = models.CharField(max_length=7, blank=True, null=True)
    iv_calc_ty = models.CharField(max_length=2, blank=True, null=True)
    iv_msquare = models.FloatField(blank=True, null=True)
    iv_price = models.FloatField(blank=True, null=True)
    iv_reo_lev = models.FloatField(blank=True, null=True)
    iv_reo_qty = models.FloatField(blank=True, null=True)
    iv_lead_ti = models.IntegerField(blank=True, null=True)
    iv_alloc_q = models.FloatField(blank=True, null=True)
    iv_need_qt = models.FloatField(blank=True, null=True)
    iv_sup_par = models.CharField(max_length=30, blank=True, null=True)
    iv_sup_cod = models.CharField(max_length=6, blank=True, null=True)
    iv_prod_co = models.CharField(max_length=2, blank=True, null=True)
    iv_used_qt = models.FloatField(blank=True, null=True)
    iv_cht_siz = models.FloatField(blank=True, null=True)
    iv_wide = models.FloatField(blank=True, null=True)
    iv_notes = models.TextField(blank=True, null=True)
    iv_aver_co = models.FloatField(blank=True, null=True)
    iv_convert = models.FloatField(blank=True, null=True)
    iv_purch_u = models.CharField(max_length=2, blank=True, null=True)
    iv_len_uom = models.CharField(max_length=2, blank=True, null=True)
    iv_last_co = models.FloatField(blank=True, null=True)
    iv_cost_me = models.CharField(max_length=1, blank=True, null=True)
    iv_pupdate = models.DateField(blank=True, null=True)
    iv_cupdate = models.DateField(blank=True, null=True)
    iv_markup = models.IntegerField(blank=True, null=True)
    iv_misc_mu = models.IntegerField(blank=True, null=True)
    iv_mat_mu = models.IntegerField(blank=True, null=True)
    iv_mat_cos = models.FloatField(blank=True, null=True)
    iv_misc_co = models.FloatField(blank=True, null=True)
    iv_man_cos = models.FloatField(blank=True, null=True)
    iv_comp_as = models.CharField(max_length=1, blank=True, null=True)
    iv_make_bu = models.CharField(max_length=1, blank=True, null=True)
    iv_setup_c = models.FloatField(blank=True, null=True)
    iv_sub_cos = models.FloatField(blank=True, null=True)
    iv_quote_n = models.CharField(max_length=15, blank=True, null=True)
    iv_ext_des = models.TextField(blank=True, null=True)
    iv_part_ty = models.CharField(max_length=1, blank=True, null=True)
    iv_lot_siz = models.FloatField(blank=True, null=True)
    iv_il_id = models.CharField(max_length=10, blank=True, null=True)
    iv_ib_id = models.CharField(max_length=10, blank=True, null=True)
    iv_box_typ = models.TextField(blank=True, null=True)
    iv_box_qty = models.FloatField(blank=True, null=True)
    iv_bt_code = models.CharField(max_length=3, blank=True, null=True)
    iv_fin_wei = models.FloatField(blank=True, null=True)
    iv_alloc = models.NullBooleanField()
    iv_draw_nu = models.CharField(max_length=30, blank=True, null=True)
    iv_draw_re = models.CharField(max_length=6, blank=True, null=True)
    iv_usesuom = models.NullBooleanField()
    iv_dist_co = models.CharField(max_length=2, blank=True, null=True)
    iv_qtq = models.IntegerField(blank=True, null=True)
    iv_weeks_o = models.FloatField(blank=True, null=True)
    iv_height = models.FloatField(blank=True, null=True)
    iv_in_lowc = models.NullBooleanField()
    iv_purge_d = models.DateField(blank=True, null=True)
    iv_app_onl = models.NullBooleanField()
    iv_abc_typ = models.CharField(max_length=1, blank=True, null=True)
    iv_count_d = models.DateField(blank=True, null=True)
    iv_count_2 = models.IntegerField(blank=True, null=True)
    iv_unit_ma = models.FloatField(blank=True, null=True)
    iv_unit_la = models.FloatField(blank=True, null=True)
    iv_unit_bu = models.FloatField(blank=True, null=True)
    iv_unit_ot = models.FloatField(blank=True, null=True)
    iv_user_id = models.CharField(max_length=5, blank=True, null=True)
    iv_last_mo = models.DateTimeField(blank=True, null=True)
    iv_stepup = models.IntegerField(blank=True, null=True)
    iv_web_thi = models.FloatField(blank=True, null=True)
    iv_lock_ba = models.NullBooleanField()
    iv_master = models.NullBooleanField()
    iv_master_field = models.CharField(db_column='iv_master_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    iv_old_box = models.TextField(blank=True, null=True)
    iv_req_mac = models.CharField(max_length=5, blank=True, null=True)
    iv_req_fg_field = models.CharField(db_column='iv_req_fg_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    iv_req_tg_field = models.CharField(db_column='iv_req_tg_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    iv_req_too = models.CharField(max_length=20, blank=True, null=True)
    iv_lo_code = models.CharField(max_length=10, blank=True, null=True)
    iv_class_t = models.CharField(max_length=5, blank=True, null=True)
    iv_mat_spe = models.CharField(max_length=50, blank=True, null=True)
    iv_extatrb = models.CharField(max_length=20, blank=True, null=True)
    iv_extatr2 = models.CharField(max_length=20, blank=True, null=True)
    iv_extatr3 = models.CharField(max_length=20, blank=True, null=True)
    iv_extatr4 = models.CharField(max_length=20, blank=True, null=True)
    iv_extatr5 = models.CharField(max_length=20, blank=True, null=True)
    iv_extatr6 = models.CharField(max_length=20, blank=True, null=True)
    iv_extatr7 = models.CharField(max_length=20, blank=True, null=True)
    iv_extatr8 = models.CharField(max_length=20, blank=True, null=True)
    iv_extatr9 = models.CharField(max_length=20, blank=True, null=True)
    iv_extat10 = models.CharField(max_length=20, blank=True, null=True)
    iv_cust_co = models.CharField(max_length=6, blank=True, null=True)
    iv_bf_ship = models.NullBooleanField()
    iv_pfep = models.IntegerField(blank=True, null=True)
    iv_wts_buf = models.IntegerField(blank=True, null=True)
    iv_fg_buf = models.IntegerField(blank=True, null=True)
    iv_exp_day = models.NullBooleanField()
    iv_so_stan = models.CharField(max_length=8, blank=True, null=True)
    iv_contain = models.DateField(blank=True, null=True)
    iv_contai2 = models.CharField(max_length=10, blank=True, null=True)
    iv_contai3 = models.TextField(blank=True, null=True)
    iv_family = models.CharField(max_length=5, blank=True, null=True)
    iv_wip = models.NullBooleanField()
    iv_tare_we = models.FloatField(blank=True, null=True)
    iv_qty_low = models.FloatField(blank=True, null=True)
    iv_qty_upp = models.FloatField(blank=True, null=True)
    iv_wght_lo = models.FloatField(blank=True, null=True)
    iv_wght_up = models.FloatField(blank=True, null=True)
    iv_lr_id = models.CharField(max_length=10, blank=True, null=True)
    iv_tickets = models.FloatField(blank=True, null=True)
    iv_lr_id_m = models.CharField(max_length=10, blank=True, null=True)
    iv_gage_od = models.FloatField(blank=True, null=True)
    iv_gage_o2 = models.FloatField(blank=True, null=True)
    iv_gage_do = models.FloatField(blank=True, null=True)
    iv_gage_hv = models.FloatField(blank=True, null=True)
    iv_gage_le = models.FloatField(blank=True, null=True)
    iv_gage_bf = models.FloatField(blank=True, null=True)
    iv_gage_pd = models.FloatField(blank=True, null=True)
    iv_gage_hn = models.CharField(max_length=5, blank=True, null=True)
    iv_gage_ty = models.CharField(max_length=5, blank=True, null=True)
    iv_gage_tf = models.CharField(max_length=5, blank=True, null=True)
    iv_gage_cl = models.CharField(max_length=5, blank=True, null=True)
    iv_gage_nd = models.FloatField(blank=True, null=True)
    iv_gage_pi = models.FloatField(blank=True, null=True)
    iv_gage_md = models.FloatField(blank=True, null=True)
    iv_apw_upp = models.FloatField(blank=True, null=True)
    iv_apw_low = models.FloatField(blank=True, null=True)
    iv_seriali = models.NullBooleanField()
    iv_ep_code = models.CharField(max_length=2, blank=True, null=True)
    iv_ser_typ = models.IntegerField(blank=True, null=True)
    iv_exp_tar = models.CharField(max_length=20, blank=True, null=True)
    iv_exp_cnt = models.CharField(max_length=20, blank=True, null=True)
    iv_non_sto = models.NullBooleanField()
    iv_nm_code = models.CharField(max_length=10, blank=True, null=True)
    iv_invent4 = models.CharField(max_length=1, blank=True, null=True)
    iv_pallet_field = models.FloatField(db_column='iv_pallet_', blank=True, null=True)  # Field renamed because it ended with '_'.
    iv_pallet2 = models.FloatField(blank=True, null=True)
    iv_eau = models.IntegerField(blank=True, null=True)
    iv_skip_au = models.NullBooleanField()
    iv_cert_nu = models.CharField(max_length=15, blank=True, null=True)
    iv_planner = models.CharField(max_length=5, blank=True, null=True)
    iv_obsolet = models.NullBooleanField()
    iv_parts_p = models.IntegerField(blank=True, null=True)
    iv_surchar = models.FloatField(blank=True, null=True)
    iv_no_subo = models.NullBooleanField()
    iv_ppap_da = models.DateField(blank=True, null=True)
    iv_scrap_p = models.IntegerField(blank=True, null=True)
    iv_bulk_lo = models.FloatField(blank=True, null=True)
    iv_bulk_hi = models.FloatField(blank=True, null=True)
    iv_feature = models.CharField(max_length=20, blank=True, null=True)
    iv_conv_fa = models.FloatField(blank=True, null=True)
    iv_max_qty = models.FloatField(blank=True, null=True)
    iv_extat11 = models.CharField(max_length=20, blank=True, null=True)
    iv_bulk2_l = models.FloatField(blank=True, null=True)
    iv_bulk2_h = models.FloatField(blank=True, null=True)
    iv_created = models.CharField(max_length=5, blank=True, null=True)
    iv_dt_pric = models.DateField(blank=True, null=True)
    iv_no_subt = models.NullBooleanField()
    iv_hcc = models.FloatField(blank=True, null=True)
    iv_extat12 = models.CharField(max_length=10, blank=True, null=True)
    iv_extat13 = models.CharField(max_length=5, blank=True, null=True)
    iv_extat14 = models.CharField(max_length=5, blank=True, null=True)
    iv_pack_st = models.CharField(max_length=10, blank=True, null=True)
    iv_pcs_rac = models.IntegerField(blank=True, null=True)
    iv_num_ski = models.IntegerField(blank=True, null=True)
    iv_num_car = models.IntegerField(blank=True, null=True)
    iv_commiss = models.FloatField(blank=True, null=True)
    iv_excl_sc = models.NullBooleanField()
    iv_paintfa = models.FloatField(blank=True, null=True)
    iv_inspect = models.NullBooleanField()
    iv_exclude = models.NullBooleanField()
    iv_serial_field = models.IntegerField(db_column='iv_serial_', blank=True, null=True)  # Field renamed because it ended with '_'.
    iv_minweek = models.FloatField(blank=True, null=True)
    iv_maxweek = models.FloatField(blank=True, null=True)
    iv_turns = models.IntegerField(blank=True, null=True)
    iv_continu = models.NullBooleanField()
    iv_eau_quo = models.CharField(max_length=15, blank=True, null=True)
    iv_price1 = models.FloatField(blank=True, null=True)
    iv_price2 = models.FloatField(blank=True, null=True)
    iv_price3 = models.FloatField(blank=True, null=True)
    iv_price4 = models.FloatField(blank=True, null=True)
    iv_de_id = models.CharField(max_length=2, blank=True, null=True)
    iv_small = models.NullBooleanField()
    iv_picpath = models.TextField(blank=True, null=True)
    iv_date_cr = models.DateField(blank=True, null=True)
    iv_lotspec = models.NullBooleanField()
    iv_datecre = models.DateField(blank=True, null=True)
    iv_pantick = models.CharField(max_length=20, blank=True, null=True)
    iv_manufac = models.CharField(max_length=30, blank=True, null=True)
    iv_upc = models.CharField(max_length=12, blank=True, null=True)
    iv_ff_il_i = models.CharField(max_length=10, blank=True, null=True)
    iv_ff_ib_i = models.CharField(max_length=10, blank=True, null=True)
    iv_prefere = models.CharField(max_length=1, blank=True, null=True)
    iv_produce = models.CharField(max_length=1, blank=True, null=True)
    iv_netcost = models.CharField(max_length=2, blank=True, null=True)
    iv_dontpro = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'inventor'


class Invoice(models.Model):
    in_inv_num = models.CharField(max_length=7, blank=True, primary_key=True)
    in_inv_typ = models.CharField(max_length=1, blank=True, null=True)
    in_inv_dat = models.DateField(blank=True, null=True)
    in_cust_co = models.CharField(max_length=6, blank=True, null=True)
    in_batch = models.CharField(max_length=1, blank=True, null=True)
    in_print_d = models.DateField(blank=True, null=True)
    in_ship_vi = models.CharField(max_length=40, blank=True, null=True)
    in_net_amt = models.FloatField(blank=True, null=True)
    in_taxes = models.FloatField(blank=True, null=True)
    in_tot_amt = models.FloatField(blank=True, null=True)
    in_exp_dat = models.DateField(blank=True, null=True)
    in_post = models.NullBooleanField()
    in_post_da = models.DateField(blank=True, null=True)
    in_comp_na = models.CharField(max_length=33, blank=True, null=True)
    in_address = models.CharField(max_length=33, blank=True, null=True)
    in_addres2 = models.CharField(max_length=33, blank=True, null=True)
    in_addres3 = models.CharField(max_length=33, blank=True, null=True)
    in_ship_co = models.CharField(max_length=8, blank=True, null=True)
    in_ship_da = models.DateField(blank=True, null=True)
    in_po_num = models.CharField(max_length=25, blank=True, null=True)
    in_inv_sta = models.CharField(max_length=1, blank=True, null=True)
    in_contact = models.CharField(max_length=25, blank=True, null=True)
    in_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    in_emp_id = models.CharField(max_length=5, blank=True, null=True)
    in_pay_ter = models.CharField(max_length=20, blank=True, null=True)
    in_due_dat = models.DateField(blank=True, null=True)
    in_disc_da = models.DateField(blank=True, null=True)
    in_lo_code = models.CharField(max_length=10, blank=True, null=True)
    in_type = models.CharField(max_length=1, blank=True, null=True)
    in_inv_bal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_ch_num = models.CharField(max_length=10, blank=True, null=True)
    in_ch_date = models.DateField(blank=True, null=True)
    in_cash_ap = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_stmt = models.NullBooleanField()
    in_gl_num = models.CharField(max_length=12, blank=True, null=True)
    in_gl_id = models.CharField(max_length=10, blank=True, null=True)
    in_startmo = models.NullBooleanField()
    in_entry_d = models.DateField(blank=True, null=True)
    in_ship_to = models.CharField(max_length=3, blank=True, null=True)
    in_st_id_1 = models.CharField(max_length=10, blank=True, null=True)
    in_st_id_2 = models.CharField(max_length=10, blank=True, null=True)
    in_stax_id = models.CharField(max_length=25, blank=True, null=True)
    in_tax_exe = models.NullBooleanField()
    in_exempt_field = models.CharField(db_column='in_exempt_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    in_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    in_cur_rat = models.FloatField(blank=True, null=True)
    in_net_cur = models.FloatField(blank=True, null=True)
    in_tax_cur = models.FloatField(blank=True, null=True)
    in_tot_cur = models.FloatField(blank=True, null=True)
    in_addres4 = models.CharField(max_length=33, blank=True, null=True)
    in_ca_id = models.CharField(max_length=10, blank=True, null=True)
    in_discoun = models.FloatField(blank=True, null=True)
    in_disc_cu = models.FloatField(blank=True, null=True)
    in_surchar = models.FloatField(blank=True, null=True)
    in_surch_c = models.FloatField(blank=True, null=True)
    in_grs_amt = models.FloatField(blank=True, null=True)
    in_grs_cur = models.FloatField(blank=True, null=True)
    in_note = models.TextField(blank=True, null=True)
    in_use_sur = models.NullBooleanField()
    in_split_s = models.NullBooleanField()
    in_only_su = models.NullBooleanField()
    in_fob = models.CharField(max_length=15, blank=True, null=True)
    in_billto_field = models.CharField(db_column='in_billto_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    in_foblabe = models.CharField(max_length=3, blank=True, null=True)
    in_edi_810 = models.DateField(blank=True, null=True)
    in_edi_812 = models.CharField(max_length=5, blank=True, null=True)
    in_deldate = models.DateField(blank=True, null=True)
    in_destina = models.CharField(max_length=4, blank=True, null=True)
    in_noncoll = models.NullBooleanField()
    in_nc_inv_field = models.CharField(db_column='in_nc_inv_', max_length=7, blank=True, null=True)  # Field renamed because it ended with '_'.
    in_nc_date = models.DateField(blank=True, null=True)
    in_nc_mast = models.NullBooleanField()
    in_lm_user = models.CharField(max_length=5, blank=True, null=True)
    in_lm_date = models.DateTimeField(blank=True, null=True)
    in_ex_coll = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'invoice'


class Itemdisc(models.Model):
    id_invent_field = models.CharField(db_column='id_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    id_start_q = models.FloatField(blank=True, null=True)
    id_end_qty = models.FloatField(blank=True, null=True)
    id_amount = models.FloatField(blank=True, null=True)
    id_is_cost = models.NullBooleanField()
    id_option = models.NullBooleanField()
    id_percent = models.NullBooleanField()
    id_cust_co = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemdisc'


class Ivetb(models.Model):
    db_id = models.CharField(max_length=10, blank=True, null=True)
    db_user_id = models.CharField(max_length=5, blank=True, null=True)
    db_dm_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivetb'


class Ivetissu(models.Model):
    is_guid = models.CharField(max_length=36, blank=True, null=True)
    is_date = models.DateTimeField(blank=True, null=True)
    is_order_n = models.CharField(max_length=12, blank=True, null=True)
    is_rel_num = models.IntegerField(blank=True, null=True)
    is_op_num = models.IntegerField(blank=True, null=True)
    is_invent_field = models.CharField(db_column='is_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    is_uom = models.CharField(max_length=10, blank=True, null=True)
    is_quantit = models.FloatField(blank=True, null=True)
    is_emp_id = models.CharField(max_length=5, blank=True, null=True)
    is_il_id = models.CharField(max_length=10, blank=True, null=True)
    is_ib_id = models.CharField(max_length=10, blank=True, null=True)
    is_lot_num = models.CharField(max_length=20, blank=True, null=True)
    is_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    is_rev = models.CharField(max_length=6, blank=True, null=True)
    is_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    is_tag_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivetissu'


class Ivetmenu(models.Model):
    dm_id = models.CharField(max_length=10, blank=True, null=True)
    dm_option = models.CharField(max_length=50, blank=True, null=True)
    dm_orderby = models.IntegerField(blank=True, null=True)
    dm_windown = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivetmenu'


class Ivettrgr(models.Model):
    tr_invent_field = models.CharField(db_column='tr_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    tr_fromil_field = models.CharField(db_column='tr_fromil_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    tr_fromib_field = models.CharField(db_column='tr_fromib_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    tr_toil_id = models.CharField(max_length=10, blank=True, null=True)
    tr_toib_id = models.CharField(max_length=10, blank=True, null=True)
    tr_box1 = models.IntegerField(blank=True, null=True)
    tr_qty1 = models.FloatField(blank=True, null=True)
    tr_box2 = models.IntegerField(blank=True, null=True)
    tr_qty2 = models.FloatField(blank=True, null=True)
    tr_user = models.CharField(max_length=10, blank=True, null=True)
    tr_guid = models.CharField(max_length=36, blank=True, null=True)
    tr_quantit = models.FloatField(blank=True, null=True)
    tr_print = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ivettrgr'


class Ivhazmat(models.Model):
    hm_invent_field = models.CharField(db_column='hm_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    hm_corrosi = models.NullBooleanField()
    hm_environ = models.NullBooleanField()
    hm_explbom = models.NullBooleanField()
    hm_expoint = models.NullBooleanField()
    hm_flame = models.NullBooleanField()
    hm_flameov = models.NullBooleanField()
    hm_gascyli = models.NullBooleanField()
    hm_healthh = models.NullBooleanField()
    hm_skullxc = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ivhazmat'


class Jcardman(models.Model):
    jc_id = models.CharField(max_length=10, blank=True, null=True)
    jc_run_dat = models.DateField(blank=True, null=True)
    jc_shift = models.CharField(max_length=2, blank=True, null=True)
    jc_order_n = models.CharField(max_length=12, blank=True, null=True)
    jc_operati = models.IntegerField(blank=True, null=True)
    jc_mach_co = models.CharField(max_length=5, blank=True, null=True)
    jc_emp_id = models.CharField(max_length=5, blank=True, null=True)
    jc_in_inve = models.CharField(max_length=30, blank=True, null=True)
    jc_in_qty = models.FloatField(blank=True, null=True)
    jc_hrs_ava = models.FloatField(blank=True, null=True)
    jc_hrs_set = models.FloatField(blank=True, null=True)
    jc_hrs_tot = models.FloatField(blank=True, null=True)
    jc_hrs_tdo = models.FloatField(blank=True, null=True)
    jc_hrs_odo = models.FloatField(blank=True, null=True)
    jc_hrs_pro = models.FloatField(blank=True, null=True)
    jc_down_re = models.CharField(max_length=80, blank=True, null=True)
    jc_parts_p = models.FloatField(blank=True, null=True)
    jc_parts_b = models.FloatField(blank=True, null=True)
    jc_parts_g = models.FloatField(blank=True, null=True)
    jc_out_inv = models.CharField(max_length=30, blank=True, null=True)
    jc_gp = models.FloatField(blank=True, null=True)
    jc_np = models.FloatField(blank=True, null=True)
    jc_act_phr = models.FloatField(blank=True, null=True)
    jc_adj_phr = models.FloatField(blank=True, null=True)
    jc_go_eff = models.IntegerField(blank=True, null=True)
    jc_p_eff = models.IntegerField(blank=True, null=True)
    jc_o_eff = models.IntegerField(blank=True, null=True)
    jc_run_cod = models.CharField(max_length=20, blank=True, null=True)
    jc_su = models.IntegerField(blank=True, null=True)
    jc_prod1 = models.FloatField(blank=True, null=True)
    jc_prod2 = models.FloatField(blank=True, null=True)
    jc_prod3 = models.FloatField(blank=True, null=True)
    jc_prod4 = models.FloatField(blank=True, null=True)
    jc_rework1 = models.FloatField(blank=True, null=True)
    jc_rework2 = models.FloatField(blank=True, null=True)
    jc_rework3 = models.FloatField(blank=True, null=True)
    jc_rework4 = models.FloatField(blank=True, null=True)
    jc_rework = models.FloatField(blank=True, null=True)
    jc_scrap1 = models.FloatField(blank=True, null=True)
    jc_scrap2 = models.FloatField(blank=True, null=True)
    jc_scrap3 = models.FloatField(blank=True, null=True)
    jc_scrap4 = models.FloatField(blank=True, null=True)
    jc_scrap = models.FloatField(blank=True, null=True)
    jc_track1 = models.CharField(max_length=10, blank=True, null=True)
    jc_track2 = models.CharField(max_length=10, blank=True, null=True)
    jc_track3 = models.CharField(max_length=10, blank=True, null=True)
    jc_track4 = models.CharField(max_length=10, blank=True, null=True)
    jc_good1 = models.FloatField(blank=True, null=True)
    jc_good2 = models.FloatField(blank=True, null=True)
    jc_good3 = models.FloatField(blank=True, null=True)
    jc_good4 = models.FloatField(blank=True, null=True)
    jc_burdenp = models.FloatField(blank=True, null=True)
    jc_burdens = models.FloatField(blank=True, null=True)
    jc_laborp = models.FloatField(blank=True, null=True)
    jc_labors = models.FloatField(blank=True, null=True)
    jc_num_mac = models.IntegerField(blank=True, null=True)
    jc_calc = models.CharField(max_length=2, blank=True, null=True)
    jc_ot_hrs_field = models.FloatField(db_column='jc_ot_hrs_', blank=True, null=True)  # Field renamed because it ended with '_'.
    jc_ot_hrs2 = models.FloatField(blank=True, null=True)
    jc_rel_num = models.IntegerField(blank=True, null=True)
    jc_in_inv2 = models.CharField(max_length=30, blank=True, null=True)
    jc_in_inv3 = models.CharField(max_length=30, blank=True, null=True)
    jc_in_inv4 = models.CharField(max_length=30, blank=True, null=True)
    jc_in_inv5 = models.CharField(max_length=30, blank=True, null=True)
    jc_in_inv6 = models.CharField(max_length=30, blank=True, null=True)
    jc_in_inv7 = models.CharField(max_length=30, blank=True, null=True)
    jc_in_inv8 = models.CharField(max_length=30, blank=True, null=True)
    jc_in_inv9 = models.CharField(max_length=30, blank=True, null=True)
    jc_in_in10 = models.CharField(max_length=30, blank=True, null=True)
    jc_in_qty1 = models.FloatField(blank=True, null=True)
    jc_in_qty2 = models.FloatField(blank=True, null=True)
    jc_in_qty3 = models.FloatField(blank=True, null=True)
    jc_in_qty4 = models.FloatField(blank=True, null=True)
    jc_in_qty5 = models.FloatField(blank=True, null=True)
    jc_in_qty6 = models.FloatField(blank=True, null=True)
    jc_in_qty7 = models.FloatField(blank=True, null=True)
    jc_in_qty8 = models.FloatField(blank=True, null=True)
    jc_in_qty9 = models.FloatField(blank=True, null=True)
    jc_calc1 = models.CharField(max_length=2, blank=True, null=True)
    jc_calc2 = models.CharField(max_length=2, blank=True, null=True)
    jc_calc3 = models.CharField(max_length=2, blank=True, null=True)
    jc_calc4 = models.CharField(max_length=2, blank=True, null=True)
    jc_calc5 = models.CharField(max_length=2, blank=True, null=True)
    jc_calc6 = models.CharField(max_length=2, blank=True, null=True)
    jc_calc7 = models.CharField(max_length=2, blank=True, null=True)
    jc_calc8 = models.CharField(max_length=2, blank=True, null=True)
    jc_calc9 = models.CharField(max_length=2, blank=True, null=True)
    jc_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    jc_heat_n2 = models.IntegerField(blank=True, null=True)
    jc_heat_n3 = models.IntegerField(blank=True, null=True)
    jc_heat_n4 = models.IntegerField(blank=True, null=True)
    jc_heat_n5 = models.IntegerField(blank=True, null=True)
    jc_heat_n6 = models.IntegerField(blank=True, null=True)
    jc_heat_n7 = models.IntegerField(blank=True, null=True)
    jc_heat_n8 = models.IntegerField(blank=True, null=True)
    jc_heat_n9 = models.IntegerField(blank=True, null=True)
    jc_heat_10 = models.IntegerField(blank=True, null=True)
    jc_ws = models.NullBooleanField()
    jc_review1 = models.FloatField(blank=True, null=True)
    jc_review2 = models.FloatField(blank=True, null=True)
    jc_review3 = models.FloatField(blank=True, null=True)
    jc_review = models.FloatField(blank=True, null=True)
    jc_defect = models.CharField(max_length=10, blank=True, null=True)
    jc_il_id = models.CharField(max_length=10, blank=True, null=True)
    jc_ib_id = models.CharField(max_length=10, blank=True, null=True)
    jc_ij_id = models.CharField(max_length=10, blank=True, null=True)
    jc_sc_ij_i = models.CharField(max_length=10, blank=True, null=True)
    jc_zero_wi = models.NullBooleanField()
    jc_move_st = models.NullBooleanField()
    jc_dot_hrs = models.FloatField(blank=True, null=True)
    jc_dot_hr2 = models.FloatField(blank=True, null=True)
    jc_complet = models.NullBooleanField()
    jc_lot_num = models.CharField(max_length=20, blank=True, null=True)
    jc_notes = models.TextField(blank=True, null=True)
    jc_other_d = models.CharField(max_length=5, blank=True, null=True)
    jc_perc_at = models.IntegerField(blank=True, null=True)
    jc_inlot_n = models.CharField(max_length=20, blank=True, null=True)
    jc_wip_tra = models.NullBooleanField()
    jc_resave = models.NullBooleanField()
    jc_insp_by = models.CharField(max_length=5, blank=True, null=True)
    jc_repost_field = models.NullBooleanField(db_column='jc_repost_')  # Field renamed because it ended with '_'.
    jc_incl_re = models.NullBooleanField()
    jc_reject = models.IntegerField(blank=True, null=True)
    jc_id_code = models.CharField(max_length=10, blank=True, null=True)
    jc_de_id = models.CharField(max_length=10, blank=True, null=True)
    jc_startup = models.NullBooleanField()
    jc_aj_id = models.CharField(max_length=10, blank=True, null=True)
    jc_passfai = models.IntegerField(blank=True, null=True)
    jc_tool_ty = models.CharField(max_length=20, blank=True, null=True)
    jc_st_id = models.CharField(max_length=2, blank=True, null=True)
    jc_lc_id = models.CharField(max_length=10, blank=True, null=True)
    jc_rg_id = models.CharField(max_length=10, blank=True, null=True)
    jc_wp_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jcardman'


class Jcmobdet(models.Model):
    id = models.CharField(max_length=10, blank=True, primary_key=True)
    jm_id = models.CharField(max_length=10, blank=True, null=True)
    timecat = models.CharField(max_length=2, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    elapsetime = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jcmobdet'


class Jcmobile(models.Model):
    ddate = models.DateField(blank=True, null=True)
    cemp = models.CharField(max_length=5, blank=True, null=True)
    cruncode = models.CharField(max_length=20, blank=True, null=True)
    ncount = models.IntegerField(blank=True, null=True)
    nscrap = models.IntegerField(blank=True, null=True)
    nproduced = models.IntegerField(blank=True, null=True)
    nhours = models.FloatField(blank=True, null=True)
    cdown_reas = models.CharField(max_length=60, blank=True, null=True)
    nsuhours = models.FloatField(blank=True, null=True)
    ndnhours = models.FloatField(blank=True, null=True)
    cdtcode = models.CharField(max_length=5, blank=True, null=True)
    validrec = models.CharField(max_length=1, blank=True, null=True)
    imported = models.NullBooleanField()
    dateimport = models.DateField(blank=True, null=True)
    jm_id = models.CharField(max_length=10, blank=True, null=True)
    jm_inproce = models.NullBooleanField()
    jm_state = models.CharField(max_length=20, blank=True, null=True)
    aj_id = models.CharField(max_length=10, blank=True, null=True)
    readytopro = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'jcmobile'


class Kpi(models.Model):
    kp_id = models.CharField(max_length=10, blank=True, null=True)
    kp_legend = models.CharField(max_length=50, blank=True, null=True)
    kp_categor = models.CharField(max_length=10, blank=True, null=True)
    kp_units = models.CharField(max_length=20, blank=True, null=True)
    kp_target_field = models.FloatField(db_column='kp_target_', blank=True, null=True)  # Field renamed because it ended with '_'.
    kp_graphra = models.FloatField(blank=True, null=True)
    kp_lefttor = models.NullBooleanField()
    kp_redrang = models.FloatField(blank=True, null=True)
    kp_yellowr = models.FloatField(blank=True, null=True)
    kp_greenra = models.FloatField(blank=True, null=True)
    kp_timefra = models.CharField(max_length=1, blank=True, null=True)
    kp_1 = models.FloatField(blank=True, null=True)
    kp_2 = models.FloatField(blank=True, null=True)
    kp_3 = models.FloatField(blank=True, null=True)
    kp_4 = models.FloatField(blank=True, null=True)
    kp_5 = models.FloatField(blank=True, null=True)
    kp_6 = models.FloatField(blank=True, null=True)
    kp_7 = models.FloatField(blank=True, null=True)
    kp_8 = models.FloatField(blank=True, null=True)
    kp_9 = models.FloatField(blank=True, null=True)
    kp_10 = models.FloatField(blank=True, null=True)
    kp_11 = models.FloatField(blank=True, null=True)
    kp_12 = models.FloatField(blank=True, null=True)
    kp_percent = models.FloatField(blank=True, null=True)
    kp_color = models.CharField(max_length=1, blank=True, null=True)
    kp_dept = models.CharField(max_length=20, blank=True, null=True)
    kp_respons = models.CharField(max_length=30, blank=True, null=True)
    kp_graphle = models.CharField(max_length=30, blank=True, null=True)
    kp_inactiv = models.NullBooleanField()
    kp_subtype = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kpi'


class Kpidata(models.Model):
    kd_id = models.CharField(max_length=10, blank=True, null=True)
    kd_kp_id = models.CharField(max_length=10, blank=True, null=True)
    kd_date = models.DateField(blank=True, null=True)
    kd_quantit = models.FloatField(blank=True, null=True)
    kd_ks_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kpidata'


class Kpimonit(models.Model):
    ks_id = models.CharField(max_length=10, blank=True, null=True)
    ks_kp_id = models.CharField(max_length=10, blank=True, null=True)
    ks_st_code = models.CharField(max_length=10, blank=True, null=True)
    ks_kp_targ = models.FloatField(blank=True, null=True)
    ks_kp_grap = models.FloatField(blank=True, null=True)
    ks_kp_redr = models.FloatField(blank=True, null=True)
    ks_kp_yell = models.FloatField(blank=True, null=True)
    ks_kp_gree = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kpimonit'


class LabRpt(models.Model):
    lr_id = models.CharField(max_length=10, blank=True, null=True)
    lr_name = models.CharField(max_length=20, blank=True, null=True)
    lr_desc = models.CharField(max_length=50, blank=True, null=True)
    lr_filenam = models.CharField(max_length=8, blank=True, null=True)
    lr_type = models.CharField(max_length=1, blank=True, null=True)
    lr_donor = models.CharField(max_length=8, blank=True, null=True)
    lr_user_id = models.CharField(max_length=5, blank=True, null=True)
    lr_date = models.DateField(blank=True, null=True)
    lr_no_copi = models.IntegerField(blank=True, null=True)
    lr_cust_co = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_rpt'


class Laser(models.Model):
    lz_id = models.CharField(max_length=10, blank=True, null=True)
    lz_mat_cod = models.CharField(max_length=3, blank=True, null=True)
    lz_mat_thk = models.FloatField(blank=True, null=True)
    lz_lg_cont = models.FloatField(blank=True, null=True)
    lz_md_cont = models.FloatField(blank=True, null=True)
    lz_sm_cont = models.FloatField(blank=True, null=True)
    lz_pierce = models.FloatField(blank=True, null=True)
    lz_lg_con2 = models.FloatField(blank=True, null=True)
    lz_md_con2 = models.FloatField(blank=True, null=True)
    lz_sm_con2 = models.FloatField(blank=True, null=True)
    lz_pierce_field = models.FloatField(db_column='lz_pierce_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'laser'


class Lateship(models.Model):
    ls_code = models.CharField(max_length=10, blank=True, null=True)
    ls_desc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lateship'


class Locality(models.Model):
    lo_id = models.CharField(max_length=10, blank=True, null=True)
    lo_st_id = models.CharField(max_length=10, blank=True, null=True)
    lo_name = models.CharField(max_length=25, blank=True, null=True)
    lo_stx_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locality'


class Location(models.Model):
    lo_code = models.CharField(max_length=10, blank=True, null=True)
    lo_desc = models.CharField(max_length=30, blank=True, null=True)
    lo_size = models.CharField(max_length=1, blank=True, null=True)
    lo_comp_na = models.CharField(max_length=35, blank=True, null=True)
    lo_address = models.CharField(max_length=35, blank=True, null=True)
    lo_addres2 = models.CharField(max_length=35, blank=True, null=True)
    lo_city = models.CharField(max_length=15, blank=True, null=True)
    lo_state = models.CharField(max_length=3, blank=True, null=True)
    lo_zip = models.CharField(max_length=10, blank=True, null=True)
    lo_country = models.CharField(max_length=20, blank=True, null=True)
    lo_logo = models.CharField(max_length=80, blank=True, null=True)
    lo_use = models.NullBooleanField()
    lo_phone = models.CharField(max_length=14, blank=True, null=True)
    lo_fax = models.CharField(max_length=14, blank=True, null=True)
    lo_so_memo = models.TextField(blank=True, null=True)
    lo_qu_memo = models.TextField(blank=True, null=True)
    lo_no_mark = models.NullBooleanField()
    lo_fob = models.CharField(max_length=15, blank=True, null=True)
    lo_gl_num_field = models.CharField(db_column='lo_gl_num_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    lo_foblabe = models.CharField(max_length=3, blank=True, null=True)
    lo_il_id = models.CharField(max_length=10, blank=True, null=True)
    lo_ib_id = models.CharField(max_length=10, blank=True, null=True)
    lo_prod_co = models.CharField(max_length=2, blank=True, null=True)
    lo_sh_memo = models.TextField(blank=True, null=True)
    lo_dist_co = models.CharField(max_length=2, blank=True, null=True)
    lo_useinre = models.NullBooleanField()
    lo_useinso = models.NullBooleanField()
    lo_exclpo = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'location'


class Lzcycle(models.Model):
    lc_quote_n = models.CharField(max_length=15, blank=True, null=True)
    lc_op_num = models.IntegerField(blank=True, null=True)
    lc_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    lc_desc = models.CharField(max_length=60, blank=True, null=True)
    lc_diam_th = models.FloatField(blank=True, null=True)
    lc_lgc_loc = models.FloatField(blank=True, null=True)
    lc_lgc_tra = models.FloatField(blank=True, null=True)
    lc_lgc_spp = models.FloatField(blank=True, null=True)
    lc_mdc_loc = models.FloatField(blank=True, null=True)
    lc_mdc_tra = models.FloatField(blank=True, null=True)
    lc_mdc_spp = models.FloatField(blank=True, null=True)
    lc_smc_loc = models.FloatField(blank=True, null=True)
    lc_smc_tra = models.FloatField(blank=True, null=True)
    lc_smc_spp = models.FloatField(blank=True, null=True)
    lc_pierces = models.IntegerField(blank=True, null=True)
    lc_pierce_field = models.FloatField(db_column='lc_pierce_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lc_pierce2 = models.FloatField(blank=True, null=True)
    lc_adj_spp = models.FloatField(blank=True, null=True)
    lc_total_s = models.FloatField(blank=True, null=True)
    lc_action = models.TextField(blank=True, null=True)
    lc_date = models.DateField(blank=True, null=True)
    lc_emp_id = models.CharField(max_length=5, blank=True, null=True)
    lc_order_n = models.CharField(max_length=12, blank=True, null=True)
    lc_assist_field = models.IntegerField(db_column='lc_assist_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lc_burden = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lzcycle'


class MachCal(models.Model):
    ml_mach_co = models.CharField(max_length=5, blank=True, null=True)
    ml_sch_dat = models.DateField(blank=True, null=True)
    ml_load_hr = models.CharField(max_length=124, blank=True, null=True)
    ml_ot_hrs = models.CharField(max_length=124, blank=True, null=True)
    ml_max_hrs = models.CharField(max_length=124, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mach_cal'


class MachCat(models.Model):
    mc_mach_ca = models.CharField(max_length=5, blank=True, null=True)
    mc_cat_des = models.CharField(max_length=20, blank=True, null=True)
    mc_udf_nde = models.CharField(max_length=20, blank=True, null=True)
    mc_udf_nd2 = models.CharField(max_length=20, blank=True, null=True)
    mc_udf_nd3 = models.CharField(max_length=20, blank=True, null=True)
    mc_udf_nd4 = models.CharField(max_length=20, blank=True, null=True)
    mc_udf_cde = models.CharField(max_length=20, blank=True, null=True)
    mc_udf_cd2 = models.CharField(max_length=20, blank=True, null=True)
    mc_udf_dde = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mach_cat'


class MachGrp(models.Model):
    mg_mach_co = models.CharField(max_length=5, blank=True, null=True)
    mg_g_code = models.CharField(max_length=10, blank=True, null=True)
    mg_default = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mach_grp'


class MachTyp(models.Model):
    mt_mach_co = models.CharField(max_length=5, blank=True, null=True)
    mt_mach_de = models.CharField(max_length=20, blank=True, null=True)
    mt_caltype = models.CharField(max_length=1, blank=True, null=True)
    mt_cut_off = models.FloatField(blank=True, null=True)
    mt_rate = models.FloatField(blank=True, null=True)
    mt_setup_r = models.FloatField(blank=True, null=True)
    mt_max_spe = models.FloatField(blank=True, null=True)
    mt_max_fee = models.FloatField(blank=True, null=True)
    mt_notes = models.TextField(blank=True, null=True)
    mt_cycle = models.CharField(max_length=1, blank=True, null=True)
    mt_def_hrs = models.FloatField(blank=True, null=True)
    mt_locatio = models.CharField(max_length=10, blank=True, null=True)
    mt_mach_gr = models.CharField(max_length=10, blank=True, null=True)
    mt_sched = models.NullBooleanField()
    mt_burd_ra = models.FloatField(blank=True, null=True)
    mt_pop = models.IntegerField(blank=True, null=True)
    mt_de_id = models.CharField(max_length=2, blank=True, null=True)
    mt_sell_ra = models.FloatField(blank=True, null=True)
    mt_cb_rate = models.FloatField(blank=True, null=True)
    mt_usenote = models.NullBooleanField()
    mt_infinit = models.NullBooleanField()
    mt_positio = models.IntegerField(blank=True, null=True)
    mt_nowork = models.NullBooleanField()
    mt_il_id = models.CharField(max_length=10, blank=True, null=True)
    mt_queue = models.FloatField(blank=True, null=True)
    mt_ib_id = models.CharField(max_length=10, blank=True, null=True)
    mt_is_sub = models.NullBooleanField()
    mt_supp_co = models.CharField(max_length=6, blank=True, null=True)
    mt_dist_co = models.CharField(max_length=2, blank=True, null=True)
    mt_workcel = models.NullBooleanField()
    mt_useburd = models.NullBooleanField()
    mt_il_id_w = models.CharField(max_length=10, blank=True, null=True)
    mt_seconda = models.NullBooleanField()
    mt_unatten = models.FloatField(blank=True, null=True)
    mt_line = models.IntegerField(blank=True, null=True)
    mt_spindle = models.IntegerField(blank=True, null=True)
    mt_fixed_a = models.CharField(max_length=40, blank=True, null=True)
    mt_minchar = models.FloatField(blank=True, null=True)
    mt_feature = models.CharField(max_length=20, blank=True, null=True)
    mt_inactiv = models.NullBooleanField()
    mt_id_code = models.CharField(max_length=10, blank=True, null=True)
    mt_packagi = models.NullBooleanField()
    mt_prod_co = models.CharField(max_length=2, blank=True, null=True)
    mt_sortby = models.IntegerField(blank=True, null=True)
    mt_barend_field = models.FloatField(db_column='mt_barend_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mt_bufferh = models.FloatField(blank=True, null=True)
    mt_partcou = models.IntegerField(blank=True, null=True)
    mt_hoursco = models.FloatField(blank=True, null=True)
    mt_virtual = models.IntegerField(blank=True, null=True)
    mt_emp_id = models.CharField(max_length=5, blank=True, null=True)
    mt_useinjc = models.NullBooleanField()
    mt_setup_q = models.IntegerField(blank=True, null=True)
    mt_maneng_field = models.CharField(db_column='mt_maneng_', max_length=5, blank=True, null=True)  # Field renamed because it ended with '_'.
    mt_assigne = models.CharField(max_length=5, blank=True, null=True)
    mt_type = models.IntegerField(blank=True, null=True)
    mt_assign2 = models.CharField(max_length=5, blank=True, null=True)
    mt_assign3 = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mach_typ'


class Manufact(models.Model):
    ma_id = models.CharField(max_length=10, blank=True, null=True)
    ma_manufac = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufact'


class MatType(models.Model):
    ma_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    ma_mat_nam = models.CharField(max_length=30, blank=True, null=True)
    ma_conv_fa = models.FloatField(blank=True, null=True)
    ma_sfm = models.FloatField(blank=True, null=True)
    ma_alloy_c = models.FloatField(blank=True, null=True)
    ma_resin = models.NullBooleanField()
    ma_cpg = models.FloatField(blank=True, null=True)
    ma_bo_time = models.FloatField(blank=True, null=True)
    ma_mix_tem = models.CharField(max_length=3, blank=True, null=True)
    ma_mix_tim = models.FloatField(blank=True, null=True)
    ma_resin_t = models.CharField(max_length=3, blank=True, null=True)
    ma_cat_tem = models.CharField(max_length=3, blank=True, null=True)
    ma_cure_ti = models.IntegerField(blank=True, null=True)
    ma_cure_te = models.CharField(max_length=3, blank=True, null=True)
    ma_pail_si = models.CharField(max_length=20, blank=True, null=True)
    ma_pails_p = models.IntegerField(blank=True, null=True)
    ma_duro = models.CharField(max_length=3, blank=True, null=True)
    ma_duro_lo = models.CharField(max_length=3, blank=True, null=True)
    ma_duro_hi = models.CharField(max_length=3, blank=True, null=True)
    ma_rgb = models.IntegerField(blank=True, null=True)
    mt_c_min = models.FloatField(blank=True, null=True)
    mt_c_max = models.FloatField(blank=True, null=True)
    mt_mn_min = models.FloatField(blank=True, null=True)
    mt_mn_max = models.FloatField(blank=True, null=True)
    mt_p_min = models.FloatField(blank=True, null=True)
    mt_p_max = models.FloatField(blank=True, null=True)
    mt_s_min = models.FloatField(blank=True, null=True)
    mt_s_max = models.FloatField(blank=True, null=True)
    mt_si_min = models.FloatField(blank=True, null=True)
    mt_si_max = models.FloatField(blank=True, null=True)
    mt_pb_min = models.FloatField(blank=True, null=True)
    mt_pb_max = models.FloatField(blank=True, null=True)
    mt_ni_min = models.FloatField(blank=True, null=True)
    mt_ni_max = models.FloatField(blank=True, null=True)
    mt_cr_min = models.FloatField(blank=True, null=True)
    mt_cr_max = models.FloatField(blank=True, null=True)
    mt_mo_min = models.FloatField(blank=True, null=True)
    mt_mo_max = models.FloatField(blank=True, null=True)
    mt_cu_min = models.FloatField(blank=True, null=True)
    mt_cu_max = models.FloatField(blank=True, null=True)
    mt_v_min = models.FloatField(blank=True, null=True)
    mt_v_max = models.FloatField(blank=True, null=True)
    mt_tensile = models.FloatField(blank=True, null=True)
    mt_tensil2 = models.FloatField(blank=True, null=True)
    mt_yield_m = models.FloatField(blank=True, null=True)
    mt_yield_2 = models.FloatField(blank=True, null=True)
    mt_enlong_field = models.FloatField(db_column='mt_enlong_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mt_enlong2 = models.FloatField(blank=True, null=True)
    mt_reducti = models.FloatField(blank=True, null=True)
    mt_reduct2 = models.FloatField(blank=True, null=True)
    mt_hardnes = models.FloatField(blank=True, null=True)
    mt_hardne2 = models.FloatField(blank=True, null=True)
    mt_temp_mi = models.FloatField(blank=True, null=True)
    mt_temp_ma = models.FloatField(blank=True, null=True)
    mt_al_min = models.FloatField(blank=True, null=True)
    mt_al_max = models.FloatField(blank=True, null=True)
    mt_fe_min = models.FloatField(blank=True, null=True)
    mt_fe_max = models.FloatField(blank=True, null=True)
    mt_sn_min = models.FloatField(blank=True, null=True)
    mt_sn_max = models.FloatField(blank=True, null=True)
    mt_zn_min = models.FloatField(blank=True, null=True)
    mt_zn_max = models.FloatField(blank=True, null=True)
    mt_hide = models.NullBooleanField()
    ma_specifi = models.CharField(max_length=30, blank=True, null=True)
    ma_grade = models.CharField(max_length=6, blank=True, null=True)
    ma_customr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mat_type'


class Material(models.Model):
    ma_id = models.CharField(max_length=6, blank=True, null=True)
    ma_code = models.CharField(max_length=30, blank=True, null=True)
    ma_compos = models.TextField(blank=True, null=True)
    ma_colors = models.TextField(blank=True, null=True)
    ma_arc_rat = models.TextField(blank=True, null=True)
    ma_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material'


class Mattime(models.Model):
    mt_quote_n = models.CharField(max_length=15, blank=True, null=True)
    mt_order_n = models.CharField(max_length=12, blank=True, null=True)
    mt_item = models.IntegerField(blank=True, null=True)
    mt_cut_qty = models.FloatField(blank=True, null=True)
    mt_fit_qty = models.FloatField(blank=True, null=True)
    mt_drill_q = models.FloatField(blank=True, null=True)
    mt_weld_qt = models.FloatField(blank=True, null=True)
    mt_other_q = models.FloatField(blank=True, null=True)
    mt_fit_min = models.FloatField(blank=True, null=True)
    mt_drill_m = models.FloatField(blank=True, null=True)
    mt_weld_mi = models.FloatField(blank=True, null=True)
    mt_cut_min = models.FloatField(blank=True, null=True)
    mt_other_m = models.FloatField(blank=True, null=True)
    mt_cut_tot = models.FloatField(blank=True, null=True)
    mt_fit_tot = models.FloatField(blank=True, null=True)
    mt_drill_t = models.FloatField(blank=True, null=True)
    mt_weld_to = models.FloatField(blank=True, null=True)
    mt_other_t = models.FloatField(blank=True, null=True)
    mt_time = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mattime'


class MemPart(models.Model):
    mp_id = models.CharField(max_length=10, blank=True, null=True)
    mp_vm_id = models.CharField(max_length=10, blank=True, null=True)
    mp_inv_num = models.CharField(max_length=30, blank=True, null=True)
    mp_supp_co = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mem_part'


class Message(models.Model):
    mg_id = models.IntegerField(blank=True, null=True)
    mg_from = models.CharField(max_length=60, blank=True, null=True)
    mg_subject = models.CharField(max_length=80, blank=True, null=True)
    mg_datetim = models.DateTimeField(blank=True, null=True)
    mg_message = models.TextField(blank=True, null=True)
    mg_pdffile = models.TextField(blank=True, null=True)
    mg_task = models.NullBooleanField()
    mg_informe = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'message'


class Mixer(models.Model):
    mi_id = models.CharField(max_length=10, blank=True, null=True)
    mi_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mixer'


class MsgEvnt(models.Model):
    me_id = models.IntegerField(blank=True, null=True)
    me_action = models.IntegerField(blank=True, null=True)
    me_referen = models.CharField(max_length=40, blank=True, null=True)
    me_done = models.NullBooleanField()
    me_refere2 = models.CharField(max_length=40, blank=True, null=True)
    me_refere3 = models.CharField(max_length=40, blank=True, null=True)
    me_refere4 = models.CharField(max_length=40, blank=True, null=True)
    me_refere5 = models.CharField(max_length=40, blank=True, null=True)
    me_owner = models.CharField(max_length=5, blank=True, null=True)
    me_reportc = models.TextField(blank=True, null=True)
    me_timetor = models.DateTimeField(blank=True, null=True)
    me_frequen = models.CharField(max_length=1, blank=True, null=True)
    me_kiosk = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'msg_evnt'


class MsgRcpt(models.Model):
    mr_id = models.IntegerField(blank=True, null=True)
    mr_mg_id = models.IntegerField(blank=True, null=True)
    mr_read = models.NullBooleanField()
    mr_me_id = models.IntegerField(blank=True, null=True)
    mr_sendto = models.CharField(max_length=240, blank=True, null=True)
    mr_output = models.CharField(max_length=15, blank=True, null=True)
    mr_notes = models.TextField(blank=True, null=True)
    mr_when_re = models.DateTimeField(blank=True, null=True)
    mr_deadlin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msg_rcpt'


class Mymenu(models.Model):
    mm_id = models.CharField(max_length=10, blank=True, null=True)
    mm_user_id = models.CharField(max_length=5, blank=True, null=True)
    mm_sequenc = models.IntegerField(blank=True, null=True)
    mm_form_na = models.CharField(max_length=10, blank=True, null=True)
    mm_form_ti = models.CharField(max_length=40, blank=True, null=True)
    mm_app = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mymenu'


class Naics(models.Model):
    na_ncode = models.CharField(max_length=6, blank=True, null=True)
    na_ndesc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'naics'


class Nestdet(models.Model):
    nd_id = models.CharField(max_length=10, blank=True, null=True)
    nd_nh_id = models.CharField(max_length=10, blank=True, null=True)
    nd_qty_per = models.IntegerField(blank=True, null=True)
    nd_percent = models.IntegerField(blank=True, null=True)
    nd_invent_field = models.CharField(db_column='nd_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    nd_mat_per = models.IntegerField(blank=True, null=True)
    nd_wgtperp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nestdet'


class Nesthead(models.Model):
    nh_id = models.CharField(max_length=10, blank=True, null=True)
    nh_desc = models.CharField(max_length=30, blank=True, null=True)
    nh_invent_field = models.CharField(db_column='nh_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    nh_mach_co = models.CharField(max_length=5, blank=True, null=True)
    nh_percent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nesthead'


class Nmfc(models.Model):
    nm_code = models.CharField(max_length=10, blank=True, null=True)
    nm_desc = models.CharField(max_length=40, blank=True, null=True)
    nm_class = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nmfc'


class Notecats(models.Model):
    nc_id = models.CharField(max_length=10, blank=True, null=True)
    nc_desc = models.CharField(max_length=30, blank=True, null=True)
    nc_inactiv = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'notecats'


class NsExmps(models.Model):
    ne_example = models.CharField(max_length=30, blank=True, null=True)
    ne_noun = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ns_exmps'


class NsNouns(models.Model):
    nn_noun = models.CharField(max_length=15, blank=True, null=True)
    nn_ns_code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ns_nouns'


class NsNshts(models.Model):
    ns_code = models.CharField(max_length=5, blank=True, null=True)
    ns_desc = models.CharField(max_length=30, blank=True, null=True)
    ns_hyperli = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ns_nshts'


class NsPrfxs(models.Model):
    np_prefix = models.CharField(max_length=3, blank=True, null=True)
    np_noun = models.CharField(max_length=15, blank=True, null=True)
    np_counter = models.IntegerField(blank=True, null=True)
    np_digits = models.IntegerField(blank=True, null=True)
    np_inactiv = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ns_prfxs'


class Numlog(models.Model):
    nl_datetim = models.DateTimeField(blank=True, null=True)
    nl_source = models.CharField(max_length=10, blank=True, null=True)
    nl_key = models.CharField(max_length=30, blank=True, null=True)
    nl_user = models.CharField(max_length=5, blank=True, null=True)
    nl_note = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numlog'


class Ontime(models.Model):
    ot_date = models.DateField(blank=True, null=True)
    ot_mach_co = models.CharField(max_length=5, blank=True, null=True)
    ot_de_id = models.CharField(max_length=10, blank=True, null=True)
    ot_total_o = models.IntegerField(blank=True, null=True)
    ot_total_2 = models.IntegerField(blank=True, null=True)
    ot_percent = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ontime'


class OpLots(models.Model):
    ol_id = models.CharField(max_length=10, blank=True, null=True)
    ol_quote_n = models.CharField(max_length=15, blank=True, null=True)
    ol_order_n = models.CharField(max_length=12, blank=True, null=True)
    ol_op_num = models.IntegerField(blank=True, null=True)
    ol_vend_in = models.IntegerField(blank=True, null=True)
    ol_exclude = models.NullBooleanField()
    ol_desc = models.CharField(max_length=40, blank=True, null=True)
    ol_amt = models.FloatField(blank=True, null=True)
    ol_note = models.TextField(blank=True, null=True)
    ol_invent_field = models.CharField(db_column='ol_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'op_lots'


class OpTools(models.Model):
    ot_quote_n = models.CharField(max_length=15, blank=True, null=True)
    ot_op_num = models.IntegerField(blank=True, null=True)
    ot_tool_nu = models.IntegerField(blank=True, null=True)
    ot_mach_ca = models.CharField(max_length=5, blank=True, null=True)
    ot_tool_ty = models.CharField(max_length=20, blank=True, null=True)
    ot_speed = models.FloatField(blank=True, null=True)
    ot_sp_adj = models.IntegerField(blank=True, null=True)
    ot_adj_spe = models.FloatField(blank=True, null=True)
    ot_feed = models.FloatField(blank=True, null=True)
    ot_fe_adj = models.IntegerField(blank=True, null=True)
    ot_adj_fee = models.FloatField(blank=True, null=True)
    ot_sfm = models.FloatField(blank=True, null=True)
    ot_ipr = models.FloatField(blank=True, null=True)
    ot_gp = models.FloatField(blank=True, null=True)
    ot_note = models.TextField(blank=True, null=True)
    ot_loc = models.FloatField(blank=True, null=True)
    ot_passes = models.IntegerField(blank=True, null=True)
    ot_work_di = models.FloatField(blank=True, null=True)
    ot_current = models.IntegerField(blank=True, null=True)
    ot_tool_di = models.FloatField(blank=True, null=True)
    ot_num_flu = models.IntegerField(blank=True, null=True)
    ot_const_v = models.FloatField(blank=True, null=True)
    ot_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    ot_quantit = models.IntegerField(blank=True, null=True)
    ot_desc = models.CharField(max_length=50, blank=True, null=True)
    ot_positio = models.IntegerField(blank=True, null=True)
    ot_endside = models.IntegerField(blank=True, null=True)
    ot_unit_co = models.FloatField(blank=True, null=True)
    ot_ext_cos = models.FloatField(blank=True, null=True)
    ot_gp_sec = models.FloatField(blank=True, null=True)
    ot_index_m = models.FloatField(blank=True, null=True)
    ot_index_s = models.FloatField(blank=True, null=True)
    ot_total_c = models.FloatField(blank=True, null=True)
    ot_total_2 = models.FloatField(blank=True, null=True)
    ot_cycle = models.FloatField(blank=True, null=True)
    ot_cam = models.FloatField(blank=True, null=True)
    ot_cycle_s = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'op_tools'


class Operate(models.Model):
    op_quote_n = models.CharField(max_length=15, blank=True, null=True)
    op_op_num = models.IntegerField(blank=True, null=True)
    op_type = models.CharField(max_length=1, blank=True, null=True)
    op_mach_co = models.CharField(max_length=5, blank=True, null=True)
    op_suhr = models.FloatField(blank=True, null=True)
    op_sur = models.FloatField(blank=True, null=True)
    op_su = models.FloatField(blank=True, null=True)
    op_gp = models.FloatField(blank=True, null=True)
    op_pop = models.FloatField(blank=True, null=True)
    op_np = models.FloatField(blank=True, null=True)
    op_hpu = models.FloatField(blank=True, null=True)
    op_hr = models.FloatField(blank=True, null=True)
    op_cpu = models.FloatField(blank=True, null=True)
    op_note = models.TextField(blank=True, null=True)
    op_current = models.IntegerField(blank=True, null=True)
    op_attend = models.IntegerField(blank=True, null=True)
    op_queue = models.FloatField(blank=True, null=True)
    op_dist_co = models.CharField(max_length=2, blank=True, null=True)
    op_supp_co = models.CharField(max_length=6, blank=True, null=True)
    op_unit_co = models.FloatField(blank=True, null=True)
    op_quantit = models.IntegerField(blank=True, null=True)
    op_ext_cos = models.FloatField(blank=True, null=True)
    op_mark_up = models.IntegerField(blank=True, null=True)
    op_tot_cos = models.FloatField(blank=True, null=True)
    op_distrib = models.NullBooleanField()
    op_cost1 = models.FloatField(blank=True, null=True)
    op_cost2 = models.FloatField(blank=True, null=True)
    op_cost3 = models.FloatField(blank=True, null=True)
    op_cost4 = models.FloatField(blank=True, null=True)
    op_cost5 = models.FloatField(blank=True, null=True)
    op_cost6 = models.FloatField(blank=True, null=True)
    op_cost7 = models.FloatField(blank=True, null=True)
    op_cost8 = models.FloatField(blank=True, null=True)
    op_cost9 = models.FloatField(blank=True, null=True)
    op_cost10 = models.FloatField(blank=True, null=True)
    op_recalc = models.NullBooleanField()
    op_in_inve = models.CharField(max_length=30, blank=True, null=True)
    op_out_inv = models.CharField(max_length=30, blank=True, null=True)
    op_sched = models.NullBooleanField()
    op_force = models.NullBooleanField()
    op_rewflag = models.NullBooleanField()
    op_perc_co = models.IntegerField(blank=True, null=True)
    op_g_code = models.CharField(max_length=10, blank=True, null=True)
    op_move_st = models.NullBooleanField()
    op_master_field = models.IntegerField(db_column='op_master_', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_parent_field = models.IntegerField(db_column='op_parent_', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_oplib_n = models.TextField(blank=True, null=True)
    op_il_id = models.CharField(max_length=10, blank=True, null=True)
    op_ib_id = models.CharField(max_length=10, blank=True, null=True)
    op_pagebre = models.NullBooleanField()
    op_min_cha = models.FloatField(blank=True, null=True)
    op_min_ch2 = models.FloatField(blank=True, null=True)
    op_min_ch3 = models.FloatField(blank=True, null=True)
    op_min_ch4 = models.FloatField(blank=True, null=True)
    op_min_ch5 = models.FloatField(blank=True, null=True)
    op_min_ch6 = models.FloatField(blank=True, null=True)
    op_min_ch7 = models.FloatField(blank=True, null=True)
    op_min_ch8 = models.FloatField(blank=True, null=True)
    op_min_ch9 = models.FloatField(blank=True, null=True)
    op_min_c10 = models.FloatField(blank=True, null=True)
    op_unit_c2 = models.FloatField(blank=True, null=True)
    op_unit_c3 = models.FloatField(blank=True, null=True)
    op_unit_c4 = models.FloatField(blank=True, null=True)
    op_unit_c5 = models.FloatField(blank=True, null=True)
    op_unit_c6 = models.FloatField(blank=True, null=True)
    op_unit_c7 = models.FloatField(blank=True, null=True)
    op_unit_c8 = models.FloatField(blank=True, null=True)
    op_unit_c9 = models.FloatField(blank=True, null=True)
    op_unit_10 = models.FloatField(blank=True, null=True)
    op_unit_11 = models.FloatField(blank=True, null=True)
    op_quanti2 = models.IntegerField(blank=True, null=True)
    op_quanti3 = models.IntegerField(blank=True, null=True)
    op_quanti4 = models.IntegerField(blank=True, null=True)
    op_quanti5 = models.IntegerField(blank=True, null=True)
    op_quanti6 = models.IntegerField(blank=True, null=True)
    op_quanti7 = models.IntegerField(blank=True, null=True)
    op_quanti8 = models.IntegerField(blank=True, null=True)
    op_quanti9 = models.IntegerField(blank=True, null=True)
    op_quant10 = models.IntegerField(blank=True, null=True)
    op_quant11 = models.IntegerField(blank=True, null=True)
    op_ext_co2 = models.FloatField(blank=True, null=True)
    op_ext_co3 = models.FloatField(blank=True, null=True)
    op_ext_co4 = models.FloatField(blank=True, null=True)
    op_ext_co5 = models.FloatField(blank=True, null=True)
    op_ext_co6 = models.FloatField(blank=True, null=True)
    op_ext_co7 = models.FloatField(blank=True, null=True)
    op_ext_co8 = models.FloatField(blank=True, null=True)
    op_ext_co9 = models.FloatField(blank=True, null=True)
    op_ext_c10 = models.FloatField(blank=True, null=True)
    op_ext_c11 = models.FloatField(blank=True, null=True)
    op_mark_u2 = models.IntegerField(blank=True, null=True)
    op_mark_u3 = models.IntegerField(blank=True, null=True)
    op_mark_u4 = models.IntegerField(blank=True, null=True)
    op_mark_u5 = models.IntegerField(blank=True, null=True)
    op_mark_u6 = models.IntegerField(blank=True, null=True)
    op_mark_u7 = models.IntegerField(blank=True, null=True)
    op_mark_u8 = models.IntegerField(blank=True, null=True)
    op_mark_u9 = models.IntegerField(blank=True, null=True)
    op_mark_10 = models.IntegerField(blank=True, null=True)
    op_mark_11 = models.IntegerField(blank=True, null=True)
    op_tot_co2 = models.FloatField(blank=True, null=True)
    op_tot_co3 = models.FloatField(blank=True, null=True)
    op_tot_co4 = models.FloatField(blank=True, null=True)
    op_tot_co5 = models.FloatField(blank=True, null=True)
    op_tot_co6 = models.FloatField(blank=True, null=True)
    op_tot_co7 = models.FloatField(blank=True, null=True)
    op_tot_co8 = models.FloatField(blank=True, null=True)
    op_tot_co9 = models.FloatField(blank=True, null=True)
    op_tot_c10 = models.FloatField(blank=True, null=True)
    op_tot_c11 = models.FloatField(blank=True, null=True)
    op_suhr1 = models.FloatField(blank=True, null=True)
    op_suhr2 = models.FloatField(blank=True, null=True)
    op_suhr3 = models.FloatField(blank=True, null=True)
    op_suhr4 = models.FloatField(blank=True, null=True)
    op_suhr5 = models.FloatField(blank=True, null=True)
    op_suhr6 = models.FloatField(blank=True, null=True)
    op_suhr7 = models.FloatField(blank=True, null=True)
    op_suhr8 = models.FloatField(blank=True, null=True)
    op_suhr9 = models.FloatField(blank=True, null=True)
    op_suhr10 = models.FloatField(blank=True, null=True)
    op_sur1 = models.FloatField(blank=True, null=True)
    op_sur2 = models.FloatField(blank=True, null=True)
    op_sur3 = models.FloatField(blank=True, null=True)
    op_sur4 = models.FloatField(blank=True, null=True)
    op_sur5 = models.FloatField(blank=True, null=True)
    op_sur6 = models.FloatField(blank=True, null=True)
    op_sur7 = models.FloatField(blank=True, null=True)
    op_sur8 = models.FloatField(blank=True, null=True)
    op_sur9 = models.FloatField(blank=True, null=True)
    op_sur10 = models.FloatField(blank=True, null=True)
    op_gp1 = models.FloatField(blank=True, null=True)
    op_gp2 = models.FloatField(blank=True, null=True)
    op_gp3 = models.FloatField(blank=True, null=True)
    op_gp4 = models.FloatField(blank=True, null=True)
    op_gp5 = models.FloatField(blank=True, null=True)
    op_gp6 = models.FloatField(blank=True, null=True)
    op_gp7 = models.FloatField(blank=True, null=True)
    op_gp8 = models.FloatField(blank=True, null=True)
    op_gp9 = models.FloatField(blank=True, null=True)
    op_gp10 = models.FloatField(blank=True, null=True)
    op_pop1 = models.IntegerField(blank=True, null=True)
    op_pop2 = models.IntegerField(blank=True, null=True)
    op_pop3 = models.IntegerField(blank=True, null=True)
    op_pop4 = models.IntegerField(blank=True, null=True)
    op_pop5 = models.IntegerField(blank=True, null=True)
    op_pop6 = models.IntegerField(blank=True, null=True)
    op_pop7 = models.IntegerField(blank=True, null=True)
    op_pop8 = models.IntegerField(blank=True, null=True)
    op_pop9 = models.IntegerField(blank=True, null=True)
    op_pop10 = models.IntegerField(blank=True, null=True)
    op_np1 = models.FloatField(blank=True, null=True)
    op_np2 = models.FloatField(blank=True, null=True)
    op_np3 = models.FloatField(blank=True, null=True)
    op_np4 = models.FloatField(blank=True, null=True)
    op_np5 = models.FloatField(blank=True, null=True)
    op_np6 = models.FloatField(blank=True, null=True)
    op_np7 = models.FloatField(blank=True, null=True)
    op_np8 = models.FloatField(blank=True, null=True)
    op_np9 = models.FloatField(blank=True, null=True)
    op_np10 = models.FloatField(blank=True, null=True)
    op_hpu1 = models.FloatField(blank=True, null=True)
    op_hpu2 = models.FloatField(blank=True, null=True)
    op_hpu3 = models.FloatField(blank=True, null=True)
    op_hpu4 = models.FloatField(blank=True, null=True)
    op_hpu5 = models.FloatField(blank=True, null=True)
    op_hpu6 = models.FloatField(blank=True, null=True)
    op_hpu7 = models.FloatField(blank=True, null=True)
    op_hpu8 = models.FloatField(blank=True, null=True)
    op_hpu9 = models.FloatField(blank=True, null=True)
    op_hpu10 = models.FloatField(blank=True, null=True)
    op_hr1 = models.FloatField(blank=True, null=True)
    op_hr2 = models.FloatField(blank=True, null=True)
    op_hr3 = models.FloatField(blank=True, null=True)
    op_hr4 = models.FloatField(blank=True, null=True)
    op_hr5 = models.FloatField(blank=True, null=True)
    op_hr6 = models.FloatField(blank=True, null=True)
    op_hr7 = models.FloatField(blank=True, null=True)
    op_hr8 = models.FloatField(blank=True, null=True)
    op_hr9 = models.FloatField(blank=True, null=True)
    op_hr10 = models.FloatField(blank=True, null=True)
    op_attend1 = models.IntegerField(blank=True, null=True)
    op_attend2 = models.IntegerField(blank=True, null=True)
    op_attend3 = models.IntegerField(blank=True, null=True)
    op_attend4 = models.IntegerField(blank=True, null=True)
    op_attend5 = models.IntegerField(blank=True, null=True)
    op_attend6 = models.IntegerField(blank=True, null=True)
    op_attend7 = models.IntegerField(blank=True, null=True)
    op_attend8 = models.IntegerField(blank=True, null=True)
    op_attend9 = models.IntegerField(blank=True, null=True)
    op_atten10 = models.IntegerField(blank=True, null=True)
    op_cpu1 = models.FloatField(blank=True, null=True)
    op_cpu2 = models.FloatField(blank=True, null=True)
    op_cpu3 = models.FloatField(blank=True, null=True)
    op_cpu4 = models.FloatField(blank=True, null=True)
    op_cpu5 = models.FloatField(blank=True, null=True)
    op_cpu6 = models.FloatField(blank=True, null=True)
    op_cpu7 = models.FloatField(blank=True, null=True)
    op_cpu8 = models.FloatField(blank=True, null=True)
    op_cpu9 = models.FloatField(blank=True, null=True)
    op_cpu10 = models.FloatField(blank=True, null=True)
    op_su1 = models.FloatField(blank=True, null=True)
    op_su2 = models.FloatField(blank=True, null=True)
    op_su3 = models.FloatField(blank=True, null=True)
    op_su4 = models.FloatField(blank=True, null=True)
    op_su5 = models.FloatField(blank=True, null=True)
    op_su6 = models.FloatField(blank=True, null=True)
    op_su7 = models.FloatField(blank=True, null=True)
    op_su8 = models.FloatField(blank=True, null=True)
    op_su9 = models.FloatField(blank=True, null=True)
    op_su10 = models.FloatField(blank=True, null=True)
    op_infin_m = models.FloatField(blank=True, null=True)
    op_enforce = models.NullBooleanField()
    op_setup_m = models.NullBooleanField()
    op_setup_c = models.IntegerField(blank=True, null=True)
    op_aggrega = models.IntegerField(blank=True, null=True)
    op_invent_field = models.CharField(db_column='op_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    op_last_pr = models.NullBooleanField()
    op_split = models.NullBooleanField()
    op_il_id_i = models.CharField(max_length=10, blank=True, null=True)
    op_ib_id_i = models.CharField(max_length=10, blank=True, null=True)
    op_optype = models.IntegerField(blank=True, null=True)
    op_down = models.IntegerField(blank=True, null=True)
    op_pc_lbs = models.NullBooleanField()
    op_pc_cost = models.FloatField(blank=True, null=True)
    op_aw_quot = models.CharField(max_length=15, blank=True, null=True)
    op_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    op_minqty = models.IntegerField(blank=True, null=True)
    op_hpp = models.FloatField(blank=True, null=True)
    op_mpp = models.FloatField(blank=True, null=True)
    op_spp = models.FloatField(blank=True, null=True)
    op_burden = models.FloatField(blank=True, null=True)
    op_exclude = models.NullBooleanField()
    op_pc_per_field = models.FloatField(db_column='op_pc_per_', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_unit_ra = models.FloatField(blank=True, null=True)
    op_need_qt = models.FloatField(blank=True, null=True)
    op_surchar = models.FloatField(blank=True, null=True)
    op_simple_field = models.NullBooleanField(db_column='op_simple_')  # Field renamed because it ended with '_'.
    op_lossper = models.FloatField(blank=True, null=True)
    op_load_ti = models.FloatField(blank=True, null=True)
    op_rpm = models.IntegerField(blank=True, null=True)
    op_obsolet = models.NullBooleanField()
    op_spindge = models.CharField(max_length=15, blank=True, null=True)
    op_changeg = models.CharField(max_length=15, blank=True, null=True)
    op_threadg = models.CharField(max_length=15, blank=True, null=True)
    op_st_id = models.CharField(max_length=10, blank=True, null=True)
    op_signifi = models.NullBooleanField()
    op_post_pc = models.NullBooleanField()
    op_apw = models.FloatField(blank=True, null=True)
    op_sa_id = models.CharField(max_length=10, blank=True, null=True)
    op_emp_id = models.CharField(max_length=5, blank=True, null=True)
    op_spindle = models.IntegerField(blank=True, null=True)
    op_feed_rp = models.IntegerField(blank=True, null=True)
    op_eff_thr = models.IntegerField(blank=True, null=True)
    op_casting = models.NullBooleanField()
    op_mtsc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operate'


class Operate2(models.Model):
    o2_quote_n = models.CharField(max_length=15, blank=True, null=True)
    o2_op_num = models.IntegerField(blank=True, null=True)
    o2_onetime = models.FloatField(blank=True, null=True)
    o2_amort_t = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operate2'


class OplibMd(models.Model):
    ol_id = models.IntegerField(blank=True, null=True)
    ol_code = models.CharField(max_length=15, blank=True, null=True)
    ol_descrip = models.CharField(max_length=140, blank=True, null=True)
    ol_ea1 = models.CharField(max_length=30, blank=True, null=True)
    ol_ea2 = models.CharField(max_length=30, blank=True, null=True)
    ol_ea3 = models.CharField(max_length=30, blank=True, null=True)
    ol_ea4 = models.CharField(max_length=30, blank=True, null=True)
    ol_ea5 = models.CharField(max_length=30, blank=True, null=True)
    ol_ea6 = models.CharField(max_length=30, blank=True, null=True)
    ol_ea7 = models.CharField(max_length=30, blank=True, null=True)
    ol_ea8 = models.CharField(max_length=30, blank=True, null=True)
    ol_ea9 = models.CharField(max_length=30, blank=True, null=True)
    ol_ea10 = models.CharField(max_length=30, blank=True, null=True)
    ol_notes = models.TextField(blank=True, null=True)
    ol_unit_ty = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oplib_md'


class OplibOp(models.Model):
    oo_id = models.IntegerField(blank=True, null=True)
    oo_op_num = models.IntegerField(blank=True, null=True)
    oo_type = models.CharField(max_length=1, blank=True, null=True)
    oo_mach_co = models.CharField(max_length=5, blank=True, null=True)
    oo_suhr = models.FloatField(blank=True, null=True)
    oo_sur = models.FloatField(blank=True, null=True)
    oo_su = models.FloatField(blank=True, null=True)
    oo_gp = models.FloatField(blank=True, null=True)
    oo_pop = models.IntegerField(blank=True, null=True)
    oo_np = models.FloatField(blank=True, null=True)
    oo_hpu = models.FloatField(blank=True, null=True)
    oo_hr = models.FloatField(blank=True, null=True)
    oo_cpu = models.FloatField(blank=True, null=True)
    oo_note = models.TextField(blank=True, null=True)
    oo_current = models.IntegerField(blank=True, null=True)
    oo_attend = models.IntegerField(blank=True, null=True)
    oo_queue = models.FloatField(blank=True, null=True)
    oo_dist_co = models.CharField(max_length=2, blank=True, null=True)
    oo_supp_co = models.CharField(max_length=6, blank=True, null=True)
    oo_unit_co = models.FloatField(blank=True, null=True)
    oo_quantit = models.IntegerField(blank=True, null=True)
    oo_ext_cos = models.FloatField(blank=True, null=True)
    oo_mark_up = models.IntegerField(blank=True, null=True)
    oo_tot_cos = models.FloatField(blank=True, null=True)
    oo_distrib = models.NullBooleanField()
    oo_cost1 = models.FloatField(blank=True, null=True)
    oo_cost2 = models.FloatField(blank=True, null=True)
    oo_cost3 = models.FloatField(blank=True, null=True)
    oo_cost4 = models.FloatField(blank=True, null=True)
    oo_cost5 = models.FloatField(blank=True, null=True)
    oo_cost6 = models.FloatField(blank=True, null=True)
    oo_cost7 = models.FloatField(blank=True, null=True)
    oo_cost8 = models.FloatField(blank=True, null=True)
    oo_cost9 = models.FloatField(blank=True, null=True)
    oo_cost10 = models.FloatField(blank=True, null=True)
    oo_recalc = models.NullBooleanField()
    oo_in_inve = models.CharField(max_length=30, blank=True, null=True)
    oo_out_inv = models.CharField(max_length=30, blank=True, null=True)
    oo_sched = models.NullBooleanField()
    oo_force = models.NullBooleanField()
    oo_rewflag = models.NullBooleanField()
    oo_perc_co = models.IntegerField(blank=True, null=True)
    oo_g_code = models.CharField(max_length=10, blank=True, null=True)
    oo_move_st = models.NullBooleanField()
    oo_ol_id = models.IntegerField(blank=True, null=True)
    oo_oplib_n = models.TextField(blank=True, null=True)
    oo_hpp = models.FloatField(blank=True, null=True)
    oo_mpp = models.FloatField(blank=True, null=True)
    oo_spp = models.FloatField(blank=True, null=True)
    oo_burden = models.FloatField(blank=True, null=True)
    oo_pc_cost = models.FloatField(blank=True, null=True)
    oo_st_id = models.CharField(max_length=10, blank=True, null=True)
    oo_specnot = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'oplib_op'


class OrdWip(models.Model):
    ow_id = models.CharField(max_length=10, blank=True, null=True)
    ow_order_n = models.CharField(max_length=12, blank=True, null=True)
    ow_endrec_field = models.DateField(db_column='ow_endrec_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ow_labor = models.FloatField(blank=True, null=True)
    ow_burden = models.FloatField(blank=True, null=True)
    ow_mat = models.FloatField(blank=True, null=True)
    ow_other = models.FloatField(blank=True, null=True)
    ow_prod = models.IntegerField(blank=True, null=True)
    ow_shipped = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ord_wip'


class Ordcosts(models.Model):
    order_num = models.CharField(max_length=12, blank=True, null=True)
    part_num = models.CharField(max_length=30, blank=True, null=True)
    invent_num = models.CharField(max_length=30, blank=True, null=True)
    qty_prod = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    labor = models.FloatField(blank=True, null=True)
    burden = models.FloatField(blank=True, null=True)
    material = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    perpiece = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordcosts'


class Order(models.Model):
    or_order_n = models.CharField(max_length=12, blank=True, null=True)
    or_ord_dat = models.DateField(blank=True, null=True)
    or_quote_n = models.CharField(max_length=15, blank=True, null=True)
    or_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    or_po_num = models.CharField(max_length=25, blank=True, null=True)
    or_ord_sta = models.CharField(max_length=1, blank=True, null=True)
    or_part_nu = models.CharField(max_length=30, blank=True, null=True)
    or_rev_num = models.CharField(max_length=6, blank=True, null=True)
    or_part_de = models.CharField(max_length=50, blank=True, null=True)
    or_pmemo = models.TextField(blank=True, null=True)
    or_cust_co = models.CharField(max_length=6, blank=True, null=True)
    or_emp_id = models.CharField(max_length=5, blank=True, null=True)
    or_scomm = models.FloatField(blank=True, null=True)
    or_runs = models.IntegerField(blank=True, null=True)
    or_lastop = models.IntegerField(blank=True, null=True)
    or_ord_not = models.TextField(blank=True, null=True)
    or_up_date = models.DateField(blank=True, null=True)
    or_qty_ord = models.FloatField(blank=True, null=True)
    or_qty_car = models.IntegerField(blank=True, null=True)
    or_qty_ret = models.IntegerField(blank=True, null=True)
    or_qty_shi = models.IntegerField(blank=True, null=True)
    or_qty_pro = models.FloatField(blank=True, null=True)
    or_qty_bal = models.FloatField(blank=True, null=True)
    or_qty_inv = models.FloatField(blank=True, null=True)
    or_ht = models.FloatField(blank=True, null=True)
    or_pl = models.FloatField(blank=True, null=True)
    or_tool = models.FloatField(blank=True, null=True)
    or_misc = models.FloatField(blank=True, null=True)
    or_ov = models.FloatField(blank=True, null=True)
    or_ottool = models.FloatField(blank=True, null=True)
    or_otgage = models.FloatField(blank=True, null=True)
    or_otcolle = models.FloatField(blank=True, null=True)
    or_otmisc = models.FloatField(blank=True, null=True)
    or_ht_note = models.TextField(blank=True, null=True)
    or_pl_note = models.TextField(blank=True, null=True)
    or_ppbar1 = models.FloatField(blank=True, null=True)
    or_act_ppb = models.IntegerField(blank=True, null=True)
    or_tsu1 = models.IntegerField(blank=True, null=True)
    or_tsu2 = models.IntegerField(blank=True, null=True)
    or_tsu3 = models.IntegerField(blank=True, null=True)
    or_tsu4 = models.IntegerField(blank=True, null=True)
    or_tsu5 = models.IntegerField(blank=True, null=True)
    or_tsu6 = models.IntegerField(blank=True, null=True)
    or_tsu7 = models.IntegerField(blank=True, null=True)
    or_tsu8 = models.IntegerField(blank=True, null=True)
    or_tsu9 = models.IntegerField(blank=True, null=True)
    or_tsu10 = models.IntegerField(blank=True, null=True)
    or_cpu = models.FloatField(blank=True, null=True)
    or_weight = models.FloatField(blank=True, null=True)
    or_change_field = models.CharField(db_column='or_change_', max_length=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    or_qtq = models.IntegerField(blank=True, null=True)
    or_require = models.IntegerField(blank=True, null=True)
    or_buyer = models.CharField(max_length=20, blank=True, null=True)
    or_spec_po = models.TextField(blank=True, null=True)
    or_cust_s_field = models.NullBooleanField(db_column='or_cust_s_')  # Field renamed because it ended with '_'.
    or_n_des_t = models.NullBooleanField()
    or_n_des_n = models.TextField(blank=True, null=True)
    or_os_proc = models.TextField(blank=True, null=True)
    or_spec_pk = models.TextField(blank=True, null=True)
    or_cert_re = models.TextField(blank=True, null=True)
    or_mat_spe = models.TextField(blank=True, null=True)
    or_os_pr_s = models.TextField(blank=True, null=True)
    or_spec_ma = models.TextField(blank=True, null=True)
    or_dt_r_po = models.DateField(blank=True, null=True)
    or_po_type = models.IntegerField(blank=True, null=True)
    or_cor_bp_field = models.NullBooleanField(db_column='or_cor_bp_')  # Field renamed because it ended with '_'.
    or_dt_pb_r = models.DateField(blank=True, null=True)
    or_mat_on_field = models.NullBooleanField(db_column='or_mat_on_')  # Field renamed because it ended with '_'.
    or_dt_moh_field = models.DateField(db_column='or_dt_moh_', blank=True, null=True)  # Field renamed because it ended with '_'.
    or_dt_moh2 = models.DateField(blank=True, null=True)
    or_sketch_field = models.NullBooleanField(db_column='or_sketch_')  # Field renamed because it ended with '_'.
    or_rout_bo = models.NullBooleanField()
    or_dt_prg_field = models.DateField(db_column='or_dt_prg_', blank=True, null=True)  # Field renamed because it ended with '_'.
    or_dt_tol_field = models.DateField(db_column='or_dt_tol_', blank=True, null=True)  # Field renamed because it ended with '_'.
    or_dt_tol2 = models.DateField(blank=True, null=True)
    or_dt_gag_field = models.DateField(db_column='or_dt_gag_', blank=True, null=True)  # Field renamed because it ended with '_'.
    or_dt_gag2 = models.DateField(blank=True, null=True)
    or_dt_rel_field = models.DateField(db_column='or_dt_rel_', blank=True, null=True)  # Field renamed because it ended with '_'.
    or_reviewe = models.CharField(max_length=30, blank=True, null=True)
    or_dt_rev = models.DateField(blank=True, null=True)
    or_mat = models.FloatField(blank=True, null=True)
    or_lot = models.CharField(max_length=20, blank=True, null=True)
    or_induct_field = models.IntegerField(db_column='or_induct_', blank=True, null=True)  # Field renamed because it ended with '_'.
    or_induct2 = models.IntegerField(blank=True, null=True)
    or_shard_s = models.CharField(max_length=25, blank=True, null=True)
    or_shard_i = models.CharField(max_length=25, blank=True, null=True)
    or_toteff_field = models.IntegerField(db_column='or_toteff_', blank=True, null=True)  # Field renamed because it ended with '_'.
    or_toteff2 = models.IntegerField(blank=True, null=True)
    or_case_s = models.CharField(max_length=10, blank=True, null=True)
    or_case_i = models.CharField(max_length=10, blank=True, null=True)
    or_core_s = models.CharField(max_length=10, blank=True, null=True)
    or_core_i = models.CharField(max_length=10, blank=True, null=True)
    or_plen_s = models.CharField(max_length=10, blank=True, null=True)
    or_plen_i = models.CharField(max_length=10, blank=True, null=True)
    or_note_s = models.CharField(max_length=40, blank=True, null=True)
    or_note_i = models.TextField(blank=True, null=True)
    or_ins_by = models.CharField(max_length=40, blank=True, null=True)
    or_app_by = models.CharField(max_length=25, blank=True, null=True)
    or_ins_dat = models.DateField(blank=True, null=True)
    or_app_dat = models.DateField(blank=True, null=True)
    or_qty_ext = models.IntegerField(blank=True, null=True)
    or_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    or_prod_co = models.CharField(max_length=2, blank=True, null=True)
    or_invent_field = models.CharField(db_column='or_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    or_raw_num = models.CharField(max_length=30, blank=True, null=True)
    or_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    or_line_nu = models.IntegerField(blank=True, null=True)
    or_est_mat = models.FloatField(blank=True, null=True)
    or_lo_code = models.CharField(max_length=10, blank=True, null=True)
    or_comp_da = models.DateField(blank=True, null=True)
    or_draw_nu = models.CharField(max_length=30, blank=True, null=True)
    or_draw_re = models.CharField(max_length=6, blank=True, null=True)
    or_non_bil = models.NullBooleanField()
    or_interna = models.NullBooleanField()
    or_misc_co = models.FloatField(blank=True, null=True)
    or_scrap_a = models.FloatField(blank=True, null=True)
    or_scrap_w = models.FloatField(blank=True, null=True)
    or_scrap_v = models.FloatField(blank=True, null=True)
    or_parent_field = models.CharField(db_column='or_parent_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    or_extatrb = models.CharField(max_length=30, blank=True, null=True)
    or_extatr2 = models.CharField(max_length=30, blank=True, null=True)
    or_extatr3 = models.CharField(max_length=30, blank=True, null=True)
    or_extatr4 = models.CharField(max_length=30, blank=True, null=True)
    or_extatr5 = models.CharField(max_length=30, blank=True, null=True)
    or_extatr6 = models.CharField(max_length=30, blank=True, null=True)
    or_extatr7 = models.CharField(max_length=30, blank=True, null=True)
    or_extatr8 = models.CharField(max_length=30, blank=True, null=True)
    or_extatr9 = models.CharField(max_length=30, blank=True, null=True)
    or_extat10 = models.CharField(max_length=30, blank=True, null=True)
    or_contact = models.CharField(max_length=25, blank=True, null=True)
    or_is_lot = models.IntegerField(blank=True, null=True)
    or_cont_cn = models.CharField(max_length=10, blank=True, null=True)
    or_cont_ty = models.CharField(max_length=10, blank=True, null=True)
    or_cont_de = models.CharField(max_length=20, blank=True, null=True)
    or_cont_we = models.CharField(max_length=10, blank=True, null=True)
    or_aggrega = models.NullBooleanField()
    or_user_id = models.CharField(max_length=5, blank=True, null=True)
    or_last_mo = models.DateTimeField(blank=True, null=True)
    or_seriali = models.NullBooleanField()
    or_op_last = models.CharField(max_length=30, blank=True, null=True)
    or_op_rev = models.CharField(max_length=3, blank=True, null=True)
    or_op_las2 = models.DateField(blank=True, null=True)
    or_doc_typ = models.CharField(max_length=10, blank=True, null=True)
    or_dpas = models.CharField(max_length=10, blank=True, null=True)
    or_rev_ste = models.IntegerField(blank=True, null=True)
    or_wipinfg = models.NullBooleanField()
    or_freeze = models.NullBooleanField()
    or_ser_typ = models.IntegerField(blank=True, null=True)
    or_ser_ste = models.IntegerField(blank=True, null=True)
    or_serial_field = models.CharField(db_column='or_serial_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    or_printed = models.DateField(blank=True, null=True)
    or_rework = models.NullBooleanField()
    or_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    or_markup = models.FloatField(blank=True, null=True)
    or_labor_c = models.NullBooleanField()
    or_continu = models.NullBooleanField()
    or_loctime = models.DateTimeField(blank=True, null=True)
    or_sl_id = models.CharField(max_length=10, blank=True, null=True)
    or_print_d = models.DateField(blank=True, null=True)
    or_origina = models.CharField(max_length=5, blank=True, null=True)
    or_st_id = models.CharField(max_length=2, blank=True, null=True)
    or_lc_id = models.CharField(max_length=10, blank=True, null=True)
    or_externa = models.NullBooleanField()
    or_adj_dat = models.DateField(blank=True, null=True)
    or_mat_mu = models.IntegerField(blank=True, null=True)
    or_display = models.NullBooleanField()
    or_displa2 = models.NullBooleanField()
    or_mat_mem = models.TextField(blank=True, null=True)
    or_overrid = models.NullBooleanField()
    or_project = models.IntegerField(blank=True, null=True)
    or_proj_sa = models.CharField(max_length=1, blank=True, null=True)
    or_tag_num = models.IntegerField(blank=True, null=True)
    or_proj_st = models.CharField(max_length=3, blank=True, null=True)
    or_df_id = models.CharField(max_length=10, blank=True, null=True)
    or_stat_no = models.TextField(blank=True, null=True)
    or_useopqt = models.NullBooleanField()
    or_splitpa = models.CharField(max_length=12, blank=True, null=True)
    or_warrant = models.NullBooleanField()
    or_scrap_c = models.CharField(max_length=12, blank=True, null=True)
    or_hidecom = models.NullBooleanField()
    or_jobnote = models.TextField(blank=True, null=True)
    or_jobstop = models.NullBooleanField()
    or_sigma_s = models.IntegerField(blank=True, null=True)
    or_keepzer = models.NullBooleanField()
    or_exclude = models.NullBooleanField()
    or_price_c = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'order'


class Ordopen(models.Model):
    oo_id = models.CharField(max_length=10, blank=True, null=True)
    oo_order_n = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordopen'


class Ordsord(models.Model):
    os_id = models.CharField(max_length=10, blank=True, null=True)
    os_order_n = models.CharField(max_length=15, blank=True, null=True)
    os_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    os_line_nu = models.IntegerField(blank=True, null=True)
    os_quantit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordsord'


class Orelease(models.Model):
    ol_order_n = models.CharField(max_length=12, blank=True, null=True)
    ol_rel_dat = models.DateField(blank=True, null=True)
    ol_rel_num = models.IntegerField(blank=True, null=True)
    ol_rel_qty = models.FloatField(blank=True, null=True)
    ol_rel_pro = models.FloatField(blank=True, null=True)
    ol_rel_bal = models.FloatField(blank=True, null=True)
    ol_rel_sch = models.FloatField(blank=True, null=True)
    ol_rel_shi = models.FloatField(blank=True, null=True)
    ol_quantit = models.FloatField(blank=True, null=True)
    ol_priorit = models.IntegerField(blank=True, null=True)
    ol_il = models.IntegerField(blank=True, null=True)
    ol_end_dat = models.DateField(blank=True, null=True)
    ol_fi = models.CharField(max_length=1, blank=True, null=True)
    ol_start_d = models.DateField(blank=True, null=True)
    ol_po_num = models.CharField(max_length=25, blank=True, null=True)
    ol_sch_qty = models.FloatField(blank=True, null=True)
    ol_sch_met = models.CharField(max_length=1, blank=True, null=True)
    ol_lead_ti = models.IntegerField(blank=True, null=True)
    ol_ph = models.CharField(max_length=1, blank=True, null=True)
    ol_track_n = models.CharField(max_length=15, blank=True, null=True)
    ol_proj_st = models.DateField(blank=True, null=True)
    ol_rel_sta = models.CharField(max_length=1, blank=True, null=True)
    ol_sched = models.NullBooleanField()
    ol_comp_da = models.DateField(blank=True, null=True)
    ol_lock = models.NullBooleanField()
    ol_cont_cn = models.CharField(max_length=10, blank=True, null=True)
    ol_cont_ty = models.CharField(max_length=10, blank=True, null=True)
    ol_cont_de = models.CharField(max_length=20, blank=True, null=True)
    ol_cont_we = models.CharField(max_length=10, blank=True, null=True)
    ol_lot = models.CharField(max_length=20, blank=True, null=True)
    ol_insp_da = models.DateField(blank=True, null=True)
    ol_release = models.NullBooleanField()
    ol_notes = models.TextField(blank=True, null=True)
    ol_fab_dat = models.DateField(blank=True, null=True)
    ol_shipby_field = models.DateField(db_column='ol_shipby_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ol_plannin = models.DateField(blank=True, null=True)
    ol_ordstat = models.CharField(max_length=10, blank=True, null=True)
    ol_expedit = models.CharField(max_length=10, blank=True, null=True)
    ol_owner = models.CharField(max_length=5, blank=True, null=True)
    ol_status1 = models.CharField(max_length=50, blank=True, null=True)
    ol_status2 = models.CharField(max_length=50, blank=True, null=True)
    ol_matveri = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'orelease'


class PDraw(models.Model):
    pd_id = models.IntegerField(blank=True, null=True)
    pd_pr_id = models.IntegerField(blank=True, null=True)
    pd_number = models.CharField(max_length=15, blank=True, null=True)
    pd_revisio = models.CharField(max_length=3, blank=True, null=True)
    pd_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_draw'


class Pantick(models.Model):
    pt_id = models.IntegerField(blank=True, null=True)
    pt_run_cod = models.CharField(max_length=20, blank=True, null=True)
    pt_order_n = models.CharField(max_length=12, blank=True, null=True)
    pt_rel_num = models.IntegerField(blank=True, null=True)
    pt_op_num = models.IntegerField(blank=True, null=True)
    pt_mach_co = models.CharField(max_length=5, blank=True, null=True)
    pt_num_tic = models.IntegerField(blank=True, null=True)
    pt_iss_dat = models.DateField(blank=True, null=True)
    pt_part_nu = models.CharField(max_length=30, blank=True, null=True)
    pt_rev_num = models.CharField(max_length=3, blank=True, null=True)
    pt_part_de = models.CharField(max_length=50, blank=True, null=True)
    pt_emp_nam = models.CharField(max_length=30, blank=True, null=True)
    pt_emp_id = models.CharField(max_length=5, blank=True, null=True)
    pt_invent_field = models.CharField(db_column='pt_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    pt_lot = models.CharField(max_length=10, blank=True, null=True)
    pt_ps = models.CharField(max_length=1, blank=True, null=True)
    pt_begin = models.IntegerField(blank=True, null=True)
    pt_asm_cou = models.IntegerField(blank=True, null=True)
    pt_jc_id = models.CharField(max_length=10, blank=True, null=True)
    pt_run_dat = models.DateField(blank=True, null=True)
    pt_qty_pro = models.FloatField(blank=True, null=True)
    pt_qty_scr = models.FloatField(blank=True, null=True)
    pt_qty_goo = models.FloatField(blank=True, null=True)
    pt_qty_rev = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pantick'


class Partkpi(models.Model):
    invent_num = models.CharField(max_length=30, blank=True, null=True)
    invent_des = models.CharField(max_length=50, blank=True, null=True)
    cust_code = models.CharField(max_length=6, blank=True, null=True)
    valperpart = models.FloatField(blank=True, null=True)
    valaccum = models.FloatField(blank=True, null=True)
    volaau = models.IntegerField(blank=True, null=True)
    voleau = models.IntegerField(blank=True, null=True)
    numsu52 = models.IntegerField(blank=True, null=True)
    numsuem = models.IntegerField(blank=True, null=True)
    numsuq = models.IntegerField(blank=True, null=True)
    sut52 = models.FloatField(blank=True, null=True)
    sutem = models.FloatField(blank=True, null=True)
    sutq = models.FloatField(blank=True, null=True)
    ct52 = models.FloatField(blank=True, null=True)
    ctem = models.FloatField(blank=True, null=True)
    ctq = models.FloatField(blank=True, null=True)
    peff52 = models.IntegerField(blank=True, null=True)
    peffem = models.IntegerField(blank=True, null=True)
    peffq = models.IntegerField(blank=True, null=True)
    rate52 = models.IntegerField(blank=True, null=True)
    rateem = models.IntegerField(blank=True, null=True)
    rateq = models.IntegerField(blank=True, null=True)
    scrap52 = models.FloatField(blank=True, null=True)
    scrapem = models.FloatField(blank=True, null=True)
    scrapq = models.FloatField(blank=True, null=True)
    ptactual = models.FloatField(blank=True, null=True)
    ptem = models.FloatField(blank=True, null=True)
    ptq = models.FloatField(blank=True, null=True)
    partkpiid = models.IntegerField(blank=True, null=True)
    mach_code = models.CharField(max_length=5, blank=True, null=True)
    de_id = models.CharField(max_length=2, blank=True, null=True)
    numsu52_col = models.CharField(max_length=1, blank=True, null=True)
    numsuemcol = models.CharField(max_length=1, blank=True, null=True)
    sut52_color = models.CharField(max_length=1, blank=True, null=True)
    sutemcolor = models.CharField(max_length=1, blank=True, null=True)
    ct52_color = models.CharField(max_length=1, blank=True, null=True)
    ctemcolor = models.CharField(max_length=1, blank=True, null=True)
    peff52_colo = models.CharField(max_length=1, blank=True, null=True)
    peffemcolo = models.CharField(max_length=1, blank=True, null=True)
    rate52_colo = models.CharField(max_length=1, blank=True, null=True)
    rateemcolo = models.CharField(max_length=1, blank=True, null=True)
    scrap52_col = models.CharField(max_length=1, blank=True, null=True)
    scrapemcol = models.CharField(max_length=1, blank=True, null=True)
    ptactualco = models.CharField(max_length=1, blank=True, null=True)
    ofi = models.FloatField(blank=True, null=True)
    vapercent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partkpi'


class Partmat(models.Model):
    pm_id = models.CharField(max_length=10, blank=True, null=True)
    pm_code = models.CharField(max_length=2, blank=True, null=True)
    pm_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partmat'


class Partoem(models.Model):
    po_id = models.CharField(max_length=10, blank=True, null=True)
    po_code = models.CharField(max_length=2, blank=True, null=True)
    po_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partoem'


class Partprora(models.Model):
    ppr_id = models.IntegerField(blank=True, null=True)
    invent_num = models.CharField(max_length=30, blank=True, null=True)
    invent_des = models.CharField(max_length=50, blank=True, null=True)
    cust_code = models.CharField(max_length=6, blank=True, null=True)
    numsu52 = models.IntegerField(blank=True, null=True)
    numsuem = models.IntegerField(blank=True, null=True)
    numsuq = models.IntegerField(blank=True, null=True)
    year1 = models.IntegerField(blank=True, null=True)
    year2 = models.IntegerField(blank=True, null=True)
    year3 = models.IntegerField(blank=True, null=True)
    year4 = models.IntegerField(blank=True, null=True)
    last52 = models.IntegerField(blank=True, null=True)
    last26 = models.IntegerField(blank=True, null=True)
    last13 = models.IntegerField(blank=True, null=True)
    last5 = models.IntegerField(blank=True, null=True)
    ofi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partprora'


class Partscrap(models.Model):
    psc_id = models.IntegerField(blank=True, null=True)
    invent_num = models.CharField(max_length=30, blank=True, null=True)
    invent_des = models.CharField(max_length=50, blank=True, null=True)
    cust_code = models.CharField(max_length=6, blank=True, null=True)
    numsu52 = models.IntegerField(blank=True, null=True)
    numsuem = models.IntegerField(blank=True, null=True)
    numsuq = models.IntegerField(blank=True, null=True)
    year1 = models.IntegerField(blank=True, null=True)
    year2 = models.IntegerField(blank=True, null=True)
    year3 = models.IntegerField(blank=True, null=True)
    year4 = models.IntegerField(blank=True, null=True)
    last52 = models.IntegerField(blank=True, null=True)
    last26 = models.IntegerField(blank=True, null=True)
    last13 = models.IntegerField(blank=True, null=True)
    last5 = models.IntegerField(blank=True, null=True)
    ofi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partscrap'


class Partsize(models.Model):
    ps_id = models.CharField(max_length=10, blank=True, null=True)
    ps_size = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partsize'


class Parttype(models.Model):
    pt_id = models.CharField(max_length=10, blank=True, null=True)
    pt_code = models.CharField(max_length=1, blank=True, null=True)
    pt_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parttype'


class Partvol(models.Model):
    pv_id = models.IntegerField(blank=True, null=True)
    invent_num = models.CharField(max_length=30, blank=True, null=True)
    invent_des = models.CharField(max_length=50, blank=True, null=True)
    cust_code = models.CharField(max_length=6, blank=True, null=True)
    numsu52 = models.IntegerField(blank=True, null=True)
    numsuem = models.IntegerField(blank=True, null=True)
    numsuq = models.IntegerField(blank=True, null=True)
    year1 = models.IntegerField(blank=True, null=True)
    year2 = models.IntegerField(blank=True, null=True)
    year3 = models.IntegerField(blank=True, null=True)
    year4 = models.IntegerField(blank=True, null=True)
    last52 = models.IntegerField(blank=True, null=True)
    last26 = models.IntegerField(blank=True, null=True)
    last13 = models.IntegerField(blank=True, null=True)
    last5 = models.IntegerField(blank=True, null=True)
    week1 = models.IntegerField(blank=True, null=True)
    week2 = models.IntegerField(blank=True, null=True)
    week3 = models.IntegerField(blank=True, null=True)
    week4 = models.IntegerField(blank=True, null=True)
    week5 = models.IntegerField(blank=True, null=True)
    next5 = models.IntegerField(blank=True, null=True)
    lastvsnext = models.IntegerField(blank=True, null=True)
    ofi = models.FloatField(blank=True, null=True)
    shipped52 = models.IntegerField(blank=True, null=True)
    shippedem = models.IntegerField(blank=True, null=True)
    shippedq = models.IntegerField(blank=True, null=True)
    month1 = models.IntegerField(blank=True, null=True)
    month2 = models.IntegerField(blank=True, null=True)
    month3 = models.IntegerField(blank=True, null=True)
    month4 = models.IntegerField(blank=True, null=True)
    month5 = models.IntegerField(blank=True, null=True)
    month6 = models.IntegerField(blank=True, null=True)
    month7 = models.IntegerField(blank=True, null=True)
    month8 = models.IntegerField(blank=True, null=True)
    month9 = models.IntegerField(blank=True, null=True)
    month10 = models.IntegerField(blank=True, null=True)
    month11 = models.IntegerField(blank=True, null=True)
    month12 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partvol'


class Pm(models.Model):
    pm_id = models.CharField(max_length=20, blank=True, null=True)
    pm_task = models.CharField(max_length=50, blank=True, null=True)
    pm_date = models.DateField(blank=True, null=True)
    pm_emp_id = models.CharField(max_length=5, blank=True, null=True)
    pm_group = models.CharField(max_length=10, blank=True, null=True)
    pm_ext_des = models.TextField(blank=True, null=True)
    pm_frequen = models.IntegerField(blank=True, null=True)
    pm_last_co = models.DateField(blank=True, null=True)
    pm_invent_field = models.CharField(db_column='pm_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    pm_next_du = models.DateField(blank=True, null=True)
    pm_mach_co = models.CharField(max_length=5, blank=True, null=True)
    pm_est_hou = models.FloatField(blank=True, null=True)
    pm_gage = models.NullBooleanField()
    pm_lot_num = models.CharField(max_length=20, blank=True, null=True)
    pm_supp_co = models.CharField(max_length=6, blank=True, null=True)
    pm_gt_code = models.CharField(max_length=10, blank=True, null=True)
    pm_il_id = models.CharField(max_length=10, blank=True, null=True)
    pm_size = models.FloatField(blank=True, null=True)
    pm_metric = models.NullBooleanField()
    pm_pitch = models.FloatField(blank=True, null=True)
    pm_pitch_g = models.FloatField(blank=True, null=True)
    pm_pitch_n = models.FloatField(blank=True, null=True)
    pm_poa_go = models.FloatField(blank=True, null=True)
    pm_poa_ng = models.FloatField(blank=True, null=True)
    pm_lop_go = models.FloatField(blank=True, null=True)
    pm_lop_ng = models.FloatField(blank=True, null=True)
    pm_ib_id = models.CharField(max_length=10, blank=True, null=True)
    pm_obsolet = models.NullBooleanField()
    pm_verifie = models.NullBooleanField()
    pm_tt_id = models.CharField(max_length=10, blank=True, null=True)
    pm_go_id = models.CharField(max_length=10, blank=True, null=True)
    pm_manufac = models.CharField(max_length=30, blank=True, null=True)
    pm_status = models.CharField(max_length=10, blank=True, null=True)
    pm_range = models.CharField(max_length=30, blank=True, null=True)
    pm_cbou = models.NullBooleanField()
    pm_gagecat = models.IntegerField(blank=True, null=True)
    pm_gagecla = models.CharField(max_length=10, blank=True, null=True)
    pm_diamete = models.FloatField(blank=True, null=True)
    pm_gonogo = models.IntegerField(blank=True, null=True)
    pm_threads = models.CharField(max_length=10, blank=True, null=True)
    pm_thdform = models.IntegerField(blank=True, null=True)
    pm_classof = models.IntegerField(blank=True, null=True)
    pm_cboi = models.NullBooleanField()
    pm_size_mi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pm'


class PmFail(models.Model):
    pf_id = models.CharField(max_length=10, blank=True, null=True)
    pf_po_id = models.CharField(max_length=10, blank=True, null=True)
    pf_fa_code = models.CharField(max_length=10, blank=True, null=True)
    pf_part_nu = models.CharField(max_length=30, blank=True, null=True)
    pf_part_de = models.CharField(max_length=50, blank=True, null=True)
    pf_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pm_fail'


class PmGroup(models.Model):
    pg_group = models.CharField(max_length=10, blank=True, null=True)
    pg_desc = models.CharField(max_length=50, blank=True, null=True)
    pg_task = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pm_group'


class PmOrd(models.Model):
    po_id = models.CharField(max_length=10, blank=True, null=True)
    po_emp_id = models.CharField(max_length=5, blank=True, null=True)
    po_task = models.TextField(blank=True, null=True)
    po_order_n = models.CharField(max_length=12, blank=True, null=True)
    po_comp_da = models.DateField(blank=True, null=True)
    po_comment = models.TextField(blank=True, null=True)
    po_pm_id = models.CharField(max_length=20, blank=True, null=True)
    po_passfai = models.IntegerField(blank=True, null=True)
    po_due_dat = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pm_ord'


class Pmlog(models.Model):
    pl_id = models.CharField(max_length=10, blank=True, null=True)
    pl_pm_id = models.CharField(max_length=20, blank=True, null=True)
    pl_reading = models.FloatField(blank=True, null=True)
    pl_readin2 = models.FloatField(blank=True, null=True)
    pl_action = models.TextField(blank=True, null=True)
    pl_blk_siz = models.FloatField(blank=True, null=True)
    pl_blk_si2 = models.FloatField(blank=True, null=True)
    pl_date = models.DateField(blank=True, null=True)
    pl_interva = models.FloatField(blank=True, null=True)
    pl_interv2 = models.FloatField(blank=True, null=True)
    pl_interv3 = models.FloatField(blank=True, null=True)
    pl_interv4 = models.FloatField(blank=True, null=True)
    pl_interv5 = models.FloatField(blank=True, null=True)
    pl_emp_id = models.CharField(max_length=5, blank=True, null=True)
    pl_result = models.CharField(max_length=4, blank=True, null=True)
    pl_masteru = models.CharField(max_length=30, blank=True, null=True)
    pl_interv6 = models.FloatField(blank=True, null=True)
    pl_interv7 = models.FloatField(blank=True, null=True)
    pl_paralle = models.FloatField(blank=True, null=True)
    pl_uncerta = models.FloatField(blank=True, null=True)
    pl_screw_w = models.CharField(max_length=4, blank=True, null=True)
    pl_result1 = models.FloatField(blank=True, null=True)
    pl_result2 = models.FloatField(blank=True, null=True)
    pl_result3 = models.FloatField(blank=True, null=True)
    pl_result4 = models.FloatField(blank=True, null=True)
    pl_result5 = models.FloatField(blank=True, null=True)
    pl_result6 = models.FloatField(blank=True, null=True)
    pl_result7 = models.FloatField(blank=True, null=True)
    pl_result8 = models.FloatField(blank=True, null=True)
    pl_result9 = models.FloatField(blank=True, null=True)
    pl_resul10 = models.FloatField(blank=True, null=True)
    pl_resul11 = models.FloatField(blank=True, null=True)
    pl_resul12 = models.FloatField(blank=True, null=True)
    pl_resul13 = models.FloatField(blank=True, null=True)
    pl_resul14 = models.FloatField(blank=True, null=True)
    pl_result_field = models.CharField(db_column='pl_result_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    pl_cylindr = models.FloatField(blank=True, null=True)
    pl_pass1 = models.CharField(max_length=4, blank=True, null=True)
    pl_pass2 = models.CharField(max_length=4, blank=True, null=True)
    pl_pass3 = models.CharField(max_length=4, blank=True, null=True)
    pl_pass4 = models.CharField(max_length=4, blank=True, null=True)
    pl_pass5 = models.CharField(max_length=4, blank=True, null=True)
    pl_pass6 = models.CharField(max_length=4, blank=True, null=True)
    pl_pass7 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pmlog'


class PoBun(models.Model):
    pb_po_num = models.CharField(max_length=7, blank=True, null=True)
    pb_line_nu = models.IntegerField(blank=True, null=True)
    pb_rec_no = models.IntegerField(blank=True, null=True)
    pb_bun_num = models.IntegerField(blank=True, null=True)
    pb_qty = models.FloatField(blank=True, null=True)
    pb_il_id = models.CharField(max_length=10, blank=True, null=True)
    pb_ib_id = models.CharField(max_length=10, blank=True, null=True)
    pb_lot_num = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po_bun'


class PoRectc(models.Model):
    pt_po_num = models.CharField(max_length=7, blank=True, null=True)
    pt_line_nu = models.IntegerField(blank=True, null=True)
    pt_rec_num = models.IntegerField(blank=True, null=True)
    pt_date = models.DateField(blank=True, null=True)
    pt_userid = models.CharField(max_length=5, blank=True, null=True)
    pt_startti = models.DateTimeField(blank=True, null=True)
    pt_endtime = models.DateTimeField(blank=True, null=True)
    pt_timeela = models.FloatField(blank=True, null=True)
    pt_pr_rec_field = models.IntegerField(db_column='pt_pr_rec_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pt_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po_rectc'


class Pod(models.Model):
    px_po_num = models.CharField(max_length=15, blank=True, null=True)
    px_parts_f = models.NullBooleanField()
    px_hardnes = models.NullBooleanField()
    px_bars_pc = models.NullBooleanField()
    px_bars_ma = models.NullBooleanField()
    px_bars_st = models.NullBooleanField()
    px_hardne2 = models.NullBooleanField()
    px_heat_tr = models.NullBooleanField()
    px_inert_g = models.NullBooleanField()
    px_scales = models.NullBooleanField()
    px_pull_te = models.NullBooleanField()
    px_line_nu = models.IntegerField(blank=True, null=True)
    px_dist_co = models.CharField(max_length=2, blank=True, null=True)
    px_hardne3 = models.CharField(max_length=30, blank=True, null=True)
    px_bar_tir = models.FloatField(blank=True, null=True)
    px_hard_re = models.CharField(max_length=30, blank=True, null=True)
    px_ht_spec = models.CharField(max_length=30, blank=True, null=True)
    px_pull_t2 = models.IntegerField(blank=True, null=True)
    px_vend_in = models.TextField(blank=True, null=True)
    px_pack_re = models.TextField(blank=True, null=True)
    px_print_i = models.NullBooleanField()
    px_ht_done = models.NullBooleanField()
    px_batch_i = models.NullBooleanField()
    px_add_ven = models.TextField(blank=True, null=True)
    px_mat_har = models.NullBooleanField()
    px_mat_ha2 = models.CharField(max_length=30, blank=True, null=True)
    px_plate_t = models.NullBooleanField()
    px_plate_2 = models.FloatField(blank=True, null=True)
    px_fillet = models.NullBooleanField()
    px_max_fil = models.CharField(max_length=30, blank=True, null=True)
    px_conc_re = models.TextField(blank=True, null=True)
    px_conc_a = models.CharField(max_length=15, blank=True, null=True)
    px_conc_b = models.CharField(max_length=15, blank=True, null=True)
    px_conc_c = models.CharField(max_length=15, blank=True, null=True)
    px_norm_a = models.CharField(max_length=15, blank=True, null=True)
    px_norm_b = models.CharField(max_length=15, blank=True, null=True)
    px_norm_c = models.CharField(max_length=15, blank=True, null=True)
    px_st_id = models.CharField(max_length=10, blank=True, null=True)
    px_type = models.IntegerField(blank=True, null=True)
    px_mat_spe = models.NullBooleanField()
    px_gages = models.NullBooleanField()
    px_gage_go = models.CharField(max_length=15, blank=True, null=True)
    px_gage_no = models.CharField(max_length=15, blank=True, null=True)
    px_mat_sp2 = models.CharField(max_length=30, blank=True, null=True)
    px_finish = models.NullBooleanField()
    px_finish_field = models.CharField(db_column='px_finish_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    field_null_flags = models.CharField(db_column='_null_flags', max_length=3, blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'pod'


class PodTxt(models.Model):
    pw_id = models.CharField(max_length=10, blank=True, null=True)
    pw_type = models.IntegerField(blank=True, null=True)
    pw_field_n = models.CharField(max_length=25, blank=True, null=True)
    pw_true_te = models.CharField(max_length=250, blank=True, null=True)
    pw_false_t = models.CharField(max_length=250, blank=True, null=True)
    pw_null_te = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod_txt'


class Poquote(models.Model):
    pq_seq = models.IntegerField(blank=True, null=True)
    pq_quote_n = models.CharField(max_length=15, blank=True, null=True)
    pq_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poquote'


class Ppprmg(models.Model):
    pp_minimum = models.FloatField(blank=True, null=True)
    pp_maximum = models.FloatField(blank=True, null=True)
    pp_xx_tol = models.FloatField(blank=True, null=True)
    pp_x_tol = models.FloatField(blank=True, null=True)
    pp_y_tol = models.FloatField(blank=True, null=True)
    pp_z_tol = models.FloatField(blank=True, null=True)
    pp_zz_tol = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ppprmg'


class Prelease(models.Model):
    pe_id = models.CharField(max_length=10, blank=True, null=True)
    pe_po_num = models.CharField(max_length=7, blank=True, null=True)
    pe_po_line = models.IntegerField(blank=True, null=True)
    pe_po_rel = models.IntegerField(blank=True, null=True)
    pe_po_rec = models.IntegerField(blank=True, null=True)
    pe_quantit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prelease'


class Prevact(models.Model):
    pa_id = models.CharField(max_length=10, blank=True, null=True)
    pa_date = models.DateField(blank=True, null=True)
    pa_invent_field = models.CharField(db_column='pa_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    pa_part_nu = models.CharField(max_length=30, blank=True, null=True)
    pa_part_de = models.CharField(max_length=50, blank=True, null=True)
    pa_intcirc = models.TextField(blank=True, null=True)
    pa_prevact = models.TextField(blank=True, null=True)
    pa_impl = models.TextField(blank=True, null=True)
    pa_effanal = models.TextField(blank=True, null=True)
    pa_comm = models.TextField(blank=True, null=True)
    pa_cust_co = models.CharField(max_length=6, blank=True, null=True)
    pa_supp_co = models.CharField(max_length=6, blank=True, null=True)
    pa_desc = models.CharField(max_length=100, blank=True, null=True)
    pa_emp_by = models.CharField(max_length=5, blank=True, null=True)
    pa_ca_id = models.CharField(max_length=10, blank=True, null=True)
    pa_status = models.CharField(max_length=1, blank=True, null=True)
    pa_nc_id = models.CharField(max_length=10, blank=True, null=True)
    pa_mach_co = models.CharField(max_length=5, blank=True, null=True)
    pa_op_num = models.IntegerField(blank=True, null=True)
    pa_de_id = models.CharField(max_length=2, blank=True, null=True)
    pa_status_field = models.DateField(db_column='pa_status_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pa_di_id = models.CharField(max_length=10, blank=True, null=True)
    pa_presp = models.CharField(max_length=5, blank=True, null=True)
    pa_iresp = models.CharField(max_length=5, blank=True, null=True)
    pa_eresp = models.CharField(max_length=5, blank=True, null=True)
    pa_cresp = models.CharField(max_length=5, blank=True, null=True)
    pa_pdate = models.DateField(blank=True, null=True)
    pa_idate = models.DateField(blank=True, null=True)
    pa_edate = models.DateField(blank=True, null=True)
    pa_cdate = models.DateField(blank=True, null=True)
    pa_pstatus = models.CharField(max_length=1, blank=True, null=True)
    pa_istatus = models.CharField(max_length=1, blank=True, null=True)
    pa_estatus = models.CharField(max_length=1, blank=True, null=True)
    pa_cstatus = models.CharField(max_length=1, blank=True, null=True)
    pa_needact = models.TextField(blank=True, null=True)
    pa_results = models.TextField(blank=True, null=True)
    pa_team = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prevact'


class Pricbrkt(models.Model):
    pb_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    pb_br_id = models.CharField(max_length=10, blank=True, null=True)
    pb_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pricbrkt'


class Prod(models.Model):
    pr_prod_co = models.CharField(max_length=2, blank=True, null=True)
    pr_prod_de = models.CharField(max_length=40, blank=True, null=True)
    pr_gl_num = models.CharField(max_length=12, blank=True, null=True)
    pr_pc_prod = models.CharField(max_length=5, blank=True, null=True)
    pr_commiss = models.NullBooleanField()
    pr_non_tax = models.NullBooleanField()
    pr_dv_code = models.CharField(max_length=2, blank=True, null=True)
    pr_dp_code = models.CharField(max_length=2, blank=True, null=True)
    pr_dist_co = models.CharField(max_length=2, blank=True, null=True)
    pr_gl_num_field = models.CharField(db_column='pr_gl_num_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_gl_num2 = models.CharField(max_length=12, blank=True, null=True)
    pr_gl_num3 = models.CharField(max_length=12, blank=True, null=True)
    pr_gl_num4 = models.CharField(max_length=12, blank=True, null=True)
    pr_gl_num5 = models.CharField(max_length=12, blank=True, null=True)
    pr_ex_tonn = models.NullBooleanField()
    pr_exclude = models.NullBooleanField()
    pr_gl_num6 = models.CharField(max_length=12, blank=True, null=True)
    pr_gl_num7 = models.CharField(max_length=12, blank=True, null=True)
    pr_gl_num8 = models.CharField(max_length=12, blank=True, null=True)
    pr_export = models.CharField(max_length=5, blank=True, null=True)
    pr_gl_abs_field = models.CharField(db_column='pr_gl_abs_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_gl_abs2 = models.CharField(max_length=12, blank=True, null=True)
    pr_gl_abs3 = models.CharField(max_length=12, blank=True, null=True)
    pr_ship_no = models.TextField(blank=True, null=True)
    pr_freight = models.CharField(max_length=2, blank=True, null=True)
    pr_gl_num9 = models.CharField(max_length=12, blank=True, null=True)
    pr_lo_code = models.CharField(max_length=10, blank=True, null=True)
    pr_il_id = models.CharField(max_length=10, blank=True, null=True)
    pr_hideopc = models.NullBooleanField()
    pr_excl_di = models.NullBooleanField()
    pr_obsolet = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'prod'


class Prodcat(models.Model):
    pc_prod_co = models.CharField(max_length=5, blank=True, null=True)
    pc_prod_de = models.CharField(max_length=30, blank=True, null=True)
    pc_dv_code = models.CharField(max_length=2, blank=True, null=True)
    pc_dp_code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prodcat'


class ProjOps(models.Model):
    po_id = models.IntegerField(blank=True, null=True)
    po_pr_id = models.IntegerField(blank=True, null=True)
    ao_mach_co = models.CharField(max_length=5, blank=True, null=True)
    ao_op_num = models.IntegerField(blank=True, null=True)
    ao_op_hr = models.FloatField(blank=True, null=True)
    ao_order_n = models.CharField(max_length=12, blank=True, null=True)
    ao_type = models.CharField(max_length=1, blank=True, null=True)
    ao_suhr = models.FloatField(blank=True, null=True)
    ao_sur = models.FloatField(blank=True, null=True)
    ao_su = models.FloatField(blank=True, null=True)
    ao_gp = models.FloatField(blank=True, null=True)
    ao_pop = models.FloatField(blank=True, null=True)
    ao_np = models.FloatField(blank=True, null=True)
    ao_hpu = models.FloatField(blank=True, null=True)
    ao_cpu = models.FloatField(blank=True, null=True)
    ao_note = models.TextField(blank=True, null=True)
    ao_current = models.IntegerField(blank=True, null=True)
    ao_attend = models.IntegerField(blank=True, null=True)
    ao_queue = models.FloatField(blank=True, null=True)
    ao_dist_co = models.CharField(max_length=2, blank=True, null=True)
    ao_supp_co = models.CharField(max_length=6, blank=True, null=True)
    ao_unit_co = models.FloatField(blank=True, null=True)
    ao_quantit = models.IntegerField(blank=True, null=True)
    ao_ext_cos = models.FloatField(blank=True, null=True)
    ao_mark_up = models.IntegerField(blank=True, null=True)
    ao_tot_cos = models.FloatField(blank=True, null=True)
    ao_distrib = models.NullBooleanField()
    ao_recalc = models.NullBooleanField()
    ao_tsu = models.IntegerField(blank=True, null=True)
    ao_hrs_od = models.FloatField(blank=True, null=True)
    ao_hrs_td = models.FloatField(blank=True, null=True)
    ao_hrs_tot = models.FloatField(blank=True, null=True)
    ao_hrs_av = models.FloatField(blank=True, null=True)
    ao_p_prod = models.FloatField(blank=True, null=True)
    ao_p_bad = models.IntegerField(blank=True, null=True)
    ao_p_good = models.FloatField(blank=True, null=True)
    ao_qty_bal = models.FloatField(blank=True, null=True)
    ao_hrs_pro = models.FloatField(blank=True, null=True)
    ao_hrs_set = models.FloatField(blank=True, null=True)
    ao_scrap = models.IntegerField(blank=True, null=True)
    ao_rework = models.IntegerField(blank=True, null=True)
    ao_qty_pro = models.FloatField(blank=True, null=True)
    ao_qty_inv = models.IntegerField(blank=True, null=True)
    ao_act_phr = models.FloatField(blank=True, null=True)
    ao_adj_phr = models.FloatField(blank=True, null=True)
    ao_go_eff = models.IntegerField(blank=True, null=True)
    ao_p_eff = models.IntegerField(blank=True, null=True)
    ao_su_eff = models.IntegerField(blank=True, null=True)
    ao_perc_co = models.IntegerField(blank=True, null=True)
    ao_num_mac = models.IntegerField(blank=True, null=True)
    ao_qty_ord = models.IntegerField(blank=True, null=True)
    ao_incl_su = models.CharField(max_length=100, blank=True, null=True)
    ao_end_dat = models.TextField(blank=True, null=True)
    ao_sc_off = models.CharField(max_length=100, blank=True, null=True)
    ao_labors = models.FloatField(blank=True, null=True)
    ao_burdens = models.FloatField(blank=True, null=True)
    ao_laborp = models.FloatField(blank=True, null=True)
    ao_burdenp = models.FloatField(blank=True, null=True)
    ao_force_m = models.CharField(max_length=100, blank=True, null=True)
    ao_sched_q = models.TextField(blank=True, null=True)
    ao_in_inve = models.CharField(max_length=30, blank=True, null=True)
    ao_out_inv = models.CharField(max_length=30, blank=True, null=True)
    ao_sched = models.NullBooleanField()
    ao_force = models.NullBooleanField()
    ao_rewflag = models.NullBooleanField()
    ao_g_code = models.CharField(max_length=10, blank=True, null=True)
    ao_review = models.IntegerField(blank=True, null=True)
    ao_move_st = models.NullBooleanField()
    ao_complet = models.NullBooleanField()
    ao_master_field = models.IntegerField(db_column='ao_master_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_parent_field = models.IntegerField(db_column='ao_parent_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_oplib_n = models.TextField(blank=True, null=True)
    ao_il_id = models.CharField(max_length=10, blank=True, null=True)
    ao_ib_id = models.CharField(max_length=10, blank=True, null=True)
    ao_pagebre = models.NullBooleanField()
    ao_min_cha = models.FloatField(blank=True, null=True)
    ao_infin_m = models.FloatField(blank=True, null=True)
    ao_enforce = models.NullBooleanField()
    ao_setup_m = models.NullBooleanField()
    ao_setup_c = models.IntegerField(blank=True, null=True)
    ao_aggrega = models.IntegerField(blank=True, null=True)
    ao_last_pr = models.NullBooleanField()
    ao_split = models.NullBooleanField()
    ao_il_id_i = models.CharField(max_length=10, blank=True, null=True)
    ao_ib_id_i = models.CharField(max_length=10, blank=True, null=True)
    ao_optype = models.IntegerField(blank=True, null=True)
    ao_down = models.IntegerField(blank=True, null=True)
    ao_pc_lbs = models.NullBooleanField()
    ao_pc_cost = models.FloatField(blank=True, null=True)
    ao_aw_orde = models.CharField(max_length=8, blank=True, null=True)
    ao_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    ao_infstar = models.DateField(blank=True, null=True)
    ao_infend_field = models.DateField(db_column='ao_infend_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_statnot = models.TextField(blank=True, null=True)
    ao_minqty = models.IntegerField(blank=True, null=True)
    ao_hpp = models.FloatField(blank=True, null=True)
    ao_mpp = models.FloatField(blank=True, null=True)
    ao_spp = models.FloatField(blank=True, null=True)
    ao_burden = models.FloatField(blank=True, null=True)
    ao_exclude = models.NullBooleanField()
    ao_comp_da = models.DateField(blank=True, null=True)
    ao_sl = models.TextField(blank=True, null=True)
    ao_pc_per_field = models.FloatField(db_column='ao_pc_per_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_unit_ra = models.FloatField(blank=True, null=True)
    ao_need_qt = models.FloatField(blank=True, null=True)
    ao_surchar = models.FloatField(blank=True, null=True)
    ao_simple_field = models.NullBooleanField(db_column='ao_simple_')  # Field renamed because it ended with '_'.
    ao_lossper = models.FloatField(blank=True, null=True)
    ao_load_ti = models.FloatField(blank=True, null=True)
    ao_rpm = models.IntegerField(blank=True, null=True)
    ao_spindge = models.CharField(max_length=15, blank=True, null=True)
    ao_changeg = models.CharField(max_length=15, blank=True, null=True)
    ao_threadg = models.CharField(max_length=15, blank=True, null=True)
    ao_st_id = models.CharField(max_length=10, blank=True, null=True)
    ao_signifi = models.NullBooleanField()
    ao_post_pc = models.NullBooleanField()
    ao_sa_id = models.CharField(max_length=10, blank=True, null=True)
    ao_donotor = models.NullBooleanField()
    ao_cost1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proj_ops'


class ProjPo(models.Model):
    pp_id = models.IntegerField(blank=True, null=True)
    pp_pr_id = models.IntegerField(blank=True, null=True)
    pp_po_num = models.CharField(max_length=7, blank=True, null=True)
    pp_po_line = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proj_po'


class Project(models.Model):
    pr_id = models.IntegerField(blank=True, null=True)
    pr_proj_or = models.CharField(max_length=12, blank=True, null=True)
    pr_install = models.CharField(max_length=30, blank=True, null=True)
    pr_item_nu = models.IntegerField(blank=True, null=True)
    pr_subitem = models.IntegerField(blank=True, null=True)
    pr_pcpart = models.IntegerField(blank=True, null=True)
    pr_req_sho = models.NullBooleanField()
    pr_order_n = models.CharField(max_length=12, blank=True, null=True)
    pr_invnon = models.IntegerField(blank=True, null=True)
    pr_invent_field = models.CharField(db_column='pr_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_part_nu = models.CharField(max_length=30, blank=True, null=True)
    pr_purch_u = models.CharField(max_length=2, blank=True, null=True)
    pr_islot = models.NullBooleanField()
    pr_make_bu = models.CharField(max_length=1, blank=True, null=True)
    pr_paint = models.CharField(max_length=20, blank=True, null=True)
    pr_quantit = models.FloatField(blank=True, null=True)
    pr_unit_co = models.FloatField(blank=True, null=True)
    pr_ext_cos = models.FloatField(blank=True, null=True)
    pr_reserve = models.FloatField(blank=True, null=True)
    pr_bal_nee = models.FloatField(blank=True, null=True)
    pr_part_de = models.CharField(max_length=60, blank=True, null=True)
    pr_pmemo = models.TextField(blank=True, null=True)
    pr_serial_field = models.CharField(db_column='pr_serial_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_dist_co = models.CharField(max_length=2, blank=True, null=True)
    pr_prod_co = models.CharField(max_length=2, blank=True, null=True)
    pr_require = models.DateField(blank=True, null=True)
    pr_prepurc = models.NullBooleanField()
    pr_supp_co = models.CharField(max_length=6, blank=True, null=True)
    pr_sup_par = models.CharField(max_length=30, blank=True, null=True)
    pr_cert_nu = models.CharField(max_length=15, blank=True, null=True)
    pr_lead_ti = models.IntegerField(blank=True, null=True)
    pr_donotbu = models.NullBooleanField()
    pr_non_sto = models.NullBooleanField()
    pr_obsolet = models.NullBooleanField()
    pr_dir_sto = models.IntegerField(blank=True, null=True)
    pr_po_num = models.CharField(max_length=7, blank=True, null=True)
    pr_po_line = models.IntegerField(blank=True, null=True)
    pr_qty_ord = models.FloatField(blank=True, null=True)
    pr_qty_rec = models.FloatField(blank=True, null=True)
    pr_fab_dat = models.DateField(blank=True, null=True)
    pr_ship_da = models.DateField(blank=True, null=True)
    pr_due_dat = models.DateField(blank=True, null=True)
    pr_assigne = models.CharField(max_length=5, blank=True, null=True)
    pr_stock_u = models.CharField(max_length=2, blank=True, null=True)
    pr_usesuom = models.NullBooleanField()
    pr_shape_c = models.CharField(max_length=7, blank=True, null=True)
    pr_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    pr_cht_siz = models.FloatField(blank=True, null=True)
    pr_mat_len = models.FloatField(blank=True, null=True)
    pr_width = models.FloatField(blank=True, null=True)
    pr_height = models.FloatField(blank=True, null=True)
    pr_web_thi = models.FloatField(blank=True, null=True)
    pr_bar_wei = models.FloatField(blank=True, null=True)
    pr_mat_wid = models.FloatField(blank=True, null=True)
    pr_length = models.FloatField(blank=True, null=True)
    pr_qty_per = models.FloatField(blank=True, null=True)
    pr_wgtpp = models.FloatField(blank=True, null=True)
    pr_ppbar = models.FloatField(blank=True, null=True)
    pr_mach_co = models.CharField(max_length=5, blank=True, null=True)
    pr_tot_hrs = models.FloatField(blank=True, null=True)
    pr_draw_nu = models.CharField(max_length=15, blank=True, null=True)
    pr_lock_ba = models.NullBooleanField()
    pr_rev_ste = models.IntegerField(blank=True, null=True)
    pr_confcos = models.NullBooleanField()
    pr_alloc_o = models.IntegerField(blank=True, null=True)
    pr_qinv_it = models.IntegerField(blank=True, null=True)
    pr_from_ex = models.NullBooleanField()
    pr_purch_m = models.TextField(blank=True, null=True)
    pr_purch_q = models.FloatField(blank=True, null=True)
    pr_bom_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class Projerng(models.Model):
    pe_id = models.IntegerField(blank=True, null=True)
    pe_proj_or = models.CharField(max_length=12, blank=True, null=True)
    pe_assigne = models.CharField(max_length=5, blank=True, null=True)
    pe_inactiv = models.NullBooleanField()
    pe_from = models.IntegerField(blank=True, null=True)
    pe_to = models.IntegerField(blank=True, null=True)
    pe_desc = models.CharField(max_length=30, blank=True, null=True)
    pe_next = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projerng'


class PtAsmb(models.Model):
    pa_id = models.CharField(max_length=10, blank=True, null=True)
    pa_pt_id = models.IntegerField(blank=True, null=True)
    pa_prod_tk = models.IntegerField(blank=True, null=True)
    pa_type = models.CharField(max_length=1, blank=True, null=True)
    pa_lot_num = models.CharField(max_length=20, blank=True, null=True)
    pa_invent_field = models.CharField(db_column='pa_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'pt_asmb'


class Pw(models.Model):
    pw_id = models.CharField(max_length=10, blank=True, null=True)
    pw_quote_n = models.CharField(max_length=15, blank=True, null=True)
    pw_index = models.IntegerField(blank=True, null=True)
    pw_dia1 = models.FloatField(blank=True, null=True)
    pw_dia2 = models.FloatField(blank=True, null=True)
    pw_length = models.FloatField(blank=True, null=True)
    pw_shape = models.CharField(max_length=10, blank=True, null=True)
    pw_vol = models.FloatField(blank=True, null=True)
    pw_type = models.IntegerField(blank=True, null=True)
    pw_order_n = models.CharField(max_length=12, blank=True, null=True)
    pw_qi_item = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pw'


class PyDctns(models.Model):
    dc_id = models.CharField(max_length=10, blank=True, null=True)
    dc_code = models.CharField(max_length=10, blank=True, null=True)
    dc_type = models.CharField(max_length=1, blank=True, null=True)
    dc_desc = models.CharField(max_length=35, blank=True, null=True)
    dc_name = models.CharField(max_length=35, blank=True, null=True)
    dc_address = models.CharField(max_length=35, blank=True, null=True)
    dc_addres2 = models.CharField(max_length=35, blank=True, null=True)
    dc_addres3 = models.CharField(max_length=35, blank=True, null=True)
    dc_id_no = models.CharField(max_length=15, blank=True, null=True)
    dc_e_type = models.CharField(max_length=1, blank=True, null=True)
    dc_e_rate = models.FloatField(blank=True, null=True)
    dc_r_type = models.CharField(max_length=1, blank=True, null=True)
    dc_r_rate = models.FloatField(blank=True, null=True)
    dc_pay_gl_field = models.CharField(db_column='dc_pay_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    dc_fed = models.NullBooleanField()
    dc_fica = models.NullBooleanField()
    dc_med = models.NullBooleanField()
    dc_futa = models.NullBooleanField()
    dc_empec = models.FloatField(blank=True, null=True)
    dc_exp_gl_field = models.CharField(db_column='dc_exp_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    dc_emprc = models.FloatField(blank=True, null=True)
    dc_after_b = models.IntegerField(blank=True, null=True)
    dc_frequen = models.CharField(max_length=1, blank=True, null=True)
    dc_suta = models.NullBooleanField()
    dc_sit = models.NullBooleanField()
    dc_lit1 = models.NullBooleanField()
    dc_lit2 = models.NullBooleanField()
    dc_w2_box = models.NullBooleanField()
    dc_w2_box_field = models.CharField(db_column='dc_w2_box_', max_length=2, blank=True, null=True)  # Field renamed because it ended with '_'.
    dc_e_amoun = models.FloatField(blank=True, null=True)
    dc_r_amoun = models.FloatField(blank=True, null=True)
    dc_e_date = models.DateField(blank=True, null=True)
    dc_beg_dat = models.DateField(blank=True, null=True)
    dc_beg_bal = models.FloatField(blank=True, null=True)
    dc_w2_box2 = models.NullBooleanField()
    dc_round_d = models.NullBooleanField()
    dc_e_rate_field = models.FloatField(db_column='dc_e_rate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    dc_r_rate_field = models.FloatField(db_column='dc_r_rate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    dc_e_max_p = models.NullBooleanField()
    dc_r_max_p = models.NullBooleanField()
    dc_taxable = models.NullBooleanField()
    dc_e_calc = models.CharField(max_length=1, blank=True, null=True)
    dc_r_calc = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_dctns'


class PyEldep(models.Model):
    el_id = models.CharField(max_length=10, blank=True, null=True)
    el_im_dest = models.CharField(max_length=10, blank=True, null=True)
    el_im_orig = models.CharField(max_length=10, blank=True, null=True)
    el_im_des2 = models.CharField(max_length=23, blank=True, null=True)
    el_im_ori2 = models.CharField(max_length=23, blank=True, null=True)
    el_ref_cod = models.CharField(max_length=8, blank=True, null=True)
    el_file_da = models.CharField(max_length=6, blank=True, null=True)
    el_file_ti = models.CharField(max_length=4, blank=True, null=True)
    el_prior_c = models.CharField(max_length=2, blank=True, null=True)
    el_file_id = models.CharField(max_length=1, blank=True, null=True)
    el_record_field = models.CharField(db_column='el_record_', max_length=3, blank=True, null=True)  # Field renamed because it ended with '_'.
    el_block_f = models.CharField(max_length=2, blank=True, null=True)
    el_format_field = models.CharField(db_column='el_format_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    el_ser_cla = models.CharField(max_length=3, blank=True, null=True)
    el_comp_na = models.CharField(max_length=36, blank=True, null=True)
    el_comp_id = models.CharField(max_length=10, blank=True, null=True)
    el_ent_cla = models.CharField(max_length=3, blank=True, null=True)
    el_comp_en = models.CharField(max_length=10, blank=True, null=True)
    el_comp_de = models.CharField(max_length=6, blank=True, null=True)
    el_comp_ef = models.CharField(max_length=6, blank=True, null=True)
    el_julian_field = models.CharField(db_column='el_julian_', max_length=3, blank=True, null=True)  # Field renamed because it ended with '_'.
    el_orig_st = models.CharField(max_length=1, blank=True, null=True)
    el_orig_df = models.CharField(max_length=8, blank=True, null=True)
    el_batch_n = models.CharField(max_length=7, blank=True, null=True)
    el_login_s = models.CharField(max_length=80, blank=True, null=True)
    el_balance = models.NullBooleanField()
    el_trans_c = models.CharField(max_length=2, blank=True, null=True)
    el_routing = models.CharField(max_length=9, blank=True, null=True)
    el_account = models.CharField(max_length=17, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_eldep'


class PyEmdad(models.Model):
    dd_id = models.CharField(max_length=10, blank=True, null=True)
    dd_da_id = models.CharField(max_length=10, blank=True, null=True)
    dd_occurs = models.IntegerField(blank=True, null=True)
    dd_desc = models.CharField(max_length=30, blank=True, null=True)
    dd_inactiv = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'py_emdad'


class PyEmdas(models.Model):
    da_id = models.CharField(max_length=10, blank=True, null=True)
    da_desc = models.CharField(max_length=30, blank=True, null=True)
    da_freq = models.CharField(max_length=1, blank=True, null=True)
    da_inactiv = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'py_emdas'


class PyEmhrd(models.Model):
    hd_id = models.CharField(max_length=10, blank=True, null=True)
    hd_emp_id = models.CharField(max_length=5, blank=True, null=True)
    hd_da_id = models.CharField(max_length=10, blank=True, null=True)
    hd_dd_id = models.CharField(max_length=10, blank=True, null=True)
    hd_date = models.DateField(blank=True, null=True)
    hd_occurs = models.IntegerField(blank=True, null=True)
    hd_notes = models.TextField(blank=True, null=True)
    hd_emp_id_field = models.CharField(db_column='hd_emp_id_', max_length=5, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'py_emhrd'


class PyEmhrp(models.Model):
    hp_id = models.CharField(max_length=10, blank=True, null=True)
    hp_hr_id = models.CharField(max_length=10, blank=True, null=True)
    hp_pd_id = models.CharField(max_length=10, blank=True, null=True)
    hp_order = models.IntegerField(blank=True, null=True)
    hp_evaluat = models.IntegerField(blank=True, null=True)
    hp_notes = models.TextField(blank=True, null=True)
    hp_emp_id = models.CharField(max_length=5, blank=True, null=True)
    hp_weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_emhrp'


class PyEmpdc(models.Model):
    ed_id = models.CharField(max_length=10, blank=True, null=True)
    ed_emp_id = models.CharField(max_length=5, blank=True, null=True)
    ed_dc_id = models.CharField(max_length=10, blank=True, null=True)
    ed_dc_e_ty = models.CharField(max_length=1, blank=True, null=True)
    ed_dc_e_ra = models.FloatField(blank=True, null=True)
    ed_dc_r_ty = models.CharField(max_length=1, blank=True, null=True)
    ed_dc_r_ra = models.FloatField(blank=True, null=True)
    ed_dc_empr = models.FloatField(blank=True, null=True)
    ed_dc_empe = models.FloatField(blank=True, null=True)
    ed_overrid = models.NullBooleanField()
    ed_suta = models.NullBooleanField()
    ed_sit = models.NullBooleanField()
    ed_lit1 = models.NullBooleanField()
    ed_lit2 = models.NullBooleanField()
    ed_dc_e_am = models.FloatField(blank=True, null=True)
    ed_dc_r_am = models.FloatField(blank=True, null=True)
    ed_dc_e_da = models.DateField(blank=True, null=True)
    ed_pay_gl_field = models.CharField(db_column='ed_pay_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ed_exp_gl_field = models.CharField(db_column='ed_exp_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    ed_dc_e_r2 = models.FloatField(blank=True, null=True)
    ed_dc_r_r2 = models.FloatField(blank=True, null=True)
    ed_dc_e_ma = models.NullBooleanField()
    ed_dc_r_ma = models.NullBooleanField()
    ed_sot = models.NullBooleanField()
    ed_dc_e_ca = models.CharField(max_length=1, blank=True, null=True)
    ed_dc_r_ca = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_empdc'


class PyEmpos(models.Model):
    ps_id = models.CharField(max_length=10, blank=True, null=True)
    ps_desc = models.CharField(max_length=30, blank=True, null=True)
    ps_freq = models.CharField(max_length=1, blank=True, null=True)
    ps_inactiv = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'py_empos'


class PyEmpri(models.Model):
    ei_id = models.CharField(max_length=10, blank=True, null=True)
    ei_emp_id = models.CharField(max_length=5, blank=True, null=True)
    ei_gl_num = models.CharField(max_length=12, blank=True, null=True)
    ei_type = models.CharField(max_length=1, blank=True, null=True)
    ei_code = models.CharField(max_length=10, blank=True, null=True)
    ei_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_empri'


class PyEmprt(models.Model):
    er_id = models.CharField(max_length=10, blank=True, null=True)
    er_emp_id = models.CharField(max_length=5, blank=True, null=True)
    er_pr_id = models.CharField(max_length=10, blank=True, null=True)
    er_rate_re = models.FloatField(blank=True, null=True)
    er_rate_ot = models.FloatField(blank=True, null=True)
    er_rate_do = models.FloatField(blank=True, null=True)
    er_hour_re = models.FloatField(blank=True, null=True)
    er_hour_ot = models.FloatField(blank=True, null=True)
    er_hour_do = models.FloatField(blank=True, null=True)
    er_overrid = models.NullBooleanField()
    er_ex_hour = models.NullBooleanField()
    er_reg_gl_field = models.CharField(db_column='er_reg_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    er_ot_gl_n = models.CharField(max_length=12, blank=True, null=True)
    er_dot_gl_field = models.CharField(db_column='er_dot_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    er_delete = models.NullBooleanField()
    er_vac_gl_field = models.CharField(db_column='er_vac_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    er_pto_gl_field = models.CharField(db_column='er_pto_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    er_hol_gl_field = models.CharField(db_column='er_hol_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    er_suta = models.NullBooleanField()
    er_sit = models.NullBooleanField()
    er_sot = models.NullBooleanField()
    er_lit1 = models.NullBooleanField()
    er_lit2 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'py_emprt'


class PyEmptx(models.Model):
    et_id = models.CharField(max_length=10, blank=True, null=True)
    et_emp_id = models.CharField(max_length=5, blank=True, null=True)
    et_tx_id = models.CharField(max_length=10, blank=True, null=True)
    et_ts_id = models.CharField(max_length=10, blank=True, null=True)
    et_ts_type = models.CharField(max_length=1, blank=True, null=True)
    et_tax_py_field = models.CharField(db_column='et_tax_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    et_tax_ex_field = models.CharField(db_column='et_tax_ex_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    et_exempti = models.IntegerField(blank=True, null=True)
    et_depende = models.IntegerField(blank=True, null=True)
    et_ad_tax_field = models.FloatField(db_column='et_ad_tax_', blank=True, null=True)  # Field renamed because it ended with '_'.
    et_ad_tax2 = models.CharField(max_length=1, blank=True, null=True)
    et_ad_tax3 = models.NullBooleanField()
    et_or_tax = models.NullBooleanField()
    et_or_emp = models.NullBooleanField()
    et_superce = models.NullBooleanField()
    et_ns_type = models.CharField(max_length=1, blank=True, null=True)
    et_ns_amt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_emptx'


class PyEthnc(models.Model):
    pe_code = models.CharField(max_length=6, blank=True, null=True)
    pe_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_ethnc'


class PyFedtx(models.Model):
    ft_date = models.DateField(blank=True, null=True)
    ft_taxes = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_fedtx'


class PyLclty(models.Model):
    lc_id = models.CharField(max_length=10, blank=True, null=True)
    lc_st_id = models.CharField(max_length=2, blank=True, null=True)
    lc_name = models.CharField(max_length=25, blank=True, null=True)
    lc_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_lclty'


class PyRegdc(models.Model):
    rd_id = models.CharField(max_length=10, blank=True, null=True)
    rd_rg_id = models.CharField(max_length=10, blank=True, null=True)
    rd_dc_id = models.CharField(max_length=10, blank=True, null=True)
    rd_e_type = models.CharField(max_length=1, blank=True, null=True)
    rd_r_type = models.CharField(max_length=1, blank=True, null=True)
    rd_e_rate = models.FloatField(blank=True, null=True)
    rd_r_rate = models.FloatField(blank=True, null=True)
    rd_suta = models.NullBooleanField()
    rd_sit = models.NullBooleanField()
    rd_lit1 = models.NullBooleanField()
    rd_lit2 = models.NullBooleanField()
    rd_pay_gl_field = models.CharField(db_column='rd_pay_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rd_exp_gl_field = models.CharField(db_column='rd_exp_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rd_e_amoun = models.FloatField(blank=True, null=True)
    rd_r_amoun = models.FloatField(blank=True, null=True)
    rd_e_max_a = models.FloatField(blank=True, null=True)
    rd_r_max_a = models.FloatField(blank=True, null=True)
    rd_fit = models.NullBooleanField()
    rd_mc = models.NullBooleanField()
    rd_fica = models.NullBooleanField()
    rd_futa = models.NullBooleanField()
    rd_before_field = models.IntegerField(db_column='rd_before_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rd_or_calc = models.NullBooleanField()
    rd_e_deduc = models.FloatField(blank=True, null=True)
    rd_r_deduc = models.FloatField(blank=True, null=True)
    rd_e_date = models.DateField(blank=True, null=True)
    rd_e_rate_field = models.FloatField(db_column='rd_e_rate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rd_r_rate_field = models.FloatField(db_column='rd_r_rate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rd_e_max_p = models.NullBooleanField()
    rd_r_max_p = models.NullBooleanField()
    rd_sot = models.NullBooleanField()
    rd_e_calc = models.CharField(max_length=1, blank=True, null=True)
    rd_r_calc = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_regdc'


class PyRegri(models.Model):
    ri_id = models.CharField(max_length=10, blank=True, null=True)
    ri_rg_id = models.CharField(max_length=10, blank=True, null=True)
    ri_gl_num = models.CharField(max_length=12, blank=True, null=True)
    ri_type = models.CharField(max_length=1, blank=True, null=True)
    ri_code = models.CharField(max_length=10, blank=True, null=True)
    ri_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_regri'


class PyRegrt(models.Model):
    rr_id = models.CharField(max_length=10, blank=True, null=True)
    rr_rg_id = models.CharField(max_length=10, blank=True, null=True)
    rr_pr_id = models.CharField(max_length=10, blank=True, null=True)
    rr_rate_re = models.FloatField(blank=True, null=True)
    rr_rate_ot = models.FloatField(blank=True, null=True)
    rr_rate_do = models.FloatField(blank=True, null=True)
    rr_hour_re = models.FloatField(blank=True, null=True)
    rr_hour_ot = models.FloatField(blank=True, null=True)
    rr_hour_do = models.FloatField(blank=True, null=True)
    rr_reg_gl_field = models.CharField(db_column='rr_reg_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rr_ot_gl_n = models.CharField(max_length=12, blank=True, null=True)
    rr_dot_gl_field = models.CharField(db_column='rr_dot_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rr_type = models.CharField(max_length=1, blank=True, null=True)
    rr_vac_gl_field = models.CharField(db_column='rr_vac_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rr_pto_gl_field = models.CharField(db_column='rr_pto_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rr_hol_gl_field = models.CharField(db_column='rr_hol_gl_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rr_hour_va = models.FloatField(blank=True, null=True)
    rr_hour_pt = models.FloatField(blank=True, null=True)
    rr_hour_ho = models.FloatField(blank=True, null=True)
    rr_amt_reg = models.FloatField(blank=True, null=True)
    rr_amt_ot = models.FloatField(blank=True, null=True)
    rr_amt_dot = models.FloatField(blank=True, null=True)
    rr_amt_vac = models.FloatField(blank=True, null=True)
    rr_amt_pto = models.FloatField(blank=True, null=True)
    rr_amt_hol = models.FloatField(blank=True, null=True)
    rr_amt_tot = models.FloatField(blank=True, null=True)
    rr_hour_to = models.FloatField(blank=True, null=True)
    rr_or_calc = models.NullBooleanField()
    rr_ex_hour = models.NullBooleanField()
    rr_amt_wc = models.FloatField(blank=True, null=True)
    rr_st_id = models.CharField(max_length=2, blank=True, null=True)
    rr_lc_id = models.CharField(max_length=10, blank=True, null=True)
    rr_de_id = models.CharField(max_length=2, blank=True, null=True)
    rr_jc_id = models.CharField(max_length=10, blank=True, null=True)
    rr_id_code = models.CharField(max_length=10, blank=True, null=True)
    rr_order_n = models.CharField(max_length=12, blank=True, null=True)
    rr_tax_non = models.IntegerField(blank=True, null=True)
    rr_fit = models.NullBooleanField()
    rr_fica = models.NullBooleanField()
    rr_mc = models.NullBooleanField()
    rr_futa = models.NullBooleanField()
    rr_suta = models.NullBooleanField()
    rr_sit = models.NullBooleanField()
    rr_sot = models.NullBooleanField()
    rr_lit1 = models.NullBooleanField()
    rr_lit2 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'py_regrt'


class PyRegtx(models.Model):
    rt_id = models.CharField(max_length=10, blank=True, null=True)
    rt_rg_id = models.CharField(max_length=10, blank=True, null=True)
    rt_tx_id = models.CharField(max_length=10, blank=True, null=True)
    rt_ts_id = models.CharField(max_length=10, blank=True, null=True)
    rt_or_calc = models.NullBooleanField()
    rt_tax_py_field = models.CharField(db_column='rt_tax_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rt_tax_ex_field = models.CharField(db_column='rt_tax_ex_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rt_ee_ti_a = models.FloatField(blank=True, null=True)
    rt_ee_ri_a = models.FloatField(blank=True, null=True)
    rt_ee_tax_field = models.FloatField(db_column='rt_ee_tax_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rt_er_ti_a = models.FloatField(blank=True, null=True)
    rt_er_ri_a = models.FloatField(blank=True, null=True)
    rt_er_tax_field = models.FloatField(db_column='rt_er_tax_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rt_not_cal = models.NullBooleanField()
    rt_ts_type = models.CharField(max_length=1, blank=True, null=True)
    rt_exempti = models.IntegerField(blank=True, null=True)
    rt_depende = models.IntegerField(blank=True, null=True)
    rt_ad_tax_field = models.FloatField(db_column='rt_ad_tax_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rt_ad_tax2 = models.CharField(max_length=1, blank=True, null=True)
    rt_ad_tax3 = models.NullBooleanField()
    rt_or_tax = models.NullBooleanField()
    rt_or_emp = models.NullBooleanField()
    rt_superce = models.NullBooleanField()
    rt_ns_type = models.CharField(max_length=1, blank=True, null=True)
    rt_ns_amt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_regtx'


class PyRgstr(models.Model):
    rg_id = models.CharField(max_length=10, blank=True, null=True)
    rg_number = models.IntegerField(blank=True, null=True)
    rg_type = models.CharField(max_length=1, blank=True, null=True)
    rg_emp_id = models.CharField(max_length=5, blank=True, null=True)
    rg_tax_id = models.CharField(max_length=10, blank=True, null=True)
    rg_begin_d = models.DateField(blank=True, null=True)
    rg_end_dat = models.DateField(blank=True, null=True)
    rg_entry_d = models.DateField(blank=True, null=True)
    rg_referen = models.CharField(max_length=35, blank=True, null=True)
    rg_payee = models.CharField(max_length=35, blank=True, null=True)
    rg_address = models.TextField(blank=True, null=True)
    rg_pay_typ = models.CharField(max_length=1, blank=True, null=True)
    rg_pay_fre = models.CharField(max_length=1, blank=True, null=True)
    rg_use_tca = models.NullBooleanField()
    rg_filing_field = models.CharField(db_column='rg_filing_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_filing2 = models.CharField(max_length=1, blank=True, null=True)
    rg_filing3 = models.CharField(max_length=1, blank=True, null=True)
    rg_filing4 = models.CharField(max_length=1, blank=True, null=True)
    rg_exempts = models.IntegerField(blank=True, null=True)
    rg_exempt2 = models.IntegerField(blank=True, null=True)
    rg_exempt3 = models.IntegerField(blank=True, null=True)
    rg_exempt4 = models.IntegerField(blank=True, null=True)
    rg_as_fica = models.NullBooleanField()
    rg_as_medi = models.NullBooleanField()
    rg_as_futa = models.NullBooleanField()
    rg_as_suta = models.NullBooleanField()
    rg_st_id_s = models.CharField(max_length=2, blank=True, null=True)
    rg_st_id_l = models.CharField(max_length=2, blank=True, null=True)
    rg_st_id_2 = models.CharField(max_length=2, blank=True, null=True)
    rg_tx_id_f = models.CharField(max_length=10, blank=True, null=True)
    rg_tx_id_2 = models.CharField(max_length=10, blank=True, null=True)
    rg_tx_id_m = models.CharField(max_length=10, blank=True, null=True)
    rg_tx_id_3 = models.CharField(max_length=10, blank=True, null=True)
    rg_tx_id_s = models.CharField(max_length=10, blank=True, null=True)
    rg_tx_id_4 = models.CharField(max_length=10, blank=True, null=True)
    rg_tx_id_5 = models.CharField(max_length=10, blank=True, null=True)
    rg_tt_id_s = models.CharField(max_length=10, blank=True, null=True)
    rg_tx_id_l = models.CharField(max_length=10, blank=True, null=True)
    rg_tx_id_6 = models.CharField(max_length=10, blank=True, null=True)
    rg_ad_tax_field = models.FloatField(db_column='rg_ad_tax_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_ad_tax2 = models.FloatField(blank=True, null=True)
    rg_ad_tax3 = models.FloatField(blank=True, null=True)
    rg_ad_tax4 = models.FloatField(blank=True, null=True)
    rg_vac_bas = models.CharField(max_length=1, blank=True, null=True)
    rg_vac_acc = models.CharField(max_length=1, blank=True, null=True)
    rg_vac_ann = models.FloatField(blank=True, null=True)
    rg_vac_ava = models.FloatField(blank=True, null=True)
    rg_vac_ac2 = models.FloatField(blank=True, null=True)
    rg_vac_use = models.FloatField(blank=True, null=True)
    rg_vac_rem = models.FloatField(blank=True, null=True)
    rg_pto_bas = models.CharField(max_length=1, blank=True, null=True)
    rg_pto_acc = models.CharField(max_length=1, blank=True, null=True)
    rg_pto_ann = models.FloatField(blank=True, null=True)
    rg_pto_ava = models.FloatField(blank=True, null=True)
    rg_pto_ac2 = models.FloatField(blank=True, null=True)
    rg_pto_use = models.FloatField(blank=True, null=True)
    rg_pto_rem = models.FloatField(blank=True, null=True)
    rg_slry_ho = models.FloatField(blank=True, null=True)
    rg_reg_hou = models.FloatField(blank=True, null=True)
    rg_ot_hour = models.FloatField(blank=True, null=True)
    rg_dot_hou = models.FloatField(blank=True, null=True)
    rg_vac_hou = models.FloatField(blank=True, null=True)
    rg_pto_hou = models.FloatField(blank=True, null=True)
    rg_hol_hou = models.FloatField(blank=True, null=True)
    rg_other_h = models.FloatField(blank=True, null=True)
    rg_total_h = models.FloatField(blank=True, null=True)
    rg_slry_am = models.FloatField(blank=True, null=True)
    rg_reg_amt = models.FloatField(blank=True, null=True)
    rg_ot_amt = models.FloatField(blank=True, null=True)
    rg_dot_amt = models.FloatField(blank=True, null=True)
    rg_vac_amt = models.FloatField(blank=True, null=True)
    rg_pto_amt = models.FloatField(blank=True, null=True)
    rg_hol_amt = models.FloatField(blank=True, null=True)
    rg_other_a = models.FloatField(blank=True, null=True)
    rg_gross_a = models.FloatField(blank=True, null=True)
    rg_ee_fit_field = models.FloatField(db_column='rg_ee_fit_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_ee_fica = models.FloatField(blank=True, null=True)
    rg_ee_mc_a = models.FloatField(blank=True, null=True)
    rg_ee_sit_field = models.FloatField(db_column='rg_ee_sit_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_ee_lit1 = models.FloatField(blank=True, null=True)
    rg_ee_lit2 = models.FloatField(blank=True, null=True)
    rg_ee_ded_field = models.FloatField(db_column='rg_ee_ded_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_ded_tot = models.FloatField(blank=True, null=True)
    rg_net_pay = models.FloatField(blank=True, null=True)
    rg_sub_pay = models.FloatField(blank=True, null=True)
    rg_reimb_a = models.FloatField(blank=True, null=True)
    rg_check_a = models.FloatField(blank=True, null=True)
    rg_er_fica = models.FloatField(blank=True, null=True)
    rg_er_mc_a = models.FloatField(blank=True, null=True)
    rg_er_futa = models.FloatField(blank=True, null=True)
    rg_er_suta = models.FloatField(blank=True, null=True)
    rg_er_sii_field = models.FloatField(db_column='rg_er_sii_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_er_sit_field = models.FloatField(db_column='rg_er_sit_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_er_lit1 = models.FloatField(blank=True, null=True)
    rg_er_lit2 = models.FloatField(blank=True, null=True)
    rg_er_ded_field = models.FloatField(db_column='rg_er_ded_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_er_tot_field = models.FloatField(db_column='rg_er_tot_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_ee_fit2 = models.FloatField(blank=True, null=True)
    rg_ee_fic2 = models.FloatField(blank=True, null=True)
    rg_ee_mc_t = models.FloatField(blank=True, null=True)
    rg_ee_sit2 = models.FloatField(blank=True, null=True)
    rg_ee_lit3 = models.FloatField(blank=True, null=True)
    rg_ee_lit4 = models.FloatField(blank=True, null=True)
    rg_er_fic2 = models.FloatField(blank=True, null=True)
    rg_er_mc_t = models.FloatField(blank=True, null=True)
    rg_er_fut2 = models.FloatField(blank=True, null=True)
    rg_er_sut2 = models.FloatField(blank=True, null=True)
    rg_er_sii2 = models.FloatField(blank=True, null=True)
    rg_er_sit2 = models.FloatField(blank=True, null=True)
    rg_er_lit3 = models.FloatField(blank=True, null=True)
    rg_er_lit4 = models.FloatField(blank=True, null=True)
    rg_fit_py_field = models.CharField(db_column='rg_fit_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_fica_py = models.CharField(max_length=12, blank=True, null=True)
    rg_fica_ex = models.CharField(max_length=12, blank=True, null=True)
    rg_mc_py_g = models.CharField(max_length=12, blank=True, null=True)
    rg_mc_ex_g = models.CharField(max_length=12, blank=True, null=True)
    rg_futa_py = models.CharField(max_length=12, blank=True, null=True)
    rg_futa_ex = models.CharField(max_length=12, blank=True, null=True)
    rg_suta_py = models.CharField(max_length=12, blank=True, null=True)
    rg_suta_ex = models.CharField(max_length=12, blank=True, null=True)
    rg_sii_py_field = models.CharField(db_column='rg_sii_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_sii_ex_field = models.CharField(db_column='rg_sii_ex_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_sit_py_field = models.CharField(db_column='rg_sit_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_sit_ex_field = models.CharField(db_column='rg_sit_ex_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_lit1_py = models.CharField(max_length=12, blank=True, null=True)
    rg_lit1_ex = models.CharField(max_length=12, blank=True, null=True)
    rg_lit2_py = models.CharField(max_length=12, blank=True, null=True)
    rg_lit2_ex = models.CharField(max_length=12, blank=True, null=True)
    rg_mn_id = models.CharField(max_length=10, blank=True, null=True)
    rg_or_calc = models.NullBooleanField()
    rg_or_vac_field = models.NullBooleanField(db_column='rg_or_vac_')  # Field renamed because it ended with '_'.
    rg_base_pa = models.FloatField(blank=True, null=True)
    rg_cknum = models.CharField(max_length=10, blank=True, null=True)
    rg_ckdate = models.DateField(blank=True, null=True)
    rg_electro = models.NullBooleanField()
    rg_ex_pay_field = models.NullBooleanField(db_column='rg_ex_pay_')  # Field renamed because it ended with '_'.
    rg_use_jca = models.NullBooleanField()
    rg_valid = models.NullBooleanField()
    rg_excepti = models.TextField(blank=True, null=True)
    rg_vac_esc = models.FloatField(blank=True, null=True)
    rg_pto_esc = models.FloatField(blank=True, null=True)
    rg_vac_adj = models.FloatField(blank=True, null=True)
    rg_pto_adj = models.FloatField(blank=True, null=True)
    rg_vac_beg = models.FloatField(blank=True, null=True)
    rg_pto_beg = models.FloatField(blank=True, null=True)
    rg_vac_us2 = models.FloatField(blank=True, null=True)
    rg_pto_us2 = models.FloatField(blank=True, null=True)
    rg_use_sca = models.NullBooleanField()
    rg_ad_calc = models.NullBooleanField()
    rg_ad_cal2 = models.NullBooleanField()
    rg_ad_cal3 = models.NullBooleanField()
    rg_ad_cal4 = models.NullBooleanField()
    rg_attend_field = models.FloatField(db_column='rg_attend_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_use_rca = models.NullBooleanField()
    rg_gain_sh = models.NullBooleanField()
    rg_tax_ove = models.NullBooleanField()
    rg_wc_amt = models.FloatField(blank=True, null=True)
    rg_ee_suta = models.FloatField(blank=True, null=True)
    rg_ee_sut2 = models.FloatField(blank=True, null=True)
    rg_ee_fit3 = models.FloatField(blank=True, null=True)
    rg_ee_fic3 = models.FloatField(blank=True, null=True)
    rg_ee_mc_r = models.FloatField(blank=True, null=True)
    rg_ee_sit3 = models.FloatField(blank=True, null=True)
    rg_ee_lit5 = models.FloatField(blank=True, null=True)
    rg_ee_lit6 = models.FloatField(blank=True, null=True)
    rg_er_fic3 = models.FloatField(blank=True, null=True)
    rg_er_mc_r = models.FloatField(blank=True, null=True)
    rg_er_fut3 = models.FloatField(blank=True, null=True)
    rg_er_sut3 = models.FloatField(blank=True, null=True)
    rg_er_sii3 = models.FloatField(blank=True, null=True)
    rg_er_sit3 = models.FloatField(blank=True, null=True)
    rg_er_lit5 = models.FloatField(blank=True, null=True)
    rg_er_lit6 = models.FloatField(blank=True, null=True)
    rg_ee_sut3 = models.FloatField(blank=True, null=True)
    rg_filing5 = models.CharField(max_length=1, blank=True, null=True)
    rg_eic_rc_field = models.CharField(db_column='rg_eic_rc_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_tx_id_e = models.CharField(max_length=10, blank=True, null=True)
    rg_er_eic_field = models.FloatField(db_column='rg_er_eic_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_er_eic2 = models.FloatField(blank=True, null=True)
    rg_er_eic3 = models.FloatField(blank=True, null=True)
    rg_check_m = models.CharField(max_length=30, blank=True, null=True)
    rg_as_soth = models.NullBooleanField()
    rg_tx_id_7 = models.CharField(max_length=10, blank=True, null=True)
    rg_ee_sot_field = models.FloatField(db_column='rg_ee_sot_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_er_sot_field = models.FloatField(db_column='rg_er_sot_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_ee_sot2 = models.FloatField(blank=True, null=True)
    rg_er_sot2 = models.FloatField(blank=True, null=True)
    rg_sot_py_field = models.CharField(db_column='rg_sot_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_sot_ex_field = models.CharField(db_column='rg_sot_ex_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_ee_sot3 = models.FloatField(blank=True, null=True)
    rg_er_sot3 = models.FloatField(blank=True, null=True)
    rg_filing6 = models.CharField(max_length=1, blank=True, null=True)
    rg_federal = models.NullBooleanField()
    rg_state_1 = models.NullBooleanField()
    rg_local_1 = models.NullBooleanField()
    rg_local_2 = models.NullBooleanField()
    rg_lc_id_l = models.CharField(max_length=10, blank=True, null=True)
    rg_lc_id_2 = models.CharField(max_length=10, blank=True, null=True)
    rg_as_loth = models.NullBooleanField()
    rg_as_lot2 = models.NullBooleanField()
    rg_lot1_py = models.CharField(max_length=12, blank=True, null=True)
    rg_lot1_ex = models.CharField(max_length=12, blank=True, null=True)
    rg_lot2_py = models.CharField(max_length=12, blank=True, null=True)
    rg_lot2_ex = models.CharField(max_length=12, blank=True, null=True)
    rg_ee_tax_field = models.FloatField(db_column='rg_ee_tax_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_er_tax_field = models.FloatField(db_column='rg_er_tax_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_srt_py_field = models.CharField(db_column='rg_srt_py_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_srt_ex_field = models.CharField(db_column='rg_srt_ex_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    rg_depends = models.IntegerField(blank=True, null=True)
    rg_edep_da = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_rgstr'


class PyT4Ts(models.Model):
    t4_id = models.CharField(max_length=10, blank=True, null=True)
    t4_type = models.CharField(max_length=1, blank=True, null=True)
    t4_emp_id = models.CharField(max_length=5, blank=True, null=True)
    t4_year = models.IntegerField(blank=True, null=True)
    t4_soc_ins = models.CharField(max_length=11, blank=True, null=True)
    t4_last_na = models.CharField(max_length=20, blank=True, null=True)
    t4_first_n = models.CharField(max_length=15, blank=True, null=True)
    t4_initial = models.CharField(max_length=2, blank=True, null=True)
    t4_name = models.CharField(max_length=40, blank=True, null=True)
    t4_address = models.CharField(max_length=40, blank=True, null=True)
    t4_addres2 = models.CharField(max_length=40, blank=True, null=True)
    t4_addres3 = models.CharField(max_length=40, blank=True, null=True)
    t4_emp_pro = models.CharField(max_length=2, blank=True, null=True)
    t4_emp_cod = models.CharField(max_length=2, blank=True, null=True)
    t4_void = models.NullBooleanField()
    t4_ex_cpp = models.NullBooleanField()
    t4_ex_ei = models.NullBooleanField()
    t4_ex_ppip = models.NullBooleanField()
    t4_tot_wag = models.FloatField(blank=True, null=True)
    t4_cit_wit = models.FloatField(blank=True, null=True)
    t4_cpp_wag = models.FloatField(blank=True, null=True)
    t4_cpp_wit = models.FloatField(blank=True, null=True)
    t4_ei_wage = models.FloatField(blank=True, null=True)
    t4_ei_with = models.FloatField(blank=True, null=True)
    t4_ppip_wa = models.FloatField(blank=True, null=True)
    t4_ppip_wi = models.FloatField(blank=True, null=True)
    t4_qpp_wit = models.FloatField(blank=True, null=True)
    t4_rpp_wit = models.FloatField(blank=True, null=True)
    t4_rpp_reg = models.CharField(max_length=15, blank=True, null=True)
    t4_box1_co = models.CharField(max_length=2, blank=True, null=True)
    t4_box1_am = models.FloatField(blank=True, null=True)
    t4_box2_co = models.CharField(max_length=2, blank=True, null=True)
    t4_box2_am = models.FloatField(blank=True, null=True)
    t4_box3_co = models.CharField(max_length=2, blank=True, null=True)
    t4_box3_am = models.FloatField(blank=True, null=True)
    t4_box4_co = models.CharField(max_length=2, blank=True, null=True)
    t4_box4_am = models.FloatField(blank=True, null=True)
    t4_box5_co = models.CharField(max_length=2, blank=True, null=True)
    t4_box5_am = models.FloatField(blank=True, null=True)
    t4_box6_co = models.CharField(max_length=2, blank=True, null=True)
    t4_box6_am = models.FloatField(blank=True, null=True)
    ts_bin = models.CharField(max_length=12, blank=True, null=True)
    ts_total_t = models.IntegerField(blank=True, null=True)
    t4_control = models.CharField(max_length=8, blank=True, null=True)
    t4_union_d = models.FloatField(blank=True, null=True)
    t4_donatio = models.FloatField(blank=True, null=True)
    t4_pension = models.FloatField(blank=True, null=True)
    ts_sin_1 = models.CharField(max_length=9, blank=True, null=True)
    ts_sin_2 = models.CharField(max_length=9, blank=True, null=True)
    ts_contact = models.CharField(max_length=30, blank=True, null=True)
    ts_phone_a = models.CharField(max_length=3, blank=True, null=True)
    ts_phone_1 = models.CharField(max_length=3, blank=True, null=True)
    ts_phone_2 = models.CharField(max_length=4, blank=True, null=True)
    ts_phone_e = models.CharField(max_length=4, blank=True, null=True)
    ts_cpp_wit = models.FloatField(blank=True, null=True)
    ts_ei_with = models.FloatField(blank=True, null=True)
    ts_deducti = models.FloatField(blank=True, null=True)
    ts_remitta = models.FloatField(blank=True, null=True)
    ts_differe = models.FloatField(blank=True, null=True)
    ts_overpay = models.FloatField(blank=True, null=True)
    ts_balance = models.FloatField(blank=True, null=True)
    ts_amt_enc = models.FloatField(blank=True, null=True)
    t4_alpha = models.CharField(max_length=40, blank=True, null=True)
    t4_probati = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'py_t4_ts'


class PyTaxes(models.Model):
    tx_id = models.CharField(max_length=10, blank=True, null=True)
    tx_code = models.CharField(max_length=10, blank=True, null=True)
    tx_type = models.CharField(max_length=1, blank=True, null=True)
    tx_desc = models.CharField(max_length=35, blank=True, null=True)
    tx_name = models.CharField(max_length=35, blank=True, null=True)
    tx_address = models.CharField(max_length=35, blank=True, null=True)
    tx_addres2 = models.CharField(max_length=35, blank=True, null=True)
    tx_addres3 = models.CharField(max_length=35, blank=True, null=True)
    tx_id_no = models.CharField(max_length=15, blank=True, null=True)
    tx_exemp_a = models.FloatField(blank=True, null=True)
    tx_tax_typ = models.CharField(max_length=1, blank=True, null=True)
    tx_e_rate = models.FloatField(blank=True, null=True)
    tx_calc_ty = models.CharField(max_length=1, blank=True, null=True)
    tx_level = models.CharField(max_length=1, blank=True, null=True)
    tx_e_max_t = models.FloatField(blank=True, null=True)
    tx_max_fre = models.CharField(max_length=1, blank=True, null=True)
    tx_state = models.CharField(max_length=2, blank=True, null=True)
    tx_gl_paya = models.CharField(max_length=12, blank=True, null=True)
    tx_gl_expe = models.CharField(max_length=12, blank=True, null=True)
    tx_r_rate = models.FloatField(blank=True, null=True)
    tx_cont_ty = models.CharField(max_length=1, blank=True, null=True)
    tx_r_max_t = models.FloatField(blank=True, null=True)
    tx_beg_dat = models.DateField(blank=True, null=True)
    tx_beg_bal = models.FloatField(blank=True, null=True)
    tx_round_d = models.NullBooleanField()
    tx_perc_em = models.NullBooleanField()
    tx_use_exe = models.NullBooleanField()
    tx_lc_id = models.CharField(max_length=10, blank=True, null=True)
    tx_r_rate_field = models.FloatField(db_column='tx_r_rate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    tx_use_min = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'py_taxes'


class PyTxtbl(models.Model):
    tt_id = models.CharField(max_length=10, blank=True, null=True)
    tt_tx_id = models.CharField(max_length=10, blank=True, null=True)
    tt_type = models.CharField(max_length=1, blank=True, null=True)
    tt_over = models.FloatField(blank=True, null=True)
    tt_not_ove = models.FloatField(blank=True, null=True)
    tt_tax_wit = models.FloatField(blank=True, null=True)
    tt_plus_pe = models.FloatField(blank=True, null=True)
    tt_code = models.CharField(max_length=10, blank=True, null=True)
    tt_desc = models.CharField(max_length=35, blank=True, null=True)
    tt_rate = models.FloatField(blank=True, null=True)
    tt_ts_id = models.CharField(max_length=10, blank=True, null=True)
    tt_pos = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_txtbl'


class PyVctns(models.Model):
    vs_id = models.CharField(max_length=10, blank=True, null=True)
    vs_over = models.IntegerField(blank=True, null=True)
    vs_not_ove = models.IntegerField(blank=True, null=True)
    vs_hours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_vctns'


class PyW2Ml(models.Model):
    ml_id = models.CharField(max_length=10, blank=True, null=True)
    ml_w2_id = models.CharField(max_length=10, blank=True, null=True)
    ml_st1_id = models.CharField(max_length=2, blank=True, null=True)
    ml_st1_no = models.CharField(max_length=15, blank=True, null=True)
    ml_st1_wag = models.FloatField(blank=True, null=True)
    ml_st1_wit = models.FloatField(blank=True, null=True)
    ml_st2_id = models.CharField(max_length=2, blank=True, null=True)
    ml_st2_no = models.CharField(max_length=15, blank=True, null=True)
    ml_st2_wag = models.FloatField(blank=True, null=True)
    ml_st2_wit = models.FloatField(blank=True, null=True)
    ml_lc1_nam = models.CharField(max_length=10, blank=True, null=True)
    ml_lc1_wag = models.FloatField(blank=True, null=True)
    ml_lc1_wit = models.FloatField(blank=True, null=True)
    ml_lc2_nam = models.CharField(max_length=10, blank=True, null=True)
    ml_lc2_wag = models.FloatField(blank=True, null=True)
    ml_lc2_wit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'py_w2_ml'


class PyW2W3(models.Model):
    w2_id = models.CharField(max_length=10, blank=True, null=True)
    w2_type = models.CharField(max_length=1, blank=True, null=True)
    w2_emp_id = models.CharField(max_length=5, blank=True, null=True)
    w2_year = models.IntegerField(blank=True, null=True)
    w2_control = models.CharField(max_length=8, blank=True, null=True)
    w2_soc_sec = models.CharField(max_length=20, blank=True, null=True)
    w2_name = models.CharField(max_length=40, blank=True, null=True)
    w2_address = models.CharField(max_length=40, blank=True, null=True)
    w2_addres2 = models.CharField(max_length=40, blank=True, null=True)
    w2_addres3 = models.CharField(max_length=40, blank=True, null=True)
    w2_tot_wag = models.FloatField(blank=True, null=True)
    w2_fit_wit = models.FloatField(blank=True, null=True)
    w2_ss_wage = models.FloatField(blank=True, null=True)
    w2_ss_with = models.FloatField(blank=True, null=True)
    w2_mc_wage = models.FloatField(blank=True, null=True)
    w2_mc_with = models.FloatField(blank=True, null=True)
    w2_ss_tips = models.FloatField(blank=True, null=True)
    w2_alloc_t = models.FloatField(blank=True, null=True)
    w2_advance = models.FloatField(blank=True, null=True)
    w2_dc_bene = models.FloatField(blank=True, null=True)
    w2_nq_plan = models.FloatField(blank=True, null=True)
    w2_b1_bene = models.FloatField(blank=True, null=True)
    w2_box_13 = models.TextField(blank=True, null=True)
    w2_box_oth = models.TextField(blank=True, null=True)
    w2_stat_em = models.NullBooleanField()
    w2_decease = models.NullBooleanField()
    w2_pension = models.NullBooleanField()
    w2_legal_r = models.NullBooleanField()
    w2_def_com = models.NullBooleanField()
    w2_st1_id = models.CharField(max_length=2, blank=True, null=True)
    w2_st1_no = models.CharField(max_length=15, blank=True, null=True)
    w2_st1_wag = models.FloatField(blank=True, null=True)
    w2_st1_wit = models.FloatField(blank=True, null=True)
    w2_st2_id = models.CharField(max_length=2, blank=True, null=True)
    w2_st2_no = models.CharField(max_length=15, blank=True, null=True)
    w2_st2_wag = models.FloatField(blank=True, null=True)
    w2_st2_wit = models.FloatField(blank=True, null=True)
    w2_lc1_nam = models.CharField(max_length=10, blank=True, null=True)
    w2_lc1_wag = models.FloatField(blank=True, null=True)
    w2_lc1_wit = models.FloatField(blank=True, null=True)
    w2_lc2_nam = models.CharField(max_length=10, blank=True, null=True)
    w2_lc2_wag = models.FloatField(blank=True, null=True)
    w2_lc2_wit = models.FloatField(blank=True, null=True)
    w2_void = models.NullBooleanField()
    w3_941 = models.NullBooleanField()
    w3_militar = models.NullBooleanField()
    w3_943 = models.NullBooleanField()
    w3_ct1 = models.NullBooleanField()
    w3_househo = models.NullBooleanField()
    w3_medicar = models.NullBooleanField()
    w3_establi = models.CharField(max_length=15, blank=True, null=True)
    w3_ein = models.CharField(max_length=20, blank=True, null=True)
    w3_ein_oth = models.CharField(max_length=20, blank=True, null=True)
    w3_tp_with = models.FloatField(blank=True, null=True)
    w3_contact = models.CharField(max_length=40, blank=True, null=True)
    w3_phone_a = models.CharField(max_length=3, blank=True, null=True)
    w3_phone = models.CharField(max_length=8, blank=True, null=True)
    w3_fax_ac = models.CharField(max_length=3, blank=True, null=True)
    w3_fax = models.CharField(max_length=8, blank=True, null=True)
    w3_email = models.CharField(max_length=50, blank=True, null=True)
    w3_total_w = models.IntegerField(blank=True, null=True)
    w2_alpha = models.CharField(max_length=40, blank=True, null=True)
    w2_3_rd_sic = models.NullBooleanField()
    w2_first_n = models.CharField(max_length=18, blank=True, null=True)
    w2_last_na = models.CharField(max_length=20, blank=True, null=True)
    w2_ma_code = models.CharField(max_length=2, blank=True, null=True)
    w2_ma_amou = models.FloatField(blank=True, null=True)
    w2_mb_code = models.CharField(max_length=2, blank=True, null=True)
    w2_mb_amou = models.FloatField(blank=True, null=True)
    w2_mc_code = models.CharField(max_length=2, blank=True, null=True)
    w2_mc_amou = models.FloatField(blank=True, null=True)
    w2_md_code = models.CharField(max_length=2, blank=True, null=True)
    w2_md_amou = models.FloatField(blank=True, null=True)
    w2_suffix_field = models.CharField(db_column='w2_suffix_', max_length=3, blank=True, null=True)  # Field renamed because it ended with '_'.
    w3_944 = models.NullBooleanField()
    w2_multipl = models.NullBooleanField()
    w2_hire_ex = models.FloatField(blank=True, null=True)
    w3_none_ap = models.NullBooleanField()
    w3_501_c_no = models.NullBooleanField()
    w3_501_c_n2 = models.NullBooleanField()
    w3_501_c_sl = models.NullBooleanField()
    w3_fed_gov = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'py_w2_w3'


class QCust(models.Model):
    cu_cust_co = models.CharField(max_length=6, blank=True, null=True)
    cu_cust_na = models.CharField(max_length=35, blank=True, null=True)
    cu_mail_ad = models.CharField(max_length=35, blank=True, null=True)
    cu_mail_a2 = models.CharField(max_length=35, blank=True, null=True)
    cu_mail_ci = models.CharField(max_length=30, blank=True, null=True)
    cu_mail_st = models.CharField(max_length=3, blank=True, null=True)
    cu_mail_cn = models.CharField(max_length=25, blank=True, null=True)
    cu_mail_zi = models.CharField(max_length=10, blank=True, null=True)
    cu_contact = models.CharField(max_length=25, blank=True, null=True)
    cu_cust_ph = models.CharField(max_length=14, blank=True, null=True)
    cu_cust_fa = models.CharField(max_length=14, blank=True, null=True)
    cu_cust_me = models.TextField(blank=True, null=True)
    cu_pay_ter = models.CharField(max_length=20, blank=True, null=True)
    cu_ship_vi = models.CharField(max_length=20, blank=True, null=True)
    cu_emp_id = models.CharField(max_length=5, blank=True, null=True)
    cu_commiss = models.FloatField(blank=True, null=True)
    cu_cust_ty = models.CharField(max_length=4, blank=True, null=True)
    cu_disc_co = models.CharField(max_length=6, blank=True, null=True)
    cu_ship_na = models.CharField(max_length=35, blank=True, null=True)
    cu_vend_co = models.CharField(max_length=20, blank=True, null=True)
    cu_tax = models.FloatField(blank=True, null=True)
    cu_status = models.CharField(max_length=1, blank=True, null=True)
    cu_bcp_po = models.CharField(max_length=5, blank=True, null=True)
    cu_bcp_qty = models.CharField(max_length=5, blank=True, null=True)
    cu_bcp_par = models.CharField(max_length=5, blank=True, null=True)
    cu_bcp_ven = models.CharField(max_length=5, blank=True, null=True)
    cu_gl_num = models.CharField(max_length=12, blank=True, null=True)
    cu_st_id_1 = models.CharField(max_length=10, blank=True, null=True)
    cu_st_id_2 = models.CharField(max_length=10, blank=True, null=True)
    cu_stax_id = models.CharField(max_length=25, blank=True, null=True)
    cu_login = models.CharField(max_length=8, blank=True, null=True)
    cu_pw = models.CharField(max_length=8, blank=True, null=True)
    cu_broadca = models.TextField(blank=True, null=True)
    cu_lview_s = models.NullBooleanField()
    cu_lview_2 = models.NullBooleanField()
    cu_lcreate = models.NullBooleanField()
    cu_lview_i = models.NullBooleanField()
    cu_ship_cn = models.IntegerField(blank=True, null=True)
    cu_vso_cnt = models.IntegerField(blank=True, null=True)
    cu_cso_cnt = models.IntegerField(blank=True, null=True)
    cu_vinv_cn = models.IntegerField(blank=True, null=True)
    cu_ship_da = models.DateField(blank=True, null=True)
    cu_vso_dat = models.DateField(blank=True, null=True)
    cu_cso_dat = models.DateField(blank=True, null=True)
    cu_vinv_da = models.DateField(blank=True, null=True)
    cu_bcp_inv = models.CharField(max_length=5, blank=True, null=True)
    cu_bcp_doc = models.CharField(max_length=5, blank=True, null=True)
    cu_fob = models.CharField(max_length=15, blank=True, null=True)
    cu_consign = models.IntegerField(blank=True, null=True)
    cu_consig2 = models.CharField(max_length=10, blank=True, null=True)
    cu_hold_il = models.CharField(max_length=10, blank=True, null=True)
    cu_bcp_ser = models.CharField(max_length=5, blank=True, null=True)
    cu_credit_field = models.FloatField(db_column='cu_credit_', blank=True, null=True)  # Field renamed because it ended with '_'.
    cu_credit2 = models.CharField(max_length=40, blank=True, null=True)
    cu_credit3 = models.NullBooleanField()
    cu_tax_exe = models.NullBooleanField()
    cu_exempt_field = models.CharField(db_column='cu_exempt_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    cu_website = models.CharField(max_length=60, blank=True, null=True)
    cu_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    cu_edi_thr = models.IntegerField(blank=True, null=True)
    cu_edi_id = models.CharField(max_length=20, blank=True, null=True)
    cu_label = models.IntegerField(blank=True, null=True)
    cu_spec_gr = models.CharField(max_length=20, blank=True, null=True)
    cu_ship_co = models.NullBooleanField()
    cu_packhol = models.NullBooleanField()
    cu_prod_co = models.CharField(max_length=2, blank=True, null=True)
    cu_cust_ex = models.CharField(max_length=5, blank=True, null=True)
    cu_bcp_uom = models.CharField(max_length=5, blank=True, null=True)
    cu_bcp_po_field = models.CharField(db_column='cu_bcp_po_', max_length=5, blank=True, null=True)  # Field renamed because it ended with '_'.
    cu_exc_so_field = models.NullBooleanField(db_column='cu_exc_so_')  # Field renamed because it ended with '_'.
    cu_beg_bal = models.DateField(blank=True, null=True)
    cu_beg_ba2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cu_so_pref = models.CharField(max_length=3, blank=True, null=True)
    cu_ship_wi = models.IntegerField(blank=True, null=True)
    cu_create_field = models.DateField(db_column='cu_create_', blank=True, null=True)  # Field renamed because it ended with '_'.
    cu_exp_dat = models.DateField(blank=True, null=True)
    cu_emp_id2 = models.CharField(max_length=5, blank=True, null=True)
    cu_salesta = models.IntegerField(blank=True, null=True)
    cu_lo_code = models.CharField(max_length=10, blank=True, null=True)
    cu_prospec = models.NullBooleanField()
    cu_mailcod = models.CharField(max_length=10, blank=True, null=True)
    cu_markup = models.FloatField(blank=True, null=True)
    cu_shipnot = models.TextField(blank=True, null=True)
    cu_vet_sup = models.CharField(max_length=6, blank=True, null=True)
    cu_st_excl = models.NullBooleanField()
    cu_st_no_f = models.NullBooleanField()
    cu_st_fc_r = models.FloatField(blank=True, null=True)
    cu_st_mo_d = models.IntegerField(blank=True, null=True)
    cu_st_date = models.DateField(blank=True, null=True)
    cu_st_amou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cu_prepay_field = models.IntegerField(db_column='cu_prepay_', blank=True, null=True)  # Field renamed because it ended with '_'.
    cu_enforce = models.NullBooleanField()
    cu_arnote = models.CharField(max_length=10, blank=True, null=True)
    cu_split_s = models.NullBooleanField()
    cu_bill_na = models.CharField(max_length=35, blank=True, null=True)
    cu_bill_ad = models.CharField(max_length=35, blank=True, null=True)
    cu_bill_a2 = models.CharField(max_length=35, blank=True, null=True)
    cu_bill_ci = models.CharField(max_length=30, blank=True, null=True)
    cu_bill_st = models.CharField(max_length=3, blank=True, null=True)
    cu_bill_zi = models.CharField(max_length=10, blank=True, null=True)
    cu_bill_cn = models.CharField(max_length=25, blank=True, null=True)
    cu_bill_ph = models.CharField(max_length=14, blank=True, null=True)
    cu_bill_ex = models.CharField(max_length=5, blank=True, null=True)
    cu_bill_fa = models.CharField(max_length=14, blank=True, null=True)
    cu_bill_co = models.CharField(max_length=25, blank=True, null=True)
    cu_inv_hdr = models.CharField(max_length=25, blank=True, null=True)
    cu_inv_hd2 = models.CharField(max_length=25, blank=True, null=True)
    cu_inv_hd3 = models.CharField(max_length=25, blank=True, null=True)
    cu_inv_hd4 = models.CharField(max_length=25, blank=True, null=True)
    cu_inv_hd5 = models.CharField(max_length=25, blank=True, null=True)
    cu_teritor = models.IntegerField(blank=True, null=True)
    cu_mail_a3 = models.CharField(max_length=35, blank=True, null=True)
    cu_bill_a3 = models.CharField(max_length=35, blank=True, null=True)
    cu_comm_pe = models.FloatField(blank=True, null=True)
    cu_prod_no = models.TextField(blank=True, null=True)
    cu_email_i = models.NullBooleanField()
    cu_email_2 = models.CharField(max_length=250, blank=True, null=True)
    cu_email_a = models.NullBooleanField()
    cu_email_3 = models.CharField(max_length=250, blank=True, null=True)
    cu_reg_rat = models.FloatField(blank=True, null=True)
    cu_ot_rate = models.FloatField(blank=True, null=True)
    cu_dot_rat = models.FloatField(blank=True, null=True)
    cu_foblabe = models.CharField(max_length=3, blank=True, null=True)
    cu_sco_att = models.CharField(max_length=30, blank=True, null=True)
    cu_price_e = models.CharField(max_length=5, blank=True, null=True)
    cu_price_2 = models.DateField(blank=True, null=True)
    cu_price_s = models.DateField(blank=True, null=True)
    cu_obsolet = models.NullBooleanField()
    cu_sepcofc = models.NullBooleanField()
    cu_distrib = models.CharField(max_length=10, blank=True, null=True)
    cu_gs_st = models.NullBooleanField()
    cu_no_over = models.NullBooleanField()
    cu_email_s = models.NullBooleanField()
    cu_email_4 = models.CharField(max_length=250, blank=True, null=True)
    cu_no_prin = models.NullBooleanField()
    cu_print_i = models.TextField(blank=True, null=True)
    cu_po_ln_o = models.NullBooleanField()
    cu_defcons = models.NullBooleanField()
    cu_late_al = models.IntegerField(blank=True, null=True)
    cu_collect = models.TextField(blank=True, null=True)
    cu_ex_coll = models.NullBooleanField()
    cu_cn_leve = models.IntegerField(blank=True, null=True)
    cu_excel_i = models.NullBooleanField()
    cu_excel_2 = models.NullBooleanField()
    cu_color = models.CharField(max_length=10, blank=True, null=True)
    cu_extaddr = models.TextField(blank=True, null=True)
    cu_barcode = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'q_cust'


class QCusta(models.Model):
    ca_cust_co = models.CharField(max_length=6, blank=True, null=True)
    ca_ship_ad = models.CharField(max_length=35, blank=True, null=True)
    ca_ship_a2 = models.CharField(max_length=35, blank=True, null=True)
    ca_ship_ci = models.CharField(max_length=30, blank=True, null=True)
    ca_ship_st = models.CharField(max_length=3, blank=True, null=True)
    ca_ship_cn = models.CharField(max_length=25, blank=True, null=True)
    ca_ship_zi = models.CharField(max_length=10, blank=True, null=True)
    ca_ship_na = models.CharField(max_length=35, blank=True, null=True)
    ca_default = models.NullBooleanField()
    ca_emp_id = models.CharField(max_length=5, blank=True, null=True)
    ca_st_id_1 = models.CharField(max_length=10, blank=True, null=True)
    ca_st_id_2 = models.CharField(max_length=10, blank=True, null=True)
    ca_stax_id = models.CharField(max_length=25, blank=True, null=True)
    ca_tax_exe = models.NullBooleanField()
    ca_exempt_field = models.CharField(db_column='ca_exempt_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    ca_type = models.CharField(max_length=10, blank=True, null=True)
    ca_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    ca_abbr_na = models.CharField(max_length=15, blank=True, null=True)
    ca_bol = models.NullBooleanField()
    ca_ship_a3 = models.CharField(max_length=35, blank=True, null=True)
    ca_id = models.CharField(max_length=10, blank=True, null=True)
    ca_transit = models.IntegerField(blank=True, null=True)
    ca_multi_p = models.NullBooleanField()
    ca_max_pal = models.IntegerField(blank=True, null=True)
    ca_edi_loc = models.CharField(max_length=2, blank=True, null=True)
    ca_edi_lo2 = models.CharField(max_length=5, blank=True, null=True)
    ca_box_cnt = models.IntegerField(blank=True, null=True)
    ca_master_field = models.IntegerField(db_column='ca_master_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ca_edi_ic_field = models.NullBooleanField(db_column='ca_edi_ic_')  # Field renamed because it ended with '_'.
    ca_edi_ic2 = models.CharField(max_length=2, blank=True, null=True)
    ca_edi_ic3 = models.CharField(max_length=5, blank=True, null=True)
    ca_contact = models.CharField(max_length=25, blank=True, null=True)
    ca_max_con = models.IntegerField(blank=True, null=True)
    ca_emp_id2 = models.CharField(max_length=5, blank=True, null=True)
    ca_proposa = models.NullBooleanField()
    ca_full_bo = models.NullBooleanField()
    ca_req_ps_field = models.NullBooleanField(db_column='ca_req_ps_')  # Field renamed because it ended with '_'.
    ca_2_d_barc = models.NullBooleanField()
    ca_notes = models.TextField(blank=True, null=True)
    ca_dock_co = models.CharField(max_length=5, blank=True, null=True)
    ca_comm_pe = models.FloatField(blank=True, null=True)
    ca_comm_p2 = models.FloatField(blank=True, null=True)
    ca_fob = models.CharField(max_length=15, blank=True, null=True)
    ca_billto = models.NullBooleanField()
    ca_phone = models.CharField(max_length=30, blank=True, null=True)
    ca_store = models.CharField(max_length=20, blank=True, null=True)
    ca_fax = models.CharField(max_length=30, blank=True, null=True)
    ca_foblabe = models.CharField(max_length=3, blank=True, null=True)
    ca_disc_co = models.CharField(max_length=6, blank=True, null=True)
    ca_dealer_field = models.CharField(db_column='ca_dealer_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'q_custa'


class QDraws(models.Model):
    qd_id = models.CharField(max_length=10, blank=True, null=True)
    qd_quote_n = models.CharField(max_length=15, blank=True, null=True)
    qd_number = models.CharField(max_length=15, blank=True, null=True)
    qd_revisio = models.CharField(max_length=3, blank=True, null=True)
    qd_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q_draws'


class QRevnos(models.Model):
    qn_id = models.CharField(max_length=10, blank=True, null=True)
    qn_qv_id = models.CharField(max_length=10, blank=True, null=True)
    qn_quote_n = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q_revnos'


class QRevs(models.Model):
    qv_id = models.CharField(max_length=10, blank=True, null=True)
    qv_quote_n = models.CharField(max_length=15, blank=True, null=True)
    qv_number = models.IntegerField(blank=True, null=True)
    qv_qr_code = models.CharField(max_length=6, blank=True, null=True)
    qv_sales_p = models.CharField(max_length=5, blank=True, null=True)
    qv_enter_b = models.CharField(max_length=5, blank=True, null=True)
    qv_enter_d = models.DateField(blank=True, null=True)
    qv_desc = models.TextField(blank=True, null=True)
    qv_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    qv_order_n = models.CharField(max_length=12, blank=True, null=True)
    qv_pr_id = models.IntegerField(blank=True, null=True)
    qv_po_num = models.CharField(max_length=7, blank=True, null=True)
    qv_sordq = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q_revs'


class QRsns(models.Model):
    qr_code = models.CharField(max_length=6, blank=True, null=True)
    qr_desc = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q_rsns'


class QbCoa(models.Model):
    qa_code = models.CharField(max_length=7, blank=True, null=True)
    qa_acct_na = models.CharField(max_length=31, blank=True, null=True)
    qa_acct_ty = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qb_coa'


class Qfreight(models.Model):
    qf_id = models.CharField(max_length=10, blank=True, null=True)
    qf_quote_n = models.CharField(max_length=15, blank=True, null=True)
    qf_fe_id = models.CharField(max_length=10, blank=True, null=True)
    qf_count = models.IntegerField(blank=True, null=True)
    qf_calc_fr = models.FloatField(blank=True, null=True)
    qf_calc_f2 = models.FloatField(blank=True, null=True)
    qf_calc_f3 = models.FloatField(blank=True, null=True)
    qf_calc_f4 = models.FloatField(blank=True, null=True)
    qf_calc_f5 = models.FloatField(blank=True, null=True)
    qf_calc_f6 = models.FloatField(blank=True, null=True)
    qf_calc_f7 = models.FloatField(blank=True, null=True)
    qf_calc_f8 = models.FloatField(blank=True, null=True)
    qf_calc_f9 = models.FloatField(blank=True, null=True)
    qf_calc_10 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qfreight'


class Qhist(models.Model):
    qh_id = models.CharField(max_length=10, blank=True, null=True)
    qh_quote_n = models.CharField(max_length=15, blank=True, null=True)
    qh_qq1 = models.IntegerField(blank=True, null=True)
    qh_qq2 = models.IntegerField(blank=True, null=True)
    qh_qq3 = models.IntegerField(blank=True, null=True)
    qh_qq4 = models.IntegerField(blank=True, null=True)
    qh_qq5 = models.IntegerField(blank=True, null=True)
    qh_qq6 = models.IntegerField(blank=True, null=True)
    qh_qq7 = models.IntegerField(blank=True, null=True)
    qh_qq8 = models.IntegerField(blank=True, null=True)
    qh_qq9 = models.IntegerField(blank=True, null=True)
    qh_qq10 = models.IntegerField(blank=True, null=True)
    qh_fcpu1 = models.FloatField(blank=True, null=True)
    qh_fcpu2 = models.FloatField(blank=True, null=True)
    qh_fcpu3 = models.FloatField(blank=True, null=True)
    qh_fcpu4 = models.FloatField(blank=True, null=True)
    qh_fcpu5 = models.FloatField(blank=True, null=True)
    qh_fcpu6 = models.FloatField(blank=True, null=True)
    qh_fcpu7 = models.FloatField(blank=True, null=True)
    qh_fcpu8 = models.FloatField(blank=True, null=True)
    qh_fcpu9 = models.FloatField(blank=True, null=True)
    qh_fcpu10 = models.FloatField(blank=True, null=True)
    qh_date = models.DateField(blank=True, null=True)
    qh_user_id = models.CharField(max_length=5, blank=True, null=True)
    qh_note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qhist'


class Qinv(models.Model):
    qi_quote_n = models.CharField(max_length=15, blank=True, null=True)
    qi_item = models.IntegerField(blank=True, null=True)
    qi_invent_field = models.CharField(db_column='qi_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    qi_width = models.FloatField(blank=True, null=True)
    qi_length = models.FloatField(blank=True, null=True)
    qi_quantit = models.FloatField(blank=True, null=True)
    qi_unit_co = models.FloatField(blank=True, null=True)
    qi_ext_cos = models.FloatField(blank=True, null=True)
    qi_uom = models.CharField(max_length=2, blank=True, null=True)
    qi_price = models.FloatField(blank=True, null=True)
    qi_op_num = models.IntegerField(blank=True, null=True)
    qi_markup = models.IntegerField(blank=True, null=True)
    qi_ppbar = models.FloatField(blank=True, null=True)
    qi_inv_cos = models.FloatField(blank=True, null=True)
    qi_desc = models.CharField(max_length=60, blank=True, null=True)
    qi_ext_des = models.TextField(blank=True, null=True)
    qi_stock_u = models.CharField(max_length=2, blank=True, null=True)
    qi_purch_u = models.CharField(max_length=2, blank=True, null=True)
    qi_qty1 = models.FloatField(blank=True, null=True)
    qi_qty2 = models.FloatField(blank=True, null=True)
    qi_qty3 = models.FloatField(blank=True, null=True)
    qi_qty4 = models.FloatField(blank=True, null=True)
    qi_qty5 = models.FloatField(blank=True, null=True)
    qi_qty6 = models.FloatField(blank=True, null=True)
    qi_qty7 = models.FloatField(blank=True, null=True)
    qi_qty8 = models.FloatField(blank=True, null=True)
    qi_qty9 = models.FloatField(blank=True, null=True)
    qi_qty10 = models.FloatField(blank=True, null=True)
    qi_unitcos = models.FloatField(blank=True, null=True)
    qi_unitco2 = models.FloatField(blank=True, null=True)
    qi_unitco3 = models.FloatField(blank=True, null=True)
    qi_unitco4 = models.FloatField(blank=True, null=True)
    qi_unitco5 = models.FloatField(blank=True, null=True)
    qi_unitco6 = models.FloatField(blank=True, null=True)
    qi_unitco7 = models.FloatField(blank=True, null=True)
    qi_unitco8 = models.FloatField(blank=True, null=True)
    qi_unitco9 = models.FloatField(blank=True, null=True)
    qi_unitc10 = models.FloatField(blank=True, null=True)
    qi_extcost = models.FloatField(blank=True, null=True)
    qi_extcos2 = models.FloatField(blank=True, null=True)
    qi_extcos3 = models.FloatField(blank=True, null=True)
    qi_extcos4 = models.FloatField(blank=True, null=True)
    qi_extcos5 = models.FloatField(blank=True, null=True)
    qi_extcos6 = models.FloatField(blank=True, null=True)
    qi_extcos7 = models.FloatField(blank=True, null=True)
    qi_extcos8 = models.FloatField(blank=True, null=True)
    qi_extcos9 = models.FloatField(blank=True, null=True)
    qi_extco10 = models.FloatField(blank=True, null=True)
    qi_totcost = models.FloatField(blank=True, null=True)
    qi_totcos2 = models.FloatField(blank=True, null=True)
    qi_totcos3 = models.FloatField(blank=True, null=True)
    qi_totcos4 = models.FloatField(blank=True, null=True)
    qi_totcos5 = models.FloatField(blank=True, null=True)
    qi_totcos6 = models.FloatField(blank=True, null=True)
    qi_totcos7 = models.FloatField(blank=True, null=True)
    qi_totcos8 = models.FloatField(blank=True, null=True)
    qi_totcos9 = models.FloatField(blank=True, null=True)
    qi_totco10 = models.FloatField(blank=True, null=True)
    qi_mu1 = models.IntegerField(blank=True, null=True)
    qi_mu2 = models.IntegerField(blank=True, null=True)
    qi_mu3 = models.IntegerField(blank=True, null=True)
    qi_mu4 = models.IntegerField(blank=True, null=True)
    qi_mu5 = models.IntegerField(blank=True, null=True)
    qi_mu6 = models.IntegerField(blank=True, null=True)
    qi_mu7 = models.IntegerField(blank=True, null=True)
    qi_mu8 = models.IntegerField(blank=True, null=True)
    qi_mu9 = models.IntegerField(blank=True, null=True)
    qi_mu10 = models.IntegerField(blank=True, null=True)
    qi_shape_c = models.CharField(max_length=7, blank=True, null=True)
    qi_diam_th = models.FloatField(blank=True, null=True)
    qi_mat_len = models.FloatField(blank=True, null=True)
    qi_mat_wid = models.FloatField(blank=True, null=True)
    qi_wgt_uni = models.FloatField(blank=True, null=True)
    qi_inv_non = models.IntegerField(blank=True, null=True)
    qi_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    qi_usesuom = models.NullBooleanField()
    qi_cut_off = models.FloatField(blank=True, null=True)
    qi_face_le = models.FloatField(blank=True, null=True)
    qi_fac_len = models.FloatField(blank=True, null=True)
    qi_tot_len = models.FloatField(blank=True, null=True)
    qi_act_siz = models.FloatField(blank=True, null=True)
    qi_tol_p = models.FloatField(blank=True, null=True)
    qi_tol_m = models.FloatField(blank=True, null=True)
    qi_wcut_of = models.FloatField(blank=True, null=True)
    qi_wface_l = models.FloatField(blank=True, null=True)
    qi_tot_wid = models.FloatField(blank=True, null=True)
    qi_wgtpp = models.FloatField(blank=True, null=True)
    qi_act_we_field = models.FloatField(db_column='qi_act_we_', blank=True, null=True)  # Field renamed because it ended with '_'.
    qi_perc_ma = models.IntegerField(blank=True, null=True)
    qi_tot_wei = models.FloatField(blank=True, null=True)
    qi_baruse_field = models.FloatField(db_column='qi_baruse_', blank=True, null=True)  # Field renamed because it ended with '_'.
    qi_msquare = models.FloatField(blank=True, null=True)
    qi_height = models.FloatField(blank=True, null=True)
    qi_psquare = models.FloatField(blank=True, null=True)
    qi_barend_field = models.FloatField(db_column='qi_barend_', blank=True, null=True)  # Field renamed because it ended with '_'.
    qi_bar_wei = models.FloatField(blank=True, null=True)
    qi_t_bar_w = models.FloatField(blank=True, null=True)
    qi_bar_per = models.FloatField(blank=True, null=True)
    qi_calc_ty = models.CharField(max_length=2, blank=True, null=True)
    qi_mat_lb1 = models.FloatField(blank=True, null=True)
    qi_mat_lb2 = models.FloatField(blank=True, null=True)
    qi_mat_lb3 = models.FloatField(blank=True, null=True)
    qi_mat_lb4 = models.FloatField(blank=True, null=True)
    qi_mat_lb5 = models.FloatField(blank=True, null=True)
    qi_mat_lb6 = models.FloatField(blank=True, null=True)
    qi_mat_lb7 = models.FloatField(blank=True, null=True)
    qi_mat_lb8 = models.FloatField(blank=True, null=True)
    qi_mat_lb9 = models.FloatField(blank=True, null=True)
    qi_mat_l10 = models.FloatField(blank=True, null=True)
    qi_supp_co = models.CharField(max_length=6, blank=True, null=True)
    qi_part_nu = models.CharField(max_length=30, blank=True, null=True)
    qi_sup_par = models.CharField(max_length=30, blank=True, null=True)
    qi_matw_uo = models.CharField(max_length=2, blank=True, null=True)
    qi_mu_calc = models.CharField(max_length=1, blank=True, null=True)
    qi_draw_nu = models.CharField(max_length=15, blank=True, null=True)
    qi_partw_u = models.CharField(max_length=2, blank=True, null=True)
    qi_ppbdont = models.NullBooleanField()
    qi_cav_ppo = models.IntegerField(blank=True, null=True)
    qi_waste_p = models.FloatField(blank=True, null=True)
    qi_part_vo = models.FloatField(blank=True, null=True)
    qi_part_we = models.FloatField(blank=True, null=True)
    qi_order_n = models.CharField(max_length=12, blank=True, null=True)
    qi_al_id = models.CharField(max_length=10, blank=True, null=True)
    qi_scrap_p = models.FloatField(blank=True, null=True)
    qi_chipwei = models.FloatField(blank=True, null=True)
    qi_chipcos = models.FloatField(blank=True, null=True)
    qi_lead_ti = models.IntegerField(blank=True, null=True)
    qi_status = models.CharField(max_length=1, blank=True, null=True)
    qi_require = models.DateField(blank=True, null=True)
    qi_purch_i = models.TextField(blank=True, null=True)
    qi_fin_wei = models.FloatField(blank=True, null=True)
    qi_lock = models.NullBooleanField()
    qi_area = models.FloatField(blank=True, null=True)
    qi_ftperc = models.FloatField(blank=True, null=True)
    qi_shrinka = models.IntegerField(blank=True, null=True)
    qi_extcutl = models.FloatField(blank=True, null=True)
    qi_extpcsp = models.IntegerField(blank=True, null=True)
    qi_extdrop = models.FloatField(blank=True, null=True)
    qi_extruno = models.FloatField(blank=True, null=True)
    qi_extwpf = models.FloatField(blank=True, null=True)
    qi_extbutt = models.FloatField(blank=True, null=True)
    qi_extbill = models.FloatField(blank=True, null=True)
    qi_web_thi = models.FloatField(blank=True, null=True)
    qi_lock_ba = models.NullBooleanField()
    qi_in_mm = models.IntegerField(blank=True, null=True)
    qi_std_cs_field = models.CharField(db_column='qi_std_cs_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    qi_extuse_field = models.FloatField(db_column='qi_extuse_', blank=True, null=True)  # Field renamed because it ended with '_'.
    qi_exthole = models.IntegerField(blank=True, null=True)
    qi_extdie_field = models.CharField(db_column='qi_extdie_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    qi_lengthw = models.IntegerField(blank=True, null=True)
    qi_misc1 = models.FloatField(blank=True, null=True)
    qi_misc2 = models.FloatField(blank=True, null=True)
    qi_misc3 = models.FloatField(blank=True, null=True)
    qi_misc4 = models.FloatField(blank=True, null=True)
    qi_misc5 = models.FloatField(blank=True, null=True)
    qi_misc6 = models.FloatField(blank=True, null=True)
    qi_misc7 = models.FloatField(blank=True, null=True)
    qi_misc8 = models.FloatField(blank=True, null=True)
    qi_misc9 = models.FloatField(blank=True, null=True)
    qi_misc10 = models.FloatField(blank=True, null=True)
    qi_cut_des = models.CharField(max_length=30, blank=True, null=True)
    qi_make_bu = models.CharField(max_length=1, blank=True, null=True)
    qi_cert_nu = models.CharField(max_length=15, blank=True, null=True)
    qi_barend2 = models.FloatField(blank=True, null=True)
    qi_mat_inc = models.IntegerField(blank=True, null=True)
    qi_obsolet = models.NullBooleanField()
    qi_islot = models.NullBooleanField()
    qi_donotbu = models.NullBooleanField()
    qi_non_sto = models.NullBooleanField()
    qi_mat_ref = models.TextField(blank=True, null=True)
    qi_grade = models.CharField(max_length=10, blank=True, null=True)
    qi_shipsep = models.NullBooleanField()
    qi_confcos = models.NullBooleanField()
    qi_dist_co = models.CharField(max_length=2, blank=True, null=True)
    qi_pour_nu = models.IntegerField(blank=True, null=True)
    qi_ship_st = models.IntegerField(blank=True, null=True)
    qi_de_id = models.CharField(max_length=10, blank=True, null=True)
    qi_paintfa = models.FloatField(blank=True, null=True)
    qi_paintar = models.FloatField(blank=True, null=True)
    qi_sequenc = models.IntegerField(blank=True, null=True)
    qi_lockmat = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'qinv'


class QinvOps(models.Model):
    qo_id = models.CharField(max_length=10, blank=True, null=True)
    qo_quote_n = models.CharField(max_length=15, blank=True, null=True)
    qo_order_n = models.CharField(max_length=12, blank=True, null=True)
    qo_item = models.IntegerField(blank=True, null=True)
    qo_parent = models.CharField(max_length=30, blank=True, null=True)
    qo_part_nu = models.CharField(max_length=30, blank=True, null=True)
    qo_op_num = models.IntegerField(blank=True, null=True)
    qo_order = models.IntegerField(blank=True, null=True)
    qo_quantit = models.IntegerField(blank=True, null=True)
    qo_bom_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qinv_ops'


class Qinvfrt(models.Model):
    qf_id = models.CharField(max_length=10, blank=True, null=True)
    qf_ucc_exc = models.FloatField(blank=True, null=True)
    qf_ucc_dol = models.FloatField(blank=True, null=True)
    qf_ucc_frt = models.CharField(max_length=20, blank=True, null=True)
    qf_ucc_fr2 = models.FloatField(blank=True, null=True)
    qf_ucc_fr3 = models.FloatField(blank=True, null=True)
    qf_ucc_fr4 = models.FloatField(blank=True, null=True)
    qf_ucc_add = models.FloatField(blank=True, null=True)
    qf_ucc_eur = models.FloatField(blank=True, null=True)
    qf_ucc_ad2 = models.FloatField(blank=True, null=True)
    qf_ucc_ad3 = models.FloatField(blank=True, null=True)
    qf_ucc_ad4 = models.FloatField(blank=True, null=True)
    qf_ucc_ad5 = models.FloatField(blank=True, null=True)
    qf_ucc_ad6 = models.FloatField(blank=True, null=True)
    qf_ucc_tot = models.FloatField(blank=True, null=True)
    qf_ucc_cos = models.FloatField(blank=True, null=True)
    qf_quote_n = models.CharField(max_length=15, blank=True, null=True)
    qf_item = models.IntegerField(blank=True, null=True)
    qf_order_n = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qinvfrt'


class Quote(models.Model):
    q1_quote_n = models.CharField(max_length=15, blank=True, null=True)
    q1_req_num = models.CharField(max_length=20, blank=True, null=True)
    q1_part_nu = models.CharField(max_length=30, blank=True, null=True)
    q1_draw_nu = models.CharField(max_length=30, blank=True, null=True)
    q1_rev_num = models.CharField(max_length=6, blank=True, null=True)
    q1_cust_co = models.CharField(max_length=6, blank=True, null=True)
    q1_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    q1_quote_d = models.DateField(blank=True, null=True)
    q1_req_dat = models.DateField(blank=True, null=True)
    q1_sent_da = models.DateField(blank=True, null=True)
    q1_last_up = models.DateField(blank=True, null=True)
    q1_q_memo = models.TextField(blank=True, null=True)
    q1_invent_field = models.CharField(db_column='q1_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    q1_qq1 = models.FloatField(blank=True, null=True)
    q1_qq2 = models.FloatField(blank=True, null=True)
    q1_qq3 = models.FloatField(blank=True, null=True)
    q1_qq4 = models.FloatField(blank=True, null=True)
    q1_qq5 = models.FloatField(blank=True, null=True)
    q1_qq6 = models.FloatField(blank=True, null=True)
    q1_qq7 = models.FloatField(blank=True, null=True)
    q1_qq8 = models.FloatField(blank=True, null=True)
    q1_qq9 = models.FloatField(blank=True, null=True)
    q1_qq10 = models.FloatField(blank=True, null=True)
    q1_setup1 = models.FloatField(blank=True, null=True)
    q1_setup2 = models.FloatField(blank=True, null=True)
    q1_setup3 = models.FloatField(blank=True, null=True)
    q1_setup4 = models.FloatField(blank=True, null=True)
    q1_setup5 = models.FloatField(blank=True, null=True)
    q1_setup6 = models.FloatField(blank=True, null=True)
    q1_setup7 = models.FloatField(blank=True, null=True)
    q1_setup8 = models.FloatField(blank=True, null=True)
    q1_setup9 = models.FloatField(blank=True, null=True)
    q1_setup10 = models.FloatField(blank=True, null=True)
    q1_ot_cost = models.FloatField(blank=True, null=True)
    q1_pmemo = models.TextField(blank=True, null=True)
    q1_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    q1_act_siz = models.FloatField(blank=True, null=True)
    q1_tol_p = models.FloatField(blank=True, null=True)
    q1_tol_m = models.FloatField(blank=True, null=True)
    q1_mat_len = models.FloatField(blank=True, null=True)
    q1_shape_c = models.CharField(max_length=7, blank=True, null=True)
    q1_m_memo = models.TextField(blank=True, null=True)
    q1_finish = models.CharField(max_length=5, blank=True, null=True)
    q1_part_le = models.FloatField(blank=True, null=True)
    q1_cut_off = models.FloatField(blank=True, null=True)
    q1_face_le = models.FloatField(blank=True, null=True)
    q1_tot_len = models.FloatField(blank=True, null=True)
    q1_part_wi = models.FloatField(blank=True, null=True)
    q1_wcut_of = models.FloatField(blank=True, null=True)
    q1_wface_l = models.FloatField(blank=True, null=True)
    q1_tot_wid = models.FloatField(blank=True, null=True)
    q1_mach_co = models.CharField(max_length=5, blank=True, null=True)
    q1_totbar_field = models.FloatField(db_column='q1_totbar_', blank=True, null=True)  # Field renamed because it ended with '_'.
    q1_barend_field = models.FloatField(db_column='q1_barend_', blank=True, null=True)  # Field renamed because it ended with '_'.
    q1_baruse_field = models.FloatField(db_column='q1_baruse_', blank=True, null=True)  # Field renamed because it ended with '_'.
    q1_bar_wei = models.FloatField(blank=True, null=True)
    q1_t_bar_w = models.FloatField(blank=True, null=True)
    q1_ppbar = models.FloatField(blank=True, null=True)
    q1_bar_per = models.FloatField(blank=True, null=True)
    q1_perc_ma = models.IntegerField(blank=True, null=True)
    q1_tot_wei = models.FloatField(blank=True, null=True)
    q1_act_we_field = models.FloatField(db_column='q1_act_we_', blank=True, null=True)  # Field renamed because it ended with '_'.
    q1_supp_co = models.CharField(max_length=6, blank=True, null=True)
    q1_valid_d = models.CharField(max_length=10, blank=True, null=True)
    q1_deliver = models.CharField(max_length=50, blank=True, null=True)
    q1_part_de = models.CharField(max_length=50, blank=True, null=True)
    q1_uom = models.CharField(max_length=1, blank=True, null=True)
    q1_wgtpp = models.FloatField(blank=True, null=True)
    q1_prep_by = models.CharField(max_length=30, blank=True, null=True)
    q1_bom_mat = models.FloatField(blank=True, null=True)
    q1_cht_siz = models.FloatField(blank=True, null=True)
    q1_wide = models.FloatField(blank=True, null=True)
    q1_cust_c2 = models.CharField(max_length=30, blank=True, null=True)
    q1_chipwei = models.FloatField(blank=True, null=True)
    q1_chipcos = models.FloatField(blank=True, null=True)
    q1_chipvol = models.FloatField(blank=True, null=True)
    q1_addrl = models.CharField(max_length=33, blank=True, null=True)
    q1_height = models.FloatField(blank=True, null=True)
    q1_fob = models.CharField(max_length=15, blank=True, null=True)
    q1_qr1 = models.FloatField(blank=True, null=True)
    q1_qr2 = models.FloatField(blank=True, null=True)
    q1_qr3 = models.FloatField(blank=True, null=True)
    q1_qr4 = models.FloatField(blank=True, null=True)
    q1_qr5 = models.FloatField(blank=True, null=True)
    q1_qr6 = models.FloatField(blank=True, null=True)
    q1_qr7 = models.FloatField(blank=True, null=True)
    q1_qr8 = models.FloatField(blank=True, null=True)
    q1_qr9 = models.FloatField(blank=True, null=True)
    q1_qr10 = models.FloatField(blank=True, null=True)
    q1_partw_u = models.CharField(max_length=2, blank=True, null=True)
    q1_matw_uo = models.CharField(max_length=2, blank=True, null=True)
    q1_len_uom = models.CharField(max_length=2, blank=True, null=True)
    q1_psquare = models.FloatField(blank=True, null=True)
    q1_msquare = models.FloatField(blank=True, null=True)
    q1_inv_cos = models.FloatField(blank=True, null=True)
    q1_icost1 = models.FloatField(blank=True, null=True)
    q1_icost2 = models.FloatField(blank=True, null=True)
    q1_icost3 = models.FloatField(blank=True, null=True)
    q1_icost4 = models.FloatField(blank=True, null=True)
    q1_icost5 = models.FloatField(blank=True, null=True)
    q1_icost6 = models.FloatField(blank=True, null=True)
    q1_icost7 = models.FloatField(blank=True, null=True)
    q1_icost8 = models.FloatField(blank=True, null=True)
    q1_icost9 = models.FloatField(blank=True, null=True)
    q1_icost10 = models.FloatField(blank=True, null=True)
    q1_comp_na = models.CharField(max_length=35, blank=True, null=True)
    q1_address = models.CharField(max_length=35, blank=True, null=True)
    q1_addres2 = models.CharField(max_length=35, blank=True, null=True)
    q1_addres3 = models.CharField(max_length=35, blank=True, null=True)
    q1_folup_d = models.DateField(blank=True, null=True)
    q1_status = models.CharField(max_length=1, blank=True, null=True)
    q1_nq_equi = models.NullBooleanField()
    q1_nq_part = models.NullBooleanField()
    q1_nq_par2 = models.NullBooleanField()
    q1_nq_cfg = models.NullBooleanField()
    q1_nq_cfgd = models.CharField(max_length=50, blank=True, null=True)
    q1_nq_tol = models.NullBooleanField()
    q1_nq_told = models.CharField(max_length=50, blank=True, null=True)
    q1_nq_oth = models.NullBooleanField()
    q1_nq_othd = models.CharField(max_length=50, blank=True, null=True)
    q1_nq_quan = models.NullBooleanField()
    q1_nq_engo = models.NullBooleanField()
    q1_nq_quot = models.DateField(blank=True, null=True)
    q1_nq_noti = models.NullBooleanField()
    q1_nq_oth2 = models.NullBooleanField()
    q1_nq_oth3 = models.TextField(blank=True, null=True)
    q1_scrap_p = models.IntegerField(blank=True, null=True)
    q1_fin_wei = models.FloatField(blank=True, null=True)
    q1_lo_code = models.CharField(max_length=10, blank=True, null=True)
    q1_lock = models.NullBooleanField()
    q1_draw_re = models.CharField(max_length=6, blank=True, null=True)
    q1_hub_typ = models.CharField(max_length=20, blank=True, null=True)
    q1_sfb_od = models.FloatField(blank=True, null=True)
    q1_sfb_id = models.FloatField(blank=True, null=True)
    q1_sfb_len = models.FloatField(blank=True, null=True)
    q1_sf1_od = models.FloatField(blank=True, null=True)
    q1_sf1_len = models.FloatField(blank=True, null=True)
    q1_sf2_od = models.FloatField(blank=True, null=True)
    q1_sf2_len = models.FloatField(blank=True, null=True)
    q1_addsub = models.FloatField(blank=True, null=True)
    q1_cast_od = models.FloatField(blank=True, null=True)
    q1_cast_id = models.FloatField(blank=True, null=True)
    q1_mold_id = models.CharField(max_length=10, blank=True, null=True)
    q1_cast_ov = models.FloatField(blank=True, null=True)
    q1_ship_co = models.CharField(max_length=35, blank=True, null=True)
    q1_sh_ad1 = models.CharField(max_length=35, blank=True, null=True)
    q1_sh_ad2 = models.CharField(max_length=35, blank=True, null=True)
    q1_sh_ad3 = models.CharField(max_length=35, blank=True, null=True)
    q1_extatrb = models.CharField(max_length=30, blank=True, null=True)
    q1_extatr2 = models.CharField(max_length=30, blank=True, null=True)
    q1_extatr3 = models.CharField(max_length=30, blank=True, null=True)
    q1_extatr4 = models.CharField(max_length=30, blank=True, null=True)
    q1_extatr5 = models.CharField(max_length=30, blank=True, null=True)
    q1_extatr6 = models.CharField(max_length=30, blank=True, null=True)
    q1_extatr7 = models.CharField(max_length=30, blank=True, null=True)
    q1_extatr8 = models.CharField(max_length=30, blank=True, null=True)
    q1_extatr9 = models.CharField(max_length=30, blank=True, null=True)
    q1_extat10 = models.CharField(max_length=30, blank=True, null=True)
    q1_enginee = models.CharField(max_length=3, blank=True, null=True)
    q1_lot = models.IntegerField(blank=True, null=True)
    q1_dqtr = models.IntegerField(blank=True, null=True)
    q1_usesuom = models.NullBooleanField()
    q1_setup_m = models.FloatField(blank=True, null=True)
    q1_parent_field = models.CharField(db_column='q1_parent_', max_length=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    q1_fg_inve = models.CharField(max_length=30, blank=True, null=True)
    q1_pay_ter = models.CharField(max_length=20, blank=True, null=True)
    q1_ship_vi = models.CharField(max_length=40, blank=True, null=True)
    q1_prod_co = models.CharField(max_length=2, blank=True, null=True)
    q1_qty_per = models.IntegerField(blank=True, null=True)
    q1_overrid = models.NullBooleanField()
    q1_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    q1_cur_rat = models.FloatField(blank=True, null=True)
    q1_cot_cos = models.FloatField(blank=True, null=True)
    q1_mat_inc = models.IntegerField(blank=True, null=True)
    q1_std_plt = models.CharField(max_length=10, blank=True, null=True)
    q1_std_pkg = models.CharField(max_length=10, blank=True, null=True)
    q1_op_last = models.CharField(max_length=30, blank=True, null=True)
    q1_op_rev = models.CharField(max_length=3, blank=True, null=True)
    q1_op_las2 = models.DateField(blank=True, null=True)
    q1_doc_typ = models.CharField(max_length=10, blank=True, null=True)
    q1_user_id = models.CharField(max_length=5, blank=True, null=True)
    q1_last_mo = models.DateTimeField(blank=True, null=True)
    q1_cust_ph = models.CharField(max_length=14, blank=True, null=True)
    q1_cust_fa = models.CharField(max_length=14, blank=True, null=True)
    q1_proj_de = models.CharField(max_length=50, blank=True, null=True)
    q1_rev_nex = models.IntegerField(blank=True, null=True)
    q1_dpas = models.CharField(max_length=10, blank=True, null=True)
    q1_sh_ad4 = models.CharField(max_length=35, blank=True, null=True)
    q1_ca_id = models.CharField(max_length=10, blank=True, null=True)
    q1_eng_mas = models.NullBooleanField()
    q1_eau = models.IntegerField(blank=True, null=True)
    q1_generic = models.NullBooleanField()
    q1_autorou = models.IntegerField(blank=True, null=True)
    q1_max_tru = models.IntegerField(blank=True, null=True)
    q1_addres4 = models.CharField(max_length=35, blank=True, null=True)
    q1_ex1 = models.NullBooleanField()
    q1_ex2 = models.NullBooleanField()
    q1_ex3 = models.NullBooleanField()
    q1_ex4 = models.NullBooleanField()
    q1_ex5 = models.NullBooleanField()
    q1_ex6 = models.NullBooleanField()
    q1_ex7 = models.NullBooleanField()
    q1_ex8 = models.NullBooleanField()
    q1_ex9 = models.NullBooleanField()
    q1_ex10 = models.NullBooleanField()
    q1_fab_dat = models.DateField(blank=True, null=True)
    q1_ship_da = models.DateField(blank=True, null=True)
    q1_std_gen = models.CharField(max_length=10, blank=True, null=True)
    q1_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    q1_subord_field = models.CharField(db_column='q1_subord_', max_length=7, blank=True, null=True)  # Field renamed because it ended with '_'.
    q1_lead_ti = models.IntegerField(blank=True, null=True)
    q1_shipsep = models.NullBooleanField()
    q1_due_dat = models.DateField(blank=True, null=True)
    q1_foblabe = models.CharField(max_length=3, blank=True, null=True)
    q1_install = models.CharField(max_length=30, blank=True, null=True)
    q1_op_num = models.IntegerField(blank=True, null=True)
    q1_op_mu = models.FloatField(blank=True, null=True)
    q1_apr = models.FloatField(blank=True, null=True)
    q1_rel1 = models.IntegerField(blank=True, null=True)
    q1_rel2 = models.IntegerField(blank=True, null=True)
    q1_rel3 = models.IntegerField(blank=True, null=True)
    q1_rel4 = models.IntegerField(blank=True, null=True)
    q1_rel5 = models.IntegerField(blank=True, null=True)
    q1_rel6 = models.IntegerField(blank=True, null=True)
    q1_rel7 = models.IntegerField(blank=True, null=True)
    q1_rel8 = models.IntegerField(blank=True, null=True)
    q1_rel9 = models.IntegerField(blank=True, null=True)
    q1_rel10 = models.IntegerField(blank=True, null=True)
    q1_days1 = models.IntegerField(blank=True, null=True)
    q1_days2 = models.IntegerField(blank=True, null=True)
    q1_days3 = models.IntegerField(blank=True, null=True)
    q1_days4 = models.IntegerField(blank=True, null=True)
    q1_days5 = models.IntegerField(blank=True, null=True)
    q1_days6 = models.IntegerField(blank=True, null=True)
    q1_days7 = models.IntegerField(blank=True, null=True)
    q1_days8 = models.IntegerField(blank=True, null=True)
    q1_days9 = models.IntegerField(blank=True, null=True)
    q1_days10 = models.IntegerField(blank=True, null=True)
    q1_cc1 = models.FloatField(blank=True, null=True)
    q1_cc2 = models.FloatField(blank=True, null=True)
    q1_cc3 = models.FloatField(blank=True, null=True)
    q1_cc4 = models.FloatField(blank=True, null=True)
    q1_cc5 = models.FloatField(blank=True, null=True)
    q1_cc6 = models.FloatField(blank=True, null=True)
    q1_cc7 = models.FloatField(blank=True, null=True)
    q1_cc8 = models.FloatField(blank=True, null=True)
    q1_cc9 = models.FloatField(blank=True, null=True)
    q1_cc10 = models.FloatField(blank=True, null=True)
    q1_bypass_field = models.NullBooleanField(db_column='q1_bypass_')  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'quote'


class Quote2(models.Model):
    q2_quote_n = models.CharField(max_length=15, blank=True, null=True)
    q2_lastop = models.IntegerField(blank=True, null=True)
    q2_tsu = models.FloatField(blank=True, null=True)
    q2_tmc = models.FloatField(blank=True, null=True)
    q2_tsmc_1 = models.FloatField(blank=True, null=True)
    q2_tsmc_2 = models.FloatField(blank=True, null=True)
    q2_tsmc_3 = models.FloatField(blank=True, null=True)
    q2_tsmc_4 = models.FloatField(blank=True, null=True)
    q2_tsmc_5 = models.FloatField(blank=True, null=True)
    q2_tsmc_6 = models.FloatField(blank=True, null=True)
    q2_tsmc_7 = models.FloatField(blank=True, null=True)
    q2_tsmc_8 = models.FloatField(blank=True, null=True)
    q2_tsmc_9 = models.FloatField(blank=True, null=True)
    q2_tsmc_10 = models.FloatField(blank=True, null=True)
    q2_mcpu_1 = models.FloatField(blank=True, null=True)
    q2_mcpu_2 = models.FloatField(blank=True, null=True)
    q2_mcpu_3 = models.FloatField(blank=True, null=True)
    q2_mcpu_4 = models.FloatField(blank=True, null=True)
    q2_mcpu_5 = models.FloatField(blank=True, null=True)
    q2_mcpu_6 = models.FloatField(blank=True, null=True)
    q2_mcpu_7 = models.FloatField(blank=True, null=True)
    q2_mcpu_8 = models.FloatField(blank=True, null=True)
    q2_mcpu_9 = models.FloatField(blank=True, null=True)
    q2_mcpu_10 = models.FloatField(blank=True, null=True)
    q2_htc_1 = models.FloatField(blank=True, null=True)
    q2_htc_2 = models.FloatField(blank=True, null=True)
    q2_htc_3 = models.FloatField(blank=True, null=True)
    q2_htc_4 = models.FloatField(blank=True, null=True)
    q2_htc_5 = models.FloatField(blank=True, null=True)
    q2_htc_6 = models.FloatField(blank=True, null=True)
    q2_htc_7 = models.FloatField(blank=True, null=True)
    q2_htc_8 = models.FloatField(blank=True, null=True)
    q2_htc_9 = models.FloatField(blank=True, null=True)
    q2_htc_10 = models.FloatField(blank=True, null=True)
    q2_pc_1 = models.FloatField(blank=True, null=True)
    q2_pc_2 = models.FloatField(blank=True, null=True)
    q2_pc_3 = models.FloatField(blank=True, null=True)
    q2_pc_4 = models.FloatField(blank=True, null=True)
    q2_pc_5 = models.FloatField(blank=True, null=True)
    q2_pc_6 = models.FloatField(blank=True, null=True)
    q2_pc_7 = models.FloatField(blank=True, null=True)
    q2_pc_8 = models.FloatField(blank=True, null=True)
    q2_pc_9 = models.FloatField(blank=True, null=True)
    q2_pc_10 = models.FloatField(blank=True, null=True)
    q2_tc_1 = models.FloatField(blank=True, null=True)
    q2_tc_2 = models.FloatField(blank=True, null=True)
    q2_tc_3 = models.FloatField(blank=True, null=True)
    q2_tc_4 = models.FloatField(blank=True, null=True)
    q2_tc_5 = models.FloatField(blank=True, null=True)
    q2_tc_6 = models.FloatField(blank=True, null=True)
    q2_tc_7 = models.FloatField(blank=True, null=True)
    q2_tc_8 = models.FloatField(blank=True, null=True)
    q2_tc_9 = models.FloatField(blank=True, null=True)
    q2_tc_10 = models.FloatField(blank=True, null=True)
    q2_mc_1 = models.FloatField(blank=True, null=True)
    q2_mc_2 = models.FloatField(blank=True, null=True)
    q2_mc_3 = models.FloatField(blank=True, null=True)
    q2_mc_4 = models.FloatField(blank=True, null=True)
    q2_mc_5 = models.FloatField(blank=True, null=True)
    q2_mc_6 = models.FloatField(blank=True, null=True)
    q2_mc_7 = models.FloatField(blank=True, null=True)
    q2_mc_8 = models.FloatField(blank=True, null=True)
    q2_mc_9 = models.FloatField(blank=True, null=True)
    q2_mc_10 = models.FloatField(blank=True, null=True)
    q2_mc1 = models.FloatField(blank=True, null=True)
    q2_mc2 = models.FloatField(blank=True, null=True)
    q2_mc3 = models.FloatField(blank=True, null=True)
    q2_mc4 = models.FloatField(blank=True, null=True)
    q2_mc5 = models.FloatField(blank=True, null=True)
    q2_mc6 = models.FloatField(blank=True, null=True)
    q2_mc7 = models.FloatField(blank=True, null=True)
    q2_mc8 = models.FloatField(blank=True, null=True)
    q2_mc9 = models.FloatField(blank=True, null=True)
    q2_mc10 = models.FloatField(blank=True, null=True)
    q2_tsu1 = models.FloatField(blank=True, null=True)
    q2_tsu2 = models.FloatField(blank=True, null=True)
    q2_tsu3 = models.FloatField(blank=True, null=True)
    q2_tsu4 = models.FloatField(blank=True, null=True)
    q2_tsu5 = models.FloatField(blank=True, null=True)
    q2_tsu6 = models.FloatField(blank=True, null=True)
    q2_tsu7 = models.FloatField(blank=True, null=True)
    q2_tsu8 = models.FloatField(blank=True, null=True)
    q2_tsu9 = models.FloatField(blank=True, null=True)
    q2_tsu10 = models.FloatField(blank=True, null=True)
    q2_sumu1 = models.IntegerField(blank=True, null=True)
    q2_sumu2 = models.IntegerField(blank=True, null=True)
    q2_sumu3 = models.IntegerField(blank=True, null=True)
    q2_sumu4 = models.IntegerField(blank=True, null=True)
    q2_sumu5 = models.IntegerField(blank=True, null=True)
    q2_sumu6 = models.IntegerField(blank=True, null=True)
    q2_sumu7 = models.IntegerField(blank=True, null=True)
    q2_sumu8 = models.IntegerField(blank=True, null=True)
    q2_sumu9 = models.IntegerField(blank=True, null=True)
    q2_sumu10 = models.IntegerField(blank=True, null=True)
    q2_tmc1 = models.FloatField(blank=True, null=True)
    q2_tmc2 = models.FloatField(blank=True, null=True)
    q2_tmc3 = models.FloatField(blank=True, null=True)
    q2_tmc4 = models.FloatField(blank=True, null=True)
    q2_tmc5 = models.FloatField(blank=True, null=True)
    q2_tmc6 = models.FloatField(blank=True, null=True)
    q2_tmc7 = models.FloatField(blank=True, null=True)
    q2_tmc8 = models.FloatField(blank=True, null=True)
    q2_tmc9 = models.FloatField(blank=True, null=True)
    q2_tmc10 = models.FloatField(blank=True, null=True)
    q2_ov1 = models.FloatField(blank=True, null=True)
    q2_ov2 = models.FloatField(blank=True, null=True)
    q2_ov3 = models.FloatField(blank=True, null=True)
    q2_ov4 = models.FloatField(blank=True, null=True)
    q2_ov5 = models.FloatField(blank=True, null=True)
    q2_ov6 = models.FloatField(blank=True, null=True)
    q2_ov7 = models.FloatField(blank=True, null=True)
    q2_ov8 = models.FloatField(blank=True, null=True)
    q2_ov9 = models.FloatField(blank=True, null=True)
    q2_ov10 = models.FloatField(blank=True, null=True)
    q2_ovmu1 = models.IntegerField(blank=True, null=True)
    q2_ovmu2 = models.IntegerField(blank=True, null=True)
    q2_ovmu3 = models.IntegerField(blank=True, null=True)
    q2_ovmu4 = models.IntegerField(blank=True, null=True)
    q2_ovmu5 = models.IntegerField(blank=True, null=True)
    q2_ovmu6 = models.IntegerField(blank=True, null=True)
    q2_ovmu7 = models.IntegerField(blank=True, null=True)
    q2_ovmu8 = models.IntegerField(blank=True, null=True)
    q2_ovmu9 = models.IntegerField(blank=True, null=True)
    q2_ovmu10 = models.IntegerField(blank=True, null=True)
    q2_gtmc1 = models.FloatField(blank=True, null=True)
    q2_gtmc2 = models.FloatField(blank=True, null=True)
    q2_gtmc3 = models.FloatField(blank=True, null=True)
    q2_gtmc4 = models.FloatField(blank=True, null=True)
    q2_gtmc5 = models.FloatField(blank=True, null=True)
    q2_gtmc6 = models.FloatField(blank=True, null=True)
    q2_gtmc7 = models.FloatField(blank=True, null=True)
    q2_gtmc8 = models.FloatField(blank=True, null=True)
    q2_gtmc9 = models.FloatField(blank=True, null=True)
    q2_gtmc10 = models.FloatField(blank=True, null=True)
    q2_misc1 = models.FloatField(blank=True, null=True)
    q2_misc2 = models.FloatField(blank=True, null=True)
    q2_misc3 = models.FloatField(blank=True, null=True)
    q2_misc4 = models.FloatField(blank=True, null=True)
    q2_misc5 = models.FloatField(blank=True, null=True)
    q2_misc6 = models.FloatField(blank=True, null=True)
    q2_misc7 = models.FloatField(blank=True, null=True)
    q2_misc8 = models.FloatField(blank=True, null=True)
    q2_misc9 = models.FloatField(blank=True, null=True)
    q2_misc10 = models.FloatField(blank=True, null=True)
    q2_gt1 = models.FloatField(blank=True, null=True)
    q2_gt2 = models.FloatField(blank=True, null=True)
    q2_gt3 = models.FloatField(blank=True, null=True)
    q2_gt4 = models.FloatField(blank=True, null=True)
    q2_gt5 = models.FloatField(blank=True, null=True)
    q2_gt6 = models.FloatField(blank=True, null=True)
    q2_gt7 = models.FloatField(blank=True, null=True)
    q2_gt8 = models.FloatField(blank=True, null=True)
    q2_gt9 = models.FloatField(blank=True, null=True)
    q2_gt10 = models.FloatField(blank=True, null=True)
    q2_sc1 = models.FloatField(blank=True, null=True)
    q2_sc2 = models.FloatField(blank=True, null=True)
    q2_sc3 = models.FloatField(blank=True, null=True)
    q2_sc4 = models.FloatField(blank=True, null=True)
    q2_sc5 = models.FloatField(blank=True, null=True)
    q2_sc6 = models.FloatField(blank=True, null=True)
    q2_sc7 = models.FloatField(blank=True, null=True)
    q2_sc8 = models.FloatField(blank=True, null=True)
    q2_sc9 = models.FloatField(blank=True, null=True)
    q2_sc10 = models.FloatField(blank=True, null=True)
    q2_fcpu1 = models.FloatField(blank=True, null=True)
    q2_fcpu2 = models.FloatField(blank=True, null=True)
    q2_fcpu3 = models.FloatField(blank=True, null=True)
    q2_fcpu4 = models.FloatField(blank=True, null=True)
    q2_fcpu5 = models.FloatField(blank=True, null=True)
    q2_fcpu6 = models.FloatField(blank=True, null=True)
    q2_fcpu7 = models.FloatField(blank=True, null=True)
    q2_fcpu8 = models.FloatField(blank=True, null=True)
    q2_fcpu9 = models.FloatField(blank=True, null=True)
    q2_fcpu10 = models.FloatField(blank=True, null=True)
    q2_tottc = models.FloatField(blank=True, null=True)
    q2_totgc = models.FloatField(blank=True, null=True)
    q2_totcc = models.FloatField(blank=True, null=True)
    q2_totmc = models.FloatField(blank=True, null=True)
    q2_fenote = models.TextField(blank=True, null=True)
    q2_mannote = models.TextField(blank=True, null=True)
    q2_salespe = models.FloatField(blank=True, null=True)
    q2_salesp2 = models.CharField(max_length=5, blank=True, null=True)
    q2_ht_note = models.TextField(blank=True, null=True)
    q2_pl_note = models.TextField(blank=True, null=True)
    q2_no_quot = models.CharField(max_length=1, blank=True, null=True)
    q2_induct_field = models.CharField(db_column='q2_induct_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    q2_shard_s = models.CharField(max_length=25, blank=True, null=True)
    q2_toteff_field = models.CharField(db_column='q2_toteff_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    q2_case_s = models.CharField(max_length=10, blank=True, null=True)
    q2_core_s = models.CharField(max_length=10, blank=True, null=True)
    q2_plen_s = models.CharField(max_length=10, blank=True, null=True)
    q2_note_s = models.CharField(max_length=40, blank=True, null=True)
    q2_inc_sub = models.CharField(max_length=1, blank=True, null=True)
    q2_misc_no = models.TextField(blank=True, null=True)
    q2_overrid = models.NullBooleanField()
    q2_gtmat1 = models.FloatField(blank=True, null=True)
    q2_gtmat2 = models.FloatField(blank=True, null=True)
    q2_gtmat3 = models.FloatField(blank=True, null=True)
    q2_gtmat4 = models.FloatField(blank=True, null=True)
    q2_gtmat5 = models.FloatField(blank=True, null=True)
    q2_gtmat6 = models.FloatField(blank=True, null=True)
    q2_gtmat7 = models.FloatField(blank=True, null=True)
    q2_gtmat8 = models.FloatField(blank=True, null=True)
    q2_gtmat9 = models.FloatField(blank=True, null=True)
    q2_gtmat10 = models.FloatField(blank=True, null=True)
    q2_decimal = models.IntegerField(blank=True, null=True)
    q2_app_by = models.CharField(max_length=25, blank=True, null=True)
    q2_ins_by = models.CharField(max_length=25, blank=True, null=True)
    q2_shard_i = models.CharField(max_length=15, blank=True, null=True)
    q2_note_i = models.TextField(blank=True, null=True)
    q2_lot = models.CharField(max_length=20, blank=True, null=True)
    q2_case_i = models.CharField(max_length=10, blank=True, null=True)
    q2_plen_i = models.CharField(max_length=10, blank=True, null=True)
    q2_matmu1 = models.IntegerField(blank=True, null=True)
    q2_matmu2 = models.IntegerField(blank=True, null=True)
    q2_matmu3 = models.IntegerField(blank=True, null=True)
    q2_matmu4 = models.IntegerField(blank=True, null=True)
    q2_matmu5 = models.IntegerField(blank=True, null=True)
    q2_matmu6 = models.IntegerField(blank=True, null=True)
    q2_matmu7 = models.IntegerField(blank=True, null=True)
    q2_matmu8 = models.IntegerField(blank=True, null=True)
    q2_matmu9 = models.IntegerField(blank=True, null=True)
    q2_matmu10 = models.IntegerField(blank=True, null=True)
    q2_exclcom = models.NullBooleanField()
    q2_cfcpu1 = models.FloatField(blank=True, null=True)
    q2_cfcpu2 = models.FloatField(blank=True, null=True)
    q2_cfcpu3 = models.FloatField(blank=True, null=True)
    q2_cfcpu4 = models.FloatField(blank=True, null=True)
    q2_cfcpu5 = models.FloatField(blank=True, null=True)
    q2_cfcpu6 = models.FloatField(blank=True, null=True)
    q2_cfcpu7 = models.FloatField(blank=True, null=True)
    q2_cfcpu8 = models.FloatField(blank=True, null=True)
    q2_cfcpu9 = models.FloatField(blank=True, null=True)
    q2_cfcpu10 = models.FloatField(blank=True, null=True)
    q2_excsetu = models.NullBooleanField()
    q2_salesp3 = models.CharField(max_length=5, blank=True, null=True)
    q2_salesp4 = models.FloatField(blank=True, null=True)
    q2_excmatl = models.NullBooleanField()
    q2_ptools = models.FloatField(blank=True, null=True)
    q2_inc_mis = models.NullBooleanField()
    q2_excplat = models.NullBooleanField()
    q2_gm = models.NullBooleanField()
    q2_qtyuom = models.CharField(max_length=4, blank=True, null=True)
    q2_apr1 = models.FloatField(blank=True, null=True)
    q2_apr2 = models.FloatField(blank=True, null=True)
    q2_apr3 = models.FloatField(blank=True, null=True)
    q2_apr4 = models.FloatField(blank=True, null=True)
    q2_apr5 = models.FloatField(blank=True, null=True)
    q2_apr6 = models.FloatField(blank=True, null=True)
    q2_apr7 = models.FloatField(blank=True, null=True)
    q2_apr8 = models.FloatField(blank=True, null=True)
    q2_apr9 = models.FloatField(blank=True, null=True)
    q2_apr10 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote2'


class Rate(models.Model):
    ra_carrier = models.CharField(max_length=10, blank=True, null=True)
    ra_ship_ty = models.CharField(max_length=20, blank=True, null=True)
    ra_commerc = models.NullBooleanField()
    ra_zone = models.CharField(max_length=10, blank=True, null=True)
    ra_max_wei = models.CharField(max_length=10, blank=True, null=True)
    ra_hundred = models.NullBooleanField()
    ra_rate = models.FloatField(blank=True, null=True)
    ra_residen = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'rate'


class Ratehist(models.Model):
    rh_id = models.CharField(max_length=10, blank=True, null=True)
    rh_emp_id = models.CharField(max_length=5, blank=True, null=True)
    rh_date_ef = models.DateField(blank=True, null=True)
    rh_hourly = models.FloatField(blank=True, null=True)
    rh_salary = models.FloatField(blank=True, null=True)
    rh_shift_d = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratehist'


class Reclock(models.Model):
    rl_user_id = models.CharField(max_length=5, blank=True, null=True)
    rl_table = models.CharField(max_length=10, blank=True, null=True)
    rl_key = models.CharField(max_length=30, blank=True, null=True)
    rl_app = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reclock'


class ReqDept(models.Model):
    rd_id = models.CharField(max_length=10, blank=True, null=True)
    rd_doc_typ = models.CharField(max_length=10, blank=True, null=True)
    rd_de_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_dept'


class Ressched(models.Model):
    rs_sched_d = models.DateField(blank=True, null=True)
    rs_order_n = models.CharField(max_length=12, blank=True, null=True)
    rs_rel_num = models.IntegerField(blank=True, null=True)
    rs_mat_cod = models.CharField(max_length=6, blank=True, null=True)
    rs_pour_nu = models.IntegerField(blank=True, null=True)
    rs_cust_co = models.CharField(max_length=6, blank=True, null=True)
    rs_mach_co = models.CharField(max_length=5, blank=True, null=True)
    rs_invent_field = models.CharField(db_column='rs_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    rs_flow_ra = models.IntegerField(blank=True, null=True)
    rs_totalgp = models.IntegerField(blank=True, null=True)
    rs_resingp = models.IntegerField(blank=True, null=True)
    rs_cav_ppo = models.IntegerField(blank=True, null=True)
    rs_duro = models.CharField(max_length=3, blank=True, null=True)
    rs_pigment = models.CharField(max_length=20, blank=True, null=True)
    rs_qty_pro = models.FloatField(blank=True, null=True)
    rs_qty_sch = models.FloatField(blank=True, null=True)
    rs_mpp = models.FloatField(blank=True, null=True)
    rs_ph = models.FloatField(blank=True, null=True)
    rs_mach_c2 = models.CharField(max_length=5, blank=True, null=True)
    rs_mach_c3 = models.CharField(max_length=5, blank=True, null=True)
    rs_mach_c4 = models.CharField(max_length=5, blank=True, null=True)
    rs_mach_c5 = models.CharField(max_length=5, blank=True, null=True)
    rs_mpp1 = models.FloatField(blank=True, null=True)
    rs_mpp2 = models.FloatField(blank=True, null=True)
    rs_mpp3 = models.FloatField(blank=True, null=True)
    rs_mpp4 = models.FloatField(blank=True, null=True)
    rs_ph1 = models.FloatField(blank=True, null=True)
    rs_ph2 = models.FloatField(blank=True, null=True)
    rs_ph3 = models.FloatField(blank=True, null=True)
    rs_ph4 = models.FloatField(blank=True, null=True)
    rs_emp_id = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_id1 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_id2 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_id3 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_id4 = models.CharField(max_length=5, blank=True, null=True)
    rs_shift = models.CharField(max_length=2, blank=True, null=True)
    rs_id = models.IntegerField(blank=True, null=True)
    rs_cast_op = models.IntegerField(blank=True, null=True)
    rs_ppop1 = models.IntegerField(blank=True, null=True)
    rs_ppop2 = models.IntegerField(blank=True, null=True)
    rs_ppop3 = models.IntegerField(blank=True, null=True)
    rs_ppop4 = models.IntegerField(blank=True, null=True)
    rs_qi_item = models.IntegerField(blank=True, null=True)
    rs_emp_id5 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_id6 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_id7 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_id8 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_id9 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_i10 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_i11 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp_i12 = models.CharField(max_length=5, blank=True, null=True)
    rs_emp1_qt = models.FloatField(blank=True, null=True)
    rs_emp1_q2 = models.FloatField(blank=True, null=True)
    rs_emp1_q3 = models.FloatField(blank=True, null=True)
    rs_emp2_qt = models.FloatField(blank=True, null=True)
    rs_emp2_q2 = models.FloatField(blank=True, null=True)
    rs_emp2_q3 = models.FloatField(blank=True, null=True)
    rs_emp3_qt = models.FloatField(blank=True, null=True)
    rs_emp3_q2 = models.FloatField(blank=True, null=True)
    rs_emp3_q3 = models.FloatField(blank=True, null=True)
    rs_emp4_qt = models.FloatField(blank=True, null=True)
    rs_emp4_q2 = models.FloatField(blank=True, null=True)
    rs_emp4_q3 = models.FloatField(blank=True, null=True)
    rs_priorit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ressched'


class Saccred(models.Model):
    sd_id = models.CharField(max_length=10, blank=True, null=True)
    sd_sa_desc = models.CharField(max_length=30, blank=True, null=True)
    sd_supp_co = models.CharField(max_length=6, blank=True, null=True)
    sd_expire_field = models.DateField(db_column='sd_expire_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'saccred'


class Salesapp(models.Model):
    sa_id = models.CharField(max_length=10, blank=True, null=True)
    sa_inv_num = models.CharField(max_length=7, blank=True, null=True)
    sa_line_nu = models.IntegerField(blank=True, null=True)
    sa_de_id = models.CharField(max_length=2, blank=True, null=True)
    sa_percent = models.FloatField(blank=True, null=True)
    sa_amount = models.FloatField(blank=True, null=True)
    sa_ca_code = models.CharField(max_length=12, blank=True, null=True)
    sa_gl_id = models.CharField(max_length=10, blank=True, null=True)
    sa_mr_id = models.CharField(max_length=10, blank=True, null=True)
    sa_prod_co = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesapp'


class Salescom(models.Model):
    sc_id = models.CharField(max_length=10, blank=True, null=True)
    sc_type = models.CharField(max_length=1, blank=True, null=True)
    sc_num = models.CharField(max_length=7, blank=True, null=True)
    sc_mr_id = models.CharField(max_length=10, blank=True, null=True)
    sc_line_nu = models.IntegerField(blank=True, null=True)
    sc_order = models.IntegerField(blank=True, null=True)
    sc_emp_id = models.CharField(max_length=5, blank=True, null=True)
    sc_comm_pe = models.FloatField(blank=True, null=True)
    sc_comm_am = models.FloatField(blank=True, null=True)
    sc_comm_pa = models.NullBooleanField()
    sc_paid_am = models.FloatField(blank=True, null=True)
    sc_gl_com_field = models.CharField(db_column='sc_gl_com_', max_length=12, blank=True, null=True)  # Field renamed because it ended with '_'.
    sc_gl_com2 = models.CharField(max_length=12, blank=True, null=True)
    sc_ex_gl_i = models.CharField(max_length=10, blank=True, null=True)
    sc_py_gl_i = models.CharField(max_length=10, blank=True, null=True)
    sc_dr_id = models.CharField(max_length=10, blank=True, null=True)
    sc_gl_com3 = models.CharField(max_length=12, blank=True, null=True)
    sc_gl_com4 = models.CharField(max_length=12, blank=True, null=True)
    sc_ipy_gl_field = models.CharField(db_column='sc_ipy_gl_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    sc_epy_gl_field = models.CharField(db_column='sc_epy_gl_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    sc_correct = models.NullBooleanField()
    sc_correc2 = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salescom'


class Salesrep(models.Model):
    sr_id = models.CharField(max_length=10, blank=True, null=True)
    sr_tr_id = models.CharField(max_length=10, blank=True, null=True)
    sr_emp_id = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesrep'


class Scard(models.Model):
    sc_run_dat = models.DateField(blank=True, null=True)
    sc_card_st = models.CharField(max_length=1, blank=True, null=True)
    sc_emp_id = models.CharField(max_length=5, blank=True, null=True)
    sc_tot_tim = models.FloatField(blank=True, null=True)
    sc_time_ca = models.CharField(max_length=2, blank=True, null=True)
    sc_time_c2 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_c3 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_c4 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_c5 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_c6 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_c7 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_c8 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_c9 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_10 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_11 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_12 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_13 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_14 = models.CharField(max_length=2, blank=True, null=True)
    sc_time_15 = models.CharField(max_length=2, blank=True, null=True)
    sc_time1 = models.CharField(max_length=10, blank=True, null=True)
    sc_time2 = models.CharField(max_length=10, blank=True, null=True)
    sc_time3 = models.CharField(max_length=10, blank=True, null=True)
    sc_time4 = models.CharField(max_length=10, blank=True, null=True)
    sc_time5 = models.CharField(max_length=10, blank=True, null=True)
    sc_time6 = models.CharField(max_length=10, blank=True, null=True)
    sc_time7 = models.CharField(max_length=10, blank=True, null=True)
    sc_time8 = models.CharField(max_length=10, blank=True, null=True)
    sc_time9 = models.CharField(max_length=10, blank=True, null=True)
    sc_time10 = models.CharField(max_length=10, blank=True, null=True)
    sc_time11 = models.CharField(max_length=10, blank=True, null=True)
    sc_time12 = models.CharField(max_length=10, blank=True, null=True)
    sc_time13 = models.CharField(max_length=10, blank=True, null=True)
    sc_time14 = models.CharField(max_length=10, blank=True, null=True)
    sc_time15 = models.CharField(max_length=10, blank=True, null=True)
    sc_date1 = models.DateField(blank=True, null=True)
    sc_date2 = models.DateField(blank=True, null=True)
    sc_date3 = models.DateField(blank=True, null=True)
    sc_date4 = models.DateField(blank=True, null=True)
    sc_date5 = models.DateField(blank=True, null=True)
    sc_date6 = models.DateField(blank=True, null=True)
    sc_date7 = models.DateField(blank=True, null=True)
    sc_date8 = models.DateField(blank=True, null=True)
    sc_date9 = models.DateField(blank=True, null=True)
    sc_date10 = models.DateField(blank=True, null=True)
    sc_date11 = models.DateField(blank=True, null=True)
    sc_date12 = models.DateField(blank=True, null=True)
    sc_date13 = models.DateField(blank=True, null=True)
    sc_date14 = models.DateField(blank=True, null=True)
    sc_date15 = models.DateField(blank=True, null=True)
    sc_sec1 = models.IntegerField(blank=True, null=True)
    sc_sec2 = models.IntegerField(blank=True, null=True)
    sc_sec3 = models.IntegerField(blank=True, null=True)
    sc_sec4 = models.IntegerField(blank=True, null=True)
    sc_sec5 = models.IntegerField(blank=True, null=True)
    sc_sec6 = models.IntegerField(blank=True, null=True)
    sc_sec7 = models.IntegerField(blank=True, null=True)
    sc_sec8 = models.IntegerField(blank=True, null=True)
    sc_sec9 = models.IntegerField(blank=True, null=True)
    sc_sec10 = models.IntegerField(blank=True, null=True)
    sc_sec11 = models.IntegerField(blank=True, null=True)
    sc_sec12 = models.IntegerField(blank=True, null=True)
    sc_sec13 = models.IntegerField(blank=True, null=True)
    sc_sec14 = models.IntegerField(blank=True, null=True)
    sc_sec15 = models.IntegerField(blank=True, null=True)
    sc_elap1 = models.FloatField(blank=True, null=True)
    sc_elap2 = models.FloatField(blank=True, null=True)
    sc_elap3 = models.FloatField(blank=True, null=True)
    sc_elap4 = models.FloatField(blank=True, null=True)
    sc_elap5 = models.FloatField(blank=True, null=True)
    sc_elap6 = models.FloatField(blank=True, null=True)
    sc_elap7 = models.FloatField(blank=True, null=True)
    sc_elap8 = models.FloatField(blank=True, null=True)
    sc_elap9 = models.FloatField(blank=True, null=True)
    sc_elap10 = models.FloatField(blank=True, null=True)
    sc_elap11 = models.FloatField(blank=True, null=True)
    sc_elap12 = models.FloatField(blank=True, null=True)
    sc_elap13 = models.FloatField(blank=True, null=True)
    sc_elap14 = models.FloatField(blank=True, null=True)
    sc_elap15 = models.FloatField(blank=True, null=True)
    sc_shift = models.CharField(max_length=2, blank=True, null=True)
    sc_time_mi = models.FloatField(blank=True, null=True)
    sc_er_code = models.CharField(max_length=3, blank=True, null=True)
    sc_da_id_1 = models.CharField(max_length=10, blank=True, null=True)
    sc_date_is = models.DateField(blank=True, null=True)
    sc_issued_field = models.CharField(db_column='sc_issued_', max_length=5, blank=True, null=True)  # Field renamed because it ended with '_'.
    sc_da_id_2 = models.CharField(max_length=10, blank=True, null=True)
    sc_date_i2 = models.DateField(blank=True, null=True)
    sc_issued2 = models.CharField(max_length=5, blank=True, null=True)
    sc_note_1 = models.TextField(blank=True, null=True)
    sc_note_2 = models.TextField(blank=True, null=True)
    sc_da_id_3 = models.CharField(max_length=10, blank=True, null=True)
    sc_date_i3 = models.DateField(blank=True, null=True)
    sc_issued3 = models.CharField(max_length=5, blank=True, null=True)
    sc_note_3 = models.TextField(blank=True, null=True)
    sc_er_cod2 = models.CharField(max_length=3, blank=True, null=True)
    sc_er_cod3 = models.CharField(max_length=3, blank=True, null=True)
    sc_da_id_0 = models.CharField(max_length=10, blank=True, null=True)
    sc_date_i4 = models.DateField(blank=True, null=True)
    sc_issued4 = models.CharField(max_length=5, blank=True, null=True)
    sc_note_0 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scard'


class Schboard(models.Model):
    sb_name = models.CharField(max_length=30, blank=True, null=True)
    sb_is_edit = models.NullBooleanField()
    sb_needs_r = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'schboard'


class Schedule(models.Model):
    sd_run_cod = models.CharField(max_length=20, blank=True, null=True)
    sd_mach_co = models.CharField(max_length=5, blank=True, null=True)
    sd_order_n = models.CharField(max_length=12, blank=True, null=True)
    sd_operati = models.IntegerField(blank=True, null=True)
    sd_rel_num = models.IntegerField(blank=True, null=True)
    sd_qty_sch = models.FloatField(blank=True, null=True)
    sd_start_d = models.DateField(blank=True, null=True)
    sd_new_sta = models.DateField(blank=True, null=True)
    sd_inc_su = models.CharField(max_length=1, blank=True, null=True)
    sd_slip_da = models.IntegerField(blank=True, null=True)
    sd_est_net = models.FloatField(blank=True, null=True)
    sd_act_net = models.FloatField(blank=True, null=True)
    sd_end_dat = models.DateField(blank=True, null=True)
    sd_rev_eda = models.DateField(blank=True, null=True)
    sd_parts_p = models.FloatField(blank=True, null=True)
    sd_qty_bal = models.FloatField(blank=True, null=True)
    sd_hrs_nee = models.FloatField(blank=True, null=True)
    sd_su_rema = models.FloatField(blank=True, null=True)
    sd_hrs_rem = models.FloatField(blank=True, null=True)
    sd_hrs_ava = models.FloatField(blank=True, null=True)
    sd_hrs_set = models.FloatField(blank=True, null=True)
    sd_hrs_tot = models.FloatField(blank=True, null=True)
    sd_hrs_tdo = models.FloatField(blank=True, null=True)
    sd_hrs_odo = models.FloatField(blank=True, null=True)
    sd_hrs_pro = models.FloatField(blank=True, null=True)
    sd_parts_g = models.FloatField(blank=True, null=True)
    sd_parts_b = models.FloatField(blank=True, null=True)
    sd_gp = models.FloatField(blank=True, null=True)
    sd_np = models.FloatField(blank=True, null=True)
    sd_act_phr = models.FloatField(blank=True, null=True)
    sd_adj_phr = models.FloatField(blank=True, null=True)
    sd_go_eff = models.IntegerField(blank=True, null=True)
    sd_p_eff = models.IntegerField(blank=True, null=True)
    sd_su_eff = models.IntegerField(blank=True, null=True)
    sd_ppbar = models.FloatField(blank=True, null=True)
    sd_act_ppb = models.IntegerField(blank=True, null=True)
    sd_in_inve = models.CharField(max_length=30, blank=True, null=True)
    sd_out_inv = models.CharField(max_length=30, blank=True, null=True)
    sd_req_bar = models.IntegerField(blank=True, null=True)
    sd_rework = models.FloatField(blank=True, null=True)
    sd_scrap = models.FloatField(blank=True, null=True)
    sd_notes = models.TextField(blank=True, null=True)
    sd_sl = models.TextField(blank=True, null=True)
    sd_ph = models.CharField(max_length=1, blank=True, null=True)
    sd_lock = models.NullBooleanField()
    sd_status = models.CharField(max_length=1, blank=True, null=True)
    sd_ss_sord = models.CharField(max_length=7, blank=True, null=True)
    sd_ss_line = models.IntegerField(blank=True, null=True)
    sd_ss_rel_field = models.IntegerField(db_column='sd_ss_rel_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sd_ss_due_field = models.DateField(db_column='sd_ss_due_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sd_emp_id = models.CharField(max_length=5, blank=True, null=True)
    sd_quote_n = models.CharField(max_length=15, blank=True, null=True)
    sd_op_op_n = models.IntegerField(blank=True, null=True)
    sd_type = models.IntegerField(blank=True, null=True)
    sd_bufferh = models.FloatField(blank=True, null=True)
    sd_isnewqu = models.NullBooleanField()
    sd_isorder = models.NullBooleanField()
    sd_isquote = models.NullBooleanField()
    sd_isfroze = models.NullBooleanField()
    sd_tools = models.NullBooleanField()
    sd_materia = models.NullBooleanField()
    sd_fai = models.NullBooleanField()
    sd_qualtit = models.NullBooleanField()
    sd_custome = models.NullBooleanField()
    sd_late = models.NullBooleanField()
    sd_latecus = models.NullBooleanField()
    sd_oreleas = models.CharField(max_length=15, blank=True, null=True)
    sd_is_froz = models.NullBooleanField()
    sd_mats = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class SchemaInfo(models.Model):
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'schema_info'


class Schgroup(models.Model):
    sg_g_code = models.CharField(max_length=10, blank=True, null=True)
    sg_g_desc = models.CharField(max_length=30, blank=True, null=True)
    sg_file = models.CharField(max_length=80, blank=True, null=True)
    sg_mach_op = models.NullBooleanField()
    sg_rate = models.FloatField(blank=True, null=True)
    sg_indexti = models.FloatField(blank=True, null=True)
    sg_toothco = models.IntegerField(blank=True, null=True)
    sg_toothc2 = models.IntegerField(blank=True, null=True)
    sg_toothc3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schgroup'


class Scraprec(models.Model):
    sr_id = models.CharField(max_length=10, blank=True, null=True)
    sr_order_n = models.CharField(max_length=12, blank=True, null=True)
    sr_date = models.DateField(blank=True, null=True)
    sr_desc = models.CharField(max_length=60, blank=True, null=True)
    sr_amount = models.FloatField(blank=True, null=True)
    sr_weight = models.FloatField(blank=True, null=True)
    sr_value = models.FloatField(blank=True, null=True)
    sr_jc_id = models.CharField(max_length=10, blank=True, null=True)
    sr_item = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scraprec'


class Search(models.Model):
    sc_form = models.CharField(max_length=15, blank=True, null=True)
    sc_user = models.CharField(max_length=5, blank=True, null=True)
    sc_criteri = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search'


class Servprnt(models.Model):
    sp_id = models.IntegerField(blank=True, null=True)
    sp_desc = models.CharField(max_length=40, blank=True, null=True)
    sp_printer = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servprnt'


class Shifts(models.Model):
    sf_code = models.CharField(max_length=2, blank=True, null=True)
    sf_desc = models.CharField(max_length=40, blank=True, null=True)
    sf_shift_s = models.CharField(max_length=8, blank=True, null=True)
    sf_shift_e = models.CharField(max_length=8, blank=True, null=True)
    sf_shift_t = models.FloatField(blank=True, null=True)
    sf_group = models.CharField(max_length=1, blank=True, null=True)
    sf_start_e = models.CharField(max_length=8, blank=True, null=True)
    sf_start_l = models.CharField(max_length=8, blank=True, null=True)
    sf_end_ear = models.CharField(max_length=8, blank=True, null=True)
    sf_end_lat = models.CharField(max_length=8, blank=True, null=True)
    sf_daily_o = models.FloatField(blank=True, null=True)
    sf_daily_d = models.FloatField(blank=True, null=True)
    sf_weekly_field = models.FloatField(db_column='sf_weekly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sf_weekly2 = models.FloatField(blank=True, null=True)
    sf_lunch_s = models.CharField(max_length=8, blank=True, null=True)
    sf_lunch_e = models.CharField(max_length=8, blank=True, null=True)
    sf_break1_field = models.CharField(db_column='sf_break1_', max_length=8, blank=True, null=True)  # Field renamed because it ended with '_'.
    sf_break12 = models.CharField(max_length=8, blank=True, null=True)
    sf_break2_field = models.CharField(db_column='sf_break2_', max_length=8, blank=True, null=True)  # Field renamed because it ended with '_'.
    sf_break22 = models.CharField(max_length=8, blank=True, null=True)
    sf_break3_field = models.CharField(db_column='sf_break3_', max_length=8, blank=True, null=True)  # Field renamed because it ended with '_'.
    sf_break32 = models.CharField(max_length=8, blank=True, null=True)
    sf_break4_field = models.CharField(db_column='sf_break4_', max_length=8, blank=True, null=True)  # Field renamed because it ended with '_'.
    sf_break42 = models.CharField(max_length=8, blank=True, null=True)
    sf_break5_field = models.CharField(db_column='sf_break5_', max_length=8, blank=True, null=True)  # Field renamed because it ended with '_'.
    sf_break52 = models.CharField(max_length=8, blank=True, null=True)
    sf_break13 = models.CharField(max_length=2, blank=True, null=True)
    sf_break23 = models.CharField(max_length=2, blank=True, null=True)
    sf_break33 = models.CharField(max_length=2, blank=True, null=True)
    sf_break43 = models.CharField(max_length=2, blank=True, null=True)
    sf_break53 = models.CharField(max_length=2, blank=True, null=True)
    sf_r_lim = models.IntegerField(blank=True, null=True)
    sf_min_lun = models.FloatField(blank=True, null=True)
    sf_auto_lu = models.NullBooleanField()
    sf_mon = models.NullBooleanField()
    sf_tue = models.NullBooleanField()
    sf_wed = models.NullBooleanField()
    sf_thu = models.NullBooleanField()
    sf_fri = models.NullBooleanField()
    sf_sat = models.NullBooleanField()
    sf_sun = models.NullBooleanField()
    sf_hol = models.NullBooleanField()
    sf_mon_rat = models.CharField(max_length=1, blank=True, null=True)
    sf_tue_rat = models.CharField(max_length=1, blank=True, null=True)
    sf_wed_rat = models.CharField(max_length=1, blank=True, null=True)
    sf_thu_rat = models.CharField(max_length=1, blank=True, null=True)
    sf_fri_rat = models.CharField(max_length=1, blank=True, null=True)
    sf_sat_rat = models.CharField(max_length=1, blank=True, null=True)
    sf_sun_rat = models.CharField(max_length=1, blank=True, null=True)
    sf_hol_rat = models.CharField(max_length=1, blank=True, null=True)
    sf_inactiv = models.NullBooleanField()
    sf_lunch_t = models.NullBooleanField()
    sf_lunch_j = models.NullBooleanField()
    sf_biweekl = models.NullBooleanField()
    sf_biweek2 = models.FloatField(blank=True, null=True)
    sf_biweek3 = models.FloatField(blank=True, null=True)
    sf_pr_id_1 = models.CharField(max_length=10, blank=True, null=True)
    sf_pr_id_2 = models.CharField(max_length=10, blank=True, null=True)
    sf_sun_ot = models.FloatField(blank=True, null=True)
    sf_sun_dot = models.FloatField(blank=True, null=True)
    sf_mon_ot = models.FloatField(blank=True, null=True)
    sf_mon_dot = models.FloatField(blank=True, null=True)
    sf_tue_ot = models.FloatField(blank=True, null=True)
    sf_tue_dot = models.FloatField(blank=True, null=True)
    sf_wed_ot = models.FloatField(blank=True, null=True)
    sf_wed_dot = models.FloatField(blank=True, null=True)
    sf_thu_ot = models.FloatField(blank=True, null=True)
    sf_thu_dot = models.FloatField(blank=True, null=True)
    sf_fri_ot = models.FloatField(blank=True, null=True)
    sf_fri_dot = models.FloatField(blank=True, null=True)
    sf_sat_ot = models.FloatField(blank=True, null=True)
    sf_sat_dot = models.FloatField(blank=True, null=True)
    sf_hol_ot = models.FloatField(blank=True, null=True)
    sf_hol_dot = models.FloatField(blank=True, null=True)
    sf_mon_sta = models.CharField(max_length=8, blank=True, null=True)
    sf_tue_sta = models.CharField(max_length=8, blank=True, null=True)
    sf_wed_sta = models.CharField(max_length=8, blank=True, null=True)
    sf_thu_sta = models.CharField(max_length=8, blank=True, null=True)
    sf_fri_sta = models.CharField(max_length=8, blank=True, null=True)
    sf_sat_sta = models.CharField(max_length=8, blank=True, null=True)
    sf_sun_sta = models.CharField(max_length=8, blank=True, null=True)
    sf_hol_sta = models.CharField(max_length=8, blank=True, null=True)
    sf_mon_end = models.CharField(max_length=8, blank=True, null=True)
    sf_tue_end = models.CharField(max_length=8, blank=True, null=True)
    sf_wed_end = models.CharField(max_length=8, blank=True, null=True)
    sf_thu_end = models.CharField(max_length=8, blank=True, null=True)
    sf_fri_end = models.CharField(max_length=8, blank=True, null=True)
    sf_sat_end = models.CharField(max_length=8, blank=True, null=True)
    sf_sun_end = models.CharField(max_length=8, blank=True, null=True)
    sf_hol_end = models.CharField(max_length=8, blank=True, null=True)
    sf_grace_s = models.FloatField(blank=True, null=True)
    sf_grace_2 = models.FloatField(blank=True, null=True)
    sf_grace_e = models.FloatField(blank=True, null=True)
    sf_grace_3 = models.FloatField(blank=True, null=True)
    sf_grace_l = models.FloatField(blank=True, null=True)
    sf_nightsh = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'shifts'


class ShipAb(models.Model):
    sb_ship_co = models.CharField(max_length=6, blank=True, null=True)
    sb_carrier = models.CharField(max_length=10, blank=True, null=True)
    sb_descrip = models.CharField(max_length=60, blank=True, null=True)
    sb_fee = models.FloatField(blank=True, null=True)
    sb_per = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ship_ab'


class ShipDet(models.Model):
    sd_id = models.IntegerField(blank=True, null=True)
    sd_ship_co = models.CharField(max_length=8, blank=True, null=True)
    sd_ship_da = models.DateField(blank=True, null=True)
    sd_order_n = models.CharField(max_length=12, blank=True, null=True)
    sd_rel_num = models.IntegerField(blank=True, null=True)
    sd_rel_dat = models.DateField(blank=True, null=True)
    sd_rel_qty = models.FloatField(blank=True, null=True)
    sd_order_s = models.CharField(max_length=1, blank=True, null=True)
    sd_unit_ty = models.IntegerField(blank=True, null=True)
    sd_invent_field = models.CharField(db_column='sd_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    sd_part_nu = models.CharField(max_length=30, blank=True, null=True)
    sd_rev_num = models.CharField(max_length=6, blank=True, null=True)
    sd_desc = models.CharField(max_length=50, blank=True, null=True)
    sd_pmemo = models.TextField(blank=True, null=True)
    sd_ship_no = models.TextField(blank=True, null=True)
    sd_po_num = models.CharField(max_length=25, blank=True, null=True)
    sd_ship_c2 = models.NullBooleanField()
    sd_sb1 = models.IntegerField(blank=True, null=True)
    sd_sb2 = models.IntegerField(blank=True, null=True)
    sd_sb3 = models.IntegerField(blank=True, null=True)
    sd_sb4 = models.IntegerField(blank=True, null=True)
    sd_sb5 = models.IntegerField(blank=True, null=True)
    sd_eb1 = models.IntegerField(blank=True, null=True)
    sd_eb2 = models.IntegerField(blank=True, null=True)
    sd_eb3 = models.IntegerField(blank=True, null=True)
    sd_eb4 = models.IntegerField(blank=True, null=True)
    sd_eb5 = models.IntegerField(blank=True, null=True)
    sd_bq1 = models.FloatField(blank=True, null=True)
    sd_bq2 = models.FloatField(blank=True, null=True)
    sd_bq3 = models.FloatField(blank=True, null=True)
    sd_bq4 = models.FloatField(blank=True, null=True)
    sd_bq5 = models.FloatField(blank=True, null=True)
    sd_tb1 = models.IntegerField(blank=True, null=True)
    sd_tb2 = models.IntegerField(blank=True, null=True)
    sd_tb3 = models.IntegerField(blank=True, null=True)
    sd_tb4 = models.IntegerField(blank=True, null=True)
    sd_tb5 = models.IntegerField(blank=True, null=True)
    sd_weight1 = models.FloatField(blank=True, null=True)
    sd_weight2 = models.FloatField(blank=True, null=True)
    sd_weight3 = models.FloatField(blank=True, null=True)
    sd_weight4 = models.FloatField(blank=True, null=True)
    sd_weight5 = models.FloatField(blank=True, null=True)
    sd_totw1 = models.FloatField(blank=True, null=True)
    sd_totw2 = models.FloatField(blank=True, null=True)
    sd_totw3 = models.FloatField(blank=True, null=True)
    sd_totw4 = models.FloatField(blank=True, null=True)
    sd_totw5 = models.FloatField(blank=True, null=True)
    sd_totp1 = models.FloatField(blank=True, null=True)
    sd_totp2 = models.FloatField(blank=True, null=True)
    sd_totp3 = models.FloatField(blank=True, null=True)
    sd_totp4 = models.FloatField(blank=True, null=True)
    sd_totp5 = models.FloatField(blank=True, null=True)
    sd_tot_qty = models.FloatField(blank=True, null=True)
    sd_bo_qty = models.FloatField(blank=True, null=True)
    sd_tot_wei = models.FloatField(blank=True, null=True)
    sd_tot_box = models.IntegerField(blank=True, null=True)
    sd_tare = models.FloatField(blank=True, null=True)
    sd_tare_ty = models.CharField(max_length=1, blank=True, null=True)
    sd_gt_tare = models.FloatField(blank=True, null=True)
    sd_tot_car = models.IntegerField(blank=True, null=True)
    sd_weight = models.FloatField(blank=True, null=True)
    sd_gt_weig = models.FloatField(blank=True, null=True)
    sd_num_car = models.IntegerField(blank=True, null=True)
    sd_num_ski = models.IntegerField(blank=True, null=True)
    sd_derive_field = models.NullBooleanField(db_column='sd_derive_')  # Field renamed because it ended with '_'.
    sd_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    sd_sord_re = models.IntegerField(blank=True, null=True)
    sd_ij_id = models.CharField(max_length=10, blank=True, null=True)
    sd_sord_r2 = models.IntegerField(blank=True, null=True)
    sd_sord_r3 = models.DateField(blank=True, null=True)
    sd_sord_co = models.NullBooleanField()
    sd_sord_st = models.CharField(max_length=1, blank=True, null=True)
    sd_return = models.NullBooleanField()
    sd_il_id = models.CharField(max_length=10, blank=True, null=True)
    sd_ib_id = models.CharField(max_length=10, blank=True, null=True)
    sd_contact = models.CharField(max_length=25, blank=True, null=True)
    sd_il_id_f = models.CharField(max_length=10, blank=True, null=True)
    sd_ib_id_f = models.CharField(max_length=10, blank=True, null=True)
    sd_lot_shi = models.CharField(max_length=20, blank=True, null=True)
    sd_so_unit = models.CharField(max_length=4, blank=True, null=True)
    sd_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    sd_lot_num = models.CharField(max_length=20, blank=True, null=True)
    sd_user_id = models.CharField(max_length=5, blank=True, null=True)
    sd_last_mo = models.DateTimeField(blank=True, null=True)
    sd_dont_po = models.NullBooleanField()
    sd_cm_flag = models.CharField(max_length=1, blank=True, null=True)
    sd_cm_num = models.CharField(max_length=7, blank=True, null=True)
    sd_select_field = models.NullBooleanField(db_column='sd_select_')  # Field renamed because it ended with '_'.
    sd_exp_pro = models.CharField(max_length=40, blank=True, null=True)
    sd_exp_tar = models.CharField(max_length=20, blank=True, null=True)
    sd_exp_cnt = models.CharField(max_length=20, blank=True, null=True)
    sd_exp_par = models.NullBooleanField()
    sd_exp_con = models.NullBooleanField()
    sd_exp_dut = models.IntegerField(blank=True, null=True)
    sd_exp_exp = models.CharField(max_length=80, blank=True, null=True)
    sd_exp_pri = models.NullBooleanField()
    sd_exp_pr2 = models.NullBooleanField()
    sd_exp_pr3 = models.NullBooleanField()
    sd_complet = models.NullBooleanField()
    sd_length = models.FloatField(blank=True, null=True)
    sd_width = models.FloatField(blank=True, null=True)
    sd_quantit = models.FloatField(blank=True, null=True)
    sd_wght = models.FloatField(blank=True, null=True)
    sd_rev_nu2 = models.CharField(max_length=3, blank=True, null=True)
    sd_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    sd_who_res = models.CharField(max_length=10, blank=True, null=True)
    sd_how_res = models.IntegerField(blank=True, null=True)
    sd_ls_code = models.CharField(max_length=10, blank=True, null=True)
    sd_lo_code = models.CharField(max_length=10, blank=True, null=True)
    sd_cert_no = models.TextField(blank=True, null=True)
    sd_sord_r4 = models.IntegerField(blank=True, null=True)
    sd_bt_code = models.CharField(max_length=3, blank=True, null=True)
    sd_noresup = models.NullBooleanField()
    sd_receive = models.CharField(max_length=12, blank=True, null=True)
    sd_transfe = models.NullBooleanField()
    sd_bl1 = models.FloatField(blank=True, null=True)
    sd_bl2 = models.FloatField(blank=True, null=True)
    sd_bl3 = models.FloatField(blank=True, null=True)
    sd_bl4 = models.FloatField(blank=True, null=True)
    sd_bl5 = models.FloatField(blank=True, null=True)
    sd_bw1 = models.FloatField(blank=True, null=True)
    sd_bw2 = models.FloatField(blank=True, null=True)
    sd_bw3 = models.FloatField(blank=True, null=True)
    sd_bw4 = models.FloatField(blank=True, null=True)
    sd_bw5 = models.FloatField(blank=True, null=True)
    sd_bd1 = models.FloatField(blank=True, null=True)
    sd_bd2 = models.FloatField(blank=True, null=True)
    sd_bd3 = models.FloatField(blank=True, null=True)
    sd_bd4 = models.FloatField(blank=True, null=True)
    sd_bd5 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ship_det'


class ShipVia(models.Model):
    sv_id = models.CharField(max_length=10, blank=True, null=True)
    sv_desc = models.CharField(max_length=20, blank=True, null=True)
    sv_bol = models.NullBooleanField()
    sv_surchar = models.FloatField(blank=True, null=True)
    sv_parent = models.CharField(max_length=10, blank=True, null=True)
    sv_ship_ty = models.CharField(max_length=20, blank=True, null=True)
    sv_contact = models.CharField(max_length=25, blank=True, null=True)
    sv_phone = models.CharField(max_length=14, blank=True, null=True)
    sv_scac = models.CharField(max_length=6, blank=True, null=True)
    sv_edi_mod = models.CharField(max_length=2, blank=True, null=True)
    sv_edi_eq_field = models.CharField(db_column='sv_edi_eq_', max_length=2, blank=True, null=True)  # Field renamed because it ended with '_'.
    sv_markup = models.IntegerField(blank=True, null=True)
    sv_note = models.TextField(blank=True, null=True)
    sv_obsolet = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ship_via'


class Shipping(models.Model):
    sh_ship_co = models.CharField(max_length=8, blank=True, null=True)
    sh_ship_da = models.DateField(blank=True, null=True)
    sh_cust_co = models.CharField(max_length=6, blank=True, null=True)
    sh_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    sh_tot_box = models.IntegerField(blank=True, null=True)
    sh_tot_wei = models.IntegerField(blank=True, null=True)
    sh_tot_car = models.IntegerField(blank=True, null=True)
    sh_tot_qty = models.IntegerField(blank=True, null=True)
    sh_emp_id = models.CharField(max_length=5, blank=True, null=True)
    sh_ship_vi = models.CharField(max_length=40, blank=True, null=True)
    sh_inv_fla = models.CharField(max_length=1, blank=True, null=True)
    sh_ship_no = models.TextField(blank=True, null=True)
    sh_gt_skid = models.IntegerField(blank=True, null=True)
    sh_gt_cart = models.IntegerField(blank=True, null=True)
    sh_gt_boxe = models.IntegerField(blank=True, null=True)
    sh_gt_qty = models.IntegerField(blank=True, null=True)
    sh_gt_w = models.FloatField(blank=True, null=True)
    sh_gt_tare = models.FloatField(blank=True, null=True)
    sh_gt_gtw = models.FloatField(blank=True, null=True)
    sh_inv_num = models.CharField(max_length=7, blank=True, null=True)
    sh_comp_na = models.CharField(max_length=35, blank=True, null=True)
    sh_address = models.CharField(max_length=35, blank=True, null=True)
    sh_addres2 = models.CharField(max_length=35, blank=True, null=True)
    sh_addres3 = models.CharField(max_length=35, blank=True, null=True)
    sh_track_n = models.CharField(max_length=40, blank=True, null=True)
    sh_bol_num = models.CharField(max_length=10, blank=True, null=True)
    sh_prepaid = models.NullBooleanField()
    sh_lo_code = models.CharField(max_length=10, blank=True, null=True)
    sh_positio = models.CharField(max_length=12, blank=True, null=True)
    sh_ship_ch = models.FloatField(blank=True, null=True)
    sh_consign = models.NullBooleanField()
    sh_consig2 = models.IntegerField(blank=True, null=True)
    sh_consig3 = models.DateField(blank=True, null=True)
    sh_consig4 = models.NullBooleanField()
    sh_consig5 = models.CharField(max_length=10, blank=True, null=True)
    sh_ship_ty = models.CharField(max_length=1, blank=True, null=True)
    sh_dest_zi = models.CharField(max_length=10, blank=True, null=True)
    sh_ship_me = models.CharField(max_length=20, blank=True, null=True)
    sh_misc_de = models.CharField(max_length=30, blank=True, null=True)
    sh_misc_am = models.FloatField(blank=True, null=True)
    sh_residen = models.NullBooleanField()
    sh_hundred = models.NullBooleanField()
    sh_user_id = models.CharField(max_length=5, blank=True, null=True)
    sh_last_mo = models.DateTimeField(blank=True, null=True)
    sh_prepay_field = models.IntegerField(db_column='sh_prepay_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sh_plist_p = models.NullBooleanField()
    sh_prem_fr = models.FloatField(blank=True, null=True)
    sh_premf_n = models.TextField(blank=True, null=True)
    sh_markup = models.IntegerField(blank=True, null=True)
    sh_fr_pric = models.FloatField(blank=True, null=True)
    sh_addres4 = models.CharField(max_length=35, blank=True, null=True)
    sh_ca_id = models.CharField(max_length=10, blank=True, null=True)
    sh_edi_pur = models.CharField(max_length=2, blank=True, null=True)
    sh_edi_gw = models.FloatField(blank=True, null=True)
    sh_edi_gw_field = models.CharField(db_column='sh_edi_gw_', max_length=2, blank=True, null=True)  # Field renamed because it ended with '_'.
    sh_edi_nw = models.FloatField(blank=True, null=True)
    sh_edi_nw_field = models.CharField(db_column='sh_edi_nw_', max_length=2, blank=True, null=True)  # Field renamed because it ended with '_'.
    sh_edi_pkg = models.CharField(max_length=5, blank=True, null=True)
    sh_edi_lad = models.IntegerField(blank=True, null=True)
    sh_edi_sca = models.CharField(max_length=17, blank=True, null=True)
    sh_edi_mod = models.CharField(max_length=2, blank=True, null=True)
    sh_edi_loc = models.CharField(max_length=2, blank=True, null=True)
    sh_edi_lo2 = models.CharField(max_length=5, blank=True, null=True)
    sh_edi_shi = models.DateField(blank=True, null=True)
    sh_edi_sh2 = models.CharField(max_length=5, blank=True, null=True)
    sh_edi_asn = models.IntegerField(blank=True, null=True)
    sh_edi_as2 = models.DateField(blank=True, null=True)
    sh_edi_as3 = models.CharField(max_length=5, blank=True, null=True)
    sh_edi_eq_field = models.CharField(db_column='sh_edi_eq_', max_length=2, blank=True, null=True)  # Field renamed because it ended with '_'.
    sh_edi_eq2 = models.CharField(max_length=4, blank=True, null=True)
    sh_edi_eq3 = models.CharField(max_length=10, blank=True, null=True)
    sh_edi_rq_field = models.CharField(db_column='sh_edi_rq_', max_length=2, blank=True, null=True)  # Field renamed because it ended with '_'.
    sh_edi_rq2 = models.CharField(max_length=2, blank=True, null=True)
    sh_edi_rq3 = models.CharField(max_length=2, blank=True, null=True)
    sh_edi_rq4 = models.CharField(max_length=2, blank=True, null=True)
    sh_edi_ref = models.CharField(max_length=30, blank=True, null=True)
    sh_edi_re2 = models.CharField(max_length=30, blank=True, null=True)
    sh_edi_re3 = models.CharField(max_length=30, blank=True, null=True)
    sh_edi_re4 = models.CharField(max_length=30, blank=True, null=True)
    sh_edi_ic_field = models.NullBooleanField(db_column='sh_edi_ic_')  # Field renamed because it ended with '_'.
    sh_edi_ic2 = models.CharField(max_length=5, blank=True, null=True)
    sh_edi_ic3 = models.CharField(max_length=2, blank=True, null=True)
    sh_edi_fob = models.CharField(max_length=2, blank=True, null=True)
    sh_edi_fo2 = models.CharField(max_length=6, blank=True, null=True)
    sh_edi_fo3 = models.CharField(max_length=2, blank=True, null=True)
    sh_line = models.CharField(max_length=7, blank=True, null=True)
    sh_auth = models.CharField(max_length=5, blank=True, null=True)
    sh_inv_nu2 = models.CharField(max_length=7, blank=True, null=True)
    sh_nc_id = models.CharField(max_length=10, blank=True, null=True)
    sh_class = models.CharField(max_length=10, blank=True, null=True)
    sh_qty_not = models.TextField(blank=True, null=True)
    sh_bol_not = models.TextField(blank=True, null=True)
    sh_cod_amo = models.FloatField(blank=True, null=True)
    sh_hot = models.NullBooleanField()
    sh_asn_gen = models.NullBooleanField()
    sh_void = models.NullBooleanField()
    sh_collect = models.CharField(max_length=30, blank=True, null=True)
    sh_credith = models.NullBooleanField()
    sh_approve = models.NullBooleanField()
    alt_comp_n = models.CharField(max_length=35, blank=True, null=True)
    alt_addres = models.CharField(max_length=35, blank=True, null=True)
    alt_addre2 = models.CharField(max_length=35, blank=True, null=True)
    alt_addre3 = models.CharField(max_length=35, blank=True, null=True)
    alt_addre4 = models.CharField(max_length=35, blank=True, null=True)
    third_comp = models.CharField(max_length=35, blank=True, null=True)
    third_addr = models.CharField(max_length=35, blank=True, null=True)
    third_add2 = models.CharField(max_length=35, blank=True, null=True)
    third_add3 = models.CharField(max_length=35, blank=True, null=True)
    third_add4 = models.CharField(max_length=35, blank=True, null=True)
    sh_transfe = models.CharField(max_length=10, blank=True, null=True)
    sh_suffixs = models.IntegerField(blank=True, null=True)
    sh_import_field = models.DateField(db_column='sh_import_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sh_bol_exp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping'


class Shiptype(models.Model):
    sh_ship_ty = models.CharField(max_length=20, blank=True, null=True)
    sh_carrier = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shiptype'


class ShopCon(models.Model):
    sp_mach_na = models.CharField(max_length=10, blank=True, null=True)
    sp_mach_co = models.CharField(max_length=5, blank=True, null=True)
    sp_mach_de = models.CharField(max_length=20, blank=True, null=True)
    sp_il_code = models.CharField(max_length=10, blank=True, null=True)
    sp_type = models.CharField(max_length=1, blank=True, null=True)
    sp_x = models.IntegerField(blank=True, null=True)
    sp_y = models.IntegerField(blank=True, null=True)
    sp_image = models.CharField(max_length=80, blank=True, null=True)
    sp_width = models.IntegerField(blank=True, null=True)
    sp_height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_con'


class Shoploc(models.Model):
    sl_locatio = models.CharField(max_length=15, blank=True, null=True)
    sl_emp_id = models.CharField(max_length=5, blank=True, null=True)
    sl_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shoploc'


class Shoptalk(models.Model):
    st_id = models.CharField(max_length=10, blank=True, null=True)
    st_emp_id = models.CharField(max_length=5, blank=True, null=True)
    st_datetim = models.DateTimeField(blank=True, null=True)
    st_order_n = models.CharField(max_length=12, blank=True, null=True)
    st_invent_field = models.CharField(db_column='st_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    st_cust_co = models.CharField(max_length=6, blank=True, null=True)
    st_supp_co = models.CharField(max_length=6, blank=True, null=True)
    st_comment = models.TextField(blank=True, null=True)
    st_mach_co = models.CharField(max_length=5, blank=True, null=True)
    st_part_nu = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shoptalk'


class Sobom(models.Model):
    so_id = models.CharField(max_length=10, blank=True, null=True)
    sordnum = models.CharField(max_length=7, blank=True, null=True)
    soforecast = models.NullBooleanField()
    linenum = models.IntegerField(blank=True, null=True)
    relnum = models.IntegerField(blank=True, null=True)
    clevel = models.IntegerField(blank=True, null=True)
    clevel_lin = models.CharField(max_length=2, blank=True, null=True)
    bomnode = models.IntegerField(blank=True, null=True)
    inventnum = models.CharField(max_length=30, blank=True, null=True)
    invent_typ = models.CharField(max_length=5, blank=True, null=True)
    partnum = models.CharField(max_length=30, blank=True, null=True)
    make_buy = models.CharField(max_length=4, blank=True, null=True)
    iv_supp_co = models.CharField(max_length=6, blank=True, null=True)
    iv_planner = models.CharField(max_length=5, blank=True, null=True)
    exclfrommr = models.NullBooleanField()
    purchunit = models.CharField(max_length=2, blank=True, null=True)
    calctype = models.CharField(max_length=2, blank=True, null=True)
    alloc = models.NullBooleanField()
    iv_stock_u = models.CharField(max_length=15, blank=True, null=True)
    iv_purch_u = models.CharField(max_length=15, blank=True, null=True)
    partcnt = models.FloatField(blank=True, null=True)
    partdesc = models.CharField(max_length=50, blank=True, null=True)
    shipdate = models.DateField(blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    promdate = models.DateField(blank=True, null=True)
    shipbydate = models.DateField(blank=True, null=True)
    fabdate = models.DateField(blank=True, null=True)
    relqty = models.FloatField(blank=True, null=True)
    qtybal = models.FloatField(blank=True, null=True)
    qtyneed = models.FloatField(blank=True, null=True)
    qtytoprod = models.FloatField(blank=True, null=True)
    reolevel = models.FloatField(blank=True, null=True)
    reoqty = models.FloatField(blank=True, null=True)
    qtyonhand = models.FloatField(blank=True, null=True)
    leadtime = models.IntegerField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    parentp = models.CharField(max_length=30, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    iv_date_1 = models.DateField(blank=True, null=True)
    iv_date_2 = models.DateField(blank=True, null=True)
    iv_date_3 = models.DateField(blank=True, null=True)
    iv_date_4 = models.DateField(blank=True, null=True)
    iv_date_5 = models.DateField(blank=True, null=True)
    iv_date_6 = models.DateField(blank=True, null=True)
    iv_date_7 = models.DateField(blank=True, null=True)
    iv_date_8 = models.DateField(blank=True, null=True)
    iv_date_9 = models.DateField(blank=True, null=True)
    iv_date_10 = models.DateField(blank=True, null=True)
    iv_date_11 = models.DateField(blank=True, null=True)
    iv_date_12 = models.DateField(blank=True, null=True)
    iv_date_13 = models.DateField(blank=True, null=True)
    iv_date_14 = models.DateField(blank=True, null=True)
    iv_date_15 = models.DateField(blank=True, null=True)
    iv_date_16 = models.DateField(blank=True, null=True)
    iv_date_17 = models.DateField(blank=True, null=True)
    iv_date_18 = models.DateField(blank=True, null=True)
    iv_date_19 = models.DateField(blank=True, null=True)
    iv_date_20 = models.DateField(blank=True, null=True)
    iv_date_21 = models.DateField(blank=True, null=True)
    iv_date_22 = models.DateField(blank=True, null=True)
    iv_date_23 = models.DateField(blank=True, null=True)
    iv_date_24 = models.DateField(blank=True, null=True)
    iv_date_25 = models.DateField(blank=True, null=True)
    iv_date_26 = models.DateField(blank=True, null=True)
    iv_date_27 = models.DateField(blank=True, null=True)
    iv_date_28 = models.DateField(blank=True, null=True)
    iv_date_29 = models.DateField(blank=True, null=True)
    iv_date_30 = models.DateField(blank=True, null=True)
    iv_date_31 = models.DateField(blank=True, null=True)
    iv_date_32 = models.DateField(blank=True, null=True)
    iv_date_33 = models.DateField(blank=True, null=True)
    iv_date_34 = models.DateField(blank=True, null=True)
    iv_date_35 = models.DateField(blank=True, null=True)
    iv_date_36 = models.DateField(blank=True, null=True)
    iv_qty_1 = models.FloatField(blank=True, null=True)
    iv_qty_2 = models.FloatField(blank=True, null=True)
    iv_qty_3 = models.FloatField(blank=True, null=True)
    iv_qty_4 = models.FloatField(blank=True, null=True)
    iv_qty_5 = models.FloatField(blank=True, null=True)
    iv_qty_6 = models.FloatField(blank=True, null=True)
    iv_qty_7 = models.FloatField(blank=True, null=True)
    iv_qty_8 = models.FloatField(blank=True, null=True)
    iv_qty_9 = models.FloatField(blank=True, null=True)
    iv_qty_10 = models.FloatField(blank=True, null=True)
    iv_qty_11 = models.FloatField(blank=True, null=True)
    iv_qty_12 = models.FloatField(blank=True, null=True)
    iv_qty_13 = models.FloatField(blank=True, null=True)
    iv_qty_14 = models.FloatField(blank=True, null=True)
    iv_qty_15 = models.FloatField(blank=True, null=True)
    iv_qty_16 = models.FloatField(blank=True, null=True)
    iv_qty_17 = models.FloatField(blank=True, null=True)
    iv_qty_18 = models.FloatField(blank=True, null=True)
    iv_qty_19 = models.FloatField(blank=True, null=True)
    iv_qty_20 = models.FloatField(blank=True, null=True)
    iv_qty_21 = models.FloatField(blank=True, null=True)
    iv_qty_22 = models.FloatField(blank=True, null=True)
    iv_qty_23 = models.FloatField(blank=True, null=True)
    iv_qty_24 = models.FloatField(blank=True, null=True)
    iv_qty_25 = models.FloatField(blank=True, null=True)
    iv_qty_26 = models.FloatField(blank=True, null=True)
    iv_qty_27 = models.FloatField(blank=True, null=True)
    iv_qty_28 = models.FloatField(blank=True, null=True)
    iv_qty_29 = models.FloatField(blank=True, null=True)
    iv_qty_30 = models.FloatField(blank=True, null=True)
    iv_qty_31 = models.FloatField(blank=True, null=True)
    iv_qty_32 = models.FloatField(blank=True, null=True)
    iv_qty_33 = models.FloatField(blank=True, null=True)
    iv_qty_34 = models.FloatField(blank=True, null=True)
    iv_qty_35 = models.FloatField(blank=True, null=True)
    iv_qty_36 = models.FloatField(blank=True, null=True)
    iv_onhand_field = models.FloatField(db_column='iv_onhand_', blank=True, null=True)  # Field renamed because it ended with '_'.
    iv_onhand2 = models.FloatField(blank=True, null=True)
    iv_onhand3 = models.FloatField(blank=True, null=True)
    iv_onhand4 = models.FloatField(blank=True, null=True)
    iv_onhand5 = models.FloatField(blank=True, null=True)
    iv_onhand6 = models.FloatField(blank=True, null=True)
    iv_onhand7 = models.FloatField(blank=True, null=True)
    iv_onhand8 = models.FloatField(blank=True, null=True)
    iv_onhand9 = models.FloatField(blank=True, null=True)
    iv_onhan10 = models.FloatField(blank=True, null=True)
    iv_onhan11 = models.FloatField(blank=True, null=True)
    iv_onhan12 = models.FloatField(blank=True, null=True)
    iv_onhan13 = models.FloatField(blank=True, null=True)
    iv_onhan14 = models.FloatField(blank=True, null=True)
    iv_onhan15 = models.FloatField(blank=True, null=True)
    iv_onhan16 = models.FloatField(blank=True, null=True)
    iv_onhan17 = models.FloatField(blank=True, null=True)
    iv_onhan18 = models.FloatField(blank=True, null=True)
    iv_onhan19 = models.FloatField(blank=True, null=True)
    iv_onhan20 = models.FloatField(blank=True, null=True)
    iv_onhan21 = models.FloatField(blank=True, null=True)
    iv_onhan22 = models.FloatField(blank=True, null=True)
    iv_onhan23 = models.FloatField(blank=True, null=True)
    iv_onhan24 = models.FloatField(blank=True, null=True)
    iv_onhan25 = models.FloatField(blank=True, null=True)
    iv_onhan26 = models.FloatField(blank=True, null=True)
    iv_onhan27 = models.FloatField(blank=True, null=True)
    iv_onhan28 = models.FloatField(blank=True, null=True)
    iv_onhan29 = models.FloatField(blank=True, null=True)
    iv_onhan30 = models.FloatField(blank=True, null=True)
    iv_onhan31 = models.FloatField(blank=True, null=True)
    iv_onhan32 = models.FloatField(blank=True, null=True)
    iv_onhan33 = models.FloatField(blank=True, null=True)
    iv_onhan34 = models.FloatField(blank=True, null=True)
    iv_onhan35 = models.FloatField(blank=True, null=True)
    iv_onhan36 = models.FloatField(blank=True, null=True)
    iv_balreq_field = models.FloatField(db_column='iv_balreq_', blank=True, null=True)  # Field renamed because it ended with '_'.
    iv_balreq2 = models.FloatField(blank=True, null=True)
    iv_balreq3 = models.FloatField(blank=True, null=True)
    iv_balreq4 = models.FloatField(blank=True, null=True)
    iv_balreq5 = models.FloatField(blank=True, null=True)
    iv_balreq6 = models.FloatField(blank=True, null=True)
    iv_balreq7 = models.FloatField(blank=True, null=True)
    iv_balreq8 = models.FloatField(blank=True, null=True)
    iv_balreq9 = models.FloatField(blank=True, null=True)
    iv_balre10 = models.FloatField(blank=True, null=True)
    iv_balre11 = models.FloatField(blank=True, null=True)
    iv_balre12 = models.FloatField(blank=True, null=True)
    iv_balre13 = models.FloatField(blank=True, null=True)
    iv_balre14 = models.FloatField(blank=True, null=True)
    iv_balre15 = models.FloatField(blank=True, null=True)
    iv_balre16 = models.FloatField(blank=True, null=True)
    iv_balre17 = models.FloatField(blank=True, null=True)
    iv_balre18 = models.FloatField(blank=True, null=True)
    iv_balre19 = models.FloatField(blank=True, null=True)
    iv_balre20 = models.FloatField(blank=True, null=True)
    iv_balre21 = models.FloatField(blank=True, null=True)
    iv_balre22 = models.FloatField(blank=True, null=True)
    iv_balre23 = models.FloatField(blank=True, null=True)
    iv_balre24 = models.FloatField(blank=True, null=True)
    iv_balre25 = models.FloatField(blank=True, null=True)
    iv_balre26 = models.FloatField(blank=True, null=True)
    iv_balre27 = models.FloatField(blank=True, null=True)
    iv_balre28 = models.FloatField(blank=True, null=True)
    iv_balre29 = models.FloatField(blank=True, null=True)
    iv_balre30 = models.FloatField(blank=True, null=True)
    iv_balre31 = models.FloatField(blank=True, null=True)
    iv_balre32 = models.FloatField(blank=True, null=True)
    iv_balre33 = models.FloatField(blank=True, null=True)
    iv_balre34 = models.FloatField(blank=True, null=True)
    iv_balre35 = models.FloatField(blank=True, null=True)
    iv_balre36 = models.FloatField(blank=True, null=True)
    iv_onorder = models.FloatField(blank=True, null=True)
    iv_onorde2 = models.FloatField(blank=True, null=True)
    iv_onorde3 = models.FloatField(blank=True, null=True)
    iv_onorde4 = models.FloatField(blank=True, null=True)
    iv_onorde5 = models.FloatField(blank=True, null=True)
    iv_onorde6 = models.FloatField(blank=True, null=True)
    iv_onorde7 = models.FloatField(blank=True, null=True)
    iv_onorde8 = models.FloatField(blank=True, null=True)
    iv_onorde9 = models.FloatField(blank=True, null=True)
    iv_onord10 = models.FloatField(blank=True, null=True)
    iv_onord11 = models.FloatField(blank=True, null=True)
    iv_onord12 = models.FloatField(blank=True, null=True)
    iv_onord13 = models.FloatField(blank=True, null=True)
    iv_onord14 = models.FloatField(blank=True, null=True)
    iv_onord15 = models.FloatField(blank=True, null=True)
    iv_onord16 = models.FloatField(blank=True, null=True)
    iv_onord17 = models.FloatField(blank=True, null=True)
    iv_onord18 = models.FloatField(blank=True, null=True)
    iv_onord19 = models.FloatField(blank=True, null=True)
    iv_onord20 = models.FloatField(blank=True, null=True)
    iv_onord21 = models.FloatField(blank=True, null=True)
    iv_onord22 = models.FloatField(blank=True, null=True)
    iv_onord23 = models.FloatField(blank=True, null=True)
    iv_onord24 = models.FloatField(blank=True, null=True)
    iv_onord25 = models.FloatField(blank=True, null=True)
    iv_onord26 = models.FloatField(blank=True, null=True)
    iv_onord27 = models.FloatField(blank=True, null=True)
    iv_onord28 = models.FloatField(blank=True, null=True)
    iv_onord29 = models.FloatField(blank=True, null=True)
    iv_onord30 = models.FloatField(blank=True, null=True)
    iv_onord31 = models.FloatField(blank=True, null=True)
    iv_onord32 = models.FloatField(blank=True, null=True)
    iv_onord33 = models.FloatField(blank=True, null=True)
    iv_onord34 = models.FloatField(blank=True, null=True)
    iv_onord35 = models.FloatField(blank=True, null=True)
    iv_onord36 = models.FloatField(blank=True, null=True)
    so_po_num = models.CharField(max_length=25, blank=True, null=True)
    ss_confirm = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'sobom'


class Sodetlot(models.Model):
    sl_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    sl_line_nu = models.IntegerField(blank=True, null=True)
    sl_ic_id = models.CharField(max_length=10, blank=True, null=True)
    sl_ic_quan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sodetlot'


class Sopicked(models.Model):
    sp_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    sp_lo_code = models.CharField(max_length=10, blank=True, null=True)
    sp_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sopicked'


class Sord(models.Model):
    so_sord_nu = models.CharField(max_length=7, blank=True, primary_key=True)
    so_inv_num = models.CharField(max_length=7, blank=True, null=True)
    so_inv_dat = models.DateField(blank=True, null=True)
    so_cust_co = models.CharField(max_length=6, blank=True, null=True)
    so_batch = models.CharField(max_length=1, blank=True, null=True)
    so_print_d = models.DateField(blank=True, null=True)
    so_ship_vi = models.CharField(max_length=40, blank=True, null=True)
    so_net_amt = models.FloatField(blank=True, null=True)
    so_taxes = models.FloatField(blank=True, null=True)
    so_tot_amt = models.FloatField(blank=True, null=True)
    so_post = models.CharField(max_length=1, blank=True, null=True)
    so_post_da = models.DateField(blank=True, null=True)
    so_comp_na = models.CharField(max_length=33, blank=True, null=True)
    so_address = models.CharField(max_length=33, blank=True, null=True)
    so_addres2 = models.CharField(max_length=33, blank=True, null=True)
    so_addres3 = models.CharField(max_length=33, blank=True, null=True)
    so_ship_da = models.DateField(blank=True, null=True)
    so_po_num = models.CharField(max_length=25, blank=True, null=True)
    so_inv_sta = models.CharField(max_length=1, blank=True, null=True)
    so_contact = models.CharField(max_length=25, blank=True, null=True)
    so_emp_id = models.CharField(max_length=5, blank=True, null=True)
    so_pay_ter = models.CharField(max_length=20, blank=True, null=True)
    so_lo_code = models.CharField(max_length=10, blank=True, null=True)
    so_prepaid = models.NullBooleanField()
    so_discoun = models.FloatField(blank=True, null=True)
    so_isquote = models.NullBooleanField()
    so_rec_dat = models.DateField(blank=True, null=True)
    so_consign = models.NullBooleanField()
    so_entered = models.CharField(max_length=5, blank=True, null=True)
    so_note = models.TextField(blank=True, null=True)
    so_ship_co = models.NullBooleanField()
    so_consig2 = models.NullBooleanField()
    so_consig3 = models.IntegerField(blank=True, null=True)
    so_consig4 = models.CharField(max_length=10, blank=True, null=True)
    so_ship_to = models.CharField(max_length=3, blank=True, null=True)
    so_ship_ty = models.CharField(max_length=1, blank=True, null=True)
    so_progres = models.NullBooleanField()
    so_user_id = models.CharField(max_length=5, blank=True, null=True)
    so_last_mo = models.DateTimeField(blank=True, null=True)
    so_st_id_1 = models.CharField(max_length=10, blank=True, null=True)
    so_st_id_2 = models.CharField(max_length=10, blank=True, null=True)
    so_stax_id = models.CharField(max_length=25, blank=True, null=True)
    so_tax_exe = models.NullBooleanField()
    so_exempt_field = models.CharField(db_column='so_exempt_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    so_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    so_cur_rat = models.FloatField(blank=True, null=True)
    so_net_cur = models.FloatField(blank=True, null=True)
    so_tax_cur = models.FloatField(blank=True, null=True)
    so_tot_cur = models.FloatField(blank=True, null=True)
    so_disc_cu = models.FloatField(blank=True, null=True)
    so_prepay_field = models.IntegerField(db_column='so_prepay_', blank=True, null=True)  # Field renamed because it ended with '_'.
    so_abbr_na = models.CharField(max_length=15, blank=True, null=True)
    so_addres4 = models.CharField(max_length=33, blank=True, null=True)
    so_rev_ste = models.IntegerField(blank=True, null=True)
    so_type = models.IntegerField(blank=True, null=True)
    so_ca_id = models.CharField(max_length=10, blank=True, null=True)
    so_surchar = models.FloatField(blank=True, null=True)
    so_surch_c = models.FloatField(blank=True, null=True)
    so_grs_amt = models.FloatField(blank=True, null=True)
    so_grs_cur = models.FloatField(blank=True, null=True)
    so_rec_sor = models.NullBooleanField()
    so_standin = models.CharField(max_length=7, blank=True, null=True)
    so_rev = models.IntegerField(blank=True, null=True)
    so_phone = models.CharField(max_length=14, blank=True, null=True)
    so_fax = models.CharField(max_length=14, blank=True, null=True)
    so_backlog = models.NullBooleanField()
    so_expire_field = models.DateField(db_column='so_expire_', blank=True, null=True)  # Field renamed because it ended with '_'.
    so_enforce = models.NullBooleanField()
    so_use_sur = models.NullBooleanField()
    so_fob = models.CharField(max_length=15, blank=True, null=True)
    so_billto_field = models.CharField(db_column='so_billto_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    so_sumbill = models.NullBooleanField()
    so_ch_over = models.NullBooleanField()
    so_foblabe = models.CharField(max_length=3, blank=True, null=True)
    so_closed_field = models.DateField(db_column='so_closed_', blank=True, null=True)  # Field renamed because it ended with '_'.
    so_exc_jhr = models.NullBooleanField()
    so_approve = models.NullBooleanField()
    so_edi_co_field = models.CharField(db_column='so_edi_co_', max_length=25, blank=True, null=True)  # Field renamed because it ended with '_'.
    so_edi_855 = models.DateField(blank=True, null=True)
    so_collect = models.CharField(max_length=30, blank=True, null=True)
    so_forecas = models.NullBooleanField()
    so_apprv_b = models.CharField(max_length=5, blank=True, null=True)
    so_apprv_s = models.CharField(max_length=1, blank=True, null=True)
    so_appr_da = models.DateField(blank=True, null=True)
    so_appr_me = models.TextField(blank=True, null=True)
    so_asnemai = models.TextField(blank=True, null=True)
    so_followu = models.DateField(blank=True, null=True)

    def calculate_status(self):
        status_dict = {
            'O': 'Open',
            'C': 'Closed'
        }

        return status_dict[self.so_inv_sta]

    status = property(calculate_status)

    class Meta:
        managed = False
        db_table = 'sord'


class SordBom(models.Model):
    sb_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    sb_line_nu = models.IntegerField(blank=True, null=True)
    parent = models.CharField(max_length=30, blank=True, null=True)
    part_num = models.CharField(max_length=30, blank=True, null=True)
    sb_quote_n = models.CharField(max_length=15, blank=True, null=True)
    sb_order_n = models.CharField(max_length=12, blank=True, null=True)
    sb_pr_id = models.IntegerField(blank=True, null=True)
    count = models.FloatField(blank=True, null=True)
    nocost = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'sord_bom'


class SordDet(models.Model):
    sd_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    sd_inv_num = models.CharField(max_length=7, blank=True, null=True)
    sd_line_nu = models.IntegerField(blank=True, null=True)
    sd_tran_ty = models.CharField(max_length=2, blank=True, null=True)
    sd_quote_n = models.CharField(max_length=15, blank=True, null=True)
    sd_invent_field = models.CharField(db_column='sd_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    sd_ship_co = models.CharField(max_length=8, blank=True, null=True)
    sd_desc = models.CharField(max_length=50, blank=True, null=True)
    sd_prod_co = models.CharField(max_length=2, blank=True, null=True)
    sd_qty_ord = models.FloatField(blank=True, null=True)
    sd_qty_shi = models.FloatField(blank=True, null=True)
    sd_qty_bo = models.FloatField(blank=True, null=True)
    sd_unit_ty = models.CharField(max_length=4, blank=True, null=True)
    sd_unit_pr = models.FloatField(blank=True, null=True)
    sd_discoun = models.FloatField(blank=True, null=True)
    sd_disc_pr = models.FloatField(blank=True, null=True)
    sd_ext_pri = models.FloatField(blank=True, null=True)
    sd_te = models.CharField(max_length=1, blank=True, null=True)
    sd_note = models.TextField(blank=True, null=True)
    sd_note_fl = models.CharField(max_length=1, blank=True, null=True)
    sd_order_n = models.CharField(max_length=12, blank=True, null=True)
    sd_rel_dat = models.DateField(blank=True, null=True)
    sd_po_num = models.CharField(max_length=15, blank=True, null=True)
    sd_rel_qty = models.FloatField(blank=True, null=True)
    sd_qty_all = models.FloatField(blank=True, null=True)
    sd_qq = models.IntegerField(blank=True, null=True)
    sd_part_nu = models.CharField(max_length=30, blank=True, null=True)
    sd_rev_num = models.CharField(max_length=6, blank=True, null=True)
    sd_ext_uni = models.FloatField(blank=True, null=True)
    sd_pmemo = models.TextField(blank=True, null=True)
    sd_tax_rat = models.FloatField(blank=True, null=True)
    sd_contact = models.CharField(max_length=25, blank=True, null=True)
    sd_st_id = models.CharField(max_length=10, blank=True, null=True)
    sd_emp_id = models.CharField(max_length=5, blank=True, null=True)
    sd_comm_fl = models.NullBooleanField()
    sd_comm_pe = models.FloatField(blank=True, null=True)
    sd_comm_am = models.FloatField(blank=True, null=True)
    sd_user_id = models.CharField(max_length=5, blank=True, null=True)
    sd_last_mo = models.DateTimeField(blank=True, null=True)
    sd_unit_cu = models.FloatField(blank=True, null=True)
    sd_disc_cu = models.FloatField(blank=True, null=True)
    sd_ext_cur = models.FloatField(blank=True, null=True)
    sd_extu_cu = models.FloatField(blank=True, null=True)
    sd_gm_dock = models.CharField(max_length=12, blank=True, null=True)
    sd_gm_math = models.CharField(max_length=10, blank=True, null=True)
    sd_gm_ref = models.CharField(max_length=10, blank=True, null=True)
    sd_gm_cont = models.CharField(max_length=15, blank=True, null=True)
    sd_gm_z13 = models.CharField(max_length=20, blank=True, null=True)
    sd_gm_z14 = models.CharField(max_length=20, blank=True, null=True)
    sd_gm_z15 = models.CharField(max_length=20, blank=True, null=True)
    sd_gm_z16 = models.CharField(max_length=20, blank=True, null=True)
    sd_gm_z17 = models.CharField(max_length=20, blank=True, null=True)
    sd_gm_lice = models.CharField(max_length=30, blank=True, null=True)
    sd_gm_gros = models.CharField(max_length=15, blank=True, null=True)
    sd_gm_pcs_field = models.CharField(db_column='sd_gm_pcs_', max_length=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    sd_il_id = models.CharField(max_length=10, blank=True, null=True)
    sd_ib_id = models.CharField(max_length=10, blank=True, null=True)
    sd_lot_num = models.CharField(max_length=20, blank=True, null=True)
    sd_heat_nu = models.CharField(max_length=30, blank=True, null=True)
    sd_backflu = models.NullBooleanField()
    sd_decimal = models.IntegerField(blank=True, null=True)
    sd_roll_in = models.FloatField(blank=True, null=True)
    sd_roll_ou = models.FloatField(blank=True, null=True)
    sd_sheet_w = models.FloatField(blank=True, null=True)
    sd_sheet_l = models.FloatField(blank=True, null=True)
    sd_sheet_c = models.FloatField(blank=True, null=True)
    sd_price_p = models.FloatField(blank=True, null=True)
    sd_sheet_g = models.CharField(max_length=1, blank=True, null=True)
    sd_dont_as = models.NullBooleanField()
    sd_emp_id2 = models.CharField(max_length=5, blank=True, null=True)
    sd_comm_p2 = models.FloatField(blank=True, null=True)
    sd_comm_a2 = models.FloatField(blank=True, null=True)
    sd_lo_code = models.CharField(max_length=10, blank=True, null=True)
    sd_overrid = models.NullBooleanField()
    sd_req_cof = models.NullBooleanField()
    sd_req_mat = models.NullBooleanField()
    sd_req_plc = models.NullBooleanField()
    sd_req_htc = models.NullBooleanField()
    sd_surchar = models.FloatField(blank=True, null=True)
    sd_surch_c = models.FloatField(blank=True, null=True)
    sd_multi_r = models.NullBooleanField()
    sd_serial_field = models.CharField(db_column='sd_serial_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    sd_ser_typ = models.IntegerField(blank=True, null=True)
    sd_seriali = models.NullBooleanField()
    sd_exp_pro = models.CharField(max_length=40, blank=True, null=True)
    sd_exp_tar = models.CharField(max_length=20, blank=True, null=True)
    sd_exp_cnt = models.CharField(max_length=20, blank=True, null=True)
    sd_exp_par = models.NullBooleanField()
    sd_exp_con = models.NullBooleanField()
    sd_exp_dut = models.IntegerField(blank=True, null=True)
    sd_exp_exp = models.CharField(max_length=80, blank=True, null=True)
    sd_exp_pri = models.NullBooleanField()
    sd_exp_pr2 = models.NullBooleanField()
    sd_exp_pr3 = models.NullBooleanField()
    sd_prod_li = models.CharField(max_length=30, blank=True, null=True)
    sd_exclude = models.NullBooleanField()
    sd_customi = models.FloatField(blank=True, null=True)
    sd_comp_na = models.CharField(max_length=33, blank=True, null=True)
    sd_address = models.CharField(max_length=33, blank=True, null=True)
    sd_addres2 = models.CharField(max_length=33, blank=True, null=True)
    sd_addres3 = models.CharField(max_length=33, blank=True, null=True)
    sd_addres4 = models.CharField(max_length=33, blank=True, null=True)
    sd_ca_id = models.CharField(max_length=10, blank=True, null=True)
    sd_length = models.FloatField(blank=True, null=True)
    sd_width = models.FloatField(blank=True, null=True)
    sd_quantit = models.FloatField(blank=True, null=True)
    sd_wght = models.FloatField(blank=True, null=True)
    sd_po_line = models.CharField(max_length=7, blank=True, null=True)
    sd_complet = models.NullBooleanField()
    sd_rev_lev = models.CharField(max_length=3, blank=True, null=True)
    sd_recurri = models.NullBooleanField()
    sd_mu_gm = models.IntegerField(blank=True, null=True)
    sd_confcos = models.NullBooleanField()
    sd_dont_po = models.NullBooleanField()
    sd_holes = models.IntegerField(blank=True, null=True)
    sd_stock_i = models.NullBooleanField()
    sd_pr_inst = models.CharField(max_length=30, blank=True, null=True)
    sd_alterna = models.FloatField(blank=True, null=True)
    sd_edi_ack = models.CharField(max_length=2, blank=True, null=True)
    sd_edi_qty = models.FloatField(blank=True, null=True)
    sd_return_field = models.FloatField(db_column='sd_return_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sd_return = models.NullBooleanField()
    sd_return2 = models.FloatField(blank=True, null=True)
    sd_rma = models.CharField(max_length=10, blank=True, null=True)
    sd_return3 = models.TextField(blank=True, null=True)
    sd_return4 = models.CharField(max_length=8, blank=True, null=True)
    sd_gm_tran = models.NullBooleanField()
    sd_qtyuom = models.CharField(max_length=4, blank=True, null=True)
    sd_ccnote = models.TextField(blank=True, null=True)
    sd_receive = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sord_det'


class SordDs(models.Model):
    ss_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    ss_line_nu = models.IntegerField(blank=True, null=True)
    ss_rel_num = models.IntegerField(blank=True, null=True)
    ss_due_dat = models.DateField(blank=True, null=True)
    ss_status = models.CharField(max_length=1, blank=True, null=True)
    ss_qty_rel = models.FloatField(blank=True, null=True)
    ss_prom_da = models.DateField(blank=True, null=True)
    ss_qty_pro = models.FloatField(blank=True, null=True)
    ss_qty_shi = models.FloatField(blank=True, null=True)
    ss_qty_bal = models.FloatField(blank=True, null=True)
    ss_po_num = models.CharField(max_length=25, blank=True, null=True)
    ss_confirm = models.NullBooleanField()
    ss_qty_cum = models.FloatField(blank=True, null=True)
    ss_red_sta = models.CharField(max_length=1, blank=True, null=True)
    ss_reviewe = models.NullBooleanField()
    ss_note = models.TextField(blank=True, null=True)
    ss_modifie = models.NullBooleanField()
    ss_shipby_field = models.DateField(db_column='ss_shipby_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ss_reset_c = models.NullBooleanField()
    ss_reset_2 = models.FloatField(blank=True, null=True)
    ss_earlies = models.DateField(blank=True, null=True)
    ss_latest_field = models.DateField(db_column='ss_latest_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ss_auth_co = models.CharField(max_length=5, blank=True, null=True)
    ss_dock_co = models.CharField(max_length=5, blank=True, null=True)
    ss_comp_na = models.CharField(max_length=35, blank=True, null=True)
    ss_address = models.CharField(max_length=35, blank=True, null=True)
    ss_addres2 = models.CharField(max_length=35, blank=True, null=True)
    ss_addres3 = models.CharField(max_length=35, blank=True, null=True)
    ss_addres4 = models.CharField(max_length=35, blank=True, null=True)
    ss_cust_co = models.CharField(max_length=6, blank=True, null=True)
    ss_ca_id = models.CharField(max_length=10, blank=True, null=True)
    ss_ca_stor = models.CharField(max_length=20, blank=True, null=True)
    ss_fab_dat = models.DateField(blank=True, null=True)
    ss_order_n = models.CharField(max_length=12, blank=True, null=True)
    ss_eng_sda = models.DateField(blank=True, null=True)
    ss_eng_eda = models.DateField(blank=True, null=True)
    ss_fab_sda = models.DateField(blank=True, null=True)
    ss_fab_eda = models.DateField(blank=True, null=True)
    ss_est_hrs = models.FloatField(blank=True, null=True)
    ss_clevel = models.IntegerField(blank=True, null=True)
    ss_receive = models.DateField(blank=True, null=True)
    ss_cust_re = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sord_ds'


class Sordcust(models.Model):
    sc_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    sc_line_nu = models.IntegerField(blank=True, null=True)
    sc_cust_co = models.CharField(max_length=6, blank=True, null=True)
    sc_quantit = models.IntegerField(blank=True, null=True)
    sc_percent = models.FloatField(blank=True, null=True)
    sc_fixedam = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sordcust'


class Sordq(models.Model):
    so_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    so_inv_num = models.CharField(max_length=7, blank=True, null=True)
    so_inv_dat = models.DateField(blank=True, null=True)
    so_cust_co = models.CharField(max_length=6, blank=True, null=True)
    so_batch = models.CharField(max_length=1, blank=True, null=True)
    so_print_d = models.DateField(blank=True, null=True)
    so_ship_vi = models.CharField(max_length=20, blank=True, null=True)
    so_net_amt = models.FloatField(blank=True, null=True)
    so_taxes = models.FloatField(blank=True, null=True)
    so_tot_amt = models.FloatField(blank=True, null=True)
    so_post = models.CharField(max_length=1, blank=True, null=True)
    so_post_da = models.DateField(blank=True, null=True)
    so_comp_na = models.CharField(max_length=33, blank=True, null=True)
    so_address = models.CharField(max_length=33, blank=True, null=True)
    so_addres2 = models.CharField(max_length=33, blank=True, null=True)
    so_addres3 = models.CharField(max_length=33, blank=True, null=True)
    so_ship_da = models.DateField(blank=True, null=True)
    so_po_num = models.CharField(max_length=25, blank=True, null=True)
    so_inv_sta = models.CharField(max_length=1, blank=True, null=True)
    so_contact = models.CharField(max_length=25, blank=True, null=True)
    so_emp_id = models.CharField(max_length=5, blank=True, null=True)
    so_pay_ter = models.CharField(max_length=20, blank=True, null=True)
    so_lo_code = models.CharField(max_length=10, blank=True, null=True)
    so_prepaid = models.NullBooleanField()
    so_discoun = models.FloatField(blank=True, null=True)
    so_isquote = models.NullBooleanField()
    so_rec_dat = models.DateField(blank=True, null=True)
    so_consign = models.NullBooleanField()
    so_entered = models.CharField(max_length=5, blank=True, null=True)
    so_note = models.TextField(blank=True, null=True)
    so_ship_co = models.NullBooleanField()
    so_consig2 = models.NullBooleanField()
    so_consig3 = models.IntegerField(blank=True, null=True)
    so_consig4 = models.CharField(max_length=10, blank=True, null=True)
    so_ship_to = models.CharField(max_length=3, blank=True, null=True)
    so_ship_ty = models.CharField(max_length=1, blank=True, null=True)
    so_progres = models.NullBooleanField()
    so_user_id = models.CharField(max_length=5, blank=True, null=True)
    so_last_mo = models.DateTimeField(blank=True, null=True)
    so_st_id_1 = models.CharField(max_length=10, blank=True, null=True)
    so_st_id_2 = models.CharField(max_length=10, blank=True, null=True)
    so_stax_id = models.CharField(max_length=25, blank=True, null=True)
    so_tax_exe = models.NullBooleanField()
    so_exempt_field = models.CharField(db_column='so_exempt_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    so_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    so_cur_rat = models.FloatField(blank=True, null=True)
    so_net_cur = models.FloatField(blank=True, null=True)
    so_tax_cur = models.FloatField(blank=True, null=True)
    so_tot_cur = models.FloatField(blank=True, null=True)
    so_disc_cu = models.FloatField(blank=True, null=True)
    so_prepay_field = models.IntegerField(db_column='so_prepay_', blank=True, null=True)  # Field renamed because it ended with '_'.
    so_abbr_na = models.CharField(max_length=15, blank=True, null=True)
    so_addres4 = models.CharField(max_length=33, blank=True, null=True)
    so_rev_ste = models.IntegerField(blank=True, null=True)
    so_type = models.IntegerField(blank=True, null=True)
    so_ca_id = models.CharField(max_length=13, blank=True, null=True)
    so_surchar = models.FloatField(blank=True, null=True)
    so_surch_c = models.FloatField(blank=True, null=True)
    so_grs_amt = models.FloatField(blank=True, null=True)
    so_grs_cur = models.FloatField(blank=True, null=True)
    so_rec_sor = models.NullBooleanField()
    so_standin = models.CharField(max_length=7, blank=True, null=True)
    so_rev = models.IntegerField(blank=True, null=True)
    so_phone = models.CharField(max_length=14, blank=True, null=True)
    so_fax = models.CharField(max_length=14, blank=True, null=True)
    so_backlog = models.NullBooleanField()
    so_expire_field = models.DateField(db_column='so_expire_', blank=True, null=True)  # Field renamed because it ended with '_'.
    so_enforce = models.NullBooleanField()
    so_use_sur = models.NullBooleanField()
    so_fob = models.CharField(max_length=15, blank=True, null=True)
    so_billto_field = models.CharField(db_column='so_billto_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    so_sumbill = models.NullBooleanField()
    so_ch_over = models.NullBooleanField()
    so_foblabe = models.CharField(max_length=3, blank=True, null=True)
    so_closed_field = models.DateField(db_column='so_closed_', blank=True, null=True)  # Field renamed because it ended with '_'.
    so_exc_jhr = models.NullBooleanField()
    so_approve = models.NullBooleanField()
    so_edi_co_field = models.CharField(db_column='so_edi_co_', max_length=25, blank=True, null=True)  # Field renamed because it ended with '_'.
    so_edi_855 = models.DateField(blank=True, null=True)
    so_disc_co = models.CharField(max_length=6, blank=True, null=True)
    so_collect = models.CharField(max_length=30, blank=True, null=True)
    so_deliver = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sordq'


class Specgrp(models.Model):
    sg_id = models.CharField(max_length=10, blank=True, null=True)
    sg_spec_gr = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specgrp'


class Specstds(models.Model):
    ss_id = models.CharField(max_length=10, blank=True, null=True)
    ss_sg_id = models.CharField(max_length=10, blank=True, null=True)
    ss_st_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specstds'


class Srelease(models.Model):
    sr_id = models.CharField(max_length=10, blank=True, null=True)
    sr_ship_co = models.CharField(max_length=8, blank=True, null=True)
    sr_sd_id = models.IntegerField(blank=True, null=True)
    sr_type = models.CharField(max_length=1, blank=True, null=True)
    sr_order_n = models.CharField(max_length=12, blank=True, null=True)
    sr_rel_num = models.IntegerField(blank=True, null=True)
    sr_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    sr_sord_re = models.IntegerField(blank=True, null=True)
    sr_sord_r2 = models.IntegerField(blank=True, null=True)
    sr_quantit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'srelease'


class State(models.Model):
    st_id = models.CharField(max_length=10, blank=True, null=True)
    st_co_id = models.CharField(max_length=10, blank=True, null=True)
    st_name = models.CharField(max_length=25, blank=True, null=True)
    st_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class States(models.Model):
    st_id = models.CharField(max_length=2, blank=True, null=True)
    st_name = models.CharField(max_length=25, blank=True, null=True)
    st_country = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'


class Stdsab(models.Model):
    sb_id = models.CharField(max_length=10, blank=True, null=True)
    sb_type = models.CharField(max_length=1, blank=True, null=True)
    sb_po_sord = models.CharField(max_length=7, blank=True, null=True)
    sb_line_nu = models.IntegerField(blank=True, null=True)
    sb_st_id = models.CharField(max_length=10, blank=True, null=True)
    sb_display = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'stdsab'


class Storebrd(models.Model):
    sb_id = models.CharField(max_length=10, blank=True, null=True)
    sb_store = models.CharField(max_length=20, blank=True, null=True)
    sb_ca_id = models.CharField(max_length=10, blank=True, null=True)
    sb_brand = models.CharField(max_length=40, blank=True, null=True)
    sb_style = models.CharField(max_length=40, blank=True, null=True)
    sb_backpan = models.CharField(max_length=20, blank=True, null=True)
    sb_active_field = models.DateField(db_column='sb_active_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sb_inactiv = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storebrd'


class Stylemat(models.Model):
    sm_id = models.CharField(max_length=6, blank=True, null=True)
    sm_st_id = models.CharField(max_length=6, blank=True, null=True)
    sm_st_code = models.CharField(max_length=25, blank=True, null=True)
    sm_ma_id = models.CharField(max_length=6, blank=True, null=True)
    sm_ma_code = models.CharField(max_length=30, blank=True, null=True)
    sm_seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stylemat'


class Styles(models.Model):
    st_id = models.CharField(max_length=6, blank=True, null=True)
    st_code = models.CharField(max_length=25, blank=True, null=True)
    st_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'styles'


class SuppAcc(models.Model):
    sc_supp_co = models.CharField(max_length=6, blank=True, null=True)
    sc_gl_num = models.CharField(max_length=12, blank=True, null=True)
    sc_percent = models.IntegerField(blank=True, null=True)
    sc_dist_co = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supp_acc'


class Suppa(models.Model):
    sa_id = models.CharField(max_length=10, blank=True, null=True)
    sa_supp_co = models.CharField(max_length=6, blank=True, null=True)
    sa_name = models.CharField(max_length=35, blank=True, null=True)
    sa_address = models.CharField(max_length=35, blank=True, null=True)
    sa_addres2 = models.CharField(max_length=35, blank=True, null=True)
    sa_city = models.CharField(max_length=30, blank=True, null=True)
    sa_state = models.CharField(max_length=2, blank=True, null=True)
    sa_zip = models.CharField(max_length=10, blank=True, null=True)
    sa_cntry = models.CharField(max_length=15, blank=True, null=True)
    sa_isremit = models.NullBooleanField()
    sa_phone = models.CharField(max_length=14, blank=True, null=True)
    sa_fax = models.CharField(max_length=14, blank=True, null=True)
    sa_contact = models.CharField(max_length=20, blank=True, null=True)
    sa_email = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppa'


class Supplier(models.Model):
    sp_supp_co = models.CharField(max_length=6, blank=True, null=True)
    sp_supp_na = models.CharField(max_length=35, blank=True, null=True)
    sp_contact = models.CharField(max_length=20, blank=True, null=True)
    sp_address = models.CharField(max_length=35, blank=True, null=True)
    sp_addres2 = models.CharField(max_length=35, blank=True, null=True)
    sp_city = models.CharField(max_length=30, blank=True, null=True)
    sp_state = models.CharField(max_length=3, blank=True, null=True)
    sp_zip = models.CharField(max_length=10, blank=True, null=True)
    sp_phone = models.CharField(max_length=14, blank=True, null=True)
    sp_fax = models.CharField(max_length=14, blank=True, null=True)
    sp_memo = models.TextField(blank=True, null=True)
    sp_def_mu = models.IntegerField(blank=True, null=True)
    sp_tax = models.FloatField(blank=True, null=True)
    sp_account = models.CharField(max_length=12, blank=True, null=True)
    sp_issuppl = models.NullBooleanField()
    sp_status = models.CharField(max_length=1, blank=True, null=True)
    sp_crlimit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sp_1099 = models.NullBooleanField()
    sp_1099_box = models.CharField(max_length=2, blank=True, null=True)
    sp_fedid = models.CharField(max_length=15, blank=True, null=True)
    sp_terms = models.CharField(max_length=20, blank=True, null=True)
    sp_poreqd = models.NullBooleanField()
    sp_email = models.CharField(max_length=40, blank=True, null=True)
    sp_min_cha = models.FloatField(blank=True, null=True)
    sp_supp_ty = models.CharField(max_length=4, blank=True, null=True)
    sp_app_sta = models.IntegerField(blank=True, null=True)
    sp_emp_id = models.CharField(max_length=5, blank=True, null=True)
    sp_app_dat = models.DateField(blank=True, null=True)
    sp_fob = models.CharField(max_length=15, blank=True, null=True)
    sp_ship_vi = models.CharField(max_length=20, blank=True, null=True)
    sp_website = models.CharField(max_length=100, blank=True, null=True)
    sp_dday_1 = models.NullBooleanField()
    sp_dday_2 = models.NullBooleanField()
    sp_dday_3 = models.NullBooleanField()
    sp_dday_4 = models.NullBooleanField()
    sp_dday_5 = models.NullBooleanField()
    sp_dday_6 = models.NullBooleanField()
    sp_dday_7 = models.NullBooleanField()
    sp_credit_field = models.NullBooleanField(db_column='sp_credit_')  # Field renamed because it ended with '_'.
    sp_acct_nu = models.CharField(max_length=30, blank=True, null=True)
    sp_rec_bal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sp_rec_dat = models.DateField(blank=True, null=True)
    sp_cur_cod = models.CharField(max_length=10, blank=True, null=True)
    sp_st_id_1 = models.CharField(max_length=10, blank=True, null=True)
    sp_st_id_2 = models.CharField(max_length=10, blank=True, null=True)
    sp_stax_id = models.CharField(max_length=25, blank=True, null=True)
    sp_tax_exe = models.NullBooleanField()
    sp_exempt_field = models.CharField(db_column='sp_exempt_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    sp_cust_co = models.CharField(max_length=20, blank=True, null=True)
    sp_def_per = models.NullBooleanField()
    sp_beg_bal = models.DateField(blank=True, null=True)
    sp_beg_ba2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sp_create_field = models.DateField(db_column='sp_create_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sp_exp_dat = models.DateField(blank=True, null=True)
    sp_cntry = models.CharField(max_length=25, blank=True, null=True)
    sp_lead_ti = models.IntegerField(blank=True, null=True)
    sp_blanket = models.CharField(max_length=20, blank=True, null=True)
    sp_electro = models.NullBooleanField()
    sp_cc_due_field = models.DateField(db_column='sp_cc_due_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sp_cc_bala = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sp_cc_ca_c = models.CharField(max_length=12, blank=True, null=True)
    sp_cc_limi = models.FloatField(blank=True, null=True)
    sp_fc_ca_c = models.CharField(max_length=12, blank=True, null=True)
    sp_exp_sup = models.CharField(max_length=12, blank=True, null=True)
    su_vet_cus = models.CharField(max_length=6, blank=True, null=True)
    sp_cc_due2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sp_cs_rec_field = models.DateField(db_column='sp_cs_rec_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sp_cs_rec2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sp_cs_due_field = models.DateField(db_column='sp_cs_due_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sp_cs_due2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sp_obsolet = models.NullBooleanField()
    sp_uses_po = models.NullBooleanField()
    sp_docktos = models.NullBooleanField()
    sp_email_p = models.NullBooleanField()
    sp_email_2 = models.CharField(max_length=40, blank=True, null=True)
    sp_freight = models.FloatField(blank=True, null=True)
    sp_freigh2 = models.FloatField(blank=True, null=True)
    sp_critica = models.NullBooleanField()
    sp_poalert = models.TextField(blank=True, null=True)
    sp_poaler2 = models.IntegerField(blank=True, null=True)
    sp_nopoale = models.NullBooleanField()
    sp_revisio = models.TextField(blank=True, null=True)
    sp_tier = models.CharField(max_length=20, blank=True, null=True)
    sp_late_al = models.IntegerField(blank=True, null=True)
    sp_autocri = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class Surftrea(models.Model):
    st_id = models.CharField(max_length=10, blank=True, null=True)
    st_code = models.CharField(max_length=1, blank=True, null=True)
    st_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surftrea'


class SvAtrb(models.Model):
    sc_id = models.CharField(max_length=10, blank=True, null=True)
    sc_ship_vi = models.CharField(max_length=20, blank=True, null=True)
    sc_vc_id = models.CharField(max_length=10, blank=True, null=True)
    sc_approve = models.NullBooleanField()
    sc_expires = models.DateField(blank=True, null=True)
    sc_desc = models.CharField(max_length=100, blank=True, null=True)
    sc_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sv_atrb'


class Tcard(models.Model):
    tc_run_dat = models.DateField(blank=True, null=True)
    tc_card_st = models.CharField(max_length=1, blank=True, null=True)
    tc_emp_id = models.CharField(max_length=5, blank=True, null=True)
    tc_tot_tim = models.FloatField(blank=True, null=True)
    tc_time_ca = models.CharField(max_length=2, blank=True, null=True)
    tc_time_c2 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_c3 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_c4 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_c5 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_c6 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_c7 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_c8 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_c9 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_10 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_11 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_12 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_13 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_14 = models.CharField(max_length=2, blank=True, null=True)
    tc_time_15 = models.CharField(max_length=2, blank=True, null=True)
    tc_time1 = models.CharField(max_length=10, blank=True, null=True)
    tc_time2 = models.CharField(max_length=10, blank=True, null=True)
    tc_time3 = models.CharField(max_length=10, blank=True, null=True)
    tc_time4 = models.CharField(max_length=10, blank=True, null=True)
    tc_time5 = models.CharField(max_length=10, blank=True, null=True)
    tc_time6 = models.CharField(max_length=10, blank=True, null=True)
    tc_time7 = models.CharField(max_length=10, blank=True, null=True)
    tc_time8 = models.CharField(max_length=10, blank=True, null=True)
    tc_time9 = models.CharField(max_length=10, blank=True, null=True)
    tc_time10 = models.CharField(max_length=10, blank=True, null=True)
    tc_time11 = models.CharField(max_length=10, blank=True, null=True)
    tc_time12 = models.CharField(max_length=10, blank=True, null=True)
    tc_time13 = models.CharField(max_length=10, blank=True, null=True)
    tc_time14 = models.CharField(max_length=10, blank=True, null=True)
    tc_time15 = models.CharField(max_length=10, blank=True, null=True)
    tc_date1 = models.DateField(blank=True, null=True)
    tc_date2 = models.DateField(blank=True, null=True)
    tc_date3 = models.DateField(blank=True, null=True)
    tc_date4 = models.DateField(blank=True, null=True)
    tc_date5 = models.DateField(blank=True, null=True)
    tc_date6 = models.DateField(blank=True, null=True)
    tc_date7 = models.DateField(blank=True, null=True)
    tc_date8 = models.DateField(blank=True, null=True)
    tc_date9 = models.DateField(blank=True, null=True)
    tc_date10 = models.DateField(blank=True, null=True)
    tc_date11 = models.DateField(blank=True, null=True)
    tc_date12 = models.DateField(blank=True, null=True)
    tc_date13 = models.DateField(blank=True, null=True)
    tc_date14 = models.DateField(blank=True, null=True)
    tc_date15 = models.DateField(blank=True, null=True)
    tc_sec1 = models.IntegerField(blank=True, null=True)
    tc_sec2 = models.IntegerField(blank=True, null=True)
    tc_sec3 = models.IntegerField(blank=True, null=True)
    tc_sec4 = models.IntegerField(blank=True, null=True)
    tc_sec5 = models.IntegerField(blank=True, null=True)
    tc_sec6 = models.IntegerField(blank=True, null=True)
    tc_sec7 = models.IntegerField(blank=True, null=True)
    tc_sec8 = models.IntegerField(blank=True, null=True)
    tc_sec9 = models.IntegerField(blank=True, null=True)
    tc_sec10 = models.IntegerField(blank=True, null=True)
    tc_sec11 = models.IntegerField(blank=True, null=True)
    tc_sec12 = models.IntegerField(blank=True, null=True)
    tc_sec13 = models.IntegerField(blank=True, null=True)
    tc_sec14 = models.IntegerField(blank=True, null=True)
    tc_sec15 = models.IntegerField(blank=True, null=True)
    tc_elap1 = models.FloatField(blank=True, null=True)
    tc_elap2 = models.FloatField(blank=True, null=True)
    tc_elap3 = models.FloatField(blank=True, null=True)
    tc_elap4 = models.FloatField(blank=True, null=True)
    tc_elap5 = models.FloatField(blank=True, null=True)
    tc_elap6 = models.FloatField(blank=True, null=True)
    tc_elap7 = models.FloatField(blank=True, null=True)
    tc_elap8 = models.FloatField(blank=True, null=True)
    tc_elap9 = models.FloatField(blank=True, null=True)
    tc_elap10 = models.FloatField(blank=True, null=True)
    tc_elap11 = models.FloatField(blank=True, null=True)
    tc_elap12 = models.FloatField(blank=True, null=True)
    tc_elap13 = models.FloatField(blank=True, null=True)
    tc_elap14 = models.FloatField(blank=True, null=True)
    tc_elap15 = models.FloatField(blank=True, null=True)
    tc_shift_s = models.CharField(max_length=10, blank=True, null=True)
    tc_shift_e = models.CharField(max_length=10, blank=True, null=True)
    tc_lunch_e = models.CharField(max_length=10, blank=True, null=True)
    tc_lunch_s = models.CharField(max_length=10, blank=True, null=True)
    tc_status = models.CharField(max_length=20, blank=True, null=True)
    tc_shift = models.CharField(max_length=2, blank=True, null=True)
    tc_exporte = models.NullBooleanField()
    tc_exp_dat = models.DateField(blank=True, null=True)
    tc_de_id1 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id2 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id3 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id4 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id5 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id6 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id7 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id8 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id9 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id10 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id11 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id12 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id13 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id14 = models.CharField(max_length=2, blank=True, null=True)
    tc_de_id15 = models.CharField(max_length=2, blank=True, null=True)
    tc_updt_us = models.CharField(max_length=5, blank=True, null=True)
    tc_updt_da = models.DateTimeField(blank=True, null=True)
    tc_act1 = models.CharField(max_length=10, blank=True, null=True)
    tc_act2 = models.CharField(max_length=10, blank=True, null=True)
    tc_act3 = models.CharField(max_length=10, blank=True, null=True)
    tc_act4 = models.CharField(max_length=10, blank=True, null=True)
    tc_act5 = models.CharField(max_length=10, blank=True, null=True)
    tc_act6 = models.CharField(max_length=10, blank=True, null=True)
    tc_act7 = models.CharField(max_length=10, blank=True, null=True)
    tc_act8 = models.CharField(max_length=10, blank=True, null=True)
    tc_act9 = models.CharField(max_length=10, blank=True, null=True)
    tc_act10 = models.CharField(max_length=10, blank=True, null=True)
    tc_act11 = models.CharField(max_length=10, blank=True, null=True)
    tc_act12 = models.CharField(max_length=10, blank=True, null=True)
    tc_act13 = models.CharField(max_length=10, blank=True, null=True)
    tc_act14 = models.CharField(max_length=10, blank=True, null=True)
    tc_act15 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tcard'


class Tcardcat(models.Model):
    tc_code = models.CharField(max_length=2, blank=True, null=True)
    tc_desc = models.CharField(max_length=20, blank=True, null=True)
    tc_io = models.CharField(max_length=1, blank=True, null=True)
    tc_perm = models.NullBooleanField()
    tc_no_ta = models.NullBooleanField()
    tc_no_jc = models.NullBooleanField()
    tc_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tcardcat'


class Terr(models.Model):
    tr_id = models.CharField(max_length=10, blank=True, null=True)
    tr_descrip = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terr'


class Thdwire(models.Model):
    tw_threads = models.CharField(max_length=10, blank=True, null=True)
    tw_wire_mm = models.FloatField(blank=True, null=True)
    tw_wire_in = models.FloatField(blank=True, null=True)
    tw_correct = models.FloatField(blank=True, null=True)
    tw_mmle4 = models.FloatField(blank=True, null=True)
    tw_mmgt4 = models.FloatField(blank=True, null=True)
    tw_pdle1_pt = models.FloatField(blank=True, null=True)
    tw_pdto4 = models.FloatField(blank=True, null=True)
    tw_pitch = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thdwire'


class Threadtype(models.Model):
    tt_id = models.CharField(max_length=10, blank=True, null=True)
    tt_descrip = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'threadtype'


class Tnestdet(models.Model):
    nd_id = models.CharField(max_length=10, blank=True, null=True)
    nd_runcode = models.CharField(max_length=20, blank=True, null=True)
    nd_order_n = models.CharField(max_length=12, blank=True, null=True)
    nd_op_num = models.IntegerField(blank=True, null=True)
    nd_pcs_raw = models.IntegerField(blank=True, null=True)
    nd_tot_sq_field = models.FloatField(db_column='nd_tot_sq_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nd_percent = models.IntegerField(blank=True, null=True)
    nd_pcs_pro = models.IntegerField(blank=True, null=True)
    nd_pcs_scr = models.IntegerField(blank=True, null=True)
    nd_pcs_goo = models.IntegerField(blank=True, null=True)
    nd_time = models.FloatField(blank=True, null=True)
    nd_materia = models.FloatField(blank=True, null=True)
    nd_part_nu = models.CharField(max_length=25, blank=True, null=True)
    nd_fg_inve = models.CharField(max_length=30, blank=True, null=True)
    nd_aj_id = models.CharField(max_length=10, blank=True, null=True)
    nd_rel_num = models.IntegerField(blank=True, null=True)
    nd_pcs_rev = models.IntegerField(blank=True, null=True)
    nd_pcs_rew = models.IntegerField(blank=True, null=True)
    nd_attend = models.IntegerField(blank=True, null=True)
    nd_trackin = models.CharField(max_length=10, blank=True, null=True)
    nd_op_comp = models.NullBooleanField()
    nd_qi_line = models.IntegerField(blank=True, null=True)
    nd_qi_item = models.IntegerField(blank=True, null=True)
    nd_np = models.FloatField(blank=True, null=True)
    nd_de_id = models.CharField(max_length=10, blank=True, null=True)
    nd_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tnestdet'


class Toolkit(models.Model):
    tk_id = models.CharField(max_length=10, blank=True, null=True)
    tk_parent_field = models.CharField(db_column='tk_parent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    tk_child_i = models.CharField(max_length=30, blank=True, null=True)
    tk_quantit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toolkit'


class Train(models.Model):
    tr_id = models.CharField(max_length=10, blank=True, null=True)
    tr_emp_id = models.CharField(max_length=5, blank=True, null=True)
    tr_standar = models.CharField(max_length=10, blank=True, null=True)
    tr_trained = models.CharField(max_length=6, blank=True, null=True)
    tr_notes = models.TextField(blank=True, null=True)
    tr_exp_dat = models.DateField(blank=True, null=True)
    tr_desc = models.CharField(max_length=50, blank=True, null=True)
    tr_date = models.DateField(blank=True, null=True)
    tr_mach_co = models.CharField(max_length=5, blank=True, null=True)
    tr_hours = models.FloatField(blank=True, null=True)
    tr_invent_field = models.CharField(db_column='tr_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    tr_dept_co = models.CharField(max_length=2, blank=True, null=True)
    tr_score = models.IntegerField(blank=True, null=True)
    tr_pf = models.IntegerField(blank=True, null=True)
    tr_train_c = models.FloatField(blank=True, null=True)
    tr_supp_co = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train'


class Traindet(models.Model):
    td_id = models.CharField(max_length=10, blank=True, null=True)
    td_tr_id = models.CharField(max_length=10, blank=True, null=True)
    td_emp_id = models.CharField(max_length=10, blank=True, null=True)
    td_score = models.IntegerField(blank=True, null=True)
    td_passfai = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traindet'


class Truck(models.Model):
    tr_id = models.CharField(max_length=10, blank=True, null=True)
    tr_date = models.DateField(blank=True, null=True)
    tr_status = models.CharField(max_length=1, blank=True, null=True)
    tr_ship_vi = models.CharField(max_length=10, blank=True, null=True)
    tr_created = models.CharField(max_length=5, blank=True, null=True)
    tr_tt_id = models.CharField(max_length=10, blank=True, null=True)
    tr_note = models.TextField(blank=True, null=True)
    tr_schedby = models.CharField(max_length=5, blank=True, null=True)
    tr_est_cos = models.FloatField(blank=True, null=True)
    tr_contact = models.CharField(max_length=30, blank=True, null=True)
    tr_appdate = models.DateTimeField(blank=True, null=True)
    tr_actdate = models.DateTimeField(blank=True, null=True)
    tr_tarp = models.NullBooleanField()
    tr_shiptim = models.DateTimeField(blank=True, null=True)
    tr_bookedd = models.DateTimeField(blank=True, null=True)
    tr_cust_co = models.CharField(max_length=6, blank=True, null=True)
    tr_type = models.IntegerField(blank=True, null=True)
    tr_partial = models.NullBooleanField()
    tr_tally_r = models.NullBooleanField()
    tr_see_not = models.NullBooleanField()
    tr_paperwo = models.NullBooleanField()
    tr_pick_pr = models.NullBooleanField()
    tr_to_be_r = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'truck'


class Truckdet(models.Model):
    td_id = models.CharField(max_length=10, blank=True, null=True)
    td_tr_id = models.CharField(max_length=10, blank=True, null=True)
    td_seq = models.IntegerField(blank=True, null=True)
    td_sord_nu = models.CharField(max_length=7, blank=True, null=True)
    td_line_nu = models.IntegerField(blank=True, null=True)
    td_rel_num = models.IntegerField(blank=True, null=True)
    td_invent_field = models.CharField(db_column='td_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    td_quantit = models.FloatField(blank=True, null=True)
    td_ship_co = models.CharField(max_length=8, blank=True, null=True)
    td_ship_li = models.IntegerField(blank=True, null=True)
    td_tarp = models.NullBooleanField()
    td_priorit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'truckdet'


class Trucklot(models.Model):
    tl_id = models.CharField(max_length=10, blank=True, null=True)
    tl_td_id = models.CharField(max_length=10, blank=True, null=True)
    tl_invent_field = models.CharField(db_column='tl_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    tl_lot_num = models.CharField(max_length=20, blank=True, null=True)
    tl_quantit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trucklot'


class Trucktyp(models.Model):
    tt_id = models.CharField(max_length=10, blank=True, null=True)
    tt_desc = models.CharField(max_length=40, blank=True, null=True)
    tt_ext_des = models.TextField(blank=True, null=True)
    tt_maxwgt = models.FloatField(blank=True, null=True)
    tt_axles = models.IntegerField(blank=True, null=True)
    tt_length = models.FloatField(blank=True, null=True)
    tt_width = models.FloatField(blank=True, null=True)
    tt_height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trucktyp'


class UseLots(models.Model):
    ul_id = models.CharField(max_length=20, blank=True, null=True)
    ul_ic_id = models.CharField(max_length=10, blank=True, null=True)
    ul_quantit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'use_lots'


class Vacation(models.Model):
    va_id = models.CharField(max_length=10, blank=True, null=True)
    va_date = models.DateField(blank=True, null=True)
    va_type = models.CharField(max_length=1, blank=True, null=True)
    va_paid = models.NullBooleanField()
    va_emp_id = models.CharField(max_length=5, blank=True, null=True)
    va_mach_co = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacation'


class Validrec(models.Model):
    va_id = models.CharField(max_length=10, blank=True, null=True)
    va_ship_co = models.CharField(max_length=8, blank=True, null=True)
    va_order_n = models.CharField(max_length=12, blank=True, null=True)
    va_invent_field = models.CharField(db_column='va_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    va_contain = models.IntegerField(blank=True, null=True)
    va_box = models.IntegerField(blank=True, null=True)
    va_quantit = models.FloatField(blank=True, null=True)
    va_user_id = models.CharField(max_length=5, blank=True, null=True)
    va_datetim = models.DateTimeField(blank=True, null=True)
    va_sord_nu = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validrec'


class Valover(models.Model):
    vo_datetim = models.DateTimeField(blank=True, null=True)
    vo_emp_id = models.CharField(max_length=5, blank=True, null=True)
    vo_order_n = models.CharField(max_length=12, blank=True, null=True)
    vo_op_num = models.IntegerField(blank=True, null=True)
    vo_supervi = models.CharField(max_length=5, blank=True, null=True)
    vo_skipped = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valover'


class Vbdocman(models.Model):
    dm_id = models.CharField(max_length=10, blank=True, null=True)
    dm_doc_typ = models.CharField(max_length=10, blank=True, null=True)
    dm_desc = models.CharField(max_length=50, blank=True, null=True)
    dm_last_up = models.DateField(blank=True, null=True)
    dm_file = models.CharField(max_length=254, blank=True, null=True)
    dm_memo = models.TextField(blank=True, null=True)
    dm_view_wi = models.IntegerField(blank=True, null=True)
    dm_protect = models.NullBooleanField()
    dm_cust_co = models.CharField(max_length=6, blank=True, null=True)
    dm_supp_co = models.CharField(max_length=6, blank=True, null=True)
    dm_emp_id = models.CharField(max_length=5, blank=True, null=True)
    dm_ca_code = models.CharField(max_length=12, blank=True, null=True)
    dm_fa_code = models.CharField(max_length=10, blank=True, null=True)
    dm_ar_inv_field = models.CharField(db_column='dm_ar_inv_', max_length=7, blank=True, null=True)  # Field renamed because it ended with '_'.
    dm_ap_inv_field = models.CharField(db_column='dm_ap_inv_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    dm_cmemo_n = models.CharField(max_length=7, blank=True, null=True)
    dm_dmemo_n = models.CharField(max_length=30, blank=True, null=True)
    dm_chk_acc = models.CharField(max_length=15, blank=True, null=True)
    dm_chk_num = models.CharField(max_length=10, blank=True, null=True)
    dm_dep_num = models.CharField(max_length=7, blank=True, null=True)
    dm_gj_id = models.CharField(max_length=10, blank=True, null=True)
    dm_referen = models.CharField(max_length=40, blank=True, null=True)
    dm_user_id = models.CharField(max_length=5, blank=True, null=True)
    dm_entry_t = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vbdocman'


class VetMemo(models.Model):
    vm_id = models.CharField(max_length=10, blank=True, null=True)
    vm_datelas = models.DateField(blank=True, null=True)
    vm_desc = models.CharField(max_length=35, blank=True, null=True)
    vm_type = models.CharField(max_length=15, blank=True, null=True)
    vm_by = models.CharField(max_length=5, blank=True, null=True)
    vm_memo = models.TextField(blank=True, null=True)
    vm_seqnum = models.IntegerField(blank=True, null=True)
    vm_nc_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vet_memo'


class ViaAtrb(models.Model):
    vc_id = models.CharField(max_length=10, blank=True, null=True)
    vc_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'via_atrb'


class Voltrend(models.Model):
    vt_invent_field = models.CharField(db_column='vt_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    vt_eau = models.IntegerField(blank=True, null=True)
    vt_aau = models.IntegerField(blank=True, null=True)
    vt_aau_52 = models.IntegerField(blank=True, null=True)
    vt_aau_26 = models.IntegerField(blank=True, null=True)
    vt_aau_13 = models.IntegerField(blank=True, null=True)
    vt_aau_4 = models.IntegerField(blank=True, null=True)
    vt_aau1 = models.IntegerField(blank=True, null=True)
    vt_aau2 = models.IntegerField(blank=True, null=True)
    vt_aau3 = models.IntegerField(blank=True, null=True)
    vt_aau4 = models.IntegerField(blank=True, null=True)
    vt_aau5 = models.IntegerField(blank=True, null=True)
    vt_aau6 = models.IntegerField(blank=True, null=True)
    vt_aau7 = models.IntegerField(blank=True, null=True)
    vt_aau8 = models.IntegerField(blank=True, null=True)
    vt_aau9 = models.IntegerField(blank=True, null=True)
    vt_aau10 = models.IntegerField(blank=True, null=True)
    vt_aau11 = models.IntegerField(blank=True, null=True)
    vt_aau12 = models.IntegerField(blank=True, null=True)
    vt_pe1 = models.FloatField(blank=True, null=True)
    vt_pe2 = models.FloatField(blank=True, null=True)
    vt_pe3 = models.FloatField(blank=True, null=True)
    vt_pe4 = models.FloatField(blank=True, null=True)
    vt_pe5 = models.FloatField(blank=True, null=True)
    vt_pe6 = models.FloatField(blank=True, null=True)
    vt_pe7 = models.FloatField(blank=True, null=True)
    vt_pe8 = models.FloatField(blank=True, null=True)
    vt_pe9 = models.FloatField(blank=True, null=True)
    vt_pe10 = models.FloatField(blank=True, null=True)
    vt_pe11 = models.FloatField(blank=True, null=True)
    vt_pe12 = models.FloatField(blank=True, null=True)
    vt_eff52 = models.FloatField(blank=True, null=True)
    vt_eff26 = models.FloatField(blank=True, null=True)
    vt_eff13 = models.FloatField(blank=True, null=True)
    vt_eff4 = models.FloatField(blank=True, null=True)
    vt_est_set = models.FloatField(blank=True, null=True)
    vt_act_set = models.FloatField(blank=True, null=True)
    vt_cust_co = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voltrend'


class Vshop(models.Model):
    vt_id = models.IntegerField(blank=True, null=True)
    vt_fullnam = models.CharField(max_length=100, blank=True, null=True)
    vt_nodenam = models.CharField(max_length=100, blank=True, null=True)
    vt_x = models.BinaryField(blank=True, null=True)
    vt_y = models.BinaryField(blank=True, null=True)
    vt_width = models.BinaryField(blank=True, null=True)
    vt_height = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vshop'


class Vupdate(models.Model):
    up_bom_quo = models.DateField(blank=True, null=True)
    del_jcbatc = models.NullBooleanField()
    doc_man_et = models.NullBooleanField()
    up_lot_id = models.NullBooleanField()
    dec_so_inv = models.NullBooleanField()
    pod_txt = models.NullBooleanField()
    fixut = models.NullBooleanField()
    uom_add_cy = models.NullBooleanField()
    up_cur_cod = models.NullBooleanField()
    up_cur_co2 = models.NullBooleanField()
    add_action = models.NullBooleanField()
    fix_inv_ec = models.NullBooleanField()
    so_phone_f = models.NullBooleanField()
    bf_ca_id = models.NullBooleanField()
    lo_po_line = models.NullBooleanField()
    check_step = models.NullBooleanField()
    set_iv_com = models.NullBooleanField()
    set_cc_pos = models.NullBooleanField()
    set_fflush = models.NullBooleanField()
    fix_unit_t = models.NullBooleanField()
    convqtyuom = models.NullBooleanField()
    invjrnlord = models.NullBooleanField()
    set_encryp = models.NullBooleanField()
    set_thdwir = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'vupdate'


class Wcscrap(models.Model):
    ws_mach_co = models.CharField(max_length=5, blank=True, null=True)
    ws_start_q = models.FloatField(blank=True, null=True)
    ws_end_qty = models.FloatField(blank=True, null=True)
    ws_scrap_p = models.FloatField(blank=True, null=True)
    ws_quote_n = models.CharField(max_length=15, blank=True, null=True)
    ws_op_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wcscrap'


class Weight(models.Model):
    wt_mat_cod = models.CharField(max_length=3, blank=True, null=True)
    wt_desc = models.CharField(max_length=20, blank=True, null=True)
    wt_weight = models.FloatField(blank=True, null=True)
    wt_bol_lin = models.CharField(max_length=30, blank=True, null=True)
    wt_bol_li2 = models.CharField(max_length=30, blank=True, null=True)
    wt_scrap = models.FloatField(blank=True, null=True)
    wt_rgb = models.IntegerField(blank=True, null=True)
    wt_ca_code = models.CharField(max_length=12, blank=True, null=True)
    wt_nburden = models.FloatField(blank=True, null=True)
    wt_o2_burde = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weight'


class Weldline(models.Model):
    wl_id = models.CharField(max_length=10, blank=True, null=True)
    wl_code = models.CharField(max_length=2, blank=True, null=True)
    wl_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weldline'


class WipAdj(models.Model):
    wa_id = models.CharField(max_length=10, blank=True, null=True)
    wa_wp_id = models.CharField(max_length=10, blank=True, null=True)
    wa_order_n = models.CharField(max_length=12, blank=True, null=True)
    wa_date = models.DateField(blank=True, null=True)
    wa_causeof = models.CharField(max_length=1, blank=True, null=True)
    wa_labor = models.FloatField(blank=True, null=True)
    wa_burden = models.FloatField(blank=True, null=True)
    wa_materia = models.FloatField(blank=True, null=True)
    wa_other = models.FloatField(blank=True, null=True)
    wa_total = models.FloatField(blank=True, null=True)
    wa_quantit = models.FloatField(blank=True, null=True)
    wa_user_id = models.CharField(max_length=5, blank=True, null=True)
    wa_datetim = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wip_adj'


class WipJrnl(models.Model):
    wp_id = models.CharField(max_length=10, blank=True, null=True)
    wp_order_n = models.CharField(max_length=12, blank=True, null=True)
    wp_date = models.DateField(blank=True, null=True)
    wp_type = models.CharField(max_length=1, blank=True, null=True)
    wp_key = models.CharField(max_length=20, blank=True, null=True)
    wp_labor = models.FloatField(blank=True, null=True)
    wp_burden = models.FloatField(blank=True, null=True)
    wp_materia = models.FloatField(blank=True, null=True)
    wp_other = models.FloatField(blank=True, null=True)
    wp_total = models.FloatField(blank=True, null=True)
    wp_referen = models.CharField(max_length=50, blank=True, null=True)
    wp_invent_field = models.CharField(db_column='wp_invent_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    wp_quantit = models.FloatField(blank=True, null=True)
    wp_user_id = models.CharField(max_length=5, blank=True, null=True)
    wp_unit_la = models.FloatField(blank=True, null=True)
    wp_unit_bu = models.FloatField(blank=True, null=True)
    wp_unit_ma = models.FloatField(blank=True, null=True)
    wp_unit_ot = models.FloatField(blank=True, null=True)
    wp_datetim = models.DateTimeField(blank=True, null=True)
    wp_prod_co = models.CharField(max_length=2, blank=True, null=True)
    wp_dist_co = models.CharField(max_length=2, blank=True, null=True)
    wp_unit_to = models.FloatField(blank=True, null=True)
    wp_op_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wip_jrnl'


class Zipcodes(models.Model):
    zc_id = models.CharField(max_length=10, blank=True, null=True)
    zc_lo_id = models.CharField(max_length=10, blank=True, null=True)
    zc_code = models.CharField(max_length=5, blank=True, null=True)
    zc_mailcod = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zipcodes'


class Zone(models.Model):
    zo_carrier = models.CharField(max_length=10, blank=True, null=True)
    zo_origin_field = models.CharField(db_column='zo_origin_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    zo_dest_zi = models.CharField(max_length=10, blank=True, null=True)
    zo_dest_z2 = models.CharField(max_length=10, blank=True, null=True)
    zo_zone = models.CharField(max_length=10, blank=True, null=True)
    zo_ship_ty = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zone'
