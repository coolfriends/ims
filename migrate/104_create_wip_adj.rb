Sequel.migration do
  change do
     create_table(:wip_adj) do
      column :wa_id, :varchar, :size => 10
      column :wa_wp_id, :varchar, :size => 10
      column :wa_order_n, :varchar, :size => 12
      column :wa_date, :date
      column :wa_causeof, :varchar, :size => 1
      column :wa_labor, :float
      column :wa_burden, :float
      column :wa_materia, :float
      column :wa_other, :float
      column :wa_total, :float
      column :wa_quantit, :float
      column :wa_user_id, :varchar, :size => 5
      column :wa_datetim, :datetime
    end
  end
end
