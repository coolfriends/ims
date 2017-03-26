Sequel.migration do
  change do
     create_table(:message) do
      column :mg_id, :integer
      column :mg_from, :varchar, :size => 60
      column :mg_subject, :varchar, :size => 80
      column :mg_datetim, :datetime
      column :mg_message, :text
      column :mg_pdffile, :text
      column :mg_task, :boolean
      column :mg_informe, :boolean
    end
  end
end
