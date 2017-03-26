Sequel.migration do
  change do
     create_table(:msg_rcpt) do
      column :mr_id, :integer
      column :mr_mg_id, :integer
      column :mr_read, :boolean
      column :mr_me_id, :integer
      column :mr_sendto, :varchar, :size => 60
      column :mr_output, :varchar, :size => 15
      column :mr_notes, :text
      column :mr_when_re, :datetime
      column :mr_deadlin, :datetime
    end
  end
end
