# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:edi_st) do
      column :es_cust_co, :varchar, size: 6
      column :es_qs_id, :varchar, size: 10
      column :es_trans_c, :varchar, size: 3
      column :es_funct_i, :varchar, size: 2
      column :es_send_ac, :boolean
      column :es_set_con, :integer
      column :es_set_co2, :integer
      column :es_ca_id, :varchar, size: 10
      column :es_resp_ag, :varchar, size: 2
      column :es_version, :varchar, size: 12
    end
  end
end
