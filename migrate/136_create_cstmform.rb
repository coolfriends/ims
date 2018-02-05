Sequel.migration do
  change do
     create_table(:cstmform) do
      column :cf_id, :varchar, :size => 10
      column :cf_report_, :varchar, :size => 50
      column :cf_referen, :varchar, :size => 20
      column :cf_quote, :boolean
      column :cf_sord, :boolean
      column :cf_shop, :boolean
      column :cf_custome, :boolean
      column :cf_vendor, :boolean
      column :cf_invento, :boolean
      column :cf_action, :boolean
      column :cf_note, :text
      column :cf_invoice, :boolean
      column :cf_ac_apin, :boolean
    end
  end
end
