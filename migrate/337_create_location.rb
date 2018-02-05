Sequel.migration do
  change do
     create_table(:location) do
      column :lo_code, :varchar, :size => 10
      column :lo_desc, :varchar, :size => 30
      column :lo_size, :varchar, :size => 1
      column :lo_comp_na, :varchar, :size => 35
      column :lo_address, :varchar, :size => 35
      column :lo_addres2, :varchar, :size => 35
      column :lo_city, :varchar, :size => 15
      column :lo_state, :varchar, :size => 3
      column :lo_zip, :varchar, :size => 10
      column :lo_country, :varchar, :size => 20
      column :lo_logo, :varchar, :size => 80
      column :lo_use, :boolean
      column :lo_phone, :varchar, :size => 14
      column :lo_fax, :varchar, :size => 14
      column :lo_so_memo, :text
      column :lo_qu_memo, :text
      column :lo_no_mark, :boolean
      column :lo_fob, :varchar, :size => 15
      column :lo_gl_num_, :varchar, :size => 12
      column :lo_foblabe, :varchar, :size => 3
      column :lo_il_id, :varchar, :size => 10
      column :lo_ib_id, :varchar, :size => 10
      column :lo_prod_co, :varchar, :size => 2
      column :lo_sh_memo, :text
      column :lo_dist_co, :varchar, :size => 2
      column :lo_useinre, :boolean
      column :lo_useinso, :boolean
      column :lo_exclpo, :boolean
    end
  end
end
