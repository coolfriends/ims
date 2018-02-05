Sequel.migration do
  change do
     create_table(:ac_1099) do
      column :sc_id, :varchar, :size => 10
      column :sc_type, :varchar, :size => 1
      column :sc_supp_co, :varchar, :size => 6
      column :sc_year, :integer
      column :sc_fedid, :varchar, :size => 35
      column :sc_name, :varchar, :size => 35
      column :sc_address, :varchar, :size => 35
      column :sc_addres2, :varchar, :size => 35
      column :sc_city, :varchar, :size => 15
      column :sc_state, :varchar, :size => 3
      column :sc_zip, :varchar, :size => 10
      column :sc_phone, :varchar, :size => 8
      column :sc_supp_ac, :varchar, :size => 12
      column :sc_2_nd_tin, :boolean
      column :sc_rents, :float
      column :sc_royalti, :float
      column :sc_other_i, :float
      column :sc_fit_wit, :float
      column :sc_fishing, :float
      column :sc_medical, :float
      column :sc_nonempl, :float
      column :sc_substit, :float
      column :sc_crop_in, :float
      column :sc_sit_wit, :float
      column :sc_state_n, :varchar, :size => 15
      column :sc_box_13, :float
      column :sc_resale, :boolean
      column :sc_void, :boolean
      column :sc_correct, :boolean
      column :sc_egp_pay, :float
      column :sc_attorne, :float
      column :sc_st1_wit, :float
      column :sc_st1_inc, :float
      column :sc_st1_sta, :varchar, :size => 15
      column :sc_st2_wit, :float
      column :sc_st2_inc, :float
      column :sc_st2_sta, :varchar, :size => 15
      column :sc_other_1, :varchar, :size => 35
      column :sc_other_2, :varchar, :size => 35
      column :sc_1099_bo, :varchar, :size => 2
      column :sc_total_1, :integer
      column :sc_final_r, :boolean
      column :sc_contact, :varchar, :size => 35
      column :sc_email, :varchar, :size => 35
      column :sc_phone_a, :varchar, :size => 3
      column :sc_fax, :varchar, :size => 8
      column :sc_fax_ac, :varchar, :size => 3
      column :sc_soc_sec, :varchar, :size => 11
      column :sc_addres3, :varchar, :size => 35
      column :sc_409_a_de, :float
      column :sc_409_a_in, :float
      column :sc_source, :varchar, :size => 1
      column :sc_foreign, :float
      column :sc_foreig2, :varchar, :size => 12
      column :sc_fatca_f, :boolean
    end
  end
end
