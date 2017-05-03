Sequel.migration do
  change do
     create_table(:as9102f2) do
      column :asf2_id, :varchar, :size => 10
      column :part_num, :varchar, :size => 30
      column :part_name, :varchar, :size => 50
      column :serial_num, :varchar, :size => 30
      column :fai_report, :varchar, :size => 30
      column :preparedby, :varchar, :size => 5
      column :preparedb2, :date
      column :comments, :text
      column :as_id, :varchar, :size => 10
    end
  end
end
