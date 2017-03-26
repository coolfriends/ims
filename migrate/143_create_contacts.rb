Sequel.migration do
  change do
     create_table(:contacts) do
      column :cc_id, :varchar, :size => 10
      column :cc_cust_co, :varchar, :size => 6
      column :cc_emp_id, :varchar, :size => 5
      column :cc_name, :varchar, :size => 25
      column :cc_address, :boolean
      column :cc_addres2, :varchar, :size => 35
      column :cc_addres3, :varchar, :size => 35
      column :cc_city, :varchar, :size => 20
      column :cc_state, :varchar, :size => 3
      column :cc_zip_cod, :varchar, :size => 10
      column :cc_country, :varchar, :size => 20
      column :cc_phone, :varchar, :size => 14
      column :cc_phone_e, :varchar, :size => 5
      column :cc_phone_c, :varchar, :size => 14
      column :cc_fax, :varchar, :size => 14
      column :cc_email, :varchar, :size => 50
      column :cc_prime_c, :boolean
      column :cc_next_co, :date
      column :cc_last_ca, :date
      column :cc_departm, :varchar, :size => 35
      column :cc_unit, :varchar, :size => 35
      column :cc_positio, :varchar, :size => 35
      column :cc_title, :varchar, :size => 35
      column :cc_interes, :integer
      column :cc_dont_co, :boolean
      column :cc_dont_re, :text
      column :cc_no_long, :boolean
      column :cc_left_ab, :date
      column :cc_home_ph, :varchar, :size => 14
      column :cc_cell_ph, :varchar, :size => 14
      column :cc_pager, :varchar, :size => 14
      column :cc_em_name, :varchar, :size => 35
      column :cc_em_phon, :varchar, :size => 14
      column :cc_em_fax, :varchar, :size => 14
      column :cc_em_note, :text
      column :cc_marital, :integer
      column :cc_childre, :varchar, :size => 75
      column :cc_sex, :integer
      column :cc_age, :integer
      column :cc_age_in, :integer
      column :cc_intere2, :text
      column :cc_eh_name, :varchar, :size => 35
      column :cc_eh_role, :varchar, :size => 35
      column :cc_eh_city, :varchar, :size => 20
      column :cc_eh_stat, :varchar, :size => 2
      column :cc_eh_left, :date
      column :cc_eh_note, :text
      column :cc_notes, :text
      column :cc_created, :varchar, :size => 5
      column :cc_create2, DateTime
      column :cc_last_lo, :varchar, :size => 5
      column :cc_last_up, DateTime
      column :cc_call_cy, :varchar, :size => 20
      column :cc_salutat, :varchar, :size => 15
      column :cc_supp_co, :varchar, :size => 6
      column :cc_ap_pers, :boolean
      column :cc_type, :varchar, :size => 10
      column :cc_sales_c, :boolean
      column :cc_ca_id, :varchar, :size => 10
      column :cc_teritor, :integer
      column :cc_inactiv, :boolean
      column :cc_email1, :varchar, :size => 50
      column :cc_email2, :varchar, :size => 50
      column :cc_email3, :varchar, :size => 50
      column :cc_email1_d, :varchar, :size => 20
      column :cc_email2_d, :varchar, :size => 20
      column :cc_email3_d, :varchar, :size => 20
      column :cc_locatio, :varchar, :size => 35
    end
  end
end
